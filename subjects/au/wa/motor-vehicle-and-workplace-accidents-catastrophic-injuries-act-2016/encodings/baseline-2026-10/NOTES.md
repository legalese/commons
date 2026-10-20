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
