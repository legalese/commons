# Cremation Act 1929 (WA) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design
defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `cra-cremation.l4`, and one case file, `cra-cases-cremation.l4`, generated
by a script (scratchpad `gen_wa_cremation-act-1929_baseline.py`) from a table of
facts. The expected values were written by hand from the text. Every question is
exported with `@export` and `@desc` for Legalese Cloud.

## Edition

- **Act:** compilation from legislation.wa.gov.au (mrdoc 37196, retrieved
  7 September 2026), as deposited at `../../registers/source-bundle/mrdoc_37196.txt`.
  Its compilation table runs to the Public Health (Consequential Provisions) Act 2016
  (Reprint 6 as at 27 October 2017). Section 285(2) of that Act is listed as
  uncommenced and is not reflected.
- **Regulations:** Cremation Regulations 1954, version 04-o0-00, currency from
  1 July 2026 (mrdoc 49624, retrieved 20 October 2026), as deposited at
  `../../../cremation-regulations-1954/registers/source-bundle/mrdoc_49624.txt`.
  Schedule 2 was last amended by SL 2026/112. Used for:
  - the permit fee (Sch 2 item 3);
  - the hours that fee turns on (r 14(2));
  - what must accompany an application (r 11, 12);
  - the referee's notice of refusal (r 14(4));
  - the 24 hours printed on the permit (Sch 1 Form 9).

## Checks

`l4 run cra-cases-cremation.l4` with the stable `l4` of VS Code extension 1.6.98:
**62 assertions satisfied, 0 errors, 0 warnings.** The module alone also runs with no
errors or warnings.

## Seat

**The family member or executor arranging a cremation.** The Act is applied to that
person when they apply for a permit, and to their dead relative's body. Nearly every
operative provision addresses someone else: the medical referee (ss 8, 8A, 10), the
crematorium (ss 3, 7, 9), the coroner or Attorney General (s 14). Each is encoded as
what it means for the person arranging. The questions are:

- whether they may apply;
- whether they must make a declaration;
- what they will pay;
- whether the permit must be granted;
- whether the coroner must be involved;
- whether the cremation may go ahead;
- whether the ashes may be delivered to them.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The
  Cremation Regulations 1954 are deposited and are used for the fee, the hours, the
  accompanying certificates and the 24-hour wait.
- **The actors the text names.** Followed: the administrator, the person with the
  administrator's written authority, the medical referee, the certifying doctor, the
  coroner, the Attorney General, the Chief Health Officer, the spouse, de facto
  partner and next of kin, and the licensed crematorium.
- **Judgments handed to others answered conditionally.** Followed. The referee's
  satisfaction (s 8(3A)(c), s 8A(c), (d)), how the death appears to the referee
  (s 8(5)), the coroner's intention and certificate (s 8A(e), (f)), a s 14 order and
  the Chief Health Officer's order (s 8A(b)) are all inputs, marked "(referee)" or
  "(coroner)".
