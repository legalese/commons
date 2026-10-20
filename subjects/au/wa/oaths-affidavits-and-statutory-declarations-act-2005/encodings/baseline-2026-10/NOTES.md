# Oaths, Affidavits and Statutory Declarations Act 2005 (WA) — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual, with the design defaults ruled on 2026-10-18.
No pipeline, no coverage table, no independent test pass, no human gate. Not for
public use as advice.

**Edition:** the WA compilation including amendments to the Legal Profession Uniform
Law Application Act 2022 (No. 9 of 2022) s 424, in force 1 July 2022, with the
Evidence Act 2025 s 492(2) shown as uncommenced, deposited at
`../../registers/source-bundle/mrdoc_48924.txt` (retrieved 2026-09-07). Brought in:
Criminal Code (WA) s 169 (`subjects/au/wa/criminal-code-act-compilation-act-1913`,
mrdoc_49336, retrieved 2026-09-07); Interpretation Act 1984 s 5 and Legal Profession
Uniform Law (WA) s 6(1), from their own subjects. No regulations under s 18 and no
Statutory Declarations Regulations 2023 (Cth) are deposited. Whether someone is a
prescribed consular official (s 3(c)), or a person before whom a Commonwealth
declaration may be made (s 12(6)(a)(ii)), is therefore an input.

**Checks:** one module (`oasda-witnesses.l4`), one case file
(`oasda-cases-witnesses.l4`), 44 assertions satisfied, 0 errors, 0 warnings, on the
stable l4 from VS Code extension 1.6.98. The case file comes from
`gen_wa_oaths-affidavits-and-statutory-declarations-act-2005_baseline.py` in the
scratchpad. Its expected values were written by hand.

## Seat

**The declarant** (the maker of a statutory declaration or affidavit), **and the
lawyer acting as authorised witness** (Daniel). The life event asks who may witness,
and the Act puts duties on both the maker and the witness, so both seats are taken.
That matches the Commonwealth Statutory Declarations Act baseline. Where the Act
speaks to a court (ss 14, 15(3)) or to a chief judicial officer (s 10), the encoding
says what that means for the maker or the witness: whether the document will be
accepted, and whether the witness is authorised.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** No instrument sets
  numbers here. **Departure:** Criminal Code s 169 is brought in. This Act creates no
  false-declaration offence, but its Schedule 1 form makes the declarant recite one,
  and the request asked for that offence. The Interpretation Act s 5 is brought in
  because Schedule 2 item 20 ("A lawyer") and s 8 ("legal practitioner") take their
  meaning from it.
- **The actors the text names:** the maker and the authorised witness. Each
  Schedule 2 class is a value of one enum.
- **A judgment left to someone else is answered conditionally.** Whether s 16 saves a
  departure is an input. So are local-law authority abroad and Commonwealth witness
  status.
- **The Act's own definitions are worked out from facts.** "Experienced legal
  practitioner" (s 8) and "lawyer" are derived. Admission and the practising
  certificate are borrowed terms, asked as facts.
- **One case:** one declaration or affidavit, and one would-be witness.
- **The Act's own terms, with glosses:** followed.
- **Operative sections in scope, machinery out:** s 10(2)-(4) (appointment), s 18 and
  commencement are out.

## The lives

- **Daniel d034** (1 June 2026, aged 30): "An authorised witness for statutory
  declarations and affidavits, by virtue of his practising certificate". The question
  is "Who may witness a statutory declaration in WA; in the Commonwealth?" It is
  answered by `May I witness this statutory declaration` (a lawyer in Perth is in
  Schedule 2; in Melbourne he is authorised only as a Commonwealth witness, and abroad
  not at all). It is also answered by `May I witness this affidavit`: authorised as an
  experienced legal practitioner, but excluded under s 9(7) where he helped prepare
  the affidavit. A third case, Daniel in 2021 one year after d031, is not yet
  authorised. Two further assertions also use the d034 facts: `Am I a lawyer` and
  `Am I an experienced legal practitioner`. The facts do not state that Daniel held
  his practising certificate continuously from d031 (24 August 2020). That is an
  assumption.

