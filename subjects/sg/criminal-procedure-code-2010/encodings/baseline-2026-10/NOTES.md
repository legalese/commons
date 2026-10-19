# Criminal Procedure Code 2010 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual
to whom the law is applied, with the design defaults ruled on 2026-10-18. No `REFUSE`. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

This encoding replaces the one moved to `solutions/Litigate.4/sg/criminal-procedure-code-2010/` on 2026-10-19. That encoding
took the First and Second Schedules (the procedural table of Penal Code offences and the criminal case disclosure laws). Its notes
were read for scope and pitfalls (its fork F1, life imprisonment and the 5- and 10-year limits, is taken here too); none of its
L4 was copied.

**Edition:** 2020 Revised Edition, informal consolidation, version in force from 15/9/2026, as deposited at
`../../registers/source-bundle/CPC2010.txt`.

**Checks:** one module (`cpc-accused.l4`), one case file (`cpc-cases-accused.l4`), 60 assertions satisfied, 0 errors, 0 warnings,
with the stable `l4` of VS Code extension 1.6.98. The case file also runs two `#TRACE`s of the s 68 duty (one kept, one broken);
they print `FULFILLED` and `BREACH` and are not counted as assertions. The case file is built by a generator
(`gen_criminal-procedure-code-2010_baseline.py`, scratchpad) whose expected values were written by hand from the text.

## Seat

**The accused person**: an individual suspected of, arrested for, charged with or convicted of an offence. The Code is
procedure, and almost every section speaks to a police officer, the Public Prosecutor or a court. The person it is applied to is
the one arrested, held, bailed, questioned, tried, sentenced and caned, so every decision is phrased as that person would ask it
(`May a police officer arrest me without a warrant`, `What is my position on bail`, `Can I be caned`).

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers brought in if deposited.** Followed. The First Schedule's
  answers (arrestable, bailable, which court) and the Fourth Schedule's list are Schedules to this Code but are tables of
  hundreds of rows; they are asked as facts the person can read off the Schedule, not encoded. The Criminal Procedure Rules
  (bail grounds, extradition release conditions) and any instrument prescribing offences compoundable under s 242 are not
  deposited: inputs, and the module says so.
- **The actors the text names.** Followed: police officer (and "of or above the rank of sergeant" where s 93 names it), the
  Public Prosecutor, the prosecution, the court, the Magistrate's Court, the District Court, the General Division of the High
  Court, the Registrars.
- **A judgment handed to someone else answered conditionally.** Followed: the court's belief on a prescribed ground, the
  officer's reason to believe particulars false, the court's finding that a fact could reasonably have been mentioned, whether a
  detention is reasonable. Each is a named input, never guessed.
- **The Act's own definitions worked out from facts, borrowed terms asked as facts.** Followed for "arrestable offence" and
  "bailable offence" (s 2(1), from the Schedule columns and other written law) and the "maximum term" test of ss 7 and 8.
  "Fine-only offence" is asked as a fact ("punishable only with a fine"), which is its whole definition.
- **One case is the text's natural unit.** Followed: one offence, one arrest, one bail decision, one sentence.
- **The Act's own terms, each with a plain gloss.** Followed, glosses in comments.
- **Operative sections in scope, machinery out.** Followed, but the Code is very large (sections numbered to 429, and seven Schedules), so
  only the provisions the accused most meets are taken (next section).

## Why this scope

From the accused's seat, the questions met first are: may I be arrested, how long can I be held, will I get bail, must I answer,
what happens if I stay silent, which court will try me and what is the most it can give me, can it be settled, can I be caned,
and can I appeal. The encoding takes ss 2(1), 7 to 9, 22(2), 23(5) and (6), 64, 65, 67, 68, 92 to 95, 232, 241, 242, 261, 303,
325, 328, 375 and 377(1), (2).

Left out: the First to Seventh Schedules as data; consent to prosecute (s 10); the rest of Part 4 (investigation powers,
audiovisual recording rules, the Third Schedule); warrants, summonses, searches and proclamations; the criminal case disclosure
procedures; charges and trial procedure; evidence beyond s 261; the presumptive minimum sentence (s 303A); community sentences,
reformative training, corrective training and preventive detention; criminal revision and the rest of the appeal Part;
everything else in the machinery. s 93(3) and (3B) are summarised in a comment, not encoded as a limb.

