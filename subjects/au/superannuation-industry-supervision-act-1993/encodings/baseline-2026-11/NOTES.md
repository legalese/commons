# Superannuation Industry (Supervision) Act 1993 (Cth) — insurance in super, TPD and income protection: baseline encoding

## Method

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is a third encoding beside `../baseline-2026-10/` and `../naive-2026-10/`, which are untouched.
Those cover the conditions of release, permanent incapacity, death benefits and nominations, and the ss 68AA, 68AAA-68AAD rules on whether cover is given at all.
This one adds what a member claiming on insurance held through super meets: the trustee's insurance covenants (including the duty to pursue a claim), the kinds of insured benefit a fund may provide, self-insurance, the conditions on MySuper death and TPD cover, income protection (temporary incapacity), insurance fees in MySuper, the action for loss from a breach of covenant and its time limit and defence, and the complaints duties.

## Edition

- **The Act:** Compilation No. 131, compilation date 10 August 2026 (amendments up to Act No. 49, 2026), register id C2026C00361, deposited at `../../registers/source-bundle/C2004A04633.txt`.
- **The Superannuation Industry (Supervision) Regulations 1994:** Compilation No. 159, compilation date 1 July 2026, register id F2026C00541, deposited at `../../../superannuation-industry-supervision-regulations-1994/registers/source-bundle/F1996B00580.txt`, with that subject's own `SOURCE-LICENSE.md`.
- **Not deposited:** ASIC's legislative instrument under s 101(1B) (who must be given written reasons on a complaint, and by when); the Corporations Act 2001 (s 912A, s 1017G, Part 7.10A, AFCA's time limits for superannuation complaints); the superannuation data and payment standards; regulations under s 29VC(2) on working out a cost recovery fee.

## Checks

Three files: `sis-ins-dates.l4` (the only daydate import), `sis-insurance.l4` (the questions), `sis-cases-insurance.l4` (the cases).

- `l4 run sis-cases-insurance.l4`: 81 assertions written, 81 satisfied, 0 errors, 0 warnings.
- `l4 run sis-insurance.l4` and `l4 run sis-ins-dates.l4`: 0 errors, 0 warnings.
- A mutation of three expected values (a date, a reg 4.07E answer, a fee answer) was caught: 78 satisfied, 3 failed.
- Expected values were worked by hand from the text, with the provision beside each group. Every `NOT` is bracketed. All 15 exported questions carry `@export` and a `@desc` on each input.

## Seat

**The fund member who is, or may be, claiming on insurance held through super** (death, terminal illness, TPD, income protection), or who pays for that cover.
The question is "What must my fund do about my cover and my claim, and what can I do if it fails?".
Almost every provision is addressed to the trustee; each is encoded as what the member can expect: "Must my fund pursue my insurance claim?", "May my fund charge me this insurance fee?", "Can I bring an action for my loss, and by when?", "Must my fund give written reasons on my complaint?".
No seat for the trustee, APRA, ASIC or a court.

The 2026-10-18 defaults:

- **The Act alone, plus the instruments that set its numbers or dates.** Followed: the Regulations are brought in for the kinds of insured benefit (regs 4.07C-4.07E), temporary incapacity (reg 6.01(2)) and its cashing restriction (Schedule 1 item 109).
- **The actors the text names.** Followed: the member (beneficiary), the trustee, a director of a corporate trustee, the insurer, the court, APRA (as the source of a licence condition), AFCA.
- **A judgment handed to someone else is answered conditionally.** Followed. Asked as facts: whether a claim has a "reasonable prospect of success" (s 52(7)(d)); whether a cost "inappropriately erode[s]" retirement income (s 52(7)(c)); whether conditions are "reasonable" (s 68AA(3)); whether the trustee is satisfied the incapacity is permanent (reg 1.03C); whether the defendant "establishes" compliance (s 55(5), (6)); the court's leave (s 55(4A)); the cost recovery amount (s 29VC).
- **The Act's own definitions worked out; borrowed terms asked.** Worked out: "insurance fee" (s 29V(9)), "temporary incapacity" (reg 6.01(2)), "insured benefit" (reg 4.07C, as a gloss), reasonable conditions (s 68AA(3), (4)). Asked: "registrable superannuation entity", "MySuper member", "self-insure", "permanent incapacity", the kind of fund, "gainfully employed".
- **One case is the text's natural unit.** Followed: one member, one kind of cover, one claim, one fee, one action.
- **The Act's own terms, each with a plain gloss.** Followed, in comments and `@desc` lines.
- **Operative sections in; machinery out.** Followed.

**No regulative rule.** None of the provisions in scope is a duty with a deadline that the member meets or could trace: s 52(7)(d) has no time ("everything that is reasonable"), s 55(4) is a time limit on a right, not a duty, and reg 4.07E(5) (amend the rules before 1 July 2016) is a past duty of the trustee's.

## Rulings on negatives and legal effects (recorded word for word, as the guide requires)