## Why this scope

Witnessing is what the life event asks about. Making and witnessing a statutory
declaration is what the declarant meets. Remote witnessing and false declarations
were asked for in the request. The affidavit's own form and signing limbs
(s 9(2)-(5)) mirror s 12(3)-(5) and were left out to keep the baseline small. The
oath forms (s 4) and court oaths (ss 6(1), 7(1)-(2)) are outside what the declarant or
the lawyer-witness needs here.

## What the Act turns out to say

1. **For statutory declarations, admission is enough, not the practising
   certificate.** Schedule 2 item 20 says "A lawyer". The Interpretation Act makes that
   an Australian lawyer, and the Uniform Law makes that anyone admitted. d034's "by
   virtue of his practising certificate" is right only for affidavits. Asserted.
2. **For affidavits, it takes a practising certificate held for 2 years.** s 8
   requires that the person "is, and has been for at least 2 years, a legal
   practitioner", which means holding a current practising certificate. A lawyer
   admitted 5 years without a certificate is not an authorised witness for an
   affidavit, though they are one for a statutory declaration. Asserted.
3. **A lawyer who worked on the affidavit cannot witness it (s 9(7)).** A JP in the
   same position still can, because the exclusion speaks only of the experienced legal
   practitioner. Statutory declarations have no equivalent exclusion. Asserted.
4. **Schedule 2 does not travel.** It applies only to a declaration "made at a place
   in Western Australia" (s 12(6)(a)). Elsewhere in Australia the witness needs
   local-law authority, or must be a Commonwealth declaration witness. Abroad, the
   witness needs to be a consular official, a local justice or notary, or have
   local-law authority. Asserted.
5. **The Act does not say a statutory declaration or an affidavit may be witnessed by
   video link.** s 7(3) allows an oath or affirmation to be administered "by means of
   an audio link or a video link". Sections 9(3)(c) and 12(3)(c) require presence and
   do not mention links. The Act says nothing about electronic signatures. The COVID-19
   modification of s 9 is not in the text and, by endnote 1M, ceased on
   31 December 2021 unless postponed. The encoding returns "not settled by this Act"
   rather than guess. Other WA laws were not read. Asserted.
6. **The Act creates no false-declaration offence.** The offence is in Criminal Code
   s 169(2): knowingly making a statement "false in a material particular" in a
   statutory declaration carries 5 years, or summarily 2 years and $24,000. A false
   statement on oath, which includes an affidavit, carries 7 years, or summarily 3
   years and $36,000 (s 169(1)). The Commonwealth Act's s 11 offence carries 4 years.
   Asserted.
7. **Pretending to be an authorised witness is an offence (s 17).** It requires
   knowledge, and carries imprisonment for 12 months. Asserted.
8. **Procedural slips are saved by substantial compliance (s 16),** and wording slips
   are saved if they are not material and not misleading. A rubber-stamp signature,
   however, makes the document inadmissible (s 15(3)). Asserted.
9. **The Act defers to the Commonwealth:** anyone before whom a Commonwealth
   declaration may be made can witness a WA declaration, in WA or elsewhere in
   Australia (s 12(6)(a)(ii), (b)(ii)). Because the Commonwealth Regulations are not
   deposited, this is an input in both baselines. Asserted.

## What would need doing before this is worth anything

- Deposit the Statutory Declarations Regulations 2023 (Cth) and any s 18 regulations.
- Read the Electronic Transactions Act 2011 (WA) and any WA remote-witnessing law to
  see whether video-link or electronic declarations are allowed outside this Act.
- Read the uncommenced Evidence Act 2025 s 492(2) amendment.
- Encode s 9(2)-(5), the affidavit's form and the maker's and witness's limbs.
- Check against WA case law on s 16 substantial compliance.
- Run an independent test pass and the human gates.
