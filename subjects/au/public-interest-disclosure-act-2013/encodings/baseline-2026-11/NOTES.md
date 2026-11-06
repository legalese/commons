# Public Interest Disclosure Act 2013 (Cth) -- baseline encoding, the discloser

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`),
from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the
2026-11-04 and 2026-11-05 rulings on negatives (below). No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The rules are in `pid-rules.l4`, the two periods
(with the one regulative rule) in `pid-dates.l4`, the only module that imports `daydate`; the questions are in a seat
module that imports both and never restates a rule (`pid-seat.l4`); the cases are in `pid-cases.l4`.

The focus asked for is the provisions a claimant meets, in the employment area. For this Act the claimant is a current or
former Commonwealth public official who reports wrongdoing and then needs the Act's protection: whether the disclosure is
a public interest disclosure at all (Part 2 Division 2), the immunities and the civil remedies for a reprisal, with the
court's orders, the costs rule, the offences and the Fair Work election (Part 2 Division 1), and the two periods Part 3
fixes for what happens to the disclosure (s 43(11) allocation, s 52 investigation), the second of which opens an external
disclosure when it is missed. Part 2 is encoded whole except as listed under Scope; Parts 3 to 5 are the officials'
machinery and are encoded only where they fix a period or a right the discloser meets.

## Edition

- **Act:** Public Interest Disclosure Act 2013, No. 133, 2013, Compilation No. 20 (compilation date 4 June 2026, register
  id C2026C00225, including amendments up to Act No. 75, 2025), deposited at `../../registers/source-bundle/C2013A00133.txt`
  (text sha256 b93102fea525a64a878a438ce44037eb22bbf5179c2f8bc3d7473b868d0accb7 per its `.meta.json`; the working copy
  this was checked against hashes differently, most likely line endings), a plain-text conversion of the Word file from
  the Federal Register of Legislation, retrieved 13 October 2026. The endnotes show no uncommenced amendment.
- **Numbers set elsewhere:** the Act's periods and penalties are in the Act itself. The PID rules (s 83) prescribe a kind
  of disclosable conduct (s 29(1) item 10), investigative agencies (s 8), excluded provisions (s 69 item 17(f)) and the
  agency some officials belong to; they are not deposited and each is asked as a fact. The value of a penalty unit is set
  by the Crimes Act 1914, not deposited; the answer is in penalty units. "NACC disclosure" and "designated publication
  restriction" come from other Acts and are asked as facts.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read; two
deliberately wrong assertions were run once in a scratch copy, since deleted, and showed as "assertion failed".

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `pid-rules.l4` | 0 | 0 | 0 | 0 |
| `pid-dates.l4` | 0 | 0 | 0 | 0 |
| `pid-seat.l4` | 0 | 0 | 0 | 0 |
| `pid-cases.l4` | 0 | 0 | 170 | 170 |

Every exported question has cases, with the edges: table positions in and out of s 69, the s 70 determination with and
without an s 69(4) exclusion; each actor and the two s 29(2) kinds against each actor, every exclusion and each way back
into s 29(2A); every s 34 item with each recipient and belief, including (ca) taking the Ombudsman out; each limb of each
item of s 26(1) alone, s 26(2A), and the emergency item with and without an earlier internal disclosure; every liability
against s 10 and s 12A, s 11A's knowledge and excuse; each element of s 13; every combination of s 14(1)(b), (2) and s 16,
and s 22A with and without (3); every penalty; each s 20 exception; and the periods on the last day, the day after, with an
extension, across a year end and across 29 February 2028.

## Seat

**The discloser** (`pid-seat.l4`): a current or former public official (or a person an authorised officer has determined
under s 70 is to be treated as one) who has made, or is thinking of making, a disclosure of wrongdoing in the Commonwealth
public sector, and who may meet a reprisal for it; and, for ss 12A and 12B, the same person as a witness who helped with
someone else's disclosure. "Am I a public official who can make a public interest disclosure?", "Is what I want to report
disclosable conduct?", "Is the person I disclosed to an authorised internal recipient?", "Is my disclosure an internal
disclosure?" (and external, emergency, legal practitioner, NACC), "Can I disclose orally or anonymously or without
mentioning the Act?", "Am I protected from this liability for my disclosure?", "As a witness am I protected from this
liability?", "Has someone taken a reprisal against me?", "What can the court order for the reprisal against me?", "Can I be
ordered to pay the other side's costs?", "What is the most they can be sentenced to?", "Would revealing or using
information that identifies me be an offence?", "By when should my disclosure be allocated?", "By when must the
investigation be completed?", "Was the investigation completed within the time limit?".

No seat for the authorised officer, the principal officer, the Ombudsman, the IGIS or a court. No seat was written for the
person accused of a reprisal or for their employer; one would ask the same rules from the other side.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed; the PID rules set no number the person meets and
  are not deposited; their prescriptions are asked as facts.
- **The text's own actors.** Followed: the discloser, the witness, the supervisor, the authorised officer, the principal
  officer, the respondent and the respondent's employer, the court.
- **Judgments answered conditionally.** Followed: "reasonable grounds" beliefs, "not, on balance, contrary to the public
  interest", "no more than is reasonably necessary", "exceptional circumstances", "significant implications", "reasonable
  administrative action", the court being satisfied, and the employer's reasonable precautions are inputs worded "if it is
  accepted that ...". Nothing decides them.
- **The Act's own definitions in L4, borrowed terms as inputs.** Followed: public official (s 69, s 70), disclosable
  conduct (ss 29-33), authorised internal recipient (s 34), public interest disclosure (s 26), takes a reprisal (s 13),
  provides assistance (s 12A(2)), identifying information (s 20(1)(b)). Intelligence information (s 41), authorised
  officer (s 36), contracted service provider (s 30), judicial officer (s 32(2)) and "relates" (s 35) are glossed in the
  input descriptions rather than worked out, because the person can state them more easily than the facts behind them.
- **One case.** One disclosure, and one reprisal claim against one respondent.
- **The Act's terms with plain glosses.** Followed, in the `@desc` of each input.
- **Operative sections in, machinery out.** Followed (Scope).

## Scope

**In:** s 10, s 11, s 11A, s 12, s 12A, s 12B; s 13; ss 14, 15(1), 16, 17, 18; the penalties of ss 19(1), (2), 20(1), (2)
and 67(1); s 20(1)-(4); s 22A; s 26(1) items 1-4, (1A), (2A); s 28; s 29 (with s 29A and s 30(1)); ss 31, 32(1), 33;
s 34; s 43(11); s 52(1)-(3), (6); s 69(1), (4); s 70(1), (3A).

**Regulative rule:** one. s 52(1) as a duty (`MUST`) on the principal officer to prepare the report within 90 days plus
any extension, with `LEST BREACH ... BECAUSE` naming s 52(6) and item 2(c)(iii); run by EVALTRACE inside "Was the
investigation completed within the time limit?", which takes only plain facts and dates. s 43(11) is a duty of "best
endeavours" with no consequence and is given as a date only. The other duties owed to the discloser (ss 44(4), 44A(3),
50, 51(4), 52(5), 60, 60A) run "as soon as reasonably practicable" or "within a reasonable time": no period to encode.

**Out, and why:**
- ss 1-7B, 8 as a whole: preliminary matters, objects, outline, and the routes of complaint to the Ombudsman or the IGIS
  (ss 7A, 7B: a complaint may be made; nothing to decide). The definitions in s 8 are used where a question needs them.
- s 15(2) (orders against people who aided, induced or conspired in the reprisal): orders against third parties; a later
  layer could add them to the list.
- s 19 beyond its penalties: the offence's elements mirror s 13 (asked there), with s 19(2)(c) recklessness, s 19(3),
  (4) and (5) for a prosecution, which the discloser does not bring; s 19A (civil proceedings need no prosecution) is
  stated in finding 6.
- s 21 (a public official not required to give a court identifying information): it is a protection a witness official
  claims in a court, with nothing for the discloser to state.
- s 22 (Fair Work Act Part 3-1 applies as if this Act were a workplace law): its effect is in the Fair Work Act 2009, not
  deposited here; only the s 22A election is encoded.
- s 23 (claims for protection in court proceedings: onus, separate proceedings, adjournment) and s 24 (effect despite
  other laws): court procedure and the Act's relation to other laws.
- s 26(2) (no disclosure made before the section commenced, 15 January 2014, is protected): historic.
- s 27 (associated allegations): an allegation made with a public interest disclosure to the same recipient is one; it
  follows the disclosure's answer and adds no question.
- s 30(2)-(4), s 32(2)-(4), ss 35, 36, 41: definitions glossed in the inputs (above).
- Part 3 apart from ss 43(11) and 52: allocation and investigation are the officials' work; the grounds on which a
  principal officer may decide not to investigate (s 48) are a discretion, not the discloser's question; notices run
  without a fixed period.
- Part 4 (duties of principal officers, authorised officers, supervisors and officials; Ombudsman and IGIS functions;
  information sharing; the remaining definitions of agency, prescribed authority, principal officer; machinery of
  government changes) and Part 5 (standards, secrecy provisions, reports, delegations, s 78 liability of officials,
  review, PID rules): machinery.

## Negatives (rulings of 2026-11-04 and 2026-11-05)

Copied word for word from `docs/ENCODING-GUIDE.md` section 5, as the guide requires of each row with `NOTHING-kind` tags:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

> **Periods, "where" and scope limits** ... (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.

> **Delegated definitions, defences and "until" bars** ... (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all" ...

> **Questions with no convention: decide case by case** ... Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover.

How they fall here. Every question but one is answered by the text's own no, so it returns a plain `BOOLEAN` (its FALSE is
the JUST FALSE of the rulings) and not `MAYBE BOOLEAN`:
- "means" or "has the meaning given by": public official (s 69(1) with the flat exclusion in s 69(4)); disclosable conduct
  (s 29 with s 8, and the flat negatives "is not disclosable conduct" in ss 29(2A), 31, 32(1), 33); public interest
  disclosure (s 26 with s 8: the items and s 26(1A) are the whole definition); takes a reprisal (s 13 with s 8, and the flat
  negative in s 13(3)); provides assistance (s 12A(2)).
- s 34: "The following table sets out who is an authorised internal recipient": a closed table.
- "If" conditions and flat negatives: s 10 ("If an individual makes a public interest disclosure"), ss 11, 11A, 12, 12B
  ("does not apply", "does not affect"); s 20(1) "commits an offence if" with (3) "do not apply if"; s 16 and s 14(1)(b)
  "if"; s 14(2) "must not make an order"; s 18 "only if"; s 22A "is not entitled".
- Periods: s 52(1) "within 90 days after": outside the period the investigation was "not completed within the time limit".
- `NOTHING`: one site. s 28(4) disapplies s 28 for a NACC disclosure and the note points to the NACC Act, outside the
  sources (`s 28 -- the form does not matter`).

A FALSE from ss 10 and 12A means "this section gives no immunity on these facts", never "no protection at all": the Fair
Work Act 2009 (s 22), the general law and other Acts may still protect the person.

### Forks

- **F1** s 43(11), s 52(1), `the day that is ... days after`: "within N days after" day D ends on D + N (the period starts
  the next day); other reading: D + N - 1.
- **F2** same functions: a last day on a weekend or public holiday is not moved; the Acts Interpretation Act 1901 s 36 is
  not deposited, and it may move it for a thing to be "done" on that day.
- **F3** s 26(1) item 3(d), `s 26(1) item 3 -- an emergency disclosure`: with an earlier internal disclosure whose
  investigation is already complete, (d) is taken as met (there is no "before ... completed" left to justify); other
  reading: (d) cannot be met, so no emergency disclosure is possible after the investigation ends (finding 7).
- **F4** s 69(1), `What I am or was`: items 7 and 8, items 15 and 16, and items 17A, 18 and 19 are joined, and item 17's
  exclusions are folded into its label; the person picks the label. Other reading: one choice per item.
- **F5** s 70, `s 26(1)(a) -- the discloser is or has been a public official`: a determination counts for every kind of
  disclosure of that information ("this Act has effect ... in relation to the disclosure of the information by the
  individual"); other reading: only for the disclosure to the authorised officer who made it.
- **F6** s 26(2A), `s 26(1) item 2 -- an external disclosure`: "to the extent that the response involves" ministerial
  action is asked as "the only inadequacy is ministerial action" (then (c)(ii) fails); a mixed case counts. Other reading:
  weigh the non-ministerial part separately.
- **F7** s 29(2), `s 29(1) and (2) -- conduct of a disclosable kind`: the two added kinds are conduct "engaged in by a
  public official" and so never an agency's or a contractor's; other reading: an agency acts through officials, so any of
  them.
- **F8** s 12A(1), `ss 12A, 12B -- the witness is protected`: the witness is protected only if the disclosure they helped
  with is a public interest disclosure ("in relation to a public interest disclosure"); other reading: help given to a
  "disclosure investigation" (s 12A(2)(b)) of any disclosure counts (finding 8).
- **F9** s 52, `s 52 -- how the investigation stands`: a report dated before the starting day counts as in time; other
  reading: the case does not arise.
- **F10** s 34, `Who I disclosed to`: one recipient choice, "the first that fits"; an authorised officer of the agency the
  conduct relates to who is also of the discloser's own agency is entered as the first.
- **F11** s 14(1)(b), `Order for a reprisal`: the three employer orders ((i)-(iii)) are one entry, since which of them is the
  court's choice.

## What the Act turns out to say

1. **An emergency disclosure need not concern disclosable conduct.** Item 3 of s 26(1) asks only for a reasonable belief in
   a substantial and imminent danger to health, safety or the environment; unlike items 1, 2 and s 26(1A), it does not
   require that the information tend to show disclosable conduct. Asserted (an emergency case with no conduct input).
2. **A witness loses immunity for any breach of a publication restriction; a discloser only for a knowing one without
   excuse.** s 11A takes s 10 away only if the discloser "knows" and "does not have a reasonable excuse"; s 12B(4) takes
   s 12A away for "proceedings against the witness for contravening a designated publication restriction", with no such
   limbs. Asserted.
3. **s 29(2)(b) reaches an official's private conduct.** It covers "conduct engaged in by a public official that could, if
   proved, give reasonable grounds for disciplinary action resulting in the termination of the official's engagement",
   with no requirement (unlike s 29(1)(b)) that it be in connection with the official's position. Asserted.
4. **For intelligence agency conduct, the discloser's own agency is not an authorised internal recipient.** Item 1 of the
   s 34 table includes "the agency to which the discloser belongs, or last belonged"; item 2 does not. An official of an
   ordinary agency who learns of intelligence agency wrongdoing must go to the intelligence agency, the IGIS, or (with no
   intelligence information) another investigative agency. Asserted.
5. **Reinstatement is only against the employer.** s 16 requires that the applicant "is or was employed in a particular
   position with the respondent"; a reprisal by a manager can bring in the employer for compensation (s 14(1)(b)) but not
   for reinstatement unless the employer is itself a respondent. Asserted (no reinstatement where not employed by the
   respondent).
6. **The time limit has one consequence, and it is the discloser's.** Missing s 52's 90 days "does not affect the validity
   of the investigation" (s 52(6)); its only effect is to satisfy item 2(c)(iii), letting the discloser make an external
   disclosure. s 43(11)'s 14 days is "best endeavours" with no consequence at all. s 19A adds that civil proceedings under
   ss 14-16 need no prosecution. Asserted (the timing cases).
7. **Item 3(d) is unclear once the investigation is over.** It asks for "exceptional circumstances justifying this
   disclosure being made before a disclosure investigation of the internal disclosure is completed"; it says nothing for a
   disclosure made after completion. Fork F3; asserted on the reading taken.
8. **Whether a witness's immunity depends on the disclosure qualifying is open.** s 12A(1) speaks of "assistance in relation
   to a public interest disclosure", but s 12A(2)(b) counts help relevant to "a disclosure investigation", which s 8
   defines by reference to Part 3, where an investigation can proceed on a disclosure later found not to be a public
   interest disclosure. Fork F8; asserted on the narrower reading.
9. **The tables have gaps in their lettering.** Item 2 of s 26(1) runs (a), (b), (c), (e), (f), (h), (i) and item 3 runs
   (a)-(d), (f): repealed paragraphs left unrenumbered. Nothing is lost, but a citation "item 2(g)" leads nowhere.

## Before relying on it

- An independent test pass and a human gate; a lawyer's view on forks F3, F5, F6 and F8.
- Deposit the PID rules made under s 83 and the Acts Interpretation Act 1901 (s 36 on the last day
  of a period), and revisit F1 and F2.
- Link to the Fair Work Act 2009 encoding (s 22 makes this Act a workplace law for Part 3-1; s 22A's election) and to the
  National Anti-Corruption Commission Act 2022 for NACC disclosures, when encoded.
- A seat for the person accused of a reprisal and their employer (s 14(2), s 18); s 15(2) and s 23.