Where the text itself says no in its own words the answer is `JUST FALSE`; elsewhere `NOTHING`.
Periods, "where" and scope limits (ruled 2026-11-05): "(a) a period the text fixes in its own words ...: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" ...: outside the scope the answer is `NOTHING`."
Defences (ruled 2026-11-05): "(b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"".
Questions with no convention are decided site by site, each with a fork line below.

### Fork register

| Provision | Function | Answer taken | Other reading |
|---|---|---|---|
| s 52(1), (7) | `Must my fund pursue my insurance claim`, `Does the cost covenant stop my fund offering this insurance` | Not a registrable superannuation entity (e.g. a self managed fund): `NOTHING`, a scope limit with no "only". | `JUST FALSE`. |
| reg 4.07D(2) | `Does reg 4.07D stop my fund insuring me against this event` | The question is asked negatively ("does it stop"), so the "must not ... unless" bar answers `JUST TRUE` when it bites and `JUST FALSE` when the event is consistent; the other bars (s 52(7)(c), ss 68AAA-68AAC) are separate questions. | Asked positively, a met "unless" could be `NOTHING` rather than a permission. |
| reg 4.07D(3)(a) | the same | A member who joined before 1 July 2014 is outside (2) for any cover: `JUST FALSE`. The text says "the continued provision of benefits", which may cover only cover already held before that day. | Cover first given after 1 July 2014 to a member who joined earlier is not "continued" and (2) applies. |
| reg 4.07D(2) | the same | Whether a policy's event (e.g. an "own occupation" TPD definition) is "consistent with" item 103 is the member's choice of input; "another event" answers that it is not. | Consistency is a matter of degree a court would decide. |
| Sch 1 item 109 | `May my fund pay my temporary incapacity benefit this way` | A monthly benefit above the pay before the incapacity: `NOTHING`. Item 109 states a purpose ("continuing (in whole or part) the gain or reward"), not a cap. | Above 100% is not "continuing" the gain: `JUST FALSE`. |
| s 68AA(2), (3) | `Is my fund excused from my MySuper death or TPD benefit` | Conditions that are not reasonable are not "conditions determined under subsection (3)", so (2) does not excuse: `JUST FALSE`. | An unreasonable condition is merely open to challenge, and the fund is excused until it is set aside. |
| s 68AA(9) | the same | A defined benefit or excluded ADF Super member: `NOTHING` (the section does not apply, so it neither requires nor excuses). | `JUST FALSE`. |
| ss 29VA, 29VC | `May my fund charge me this insurance fee in MySuper` | Not an insurance fee, or not a MySuper product: `NOTHING` (another charging rule, or the choice-product rules, may govern it). | — |
| s 55(3) | `Can I bring my s 55 action` | No loss from a breach of covenant: `NOTHING` (a grant limited in its own words; other causes of action are untouched). | `JUST FALSE`. |
| s 55(5), (6) | `Does the trustee have the s 55 compliance defence` | Loss from something other than an investment or the management of reserves (e.g. a claim mishandled): `NOTHING`. | `JUST FALSE` for this section's defence. |
| s 101(1) | `Must my fund give written reasons on my complaint`, `Where do my fund's AFCA duties come from` | A self managed fund ("other than a self managed superannuation fund"): `JUST FALSE`. An exempt public sector scheme that has not elected to join AFCA: `NOTHING` (not named; no "only"). | SMSF: `NOTHING`. |

## In scope

