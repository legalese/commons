# Motor Vehicle and Workplace Accidents (Catastrophic Injuries) Act 2016 — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design
defaults ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code
extension 1.6.98. No pipeline, no coverage table, no independent test pass, no human
gate. Not for public use as advice.

**Edition:** the Act (No. 8 of 2016) as deposited at
`../../registers/source-bundle/mrdoc_47531.txt` (legislation.wa.gov.au mrdoc 47531,
retrieved 2026-09-07). Its compilation table runs to the Workers Compensation and
Injury Management Act 2023, Pt 15 Div 3 Subdiv 11, in operation 1 July 2024. Three
provisions that Part 7 of this Act inserted into other Acts are read in their
**current** text, in those Acts' own deposits:

- Civil Liability Act 2002 s 13A (`civil-liability-act-2002/registers/source-bundle/mrdoc_49335.txt`);
- Motor Vehicle (Third Party Insurance) Act 1943 ss 3EA and 3FB (`motor-vehicle-third-party-insurance-act-1943/registers/source-bundle/mrdoc_47506.txt`).

No regulations under this Act are deposited.

**Checks:** one module (`mvwaci-ciss.l4`) and one case file (`mvwaci-cases-ciss.l4`).
45 assertions are written and 45 satisfied, with 0 errors and 0 warnings. `l4 run` on
the module gives no diagnostics. A mutation run (two expected values flipped in a
scratch copy) gave 43 satisfied, so the runner does catch failures.

## Seat

**The person catastrophically injured in a motor vehicle accident in Western
Australia, or at work.** The Act exists for them, and nearly every operative section
tells the Insurance Commission what to do for or to them. Each question is phrased as
that person would ask it: Am I eligible? May I apply, and by when? What must I be
accepted as? Must the Commission pay this? Can I have the decision reviewed, or appeal
it? Where is my care paid from? Can a court award me damages for this care need?

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers.** Followed, with one
  departure. The regulations that set the catastrophic-injury criteria, the
  interim and lifetime criteria, excluded needs, the interim period, any application
  deadline, fee caps and the appeal period are not deposited. Those are inputs or
  reported answers. The departure is that the seat asks how the scheme meets the
  common-law claim. The provisions that answer that are the ones Part 7 of this Act
  inserted into the Civil Liability Act and the MVTPI Act, so they are read here in
  their current text. Neither of those Acts' baselines encodes CLA s 13A or MVTPI
  s 3EA: the CLA baseline sends s 13A to the MVTPI baseline, and the MVTPI baseline
  lists s 3EA as not encoded.
- **The actors the text names.** Followed: the injured person, the Insurance
  Commission, the District Court, and a worker's insurer only as a fact.
- **A judgment handed to someone else is answered conditionally.** Followed. The
  following are inputs:
  - whether an owner or driver is liable in negligence (s 5(3));
  - whether the Commission is satisfied of eligibility (s 10);
  - whether it considers suspension appropriate (s 14(1));
  - whether it assessed a need as necessary and reasonable (s 18(2));
  - whether it elects to pay (s 19(3)).
- **The Act's own definitions worked out, borrowed terms asked.** Followed. "Motor
  vehicle accident" (s 4), "motor vehicle injury to which this Act applies" (s 5),
  "workplace injury to which this Act applies" (s 5A), "treatment, care and support
  needs" (s 6) and "assessed" needs (s 18(2)) are worked out from facts. "Worker" and
  "motor vehicle" are borrowed from the Workers Compensation and Injury Management
  Act 2023 and the MVTPI Act, and asked as facts.
- **One case is the text's natural unit.** Followed: one injury (`My case`), one
  expense (`The expense`).
- **The Act's own terms, each with a gloss.** Followed in the comments.
- **Operative sections in; machinery out.** Followed. Left out: registration of
  providers (beyond s 19(2)(d)), the Commission's recovery from interstate insurers
  (s 21), hospitals' and insurers' notices (ss 30, 30A(3), (4)), guidelines,
  regulation-making powers and review of the Act.

## The lives

