# Copyright Act 2021 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation, as the deposit labels itself
(amendments to Act 31 of 2022).

**Checks:** two case files, 61 assertions satisfied (26 in `cpa-cases-uses.l4`, 35 in `cpa-cases-ownership.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**13 of the 527 Singapore Acts** deposited here cite it. This row takes duration and the
user-side permitted uses: contracting out, fair use, copying for research or study, and
computational data analysis. Subsistence, ownership, exclusive rights, infringement,
remedies, the other permitted uses, moral rights, performers' rights and collective
licensing are not encoded.

## What the Act turns out to say

### 1. Contracts cannot remove the data-analysis exception at all

s 187(1)(c): a contract term is **void** so far as it excludes or restricts the
computational data analysis exception (s 244). The same goes for the public
collections, computer program, and legal proceedings exceptions. Asserted.

### 2. Standard terms cannot remove fair use

s 186(2): a term excluding a permitted use such as fair use is valid only if the
contract is **individually negotiated** and the term is fair and reasonable. A
click-through website licence fails the first condition. s 188 voids a foreign
choice-of-law clause used to evade a permitted use, or imposed on a Singapore
consumer. Asserted.

### 3. Data analysis needs lawful access

s 244 and its illustrations: circumventing a **paywall**, or breaching a database's
valid terms of use, is not lawful access, so copying for analysis is not permitted.
Using an infringing source is excused only if the user did not know, and, for a
flagrantly infringing site, could not reasonably have known. Asserted.

### 4. Acknowledgment: news has an escape, criticism does not

s 192: use for news reporting is unfair without sufficient acknowledgment **unless**
acknowledgment is impractical. Use for criticism or review is unfair without it, full
stop. Asserted.

### 5. Ten per cent or one chapter

ss 43, 194: copying for research or study is deemed fair if it is one periodical
article, or a "reasonable portion". For an edition of 10 or more pages, that means 10%
of the pages or less, or pages from a single chapter of any length. Asserted.

### 6. Duration

s 114: life plus 70 years, or 70 years from first publication if the author is not
identified. s 122: 70 years from publication for a sound recording. Asserted.

## What would need doing before this is worth anything

- The s 191 fair-use factors are taken as a conclusion, not weighed.
- The education, library and disability permitted uses are the next most-used and are
  not encoded.
- No case law was searched.

## First ownership (added 12 October 2026 for REQ-0287)

Module `cpa-ownership.l4`, cases `cpa-cases-ownership.l4` (35 assertions). Raised by the Haziq scenario, event h045:
salaried engineers write a company's software in the course of their employment, with nothing in their contracts about
ownership. Who owns the copyright?

### 1. The company, as first owner, under s 134(3)

A computer program is a literary work (s 13(1)(b)), so an authorial work (s 9). Where "in the course of a contract of
service, the employee ... makes an authorial work" (s 134(1)(a)), "the employer is the first owner of any copyright in the
relevant work" (s 134(3)), and s 133 (author as default owner) is displaced (s 134(2)). The ledger's expected answer is
right. Asserted.

### 2. The Act says "contract of service", not "employment"

The test is a contract of service, which s 7(1) defines by reference to s 2(1) of the Employment Act 1968. That Act is not
deposited here, and whether a work was made "in the course of" the contract is a question of fact for which no case law was
searched. The encoding takes both as an input. A freelance contractor is outside s 134, so the contractor (the author) owns
the copyright by default (s 133(1)(a)). Asserted.

### 3. "Absent agreement to the contrary" has a formality from 21 November 2021

s 134(5): the employer's ownership gives way to a contrary intention only in a **written** agreement between employer and
employee made on or after 21 November 2021, or in **any** agreement made before that date. An oral understanding reached
in 2023 does not displace it, but one from 2019 does. The encoding does not say what the agreement provides, only that the
default is displaced. Asserted.

### 4. The periodical exception, and it reaches code

s 134(4): where the employer is the proprietor of a periodical and a literary, dramatic or artistic work is made for
publication in one, the employer owns only the periodical publishing rights and the employee owns the rest (or, for works made
before 10 April 1987, the employer owns but the employee may restrain non-periodical publication). Musical works are not in
the list. Because a computer program is a literary work, on the words this would split ownership of code written by a magazine's
staff for publication in it; that is an inference from ss 13 and 134(4), not tested against case law. It does not touch the
REQ-0287 facts. Asserted.

### 5. Sound recordings, films, broadcasts and editions by employees: only from 21 November 2021

s 134(1)(b) brings these in only when made, provided or published on or after 21 November 2021; an employee's sound
recording from 2020 falls back on s 133 ("the maker"). Who the "maker" was is not encoded. Asserted.

### 6. The Government

s 136(1)(a), (d): the Government is first owner of an unpublished authorial work, or a sound recording or film, made by or under
its direction or control, "despite" ss 133 to 135, subject only to its own contrary agreement (s 136(2)). Paras (b) and (c),
international organisations (s 136(3), (4)) and pre-2021 commissions (s 135) are not encoded.

### Needs other instruments

- Employment Act 1968 s 2(1), for "contract of service".
- Case law on "in the course of" a contract of service, and on the employee/contractor line.
- Nothing on subsistence (qualified persons, connecting factors) is encoded, so the encoding assumes copyright subsists.
