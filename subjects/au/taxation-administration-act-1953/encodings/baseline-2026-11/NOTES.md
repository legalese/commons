# Taxation Administration Act 1953 (Cth) -- baseline encoding, Part IVD: the tax whistleblower

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18 and the 2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE
except in `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as
advice.

This encoding is a new layer beside the two existing ones, `baseline-2026-10` (the taxpayer: PAYG withholding and
instalments, general interest charge, objections, administrative penalties, private ancillary funds) and `naive-2026-10`
(the same seat, first pass). Neither was touched, and nothing here imports them. Neither covers Part IVD.

One module and a case file:

- `taa-whistleblower.l4` -- 16 exported questions of the whistleblower in four `§§` groups, with the s 14ZZW prohibition
  as one regulative rule and its trace helper;
- `taa-whistleblower-cases.l4` -- the cases.

Part IVD fixes no periods, so there is no date module.

## Edition

- **Act:** Taxation Administration Act 1953, Compilation No. 226, compilation date 27 August 2026 (register id
  C2026C00393), as deposited at `../../registers/source-bundle/C1953A00001.txt`.
- **Regulations:** Taxation Administration Regulations 2017, Compilation No. 17, compilation date 27 August 2026
  (register id F2026C00849), as deposited at
  `../../../taxation-administration-regulations-2017/registers/source-bundle/F2017L01227.txt`: Division 3A, ss 13A and
  13B, read in. Nothing else in the Regulations prescribes for Part IVD (findings 2 and 3).
- **Penalty unit:** Crimes Act 1914 s 4AA ("$330 (subject to indexation under subsection (3))"); the indexed value is
  published by notifiable instrument, so it is an input, as in `baseline-2026-10`.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. A
scratch file (since deleted) with two deliberately wrong assertions on the trace helper showed both as
`DiagnosticSeverity_Error`, "assertion failed", and an `#EVAL` of the trace of an unauthorised revelation showed
`DEONTIC BREACHED`.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `taa-whistleblower.l4` | 0 | 0 | 0 | 0 |
| `taa-whistleblower-cases.l4` | 0 | 0 | 114 | 114 |

Every expected value was worked by hand from the text. The edges: every head of s 14ZZU and of s 14ZZV(1) to (4), and
each body-corporate, trust and partnership recipient asked of the wrong kind of entity; each s 14ZZT route met and
failed one condition at a time, (1) and (1A) both met, (1A) through the Commissioner, (3) and (3B) without being an
eligible whistleblower, (3A) and a journalist; the s 14ZZX(1)(c) routes and the falsity exception; both s 14ZZZB
exceptions; each authorised recipient of s 14ZZW(2) and Regulations s 13B, consent, and the s 14ZZW(3) exception with
each limb missing and for the identity itself; both s 14ZZY offences with each element missing; the penalties at $330
and at an indexed $345; each s 14ZZZ route with each condition missing; the s 14ZZZA order lists with and without the
employer and reinstatement; s 14ZZZA(2) for dismissal, forced resignation, neither, and no compensation order; both
s 14ZZZC grounds; and one whole story chaining the questions.

## Seat

**The individual who discloses, or may disclose, information about an entity's tax affairs, and who brings or may
bring a claim for what is done to them because of it** (`taa-whistleblower.l4`): "Am I an eligible whistleblower?", "Is
the person I told an eligible recipient?", "Does my disclosure qualify?", "Am I protected, and is what I told the ATO
kept out of evidence?", "If I am sued, who must prove my immunity?", "Can I be made to reveal my identity to a court?",
"Was revealing my identity an offence?", "Was harming or threatening me an offence, and what is the most they face?",
"Can the court order a remedy, which orders, must it consider my time out of work, and can I be made to pay costs?".

No second seat. Part IVD's duties fall on whoever learns the discloser's identity and on whoever victimises them, and
its compensation orders on them and their employer. An employer seat could be added beside this one (ss 14ZZZ(2A),
14ZZZA(1)(b), (3)).