- **Chloe, c074 (15 June 2034, aged 31): a used car, licensed, with compulsory third
  party insurance through the Insurance Commission.** The event asks "what does the CTP
  cover?" The MVTPI baseline answers that the policy also insures against a
  catastrophic injury, for CISS payments only (MVTPI s 6A). This baseline answers what
  that means for Chloe if she is catastrophically injured:
  - **alone in her own car on a WA road:** the Act applies, she is eligible given the
    prescribed criteria, she must be accepted as a lifetime participant, and her care
    is paid by the CISS "without proving anyone at fault";
  - **as a passenger while Liam drives negligently:** the Act does not apply (s 5(3)).
    She may still apply, but is not eligible, and her care is a common-law claim met by
    the car's CTP policy;
  - **in a paddock, struck by a farm ute with no CTP:** outside the Act (s 5(4)).
  
  Her assessed attendant care must be paid for. Free care from her mother need not be,
  unless the Commission elects to pay.

## Why this scope

Part 2 is what the plan names, and it is all encoded (ss 8-14). It cannot be answered
without the definitions that decide whether the Act applies (ss 3-5A). The seat's
other questions reach further:

- what is paid for: ss 6, 15, 17-19;
- how to challenge a decision: ss 24-27;
- the worker's own duty: s 30A(5);
- the offences the person could commit: ss 31, 32;
- the common-law claim: CLA s 13A, MVTPI ss 3EA, 3FB.

The baseline is kept moderate (45 assertions), as asked.

## What the Act turns out to say

1. **The scheme is no-fault, but only where no one else is liable.** s 5(3) takes out
   any motor vehicle injury for which "the owner or driver of a motor vehicle has ...
   incurred liability for negligence". That person's CTP policy then meets a
   common-law claim. A driver hurt by their own driving cannot be liable to
   themselves, so they are inside the scheme. Asserted.
2. **Off private land, nobody's insurance matters.** The CTP test in s 5(4) applies
   only to accidents on private land. An unlicensed, uninsured car running out of
   control on a public WA road, with no one negligent, still brings the injury in.
   Asserted (both sides).
3. **The Act sets no deadline for applying.** s 9 has none. s 34(2)(a) lets the
   regulations impose "restrictions as to when applications can be made", but none are
   deposited. Asserted as the answer to "By when must I apply".
4. **Whether an injury is "catastrophic" is entirely for the regulations.** s 3(1)
   defines it as an injury meeting "the prescribed criteria". s 8(2) leaves the
   interim and lifetime criteria to them as well. Every case states these as facts.
5. **A worker needs an accepted claim, and must live in Australia to apply.** The Act
   applies to a work injury only with "an established entitlement to compensation",
   meaning a claim made and liability accepted or decided (s 5A(2), (3)). A worker may
   apply only while residing in Australia (s 9(1A)). Their participation is suspended
   automatically while they are abroad (s 14(1A)). For a motor vehicle injury,
   suspension abroad is at the Commission's discretion (s 14(1)). Asserted.
6. **A worker struck by a negligent driver may still come in as a workplace injury.**
   s 5A(4) sends a work injury down the motor vehicle route only if it is a motor
   vehicle injury "to which this Act applies". One excluded by s 5(3) is not, so on
   the words it remains a workplace injury. This is an inference from the text, not
   checked against practice or guidelines. Asserted.
7. **Settled or awarded future-care damages shut the door.** s 8(3): the person is not
   eligible if damages for future treatment, care and support have been awarded by
   final judgment or binding settlement. Asserted.
8. **The Commission's power to pay anyway does not reach suspension.** s 19(3) lets it
   elect to pay for the s 19(2) items (free care, care abroad, a child's ordinary
   costs, unregistered providers, breaches of the regulations). It does not reach
   s 19(5), care while participation is suspended. Asserted.
9. **s 6(2) and s 18(3)(a) pull against each other.** s 6(2) excludes the prescribed
   "excluded" kinds "subject to subsection (1)(l)", so a Commission approval seems to
   bring one back in. But s 18(3)(a) says the Commission "is not liable" for excluded
   needs at all. The encoding follows s 18(3)(a). Not asserted beyond the plain case.
10. **Part 5 gives no review of a refusal to pay a particular expense.** Review covers
    "eligibility decisions" and assessments only (ss 24-26). And s 27 gives no District
    Court appeal from a review of an assessment, because a "review decision" is one on
    an eligibility decision. Two eligibility questions (is it a motor vehicle accident,
    does the Act apply) go to the Court as of right. The rest need leave, which
    requires a question of law. Asserted.
11. **Damages for care while in the scheme, and the gaps.** Under current CLA
    s 13A(5), a participant gets no damages for care needs arising during
    participation or in future. Needs that arose before acceptance are not barred. A
    former interim participant is barred only for the interim period (s 13A(8);
    MVTPI s 3EA(4)). Neither section mentions a lifetime participant notified under
    s 12(3) that they are no longer eligible, so on the words no bar applies to them.
    Gratuitous family care counts as a care need (s 13A(3)). Asserted.