- **Act:** s 52(1), (7) (insurance covenants); s 55(3)-(7) (action for loss, time limit, directors' leave, the compliance defence); s 68AA(2)-(4), (9) (conditions on MySuper death and permanent incapacity cover); ss 29V(1), (9), 29VA(1), (10), 29VC(1) (insurance fees in MySuper); s 101(1), (1A) (AFCA membership, internal dispute resolution, written reasons on complaints).
- **Regulations:** regs 4.07C, 4.07D (permitted insured events), 4.07E (self-insurance, the transition table in (9)), 6.01(2) "temporary incapacity", Schedule 1 item 109 (cashing restriction for income protection paid from preserved benefits).

## Out of scope, and why

- **s 52(7)(a), (b)** (formulate an insurance strategy; consider the cost to all beneficiaries): duties to the membership as a whole, with no answer for one member; s 52(9)-(11) (annual outcomes assessment, including whether the insurance strategy and fees suit members): the same.
- **The other s 52 and s 52A covenants**, s 54A (prescribed covenants), ss 54B, 54C (civil penalty consequences, offences): only their effect as the basis of a s 55 action is encoded.
- **s 55(4C), (4D)** (what the court weighs on leave; the period it fixes): judgments of the court; the action is asked as brought with or without leave.
- **s 52(8B)** (funds giving only death, TPD and temporary incapacity benefits are outside the retirement income covenant): not a member's question.
- **reg 4.07D(4), (5)**, reg 4.07E(5), (6) (deemed amendment of governing rules; historical start dates): machinery; the cases assume a day on or after 1 July 2014.
- **reg 5.08(3)** (paying temporary incapacity benefits out of minimum benefits): the distinction between member-financed and mandated employer-financed benefits is not encoded.
- **Whether a TPD, death or income protection claim succeeds** is a matter of the policy's terms, not this Act; permanent incapacity and terminal medical condition as conditions of release are in `../baseline-2026-10/`.
- **AFCA's time limits for superannuation complaints and its powers** are in the Corporations Act 2001 (Part 7.10A), not deposited here.
- **Insurance opt-in rules for inactive, low-balance and under-25 accounts** (ss 68AAA-68AAF): already in `../baseline-2026-10/`.
- **Penalties, licensing, investment, Parts 8 to 32** other than s 101.

## What the Act turns out to say

1. **The trustee's duty to pursue a member's insurance claim depends on the claim having a reasonable prospect of success**, and the text gives it no time limit. s 52(7)(d): "to do everything that is reasonable to pursue an insurance claim for the benefit of a beneficiary, if the claim has a reasonable prospect of success". It is a covenant read into the governing rules of a registrable superannuation entity (s 52(1)), so a self managed fund's member does not have it from s 52. Asserted.
2. **The s 55 compliance defence does not reach a mishandled insurance claim.** s 55(5) and (6) give a defence only to an action for loss from "the making of an investment" or "the management of any reserves". A member suing because the trustee failed to pursue a TPD claim (s 52(7)(d)) faces no defence from s 55 itself, however the trustee says it complied. Asserted (`NOTHING` for that loss).
3. **Six years from the day the cause of action arose.** s 55(4): the action "may be begun at any time within 6 years after the day on which the cause of action arose"; leave against a director must be sought within the same six years (s 55(4B)). Read as ending on the same date six years on (10 March 2020 to 10 March 2026). The text does not say when a cause of action for a mishandled claim "arose" (the decline, the loss, the end of a review); that is asked. A 29 February start is carried to 28 February. Asserted.
4. **Trauma cover cannot be given inside super to a member who joined on or after 1 July 2014.** reg 4.07D(2) lets a regulated fund provide an insured benefit only for an event "consistent with" death, terminal medical condition, permanent incapacity or temporary incapacity (Schedule 1 items 102, 102A, 103, 109). Earlier members keep "the continued provision of benefits" ((3)(a)); whether that covers cover first given after 2014 is open (fork). Asserted.
5. **"Consistent with" is undefined.** Whether an "own occupation" TPD definition, wider than permanent incapacity in reg 1.03C (unlikely ever again to work in any job for which the member is reasonably qualified), is "consistent with" item 103 is not answered by the text. The encoding asks the member to classify the event.
6. **A MySuper fund's TPD duty is cut down to the policy's own terms.** s 68AA(4): conditions "are reasonable if they are the same as the terms and conditions of the policy of insurance taken out to provide the benefit", and (2): the trustees "are not required to provide" the benefit if those conditions are not met. So a member who fails the insurer's definition loses the s 68AA entitlement too. Asserted.
7. **Income protection from preserved super must be a non-commutable income stream, for no longer than the incapacity.** Schedule 1 item 109; a lump sum or a commutable stream is not allowed, nor payment for a day after the incapacity for the member's usual kind of work ended (paid to the last day: allowed; to the next: not). The amount is limited only by a purpose ("continuing (in whole or part) the gain or reward"): above 100% of prior pay is not decided (fork). Asserted.
8. **Temporary incapacity needs the member to have stopped work, or stopped being paid, because of ill-health**, and ends where permanent incapacity begins (reg 6.01(2)). A member made redundant while unwell, but not because of the ill-health, is outside it. Asserted.
9. **A MySuper insurance fee may be no more than cost recovery.** s 29VC(1); the charging rule in s 29VA(10) requires the fee to be charged to the member whose premiums or costs it relates to. One cent over the cost recovery amount fails. Asserted.
10. **A fund under the Corporations Act's dispute resolution rules still owes written reasons under the SIS Act.** s 101(1A) removes paragraphs (1)(a)-(c) only; (1)(d), written reasons for any decision on a complaint (or a failure to decide), stays. Who must receive them and by when are left to ASIC's instrument (s 101(1B)), not deposited. Asserted.
11. **Self-insurance:** a fund that did not self-insure on 1 July 2013 may give insured benefits from that day only if an insurer's policy fully supports them; a fund that did self-insure, from 1 July 2016, unless a government provides or guarantees the benefit or (for defined benefit members) APRA had not barred it. A member who was receiving a benefit, had lodged a claim or was eligible to claim immediately before 1 July 2016 keeps that position (reg 4.07E(9)). Asserted.

## What would need doing before this is worth relying on

- An independent test pass and a coverage table.
- The Corporations Act's complaints machinery (s 1017G, Part 7.10A, AFCA's time limits for TPD and death benefit complaints) and ASIC's s 101(1B) instrument.
- The meaning of "reasonable prospect of success", "consistent with" and the time a cause of action "arose" come from case law, which was not searched.
- The Insurance Contracts Act 1984 and the Life Insurance Act 1995, which govern the policy itself, are separate subjects.