- **The Act's own definitions worked out; borrowed terms asked.** Followed.
  - Worked out: "administrator" (s 2).
  - Asked as facts: "next of kin" (the Act does not define it; r 3's "nearest
    surviving relative" applies to the regulations only), "best right to apply for
    administration" and "lawful custody".
- **One case is the natural unit.** One death, one application.
- **The Act's own terms with a gloss.** Followed in the comments.
- **Operative sections in scope; machinery out.** Followed. Licensing, revocation,
  appointment of referees and regulation-making are out.

## The lives

- **chloe c086** (2052-08-19, a Monday). Graham dies at 82 at home. The funeral
  director registers the death. A cremation permit is needed, and the death is not
  reportable. His will (c087) makes Chloe executor.
  - Who may apply: Chloe as executor, or the funeral director on her written
    authority.
  - Must the funeral director declare? Yes, unless they apply as the person holding
    the body.
  - The fee: $89.10 on a Monday morning.
  - The referee must grant the permit, the coroner need not be involved, and the
    cremation may proceed once 24 hours have passed.
  - Variants test Sue's objection, Graham's own written direction, a related or
    interested doctor, a suspicious death, a coroner's investigation and a s 14 order.
- **chloe c098** (2088-11-02). Chloe dies at 85; Oliver is her executor.
  - Oliver's permit is granted; Ella's application, without his authority, is not.
  - Under s 7 the ashes may be delivered to Oliver, who obtained the permit, and not
    to Ella.
  - If Chloe's attested will asked for cremation, Oliver must use all reasonable
    endeavours to carry it out (s 13(2)).

The scenario does not say that each death was natural and certified by the
deceased's own GP, that the funeral director applied on Chloe's authority, or that
Ella wanted the ashes. These are assumed in the cases.

## Why this scope

The Act is short, and the seat meets almost all of its operative part:

- the permit (ss 8, 8A, 10, 12);
- the deceased's and the family's wishes (s 8A(b), s 13);
- the coroner (ss 8(5), 8A(e), (f), 14);
- the cremation itself (ss 3, 9);
- the ashes (s 7);
- the offence (s 15).

What is left out is machinery or addresses only the crematorium:

- licensing and its revocation (ss 4-6, 16);
- the crematorium's register and notices (regs 18-20);
- cremation elsewhere than in a crematorium (s 3(2), regs Part V). This is asked only
  as the fact that the crematorium is licensed.

Section 8B (stillborn children) is a separate path that neither life meets. It is left
out and named.

## What the Act turns out to say

1. **A funeral director holding the body is an "administrator".** Section 2's
   "administrator" includes "any person having the lawful custody of the body".
   Such a funeral director may apply in their own right and need not make the s 8(3B)
   statutory declaration. Applying on the executor's written authority does not make
   them an administrator, so the declaration is then required. Asserted.
2. **Being the widow is not enough on its own.** Sue may apply only if the medical
   referee is satisfied the administrator will not apply, of her reason, and that she
   is a proper person (s 8(3A)(c)). Asserted.
3. **When the conditions are met, the permit must be granted.** Under s 8(2) the
   referee "shall ... grant the permit"; it is not a discretion. A refusal for any
   reason other than s 8(5) can be taken to the State Administrative Tribunal
   (s 8(6)). The referee must tell the applicant of that right but need not give
   reasons (r 14(4)). Asserted.
4. **A suspicious death goes to the coroner, not to review.** If the death appears
   violent, unnatural or suspicious, the referee "shall refuse" and report it to the
   nearest coroner (s 8(5)). The permit then waits on a coroner's certificate
   (s 8A(e)), and that refusal is not reviewable. The same wait applies when the
   coroner has signified an intention to investigate (s 8A(f)). Asserted.
5. **On the text, a coroner's certificate does not replace the doctor's
   certificate.** Section 8A(a) requires a certificate of cause of death "under
   section 44" of the Births, Deaths and Marriages Registration Act 1998, with no
   exception. Yet s 44(5) of that Act relieves the doctor of the duty when the death
   must be reported to a coroner, and reg 12 lets a coroner's certificate (Form 8)
   stand in for the doctor's Form 7. Read literally, a reportable death with no s 44
   certificate cannot be cremated even after the coroner certifies. That is probably
   not what is meant, and it is the most important question for a lawyer. Asserted
   (the literal reading).
6. **The deceased's "no" needs only writing; their "yes" against the family needs
   attestation.** A written direction against cremation bars the permit unless the
   Chief Health Officer orders cremation (s 8A(b)). A written objection by the
   spouse, de facto partner or next of kin bars applying, granting and cremating
   (s 13(1)). It is overridden only by a will, codicil or signed and attested writing
   in which the deceased directed or desired cremation. The administrator then has a
   duty to use all reasonable endeavours to carry that wish out (s 13(2)). Asserted.
7. **Applying in the face of a known objection is itself an offence.** Section 13(1)
   forbids "apply[ing] for" the permit. Section 15(1) makes any contravention an
   offence punishable by a fine of up to $400 or up to one year's imprisonment.
   Asserted.
8. **The doctor's family is barred from certifying, but the spouse is not named.**
   Section 8A(g) bars a certifying doctor who is the deceased's parent, child,
   brother, sister, uncle, aunt, niece or nephew, or who is the referee or in
   partnership with the referee. A spouse is not listed. Section 12, however, bars
   anyone who knows they will take property on the death from signing "any
   certificate ... for any of the purposes of this Act". This encoding reads s 12
   with s 10 ("the proper certificate") as making such a certificate unusable, which
   is an inference. Asserted.
9. **The fee depends on when the permit is given.** It is $89.10 between 9 am and
   5 pm on a weekday, or 9 am to noon on a Saturday, public holidays excluded, and
   $147.40 at any other time (Sch 2 item 3, r 14(2)). The encoding reads "between
   9 am and 5 pm" as up to but not including 5 pm. Asserted.
10. **The permit is not valid until 24 hours after death.** This rule appears only on
    the face of the prescribed permit (Form 9), not in the Act or in the body of the
    regulations. Asserted.
11. **A s 14 order stops the cremation, not the permit.** The Attorney General or a
    coroner may forbid cremation absolutely, or until organs are removed and lodged.
    The order binds everyone who knows of it, but s 8A does not list it as a ground
    for refusing the permit. Asserted.
12. **The ashes: the Act permits delivery, it does not give a right to them.** It is
    "lawful" for the crematorium to deliver the ashes to "the person who obtained the
    permit" for removal (s 7(1)). Otherwise they may leave the crematorium only for
    burial on its site (s 7(2)). The Act gives no one else a claim and says nothing of
    the ashes once removed. Ella, not the permit holder, cannot have them delivered to
    her. Asserted.

## What would need doing before this is worth anything

- A lawyer's view on finding 5: how WA practice handles coroner's cases under
  s 8A(a). The Coroners Act 1996 and Coroners Regulations 1997 Form 4 were not read.
- A view on whether "next of kin" in s 13 is read with reg 3's order of priority.
- The Health (Miscellaneous Provisions) Act 1911 and Public Health Act 2016 powers
  behind the Chief Health Officer's order were not read.
- No case law was searched.
- No independent test pass and no human gate.