No seat for the Commissioner, the Tax Practitioners Board, the Inspector-General or the court: their functions, views
and satisfaction are asked as facts.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Regulations' ss 13A and 13B are read in;
  the penalty unit is an input.
- **The actors the text names.** Followed: the discloser, the entity, the associate, the Commissioner, the Tax
  Practitioners Board, the eligible recipient, the legal practitioner, the medical practitioner or psychologist, the
  first person, the second and third person, the officer or employee, the body corporate, the employer, the court or
  tribunal.
- **Judgments answered conditionally.** Followed: "considers that the information may assist", "reasonable grounds to
  suspect", "reasonably necessary", "all reasonable steps", "believes or suspects", "the reason, or part of the reason",
  "intends ... or is reckless", the court's being "satisfied", "thinks it necessary in the interests of justice",
  "vexatiously or without reasonable cause" are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: eligible whistleblower (s 14ZZU), eligible
  recipient (s 14ZZV with Regulations s 13A), qualifying disclosure (s 14ZZT), detriment (s 14ZZZAA, in the
  descriptions). Asked: "entity" (ITAA 1997 s 960-100), "associate" (ITAA 1936 s 318), "officer" and "senior manager"
  (Corporations Act 2001), "registered tax agent or BAS agent" (Tax Agent Services Act 2009).
- **One case.** One disclosure; one course of detrimental conduct.
- **The Act's terms with plain glosses.** Followed, in each `@desc`.
- **Operative sections in; machinery out.** Followed (see Scope).
- **Departure D1: chained answers as inputs (fork F9).** Six questions take the answer of an earlier one as an input
  whose description names it (am I an eligible whistleblower; is the person I told an eligible recipient; how did my
  disclosure qualify; can the court order a remedy), as the Corporations Act claimant baseline does. The form should ask
  the earlier question first.

## Scope

The focus named Part IVD, tax whistleblowers. Part IVD is small, so it is encoded whole but for two machinery sections.

**In:** s 2 (the definitions of eligible recipient and eligible whistleblower), ss 14ZZT, 14ZZU, 14ZZV, 14ZZW, 14ZZX,
14ZZXA, 14ZZY (with its Penalty lines), 14ZZZ, 14ZZZAA, 14ZZZA, 14ZZZB, 14ZZZC, 14ZZZD (in the s 14ZZZ question's
description); Regulations ss 13A, 13B.

**Regulative rule:** one. s 14ZZW(1): the person who learned the discloser's identity through the qualifying disclosure
SHANT reveal it, or what is likely to identify them, unless permitted (s 14ZZW(2), (3)), LEST breach; run by EVALTRACE
inside `Was revealing my identity an offence`, which takes only plain facts. The act asked about happens at time 0 and
the window closes at 1 (fork F6).

**Out, and why:**
- s 14ZZTA (which Act information given under s 14ZZT(1A) counts as obtained under, for the secrecy provisions of
  Schedule 1 s 355-30 and the Tax Agent Services Act 2009 s 90-1): information-handling machinery; it does not change
  what the discloser may claim.
- s 14ZZZE (Commonwealth compensation where Part IVD acquires property otherwise than on just terms): a constitutional
  safety valve for a person whose contract rights the Part cuts off, not a whistleblower's claim.
- The application provisions of the amending Acts and Regulations Division 7 (transitional): the encoding answers for
  disclosures under the law as compiled.
- Schedule 1 Division 355 (confidentiality of taxpayer information): the ATO's own secrecy duties, not Part IVD's.
- Crimes Act 1914 s 4B(3) (a body corporate's fine up to five times the individual's): outside the Act; the fine
  question says so.
- The Criminal Code's fault elements and defences for the ss 14ZZW and 14ZZY offences: asked as facts.

## Fork register

Each line: the provision, the function, the answer taken, the other reading.

