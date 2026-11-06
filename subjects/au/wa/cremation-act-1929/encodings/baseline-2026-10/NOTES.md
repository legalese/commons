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

## Q&A layer (seat and situations as parameters)

Added on 6 November 2026, after the graffiti encoding's design (D2, D4, D8). The baseline's files are unchanged; the layer is added beside them.

- `cra-qa.l4` imports `prelude` and `cra-cremation`. It has 30 exported questions.
- `cra-qa-cases.l4` imports the same and `cra-qa`. It has 203 cases.

### Roles

`my role` is the first input of every question. A question about another role answers `does not arise for you` and reads nothing else.

- **`I am arranging the cremation of someone who has died`**: the baseline's seat (Chloe c086, Oliver c098). It has 17 questions, one for each baseline export. Each calls the baseline's function and wraps the answer: `yes if`, `amount`, `imprisonment for` (months), or `the answer is` for `What the referee will do`.
- **`I am the spouse, de facto partner or next of kin of someone who has died`**: the people s 13(1) gives a written objection. It has 3 questions:
  - does my objection stop the cremation;
  - does the deceased's own written direction stop it (s 8A(b));
  - may the ashes be delivered to me (s 7(1)).
- **`I run a licensed crematorium`**: the licensee, bound by ss 3, 9, 10, 13(1), 14, 7 and 15(4). It has 6 questions:
  - may I cremate this body now;
  - may I deliver the ashes to this person;
  - may the ashes leave for this purpose;
  - am I guilty of my employee's or agent's offence;
  - the fine;
  - the imprisonment.
- **`I am the doctor certifying the cause of death`**: the person ss 8A(g) and 12 address. It has 4 questions:
  - can my certificate support the permit;
  - would signing be an offence (s 12 with s 15(1));
  - the fine;
  - the imprisonment.

The medical referee, the coroner, the Attorney General and the Chief Health Officer are not seats.

### Situation inputs

All are BOOLEAN. Each comes straight after `my role`. FALSE gives `does not arise for you` without reading anything else.

| Input | Roles | Questions |
|---|---|---|
| `the medical referee refused my application for a permit` | arranger | the s 8(6) review (1) |
| `the body has been cremated` | arranger, family, crematorium | the s 7 ashes questions (2 + 1 + 2) |
| `I am said to have committed an offence under this Act` | arranger, crematorium, doctor | the s 15(1) fine and imprisonment (2 + 2 + 2) |
| `I have objected in writing to the body being cremated` | family | does my objection stop the cremation (1) |
| `an employee or agent of mine is said to have committed an offence at or near my crematorium` | crematorium | s 15(4) (1) |

### Decisions

- **The baseline's facts stay in its `Death` record.** The record holds the objection, the attested wish, the direction against cremation and the coronial facts, and the arranger's questions take it whole. None of those facts is made a separate situation input: a second input for a fact the record holds could contradict it.
- **The family's questions build the record from plain answers.** `the deceased's wishes as` builds the baseline's `Death`, and the baseline's s 13(1) and s 8A(b) tests decide. Only the four fields those tests read come from the answers. The rest are filled with the plain case, which neither test reads.
- **The crematorium's cremation question calls the baseline's.** It runs `May the cremation go ahead now`. s 13(1) binds a person who "knows" of the objection, so the @desc asks for the objections the licensee knows of. The baseline does not model knowledge separately.
- **s 15(4) is a helper of the layer, not the baseline's.** It gives yes unless the licensee proves no act or neglect of theirs contributed.
- **The doctor's offence question follows s 12 only.** Signing a certificate barred by s 8A(g) (a relative, or the referee's partner) makes it unusable, but s 8A(g) addresses the referee, not the doctor. Only s 12's "No person ... shall give or sign" is an offence of the doctor's.
- **The penalty questions take the offence situation in every role.** In each role they settle on the role and that input alone.

### Not covered for the new roles

- **Crematorium:** licensing and its revocation (ss 4-6, 16), and the register and notices (regs 18-20).
- **Doctor:** the Births, Deaths and Marriages Registration Act 1998 s 44 duty itself.
- **Family:** whether "next of kin" follows reg 3's order (as in the baseline), and the ashes once removed.

### Cases

The 203 cases in `cra-qa-cases.l4` are:

| Kind | Cases |
|---|---|
| Each question for the three roles it is not about, every other input ASSUMEd | 90 |
| Each situation question with FALSE, later inputs ASSUMEd | 14 |
| Own role, worked by hand | 56 |
| Arranger's answer equal to the baseline export's answer on the same facts | 32 |
| Mirror cases | 11 |

The mirror cases ask three things from more than one seat:

- Sue's objection, with and without Graham's attested wish, from the arranger, the family and the crematorium;
- the ashes in c098, from all three seats;
- the inheriting doctor, from the arranger and the doctor.

All 203 cases are satisfied, as are the baseline's 62. There are 0 errors and 0 warnings. `l4 check cra-qa.l4` succeeds.

A scratch script checked every @export:

- `my role` is first;
- each situation input is identical wherever it is used;
- no input is DEONTIC or EVENT;
- each role branch reads its situation first.

### Fix after verification (6 November 2026)

An independent check through a local jl4-service form engine found that some inputs of the same name had different @desc values. The form shows one label per name. Fixed here (no answer changes; the 203 cases and the baseline's 62 are unchanged and satisfied):

- `the death` (8 labels), `me` (2) and `a permit has been granted` (2) now carry one @desc each, worded to cover every question that takes them.
- `at a licensed crematorium` meant a crematorium licensed under the Act for the arranger and the crematorium in the licence for the licensee. The licensee's input is now `at the crematorium named in my licence`.

Not changed:

- **Record inputs in questions of another role.** The arranger's questions take the `Death` record `the death` (and the licensee's s 9-14 question takes it too), so the form engine keeps them for the family, the crematorium and the doctor, and keeps the licensee's question for the arranger: it cannot settle a question while a record input is unanswered. The code already answers `does not arise for you` for those roles without reading the record; the gap is in how the engine decides what to drop (it should evaluate with the role alone first). Flattening the baseline's record into separate fields would restate the baseline, against the layering rule (see the decision above on the `Death` record).
