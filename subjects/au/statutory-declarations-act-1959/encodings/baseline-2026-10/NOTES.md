# Statutory Declarations Act 1959 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill. It is written from the seat of the individual to whom the law is applied,
with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage
table, no independent test pass, no human gate. Not for public use as advice.

Every decision is exported for Legalese Cloud with `@export`, and each input has a
`@desc`. No earlier encoding of this Act existed.

## Edition

- **The Act:** Compilation No. 8, compilation date 1 January 2024 ("Includes
  amendments: Act No. 92, 2023"; register id C2024C00005). Deposited at
  `../../registers/source-bundle/C1959A00052.txt` (retrieved 2026-10-13). This is
  the text as rewritten by the Statutory Declarations Amendment Act 2023, which
  commenced on 1 January 2024 (Endnote 3).
- **Statutory Declarations Regulations 2023:** **not deposited.** Everything they
  settle is an input:
  - who is a prescribed person (s 4);
  - which digital service is an approved online platform (s 9A(2)) or an approved
    identity service (s 9A(3));
  - the identity-verification conditions (s 9A(1)(b)(ii));
  - the platform information a digital declaration must carry (s 9A(1)(c)(ii)).
- **Approved forms (s 15):** not deposited. Whether a declaration is "in the approved
  form" is an input.
- **Criminal Code Chapter 2** (applied by s 5A): not deposited. The fault element for
  the falsity of the statement, and any defence, are inputs.

## Checks

- One module (`sda-declarations.l4`) and one case file (`sda-cases-declarations.l4`).
- **45 assertions satisfied, 0 errors, 0 warnings**, with the stable `l4` from VS
  Code extension 1.6.98.
- The case file is built by `gen_statutory-declarations-act-1959_baseline.py` in the
  session scratchpad. Every expected value was written by hand from the text.

One fact the life does not state is an **assumption**, labelled in the case file:
that a legal practitioner holding a practising certificate is a prescribed person
under the Regulations. Daniel's clients are the encoder's illustrations.

## Seat

**The declarant, and the person asked to witness the declaration.** The life event
asks the witness's question ("Who may witness a statutory declaration?"). The Act is
also applied to the declarant: whether the declaration is made at all, and the
offence in s 11. The decisions are phrased as these two people ask them:

- `Does the Act apply where I make my declaration`;
- `May I make a statutory declaration about any matter`;
- `May my declaration be used for this`;
- `Does s 7A recognise my signature`;
- `Is my declaration made under the Act`;
- `May I witness this declaration`;
- `What must I sign as the witness`;
- `May the platform keep a copy of my declaration`;
- `Before whom may I make the declaration that law requires`;
- `Do I commit the false declaration offence`;
- `What is the longest I can be imprisoned for a false declaration in years`.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers:** followed. The
  instrument that matters, the Regulations, is not deposited, so what it settles is
  an input.
- **The actors the text names:** the declarant, the prescribed person, the provider
  of an approved online platform. Courts (s 12) and the Minister (ss 14-16) are
  machinery and are left out.
- **Judgments handed to someone else, answered conditionally:** the witness's
  satisfaction that a copy is a true copy (s 9(c)(ii)) is an input. So are a law's
  "contrary intention" (ss 6(2), 10) and the reliability of a signing method
  (s 7A(2)(b)).
- **The Act's own definitions worked out, borrowed terms asked:** "declarant",
  "video link" and the two approved services follow s 4 and s 9A. "Prescribed
  person" is defined by reference to the Regulations, so it is asked.
- **One case:** one declaration.
- **The Act's own terms, each with a plain gloss:** followed.
- **Operative sections in, machinery out:** followed.

## The lives

- **Daniel, d034 (1 June 2026, age 30):** "An authorised witness for statutory
  declarations and affidavits, by virtue of his practising certificate." It asks
  "Who may witness a statutory declaration ... in the Commonwealth?". The answer is a
  prescribed person who watches the declarant sign, in person or by video link, and
  then signs. The encoding answers `May I witness this declaration` and `What must I
  sign as the witness`. It also checks that declarations Daniel witnesses in person
  and by video link are made under s 9. Whether a lawyer is a prescribed person is in
  the Regulations, which are not deposited, so the encoding takes it as an input. The
  WA side of d034 belongs to the WA Oaths, Affidavits and Statutory Declarations Act
  2005 encoding.

## Why this scope

The Act is short. The operative part, ss 5-11 and 13, is encoded nearly whole. The
part left out is machinery or addresses someone other than the two seats: the 1911
saving (s 3), the platform's annual report (s 9B(2)-(5)), the courts' jurisdiction
(s 12), regulations, forms and the review (ss 14-16).

## What the Act turns out to say

1. **The Act names no witness.** Who may witness is wholly a matter for the
   Regulations ("prescribed person", s 4), which are not deposited. The Act alone
   cannot answer d034. Asserted (as an input).
2. **There are exactly two ways to make a declaration (s 8).** One is observation by
   a prescribed person (s 9). The other is digital verification on an approved
   online platform (s 9A). A declaration signed with no-one watching and no platform
   is not made under the Act. Asserted.
3. **A witness may watch by video link (s 9(b)(ii)).** If they do, they may sign
   either the declaration itself or a copy they are satisfied is a true copy,
   "whether or not the copy includes the declarant's signature" (s 9(c)(ii)). A
   witness who watched in person must sign the declaration itself. Asserted.
4. **The Act does not name myGov.** A digital declaration needs four things (s 9A):
   - a platform prescribed by the Regulations;
   - identity verification by a prescribed identity service;
   - verification under prescribed conditions;
   - prescribed platform information in the declaration.

   No witness is needed. The provider may not keep a copy (s 9B(1)), but s 9B states
   no penalty. Its sanction is that the platform's prescription may be repealed
   (s 14(5)). Asserted.
5. **Signing by hand or electronically is recognised on the same test (s 7A).** The
   method must identify the signer and show their intention. It must also be reliable
   enough or proven in fact. s 7A is permissive: it does not say that other methods
   fail. The encoding answers only whether s 7A recognises the method. Asserted.
6. **Uses (s 6(2)):**
   - a declaration may be used for Commonwealth and Territory laws, unless the law
     shows a contrary intention;
   - it may be used for the administration of a Commonwealth Department, with no
     contrary-intention proviso;
   - s 6(2) does not authorise its use as evidence in a judicial proceeding, but
     s 6(3) says nothing in s 6 prevents that use.

   Asserted.
7. **Another law's "made before" (s 10).** Where another Commonwealth law requires a
   declaration before a named person, a prescribed person under s 9 will also do,
   unless that law shows a contrary intention. The s 9A digital route is not
   mentioned in s 10 (an observation from the text, not tested further). Asserted.
8. **The offence (s 11)** is intentionally making a false statement in a statutory
   declaration. The maximum is imprisonment for 4 years, and no fine is stated in
   the Act. Chapter 2 of the Criminal Code governs the fault elements (s 5A).
   Asserted.
9. **Where the Act applies (ss 5, 13):** inside and outside the Commonwealth, but
   not in an external Territory unless s 13 extends it there. It extends to Norfolk
   Island, and Endnote 5 records Proclamations for six other external Territories.
   Asserted.

## What would need doing before this is worth anything

- Deposit the Statutory Declarations Regulations 2023. Encode Schedule 1, the
  prescribed persons, as a table, so that d034 is answered from the text rather than
  from an assumed input. Encode the approved online platform and identity service
  (whether myGov is prescribed), the verification conditions and the platform
  information.
- Deposit the approved forms (s 15).
- Deposit Criminal Code Chapter 2 and settle the fault element for the falsity in
  s 11. Deposit the Crimes Act 1914 rule that converts a prison term into a fine.
- An independent test pass and a human gate.