12. **The Part 7 text in this deposit is out of date.** As enacted in 2016, it inserts
    a s 13A speaking of the "MV(CI) Act" and motor vehicle accidents only. The current
    s 13A (replaced by WCIMA 2023 s 626) covers workplace injuries too. The encoding
    reads the current text.
13. **No deduction for the injured person's own fault from catastrophic care
    damages** (MVTPI s 3FB(3)). This matches the MVTPI baseline. Asserted.
14. **A catastrophically injured worker has a 7-day duty to tell the Commission.** It
    runs from an election to keep the right to seek damages, or from receiving or
    settling damages that include future care (s 30A(5)). s 30A states no penalty.
    False or misleading information (s 31) and obstruction (s 32) each carry a fine
    of $10 000. Asserted (s 30A(5) and s 31).

## What would need doing before this is worth anything

- Deposit the Motor Vehicle (Catastrophic Injuries) Regulations 2016 (title not
  verified), and the Commission's CISS guidelines (s 33). Then encode:
  - the eligibility criteria;
  - interim and lifetime participation and the interim period;
  - excluded needs;
  - any application deadline;
  - fee caps and the appeal period.
- Check finding 6 (the negligently-struck worker) and finding 11 (the former
  lifetime participant) against the Commission's practice and any case law.
- Encode WCIMA 2023 ss 80, 92, 96 and 151 (the employer's liability for expenses ends
  on joining the CISS) in the WCIMA baseline, and cross-reference.
- An independent test pass, and the human gates.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026 (qa2). Two files, beside the baseline, which is unchanged: `mvwaci-qa.l4` (IMPORTs `prelude` and `mvwaci-ciss`) and its cases `mvwaci-qa-cases.l4` (IMPORTs `prelude`, `mvwaci-ciss` and `mvwaci-qa`). It follows the design of the Graffiti Vandalism Act layer (`../../../graffiti-vandalism-act-2016/encodings/baseline-2026-10/`, D2, D4 and D8): one deployment serves every seat, so the site's question form can drop the questions that do not arise.

**Roles.** Every exported question takes `my role` IS A Role first (`@desc Which of these describes you`), and answers `does not arise for you` for a role it is not about without reading any other input.

- `I was injured in a motor vehicle accident or at work`: the baseline's seat. 24 questions of its own (23 until the fix of 6 November 2026 split the expense question in two).
- `I act for, or care for, someone who was injured`: a person with lawful authority to act for the injured person, who may apply and be given notices for them (s 3(2)), or a family member who gives care free (s 19(2)(a), (3); CLA s 13A(3)). 4 questions of its own.
- `I provide treatment, care or support to people in the scheme`: a provider, who may need to be registered (ss 19(2)(d), 23) and whose fee the regulations may cap (s 20). 4 questions of its own.
- The two offences (s 31 false or misleading information, s 32 obstruction) bind "a person", so they are asked of all three roles and never answer `does not arise for you`. That makes 26, 6 and 6 questions per role, 34 exported.
- Not seats: the Insurance Commission, hospitals (s 30), WorkCover WA and insurers (s 30A(3), (4)), the District Court.

**Plain inputs.** The baseline's questions take records (`The accident`, `The work injury`, `My case`, `The expense`). Here the inputs are plain facts, and the records are built inside L4 (`the accident from my answers`, `the accident as the Act applies to it`, `the work injury from my answers`, `my case as the Act takes it`, `the expense from my answers`). A record field that the rule called does not read gets a fixed placeholder FALSE, with a comment: the lifetime criteria and residence for eligibility (s 8), the criteria and damages for applying (s 9), residence for acceptance, the s 19 facts for the s 18 question, and the s 19(2) items other than (d) for the provider's registration question. Since the fix of 6 November 2026 (below) some facts the baseline reads only together are asked together, and the questions after s 5 take an earlier question's answer in place of the facts it is worked out from.

**Situation inputs.** Each comes straight after `my role` (the place in the scheme before how I was injured where a question takes both). When it does not hold, the question answers `does not arise for you` and reads nothing else. The same name, type and `@desc` wherever taken.