## What the Act turns out to say

1. **A fine-only offence keeps the right to bail even where the court fears flight.** s 92(3) lets a court refuse release on a
   bailable offence only where the offence "is not a fine-only offence". Asserted.
2. **A non-bailable charge does not mean no bail.** s 93(1) lets a sergeant or above, or the court, release on bail, and s 93(2)
   makes release mandatory where there are no reasonable grounds to believe the accused committed it. Only s 95(1) (death or
   life, a court's belief on a prescribed ground, an extradition warrant) forbids release, and s 95(2) still lets the court
   release a juvenile or a sick or infirm accused, or a capital accused with an alternative punishment tried below the High
   Court. Asserted (not the juvenile, sick or infirm limb).
3. **An extradition warrant overrides a bailable offence.** s 95(1)(c) forbids release whatever the offence, unless the court is
   satisfied of the Rules' conditions. Asserted.
4. **The 7-year line for a personal bond counts enhanced penalties.** s 93(1D) and its Illustration: Penal Code s 324 with s 74A
   carries 14 years, so no personal bond. A court needs the prosecution's consent; a sergeant does not, and an officer below sergeant
   cannot release on personal bond for a non-bailable offence. Asserted (not the sergeant limb).
5. **The police have 48 hours, journey time excluded; 24 for a s 65 arrest where the bond is refused.** And s 68(1) also
   requires the period to be reasonable, so 48 hours is a ceiling, not an allowance. Asserted, and traced as a regulative rule.
6. **A District Court can try a 20-year offence if the accused consents.** s 9(3)(c), on the Public Prosecutor's application;
   but never an offence punishable with death. Reading taken (an inference, as in the moved encoding): life imprisonment is not
   a "term" within the 5- or 10-year limits of ss 7 and 8. Asserted.
7. **The sentencing powers are lower than the trial powers.** A Magistrate's Court may try a 5-year offence (s 7(1)(a)) but
   may sentence only up to 3 years, $10,000 and 6 strokes (s 303(3)); a District Court 10 years, $30,000, 12 strokes. The High
   Court has no s 303 ceiling: NOTHING. Asserted for the District Court term, the Magistrate's Court fine and strokes, and
   the High Court.
8. **The right not to incriminate oneself is in the duty to answer itself.** s 22(2) binds a person examined "to state truly",
   "except that the person need not say anything that might expose the person to a criminal charge, penalty or forfeiture". But
   s 261 lets the court draw inferences from a failure to mention, when charged, a fact later relied on. Asserted.
9. **The Public Prosecutor's composition is capped at the lower of half the maximum fine and $5,000** (s 242(1)). After charge it
   "has the effect of an acquittal"; a victim's composition with consent after charge requires the court to order "a discharge
   amounting to an acquittal" (s 241(5)). Neither section states the effect of compounding before investigations begin; the
   encoding says so with a `not stated by the Code` value. Asserted.
10. **A discharge when the Public Prosecutor drops the charge is not an acquittal unless the court directs** (s 232(2)), except
    in s 147 cases or on a later application. Asserted.
11. **Women and men over 50 cannot be caned, and the court may substitute up to 12 months.** s 325(1), (2); the limit at one
    sitting is 24 strokes for an adult, 10 for a juvenile (s 328(6)). Whether the two 12-month powers (ss 325(2), 328(2)) can
    both be used is not said: NOTHING. Neither applies to an offence before 2 January 2011. Asserted for the age limit, the juvenile
    limit, the 12 months and the NOTHING.
12. **A guilty plea limits appeal to the sentence** (s 375), and the 14 days for an appeal against conviction run from the date
    of the sentence, not of the conviction (s 377(2)(a)). Asserted.

## What would need doing before this is worth anything

- The First Schedule's 478 rows should be brought in as data so that "arrestable", "bailable" and "which court" are worked out
  from the Penal Code section, not asked; the moved encoding's notes say it holds that table.
- The Criminal Procedure Rules (the prescribed grounds for refusing bail) were not retrieved.
- s 93(3) and (3B), s 97 (High Court bail), s 102 and s 103 (revocation and absconding) are not encoded.
- No case law was read, in particular on the reasonableness of detention under s 68(1) or on inferences under s 261.
- Nothing here has had an independent test pass or a domain expert's reading.
