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

## Q&A layer (seat and situations as parameters)

Added 6 November 2026 (batch qa13), on the pattern of the Graffiti Vandalism Act 2016 encoding's `gva-seat.l4` (its
design D2, D4 and D8). The layer is `oasda-qa.l4`, with cases in `oasda-qa-cases.l4`. It imports `prelude` and
`oasda-witnesses`; `oasda-witnesses.l4` and `oasda-cases-witnesses.l4` are unchanged. Every exported question takes
`my role` first (`@desc Which of these describes you`) and answers `does not arise for you`, reading nothing else, for
the role it is not about. Every answer type carries that value: `Yes or no`, `Months`, and wrappers round the
baseline's `My standing as a statutory declaration witness`, `My standing as an affidavit witness`, `How my statutory
declaration stands`, `What this Act says about doing it remotely`, `Admissibility under ss 14 and 15` and `Most I
face`. No exported question takes a DEONTIC or EVENT input.

### Roles

The baseline already has the Act's two seats, and they are the two roles.

- `I am making a statutory declaration or an affidavit`: 8 questions. They cover s 5, s 11, the s 12 validity
  question, ss 14 and 15, both Criminal Code s 169 questions, and the two questions it shares with the witness.
- `I am asked to witness a statutory declaration or an affidavit`: 9 questions. They cover "lawyer" (Schedule 2 item
  20), s 12(6), "experienced legal practitioner" (s 8), ss 9(6)-(8) and 10(5), s 13, the two s 17 questions, and the two
  shared questions.
- Shared by both roles: the remote and electronic question (ss 7(3), 9(3)(c), 12(3)(c)) and s 15(2). s 15 speaks of
  "the maker of, or the witness to" the document, so both ask it. These two have no role they are not about.
- Not seats: the court, the chief judicial officer (s 10) and the translator (s 14).

There are 15 exports; the two shared questions are counted once each.

### Situation input

One input, shared by both roles with one name, type and `@desc`: `the document` (`Document`: `a statutory
declaration`, `an affidavit`), placed second. The Act divides by it: Part 3 (ss 8-10) is about affidavits and Part 4
(ss 11, 12) about statutory declarations.

| Question | Role | Does not arise for |
|---|---|---|
| May I affirm instead of swearing for my affidavit (s 5) | maker | `a statutory declaration` |
| May I make a statutory declaration about any matter (s 11) | maker | `an affidavit` |
| Is my statutory declaration valid (ss 12, 16) | maker | `an affidavit` |
| Am I a lawyer for Schedule 2 | witness | `an affidavit` |
| May I witness this statutory declaration (s 12(6)) | witness | `an affidavit` |
| Am I an experienced legal practitioner for affidavits (s 8) | witness | `a statutory declaration` |
| May I witness this affidavit (ss 8, 9(6)-(8), 10(5)) | witness | `a statutory declaration` |

The maker's "What is the most I face for a knowingly false statement" also takes `the document`, second, as its fact.
Criminal Code s 169 sets one maximum for a statutory declaration and another for a statement on oath, which an
affidavit is. It arises for both values. The questions that apply alike to both documents (ss 13, 14, 15, 17, the
s 169 elements, and the remote question) take no situation input.

### Decisions

- **Q1. s 5 is asked for an affidavit only.** The baseline's question already says "for example for my affidavit". A
  statutory declaration is declared, not sworn (s 12(3)(c)), so affirming instead of swearing does not arise for one.
  An oath in court (s 7) is outside both baselines.
- **Q2. The s 169 maximum takes the situation's own input as its fact,** rather than the baseline's `Kind of
  document`. The form then asks "which document" once, for the maker. A helper maps `Document` to `Kind of document`
  and lists both values.
- **Q3. Two baseline inputs were renamed for the form.** Both witness questions called their record `me`, with two
  different types. In the layer they are `me, as a declaration witness` and `me, as an affidavit witness`, so a form
  that merges inputs by name cannot mix them.
- **Q4. The "lawyer" question is asked only for a statutory declaration.** Schedule 2 item 20 is the only place the
  Act uses "lawyer". For an affidavit the test is s 8's "experienced legal practitioner", which has its own question.

### Not covered for the roles

- The witness: the witness's own limbs of s 12(4)-(5) and s 9(4)-(5) as duties (the baseline asks them only inside
  the maker's validity record), and court authorised witness appointment (s 10(2)-(4)).
- The maker: the affidavit's own form and signing limbs (s 9(2)-(5)), as in the baseline; an oath in court (s 7).

### Checks

- `l4 run` on `oasda-qa.l4` and `oasda-qa-cases.l4`, and on the baseline's `oasda-witnesses.l4` and
  `oasda-cases-witnesses.l4` (unchanged): 0 errors and 0 warnings. `l4 check oasda-qa.l4` succeeds.
- `oasda-qa-cases.l4`, generated by the scratchpad script `qa/b13/gen_oasda_cases.py` with the expected values written
  by hand in it: 75 assertions, 75 satisfied. Of these, 13 ask each one-role question for the other role, with every
  other input ASSUMEd. Another 7 ask each situation question with the other document, every later input ASSUMEd. The
  other 55 are in the role and situation that hold (the two shared questions for each role), and 15 of them (one per
  question) compare the answer with the baseline export's own answer on the same facts. With the baseline's 44, the
  encoding has 119 assertions.
- A parameter script (scratchpad `qa/b13/check_params.py`) listed the 15 exports. It found `my role` first in each, and
  `the document` second and identical in name, type and `@desc` in all 8 questions that take it. Each role branch reads
  it first. It found no DEONTIC or EVENT input, and, after the rename in Q3, no shared input with two types or texts.
- Limit (graffiti finding 31): the baseline reads `Place`, `Schedule 2 description` and `Kind of act` through
  OTHERWISE, so an ASSUMEd value of those types that is read is not caught.

### After the independent check (6 Nov 2026)

- **The site's form keeps "May I witness this statutory declaration, and how" open for the maker, and for the witness
  of an affidavit.** The verifier's form-engine run kept it open in all 15 of the maker's states, and for the witness
  with `the document` an affidavit (16 findings).
  - The layer is not wrong here. The question answers `does not arise for you` from `my role` and `the document` alone,
    before `me, as a declaration witness` is read; every case agrees, and no evaluation failed.
  - The cause is the engine. To drop a question it evaluates every combination of its open yes/no and choice inputs,
    up to 1 024 (`PROBE_CAP` in `interact-engine.ts`). The baseline's `Statutory declaration witness` has a `Place`
    (3 values), a `Schedule 2 description` (51 values) and 4 yes/no facts: 2 448 combinations by itself, and 4 896
    with `the document` open.
  - No change to the layer fixes this without changing what is asked: the baseline's s 12 rule reads the whole record,
    and the 51 Schedule 2 descriptions are the Act's own list.
  - The fix belongs in the engine (evaluate one completion with a trace when the combinations are over the cap, and
    settle when only answered inputs were read), as noted for the Civil Liability Act.
- No file was changed for this finding.