- **F1** s 14ZZT(1) and (1A) both met by one disclosure to the Commissioner -- `Does my disclosure qualify for
  protection` -- (1) is named; the consequences are the same (s 14ZZX(1)(c) covers both) -- (1A) named, or both.
- **F2** s 2 "has the meaning given by section 14ZZU" and "... 14ZZV" -- `Am I an eligible whistleblower`, `Is the
  person I told an eligible recipient` -- a definition handed to a list (ruling of 2026-11-05 (a)): FALSE where no head
  holds, so both answer a plain BOOLEAN -- NOTHING outside the list, as the Corporations Act claimant baseline answers
  for s 1317AAB (whose list has no such hand-off).
- **F3** s 14ZZX(1)(c) "if the disclosure was a disclosure of information to the Commissioner or the Tax Practitioners
  Board" -- `Is my disclosure kept out of evidence against me` -- a qualifying disclosure to anyone else fails the
  paragraph's own "if": JUST FALSE -- NOTHING (silent), as the Corporations Act sibling reads s 1317AB(1)(c).
- **F4** s 14ZZX(1)(c) "other than proceedings in respect of the falsity of the information" -- same function -- JUST
  FALSE in falsity proceedings -- NOTHING.
- **F5** s 14ZZZB "except where" (c) or (d) -- `Am I shielded from revealing my identity to a court or tribunal` -- an
  exception met lifts the shield: JUST FALSE -- NOTHING (the text says when the bar does not hold, not that disclosure
  may then be required).
- **F6** s 14ZZW(1) as a prohibition with no period -- `the duty to keep my identity confidential` -- one act asked
  about, at time 0, in a window of 1; a permitted act does not match the prohibited pattern and the window passes
  FULFILLED -- a standing prohibition with no window (a trace can then never be FULFILLED on the stable `l4`).
- **F7** s 14ZZY(1)(c), (d) "believes or suspects ... is the reason, or part of the reason" and (2)(c) "makes the threat
  because a person makes ... or may make" -- `Did they commit the victimisation offence` -- one input for "the reason
  or part of it" serves both, with the belief or suspicion asked separately for (1) -- separate inputs for each
  subsection's causal test (the threat limb's "because" may be narrower than "part of the reason").
- **F8** s 14ZZZA(2) "in making an order mentioned in paragraph (1)(a) or (b)" -- `Must the court consider how long I
  will be out of work` -- NOTHING where no compensation order is made (limited by its own wording) -- JUST FALSE.
- **F9** chained answers (departure D1) -- six questions -- an earlier answer taken as an input -- the earlier facts
  repeated.
- **F10** s 14ZZT(3A) "the entity is prescribed by the regulations", none prescribed -- `Does my disclosure qualify for
  protection` -- does not qualify on these facts -- NOTHING (a later regulation could prescribe a union or association).

## The rulings on negatives (recorded word for word, as the encoding guide requires)

From `docs/ENCODING-GUIDE.md`, section 5, as it stood on 7 November 2026:

These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.
The rule of 2026-10-29 for what `JUST FALSE` and `NOTHING` mean is the convention the rows written since then follow (applied in legalese/commons#30 and #37); it was assumed, not ruled as a whole, and the rulings below settle parts of it.
In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (Meng, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. Meng's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with GM where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

**How this encoding applies them.** JUST FALSE (or FALSE) where the text says no in its own words: ss 14ZZU and 14ZZV
(definitions handed to lists by s 2), s 14ZZT ("qualifies ... if"), s 14ZZX(1)(c) ("if", fork F3; "other than", fork
F4), s 14ZZXA ("If, in civil or criminal proceedings"), s 14ZZZB ("except where", fork F5), s 14ZZW(1) and s 14ZZY(1),
(2) ("commits an offence if"), s 14ZZW(3) ("does not apply if"), s 14ZZZ(1), (2), (2A) ("may make an order ... if"), s
14ZZZA(2) ("If"), s 14ZZZC(3) ("only if"). NOTHING, tagged, where the text does not answer: s 14ZZX and s 14ZZZB for a
disclosure that does not qualify (silent); s 14ZZZA(2) where no compensation order is made (limited by its own wording).

## What the Act turns out to say

1. **Part IVD has no route to the press or a member of parliament.** Unlike Corporations Act s 1317AAD, there is no
   public interest or emergency disclosure: a disclosure to a journalist qualifies under no subsection of s 14ZZT, so
   the s 14ZZX immunity, the s 14ZZW confidentiality offence and the s 14ZZZB shield do not reach it (s 14ZZY and
   s 14ZZZ still can, since they turn on the victimiser's belief that a qualifying disclosure "could" be made).
   Asserted.
2. **s 14ZZT(3A) is a dead route at this compilation.** It protects a disclosure to a member-based entity "prescribed by
   the regulations" (presumably a union or professional association), but the deposited Regulations (Compilation No.
   17) prescribe none: Division 3A has only s 13A (for s 14ZZV(1)(d)) and s 13B (for s 14ZZW(2)(d)). Asserted.
3. **s 14ZZU(h) prescribes no one either.** No individual is prescribed for the paragraph, so the eligible whistleblower
   list is in effect (a) to (g).
4. **A disclosure to the ATO or the Tax Practitioners Board needs no reasonable grounds.** s 14ZZT(1) and (1A) ask only
   that the discloser "considers that the information may assist"; s 14ZZT(2), for an eligible recipient, also requires
   reasonable grounds to suspect misconduct. Asserted.
5. **There is no personal work-related grievance carve-out.** Corporations Act s 1317AADA excludes such grievances from
   its protections; Part IVD has no equivalent, so a grievance that also concerns the employer's tax affairs can
   qualify.
6. **The evidence shield of s 14ZZX(1)(c) is only for disclosures to the Commissioner or the Board.** A qualifying
   disclosure to the Inspector-General of Taxation (an eligible recipient under Regulations s 13A) or to the entity's
   auditor or tax agent gets the immunities of (a), (b) and (2) but not (c) (fork F3). Asserted.
7. **The s 14ZZW(3) investigation exception never covers the discloser's identity,** only information likely to lead
   to it, and only with all reasonable steps taken. Asserted.
8. **s 14ZZW(2) has no pass-on for the regulator.** Corporations Act s 1317AAE(3) authorises ASIC, APRA and the AFP to
   pass the identity on to another authority; s 14ZZW(2) authorises a disclosure "to" the Commissioner, the AFP, a
   lawyer, the prescribed bodies (Inspector-General, Tax Practitioners Board, ACNC Commissioner) or with consent, but
   not one "by" the Commissioner to, say, ASIC or a State police force. Whether an ATO officer's onward disclosure is
   an offence, or is answered by Schedule 1 Division 355, the text leaves open.
9. **Reinstatement is for termination; a forced resignation counts only for compensation.** s 14ZZZA(1)(e) speaks of
   "the termination, or purported termination"; s 14ZZZA(2) adds "(including detrimental conduct that forces or forced
   the person to resign)" for the compensation orders only, as in the Corporations Act. Asserted.
10. **In a compensation claim the claimant need only show the harm.** s 14ZZZ(2B) puts on the claimant only the
    evidential onus for paragraph (1)(a) (the detriment or threat) and, against a company, (2A)(a) and (d); the
    belief or suspicion and its being part of the reason fall to the other side to disprove. The criminal offence of
    s 14ZZY has no such shift.

## Before relying on it

- An independent test pass, and a lawyer's look at forks F2, F3, F5 and F6.
- An employer seat (ss 14ZZZ(2A), 14ZZZA(1)(b), (3)), and the borrowed terms (entity, associate, officer, senior
  manager) worked out in later layers.
- A check, when a newer compilation of the Regulations is deposited, whether anything is prescribed for ss 14ZZT(3A)
  and 14ZZU(h).