| Input | Type and values | Does not arise when | Questions |
|---|---|---|---|
| `how I was injured` | `How I was injured`: `in an incident involving a motor vehicle, and not as a worker`; `as a worker, in an incident not involving a motor vehicle`; `as a worker, in an incident involving a motor vehicle` | the second value, for the s 4 and s 5 questions and MVTPI s 3FB; the first value, for the s 5A question and the two s 30A(5) questions | 6 as a situation. It is an ordinary input (it builds the records) of the s 5A(4) "how the Act takes it" question: with no motor vehicle the accident is built as one the Act cannot take and the s 5 answer is not read; for someone not injured as a worker the work facts are not read. "As a worker" makes the borrowed "worker" fact TRUE. (Until the fix it was also an ordinary input of eligibility, applying, acceptance and where care is paid from, which now take `how the Act takes my injury`) |
| `my place in the scheme` | `My place in the scheme`: `I have not been accepted into the scheme`; `I am an interim participant`; `I am a lifetime participant`; `my interim participation has ended, and I was not made a lifetime participant`; `I was a lifetime participant until notified that I am no longer eligible` | the two current values, for applying, by when, and acceptance (3); the first and the two former values, for still a participant, suspension, the s 15(3) assessment, s 17 costs and the s 18(5) sum (5); all but the interim and former interim values, for applying again (ss 11(3), 13); the first value only, for "is this expense within what the Commission must pay for" and "must the Commission pay this expense" (2) | 11 as a situation; the CLA s 13A question takes it as an ordinary input (mapped to the baseline's `My standing in the scheme`) |
| `the injured person's place in the scheme` | `Their place in the scheme`: `they have not been accepted into the scheme`; `they are an interim or lifetime participant`; `they were an interim participant and were not made a lifetime participant`; `they were a lifetime participant and were notified they are no longer eligible` | the first value, for the carer's s 19 question | 1 as a situation; the carer's CLA s 13A question takes it as an ordinary input |
| `I am a registered provider` | BOOLEAN | FALSE | the s 23(6) fine and s 23(7); an ordinary input of the s 19(2)(d) question |

The helpers that read these enumerations, and the new `What kind of need it is`, `Their participation when I gave the care` and `How the Act takes my injury` (in `my case as the Act takes it`), list every value and have no OTHERWISE (the graffiti finding 31).

**Decisions.**

- `My place in the scheme` stands for both the baseline's `My participation` (ss 10-12) and its `My standing in the scheme` (CLA s 13A), so the form asks one question. Its two former values are worded apart from the baseline's (`I was an interim participant and was not made a lifetime participant` is a constructor of the baseline's type): a constructor name defined in both modules is ambiguous wherever its type is not known.
- The baseline's answer enumerations are each carried in an answer type of its own (`How the Act takes it answer`, `Time limit answer`, `Acceptance answer`, `Payment answer`, `Appeal answer`, `Care funding answer`); BOOLEANs as `Yes or no`, the 7 days as `Days`, fines as `Amount`.
- "Must the Commission pay this expense" arises for a former participant too, since an expense incurred while a participant can be asked about afterwards.
- "Is this one of my treatment, care and support needs" (s 6), the review and appeal questions (ss 24-27) and the s 13A damages question take no situation: they arise before, during and after participation.
- The suspension question keeps the baseline's input `how the Act takes my injury` (motor vehicle or workplace), since a worker in a road incident may be either (s 5A(4)) and the participant knows which. Since the fix its `@desc` names the question that answers it, and eligibility, applying, acceptance and where care is paid from take the same input.
- The carer's free-care question passes TRUE for s 19(2)(a) and FALSE for the other s 19(2) items, which cannot change the answer once (2)(a) holds; the s 18 limbs and s 19(5) are still asked.

- Fix after verification (6 November 2026, qaf2). The site's form engine drops a question for a role it is not about only when it can try every combination of the question's open yes/no and choice inputs, at most 1,024 (its PROBE_CAP and ENUMERATION_CAP). Eight of the injured person's questions, built from every fact of `My case` or `The expense`, had from 3,840 to nearly ten million combinations, and the carer's free-care question 6,656; so the carer and the provider were asked the injured person's facts, the injured person was asked the carer's, and `how I was injured` and `my place in the scheme` did not drop the s 5A, applying and acceptance questions. The L4 was right; the shape was not. Now:
  - s 5 asks two pairs of facts as one yes/no each, because the baseline reads each pair only together: `a vehicle involved had WA compulsory third party insurance, or interstate compulsory cover` (s 5(4)(a) or (b); carried as the WA field, the interstate one FALSE), and `a vehicle involved was in a motor sports event, or the injury resulted from a terrorist act` (s 5(5)(a) or (b); carried as the motor sports field). 960 combinations.
  - s 5A and "how the Act takes my injury" take `the Act applies to my injury as a motor vehicle injury` (the s 5 question's answer) in place of the accident facts, since s 5A(4) reads the accident only as that answer. 96 combinations each.
  - Eligibility (s 8), applying (s 9), acceptance (ss 10, 12) and where care is paid from take `how the Act takes my injury` (the answer to that question), which the baseline reads in place of the accident and work facts, plus, for s 9, how the incident happened (s 4) and, for where care is paid from, how it happened and the driver's negligence. The record (`my case as the Act takes it`) is built so that the baseline gives the same answers: an accident the Act applies to only for a motor vehicle injury, otherwise one outside WA with the incident and the negligence as they were; a work injury with liability accepted only for a workplace injury. 12 to 480 combinations.
  - The expense question is split. "Is this expense within what the Commission must pay for" (ss 6, 18) asks the kind of need as the three kinds the baseline's s 6 rule tells apart (`What kind of need it is`: one of the listed kinds, something else approved, something else not approved), whether the regulations exclude the kind, the assessment, necessary and reasonable, a participant then, and the payment exclusion; it calls the baseline's s 18 rule. "Must the Commission pay this expense" (ss 18, 19) takes that answer, the suspension, the five s 19(2) grounds as one yes/no (the baseline reads them only together), and the s 19(3) election; it calls the baseline's export on an expense covered by s 18 exactly when that answer is yes. 480 and 80 combinations.
  - The carer's free-care question takes the same three kinds, the two regulation exclusions as one yes/no (the baseline reads them only together once the kind is one of the three), and whether the injured person was a participant then, and suspended, as one choice (`Their participation when I gave the care`). 576 combinations.
  - The answer of an earlier question is a derived input: the person asks that question first. The form does not carry one answer into another question; each such input's `@desc` names the question that answers it. The cases give each the answer the baseline gives on the same records.

**Not covered for the new roles.** For the carer: payment to a family carer under the Commission's guidelines or the regulations (not deposited); whether a particular person has "lawful authority" (guardianship and powers of attorney are other Acts). For the provider: registration itself and its conditions (regulations and Commission decisions, not deposited); the amount of any fee cap (s 20(5), regulations); the s 23(6) reasonable excuse. Hospitals' and insurers' notices (ss 30, 30A(3), (4)) are bodies' powers and duties, not seats.

**Checks.** Stable l4 1.6.98, `JL4_LIBRARY_PATH` unset.

- `mvwaci-ciss.l4` and `mvwaci-qa.l4`: no diagnostics. `l4 check mvwaci-qa.l4`: Check succeeded.
- `mvwaci-cases-ciss.l4`: 45 of 45 satisfied.
- `mvwaci-qa-cases.l4`: 239 of 239 satisfied, no error or warning (213 before the fix of 6 November 2026). It was written by the scratchpad script `gen_mv_cases.py`, which only spells out argument lists; the values are hand-worked.
  - 64 for the roles a question is not about (every other input ASSUMEd);
  - 35 for a situation value that does not hold (later inputs ASSUMEd);
  - 140 where role and situation hold. 37 of these assert equality with a baseline export or rule on the same facts, built as the baseline's own records: at least one for each of the injured person's 24 questions, the carer's two that call a baseline rule, and the two offences. Several ASSUME the facts of the other kind of injury, which shows they are not read.
- The site's form engine (`interact-engine.ts`), run against a local jl4-service with 100 random completions per question in each role-and-situation state, found no issue after the fix (818 before): the carer keeps 6 questions and is asked 9 inputs, the provider 6 and 4; for the injured person `how I was injured` drops the s 5A or the s 4, s 5 and s 3FB questions as it should, and each place in the scheme drops its questions.
- A parameter script (`check_params.py`, session scratchpad) listed all 33 exports. It found `my role` first everywhere, every shared input identical in type and `@desc`, each situation read in the first check after the role, and no DEONTIC or EVENT input. After the fix a second script (`check.py`, session scratchpad) found the same for all 34, no two exports here or in the baseline whose names share their first 60 sanitised characters, and no question with more than 1,024 combinations of yes/no and choice inputs (the largest, s 5, has 960).
- Negative controls on a scratch copy each failed: an ASSUMEd place in the scheme for a participant's question; a wrong payment answer; ASSUMEd work facts where s 5(3) excludes the motor vehicle injury.
