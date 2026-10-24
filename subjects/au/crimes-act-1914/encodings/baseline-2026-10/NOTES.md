# Crimes Act 1914 — baseline encoding, the accused's seat

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it; the two cases outside the encoding (a terrorism arrest, and a State conviction asked about in a State by anyone but a Commonwealth authority) answer `not covered`, and tests assert both.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0083` in `subjects/au/requirements.jsonl`. There was no earlier encoding of this Act to keep.

Every question is a function named as the person would ask it, with `@export` and a `@desc` on every input. There are 23 exported questions, grouped under `§§` headings in the order a person meets them — arrest, questioning, detention, sentencing, and afterwards — each heading naming its situation ("if a police officer wants to arrest you", "if you have been arrested", "if you are being sentenced", "if you have a conviction").

## Edition

The compilation registered as **C2026C00368** (Compilation No. 167, compilation date 27 August 2026, including amendments up to Act No. 66, 2026 and Act No. 70, 2026; three volumes in one file), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C1914A00012.txt`. Part IAA Division 4 is at lines 1386–1771, Part IB at 7416–9047, Part IC at 9048–9560, Part VIIC at 11886–12340.

Nothing else is brought in. The Crimes Regulations (which prescribe the Part VIIC screening bodies and offices for s 23L(2)(b)(ii)) and the 2026 penalty-unit notifiable instrument are not deposited.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ca14-accused.l4` | `ca14-cases-accused.l4` | 90 written, 90 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The accused person**: someone arrested for, questioned about, charged with or convicted of a Commonwealth offence, and later living with the conviction. The questions are the ones that person asks: "Can they arrest me without a warrant?", "How long can they hold me?", "Do I have to answer?", "Can I call a lawyer?", "My son is 16 — must someone be with him?", "Will I go to prison?", "Can I avoid a conviction?", "When can I stop telling employers?".

Part IC is written as obligations on investigating officials, Part IB as directions to the court, Part VIIC as rules for whoever holds criminal history. Each is encoded as what it means for the person: what must be done for me, by when, what the court may or must do with me, and what I may lawfully say. No question is asked from the seat of the police, a magistrate or a court.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is brought in. Where a number comes from outside (a penalty unit's dollar value, a maximum fine), the answer is in the Act's own unit or the number is an input.
- **The actors the text names:** the person, constables and investigating officials, a magistrate and bail authority, the court, an interview friend, an Aboriginal legal assistance organisation, a consular office, Commonwealth and State authorities.
- **Judgments handed to others are answered conditionally.** Every "believes on reasonable grounds", "is satisfied", "is of the opinion" is an input worded from the person's seat: the constable's beliefs (s 3W), the magistrate's satisfaction (s 23DA), the official's beliefs (ss 23H, 23K, 23L, 23N), the court's opinion and choice (ss 17A, 17B, 19B, 23V(5)). The "reasonable" end of the investigation period is not guessed: the answer is the statutory maximum.
- **The Act's own definitions are worked out from facts:** "protected suspect" (s 23B(2)), "serious Commonwealth offence" (more than 12 months), "waiting period" and "spent" (ss 85ZL, 85ZM). "Dealt with as a minor", which Part VIIC does not define, is asked as a fact.
- **One case:** one arrest and its investigation; one conviction and its sentence; one conviction asked about on one day.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Ombudsman, reporting and record-keeping provisions, delegations, the Information Commissioner's functions (Division 5 of Part VIIC).

## Scope

**In:** ss 3W, 3ZC, 3ZD (arrest without warrant, force, being told why); Part IC: s 23B (under arrest, protected suspect, serious Commonwealth offence), s 23C (investigation period, including (3), (4), (6), (7)), ss 23D(1), (5), 23DA(2), (6), (7) (extension), s 23F (caution), s 23G (friend, relative, lawyer) with s 23L, s 23H (Aboriginal persons and Torres Strait Islanders), s 23K (under 18), s 23N (interpreter), s 23P (consulate), s 23Q (treatment), s 23S (right to silence), s 23V (recording of admissions); Part IB: s 16A(1), (2), (2A), (2AA), (2AAB), s 16C, ss 17A, 17B, s 19B(1), (2A), s 20(1)(a), (2A), (5); Part VIIC: ss 85ZL ("waiting period"), 85ZM, 85ZV, 85ZW, 85ZX, 85ZY, and the Division 6 exclusions (ss 85ZZGB–85ZZGD and the matching disability and aged-care Subdivisions, s 85ZZH).

**Out:** the rest of Part IAA (search warrants, frisk and ordinary searches, stop-and-search, terrorism powers, airport powers, age determination, notices to produce); Parts IAAA–IAC; the terrorism arm of Part IC (s 3WA, ss 23DB–23DF: `not covered`); s 23M; s 23U except as noted in the caution answer; Part ID (forensic procedures); Part IB beyond the sections listed (non-parole periods, recognizance release orders, parole and licence, unfitness, mental illness, minimum penalties, s 16E custody credit); every offence in Parts II–VIIB; Part VIIC Divisions 2 (pardons for the wrongly convicted, quashed convictions) and 5, ss 85ZZJ–85ZZL; s 4AA, s 4B and s 4AB (see finding 14).

## What the Act turns out to say

1. **Arrest without warrant needs two beliefs, and ends when either goes.** A constable must believe on reasonable grounds both that I committed the offence and that a summons would not achieve one of six purposes (s 3W(1)); if, before charge, the officer in charge stops believing either, I "must be released" (s 3W(2)). Asserted.
2. **Part IC protects people who are not arrested.** A "protected suspect" (s 23B(2)) — with an investigator to be questioned, where the official believes there is sufficient evidence, or would not let me leave, or has given me reason to think so — gets every Division 3 protection (caution, lawyer, interview friend, interpreter, consulate, recording). Detention for investigation (Division 2) is for arrested people only. Asserted.
3. **The investigation period is short and capped: 4 hours, or 2 for a child or an Aboriginal person or Torres Strait Islander,** extendable once by a magistrate by up to 8 hours, and only for an offence punishable by more than 12 months (ss 23C(4), 23DA(7), 23B(1)). Time spent getting me to a station, waiting for my lawyer, resting or receiving medical attention is added back if I am not questioned during it (s 23C(7), (7A)), and the prosecution must prove it (s 23C(8)). The maximum for an adult is therefore 12 hours of investigation time. Asserted.
4. **The 2-hour limit applies to anyone who "appears to be" under 18, Aboriginal or a Torres Strait Islander** (s 23C(4)(a)), while the interview-friend rules turn on the official's belief "on reasonable grounds" (ss 23H, 23K). The encoding asks the two separately. Asserted.
5. **The right to silence survives Part IC** (s 23S(a)): I need not answer unless an Act requires it. The caution is not required where another Commonwealth law requires me to answer (s 23F(3)). Asserted.
6. **The lawyer is harder to keep away than the friend.** Section 23L lets an official delay contact on a reasonable belief of risk to evidence, witnesses or an accomplice's arrest, or urgency for others' safety; but for the lawyer only in exceptional circumstances with a Superintendent's recorded authority (s 23L(2)), and then another lawyer must be offered (s 23L(4)). Asserted.
7. **A child's interview friend cannot be waived; an adult Aboriginal person's can,** and the prosecution must prove a waiver was voluntary and informed (ss 23K, 23H(2)(d), (4)). The official may skip s 23H for a person it reasonably believes is not at a disadvantage (s 23H(8)); s 23K has no such exception. Asserted.
8. **An unrecorded admission is inadmissible in any Commonwealth prosecution** unless recording was not reasonably practicable and the full written read-back procedure was followed, or the court is satisfied, in "special circumstances", that admitting it is not contrary to the interests of justice (s 23V(1), (5)) — and then the jury must be told and warned (s 23V(7)). Where recording was practicable, the written procedure does not save it. Asserted.
9. **Prison is the last resort for every federal offence** (s 17A(1)), and **barred for a first-time property or money offence of $2,000 or less** under the listed theft, fraud and dishonesty sections, absent exceptional circumstances (s 17B). Exactly $2,000 is within s 17B. Asserted.
10. **Section 16A(2A) bars customary law and cultural practice from lessening or aggravating the offence,** except for the listed heritage offences (s 16A(2AA)); racial or ethnic hatred aggravates (s 16A(2)(mb)) except for the Criminal Code hate offences in s 16A(2AAB). Asserted.
11. **A discharge without conviction still counts as a conviction for Part VIIC** (s 85ZM(1)(b)), so it too becomes spent after the waiting period; Part VIIC does not say it need never be disclosed before then. Not separately asserted (the spent cases cover it); the encoding takes the day of the finding of guilt.
12. **A conviction is spent 10 years after the day of conviction (5 for a minor) if the sentence was not more than 30 months** (ss 85ZL, 85ZM(2)). The period "beginning on" the day of conviction ends the day before the anniversary, so the conviction is spent from the anniversary (15 March 2016 → 15 March 2026). A sentence of more than 30 months is never spent, short of a pardon. A later offence committed within the waiting period and convicted on indictment, or by a State or foreign court, holds the earlier one unspent until the later waiting period ends (ss 85ZX(2), 85ZY); a summary federal conviction does so only on the court's order (s 85ZX(1)). Asserted.
13. **Part VIIC protects a State conviction only against Commonwealth authorities and in the Territories** (s 85ZV(2)); otherwise the State's law decides (s 85ZV(3)). For a Western Australian, that is the Spent Convictions Act 1988 (WA), which has its own encoding at `subjects/au/wa/spent-convictions-act-1988/`. This encoding answers `not covered` there. Asserted.
14. **The deposit has lost four formulas.** Section 4AA(3) and (4) (the 2026 indexation of the penalty unit), s 4AB(1) (dollars to penalty units: the fraction "D 100" survives without its division sign) and s 4B(2) (the fine for an imprisonment-only offence: "the formula:" is followed directly by "where:") are missing from the text conversion. Section 4AA(1) still says $330, but from 1 July 2026 the amount is indexed for offences committed on or after that day (s 4AA(8)), and the Minister publishes it by notifiable instrument (s 4AA(1A)). So no dollar figure is computed: the s 20(5) answer is given in penalty units. A `.formulas.md` sidecar should be transcribed from the authorised rendering. Not asserted (a finding about the deposit).
15. **The exclusions that matter most are prescribed by regulation.** The working-with-children, disability and aged-care screening bodies (ss 85ZZGB–85ZZGD and the matching Subdivisions) and any s 85ZZH(k) exclusion are "prescribed" — the encoding asks who is asking, as a fact, and cannot check that the body is prescribed. Raised in the ledger.

## Raised in the ledger

- **The Crimes Regulations** prescribing the Part VIIC screening bodies and exclusions (and the offices under s 23L(2)(b)(ii)).
- **The penalty unit amount from 1 July 2026** (the notifiable instrument under s 4AA(1A)).

## What would need doing before this is worth relying on

- **A formulas sidecar** for ss 4AA(3)–(4), 4AB(1) and 4B(2) from the authorised rendering, and the 2026 penalty unit instrument, so maximum fines can be given in dollars.
- **The Crimes Regulations**, so the Part VIIC exclusions can be checked rather than asked.
- **Part IAA searches** (frisk and ordinary searches on arrest, ss 3ZE–3ZH) and **Part ID forensic procedures**, which an arrested person meets.
- **Part IB non-parole periods and recognizance release orders** (Division 4), and s 16E custody credit, for anyone sentenced to imprisonment.
- **Case law.** No case was read; "reasonable" time (s 23C(4)), "exceptional circumstances" (s 17B), the s 19B opinion and "special circumstances" (s 23V(5)) are the courts'. Each is asked as a finding.
- **The Evidence Act 1995 baseline** (`../../../evidence-act-1995/encodings/baseline-2026-10/`) answers what happens to evidence obtained without a caution (s 139) or improperly (s 138); not restated here.
- An independent test pass and a human review.

## The Crimes Regulations brought in (added 2026-10-24, REQ-0097)

**Module:** `ca14-regulations.l4`, beside `ca14-accused.l4`, which it imports; cases in `ca14-cases-regulations.l4` (15 written, 15 satisfied; `l4 run` 0 errors, 0 warnings; `ca14-cases-accused.l4` still 90 of 90). Seat: the person with a conviction.

**Instrument:** the Crimes Regulations 2019, Compilation No. 5 (F2025C01226, compilation date 13 December 2025), deposited at `subjects/au/crimes-regulations-2019/` with `parent_act` this Act.

**What the module computes:** whether a named State or Territory screening body is prescribed for work with children (reg 20) or with people with disability (reg 20A), and from that the answer to `Must I disclose this conviction` with the body treated as a Division 6 screening body only when it is prescribed. Finding 15's input is no longer needed for screening bodies.

16. **Every State's and Territory's working with children and NDIS screening body is prescribed, and some are prescribed twice.** Reg 20 lists ten bodies for children (two in Queensland, two in the ACT); reg 20A lists eight for disability. The Victorian Secretary, the South Australian central assessment unit (under a different Act for each), the Tasmanian Registrar and the ACT Commissioner appear in both. A WA applicant meets the CEO under the Working with Children (Criminal Record Checking) Act 2004 for children and the CEO under the NDIS (Worker Screening) Act 2020 for disability. Asserted.
17. **No one is prescribed for funded aged care.** Sections 85ZZGP–85ZZGR let a prescribed body for aged care worker screening be told of spent convictions, but the Regulations prescribe none, so on the deposited law a spent Commonwealth conviction stays protected from aged care screening. Asserted. (A later amendment could change this; the Register's compilation is dated 13 December 2025.)
18. **A body prescribed for one kind of work is not thereby prescribed for another.** The prescription is "to the extent that those laws relate to persons working, or seeking to work, with children" (reg 20), or are NDIS worker screening laws (reg 20A): the WA working with children CEO is not a prescribed body for NDIS screening. Asserted.
