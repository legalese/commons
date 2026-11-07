# Powers of Attorney Act 1998 (Qld): baseline encoding for claims about an attorney's dealings

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the rulings on negatives of 2026-11-04 and 2026-11-05.
There is no REFUSE, `#ASSERT REFUSED` or BECAUSE in it other than `LEST BREACH ... BECAUSE`.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The focus is what a person meets when bringing or answering a claim about an attorney's dealings with a principal's affairs: whether the power could be used, whether the document can be set aside, what the attorney was and was not allowed to do (conflict transactions, investments, mixing property, gifts, dependants), the presumption of undue influence, compensation and accounting for profits, a beneficiary's lost benefit and the proceeds of property the attorney sold, the application times, the personal representative's protection when distributing, who may apply and where, accounts and audit, costs, and reasons; and, for the attorney, the protections and relief the Act gives.

It is written in layers:

- **`poa-core.l4`**, the seat-neutral core, in the Act's own actors and terms ("the principal", "the attorney", "the court", "the tribunal", "the third person", "the beneficiary", "the personal representative"). Each function is preceded by the words of the section it encodes. Where the text sets a deadline there is a regulative rule (`DEONTIC`): four in all (ss 61D(4), 106(5)-(6), 107(4) with Succession Act s 41(8), 124). The application-time questions build the trace inside (`EVALTRACE` on the rule, with the application as the event) and read it with `CONSIDER ... WHEN FULFILLED`, so no exported question takes a `DEONTIC` or `EVENT` input.
- **`poa-dates.l4`**, small date helpers on the stable prelude's date primitives. The `daydate` library is not imported and no `YMD` is defined. The date readings are stated at its top.
- **`poa-seat.l4`**, the claimant's seat: 27 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the order a claim is met. Two groups arise only after the principal has died, and say so in their headings.
- **`poa-seat-attorney.l4`**, the attorney's seat: 8 questions over the same core, defining no name the claimant's seat defines.
- **`poa-cases-claimant.l4`** and **`poa-cases-attorney.l4`**, the cases, around one HYPOTHETICAL family (Margaret, who made an enduring power of attorney on 3 May 2021 appointing her son Daniel, and died on 14 August 2026; her granddaughter Ruby, left the house Daniel sold). The attorney's file includes mirror cases: the same facts asked from both seats, with answers asserted equal.

No earlier encoding of this Act existed. The Succession Act 1981 baseline (`subjects/au/qld/succession-act-1981/encodings/baseline-2026-11/`) is untouched; nothing is imported from it (IMPORT cannot cross folders). The Succession Act provisions that ss 61D(6) and 107(4) apply (ss 41(8) and 44) are worked by hand from that subject's deposited text, cited in the core.
No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

**Powers of Attorney Act 1998** (act-1998-022), the version in force from 28 April 2026 and current on 6 November 2026, as deposited at `../../registers/source-bundle/act-1998-022.txt` (retrieved 2026-11-06, unofficial plain-text conversion of the Queensland Legislation HTML view).

Applied by the Act and read from another deposit: the **Succession Act 1981** (Qld) s 41(8) (9 months, applied to s 107 applications by s 107(4)) and s 44(2)-(3) (the personal representative's protection, applied by ss 61D(6) and 107(4)), from `../../../succession-act-1981/registers/source-bundle/act-1981-069.txt`.

Not deposited, and so asked as facts or left out: the **Trusts Act 2025** (what a trustee may invest in, s 84(3)(a)); the **Acts Interpretation Act 1954** (how periods are counted; the readings are the encoder's, in `poa-dates.l4`); the value of a **penalty unit** (answers are in penalty units); the **Guardianship and Administration Act 2000** (QCAT's procedure, and guardians and administrators, s 70); the court rules.

## Checks

| Module | Run | Result |
|---|---|---|
| `poa-dates.l4` | `l4 run` | 0 errors, 0 warnings |
| `poa-core.l4` | `l4 run` | 0 errors, 0 warnings |
| `poa-seat.l4` | `l4 run` | 0 errors, 0 warnings |
| `poa-seat-attorney.l4` | `l4 run` | 0 errors, 0 warnings |
| `poa-cases-claimant.l4` | `l4 run` | 0 errors, 0 warnings; **155 assertions written, 155 satisfied** |
| `poa-cases-attorney.l4` | `l4 run` | 0 errors, 0 warnings; **35 assertions written, 35 satisfied** |

In addition, 4 `#TRACE`s carry an `-- expect:` line, one per regulative rule (s 106, s 107, s 61D, s 124), each a day late; each was read and ends in the breach expected, with the reason written. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read (run on 2026-11-07). Every expected value was written by hand from the text, with the arithmetic in the comment above the assertion.

## Seats

**The claimant (first seat)**: the principal whose attorney dealt with their affairs (or someone acting for them), or, after the principal's death, the principal's personal representative, a beneficiary of the estate, or a person whose benefit in the estate was lost. The principal is "you" where the principal asks; a claimant asking after the death answers the same facts about the principal. They ask:

- "Could my attorney act then? Can the power of attorney be declared invalid? Is the attorney liable for using a power that was invalid? Is a sale to someone else still good?"
- "Was my attorney allowed to buy my car, invest my money that way, mix our money, give my property away, pay for my grandchild? Is undue influence presumed? Is it an offence, and what is the most they can be fined?"
- "Can I get compensation, or the attorney's profits? By when must I apply, and is my application in time?"
- "The attorney sold the house the will left me: do I take the proceeds, can I be compensated out of the estate, by when, and can the executor distribute before I act?"
- "Can I apply to the court, which court or QCAT, can I get the attorney's accounts, who pays the costs, and when do I get reasons?"

**The attorney (second seat)**, answering such a claim: "Was I allowed to do this? Must I keep my property separate? Am I protected because I followed the court's advice, or did not know the power was invalid? Can the court relieve me? Can I be ordered to pay compensation or my profits? What is the most I can be fined? Can I resign?"

The court, QCAT, the public guardian and the public trustee are never seats; their powers appear as what the person can ask for or must be given.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** The Act sets its own numbers; the two Succession Act provisions it applies are worked in (above). No regulation is needed.
- **The actors the text names:** the principal, the attorney, the court, the tribunal, the third person, the beneficiary, the personal representative.
- **Judgments left to others are answered conditionally, as inputs:** whether a gift's value or a dependant's provision is reasonable (ss 88(1)(b), 89(2)); whether the court considers the attorney acted honestly and reasonably and ought fairly to be excused (s 105); whether the court considers the person has a sufficient interest (s 124); whether a distribution was properly made (Succession Act s 44); whether the court is satisfied of a ground (s 113(2), named in the answer, never decided).
- **The Act's own definitions are worked out from facts:** capacity and impaired capacity (schedule 3, three limbs), capacity to make an enduring power of attorney (s 41(1)), invalidity and know (s 96), conflict transaction (s 73(6)-(8)), relation and close friend (schedule 3, as the choices of the s 87 input), dependant, family (s 110(5)), interested person, the attorneys each section reaches (ss 65, 98(1), 106(9), 107(5)). Borrowed terms are asked as facts: business associate, authorised investment under the Trusts Act 2025, the general law's capacity for a document other than an enduring power of attorney.
- **One case:** one principal, one attorney, one exercise of power or transaction.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out** (below).

## Scope

**In:**

- s 33: when power under an enduring power of attorney is exercisable (financial and personal matters)
- schedule 3 capacity and impaired capacity; s 41(1) capacity to make an enduring power of attorney
- ss 113-114: the grounds for declaring a document invalid, void from the start, appointing attorneys
- ss 96, 98: invalidity, "know", and the attorney's protection when unaware
- s 99(2)-(3): a third person's transaction under an invalid power, and the purchaser's conclusive presumption (3 months; 1 year)
- s 73: conflict transactions, authorisation before and after (with s 118(2)-(4)), s 73(9) for the other party
- s 87: the presumption of undue influence
- ss 83, 84, 86, 88, 89: Part 3 for enduring powers of attorney (investment, separate property, gifts, dependants)
- ss 26, 61, 66(1), 71, 74A, 86(1): the maximum penalties
- ss 66(2), 106: compensation and accounting for profits, the payee, the 6-month times, extension
- s 107 with Succession Act s 41(8): compensation for a lost benefit, the cap, the 9 months
- ss 61A-61D: a will beneficiary's interest in proceeds, who may apply, the 6 months, the Supreme Court only
- Succession Act s 44(2)-(3), applied by ss 61D(6) and 107(4): the personal representative's protection for a distribution
- ss 109A, 110: who may apply, and the court or QCAT for each kind of application
- s 122: records, accounts, audit and a management plan
- ss 123, 125: dismissal and costs; s 124: written reasons within 28 days
- ss 72, 82: resignation (attorney seat); s 97: acting on the court's advice; s 105: relief from personal liability

**Out, and why:**

- ss 1-6B, 162-180 and schedule 1 (preliminary, relationship with other Acts, regulations, transitional provisions): machinery.
- ss 6C-6D (general and health care principles): standards the attorney applies, with no outcome the person can compute; s 118(2) refers to them and is in only as an authorisation.
- Chapter 2 (ss 7-26, other than the s 26 penalty) and chapter 3 parts 1-2, 4-5 (making, executing and revoking documents, eligible attorneys, witnesses, registration, part 3A business powers): the making and revocation of a document; revocation is asked as a fact (s 96), and the formal requirements as one fact (s 113(2)(b)). These could be added as a further layer.
- chapter 3 part 3 and chapter 4 (advance health directives, statutory health attorneys) and schedule 2 parts 2-3 (health and special health matters): health decision-making, not claims about dealings; the kinds of attorney appear only to decide which sections reach them.
- ss 67, 69, 70, 74, 77-81 (acting under the terms, execution of instruments, guardians and administrators, confidential information uses, maximum power, joint attorneys, consultation, the right to information): duties without a claim outcome to compute, other than the s 74A penalty.
- s 85 (keep records): a duty with no stated penalty; its enforcement is s 122, which is in.
- ss 99(1), 100-104 (third-party reliance on the witness certificate; health providers' protections; forensic examinations): health and third-party protections outside the claimant's or attorney's questions.
- ss 108-109, 111-112, 115-118(1), 120-121 (the court's general powers, declarations about capacity and commencement, removal and change of documents, proceeding without material, reports): powers without a date, amount or condition the person can compute beyond "the court may".
- Succession Act s 44(1) (distributions for a dependent spouse or child) and the rest of the Succession Act provisions s 107(4) applies (ss 41(2)-(7), (10)-(11)): not claims-machinery questions here.
- Limitation periods outside the Act (for a claim while both principal and attorney live): not in this Act; the Limitation of Actions Act 1974 has its own encoding.

## Negatives (the convention of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05)

The answers are enumerations, not `MAYBE BOOLEAN`; each "no" constructor stands for `JUST FALSE` and each "the Act does not settle this" constructor for `NOTHING`.
Answers say no only where the text does: "only if" (s 41(1), s 73(1), s 84(1), s 88(1)), "only" (s 61A, s 83, s 82(1)), "and not otherwise" (s 33(4)), "means" definitions (ss 96, 106(9), 107(5)), "if" conditions (ss 99(3), 105, 107(1), 113(2), Succession Act s 44), "unless" (s 97), "must not be more than" (s 89(2)), and defences not made out (ss 73(9), 98(2), 99(2): "this section gives no protection on these facts"). Where a grant or list is limited in its own words without "only" (ss 33(1), 61B(1), 61D(2), 87, 89(1), 107(2), 110, 122), the answer outside it is that the Act does not settle it.

The rulings, in the parts this encoding relies on, quoted from `docs/ENCODING-GUIDE.md` (which records them in full):

- **E1**: option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else. (This encoding answers per section.)
- **N2**: option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table.
- **Periods, "where" and scope limits**: (a) a period the text fixes in its own words: outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only": outside the scope the answer is `NOTHING`.
- **Delegated definitions, defences and "until" bars**: (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all".

Fork lines (case-by-case decisions under Meng's ruling of 2026-11-05, for the reviewer to overrule):

1. s 33(1), `the s 33 answer`: a specified time not yet come, with the principal having capacity, answers that the Act does not make the power exercisable yet (`NOTHING`); the other reading is a plain no, implied by s 33(2)-(3). Asserted.
2. s 73(6) example 6, `the s 73 answer`: providing for a dependant under s 89 is read as not a conflict transaction, because the example says so; the other reading treats examples as illustrative only (the Acts Interpretation Act is not deposited), leaving it to s 73(6)-(7). Asserted.
3. ss 72, 82, `the resignation answer`: a statutory health attorney answers `NOTHING` (Part 1 does not apply to them, s 65, and s 82 speaks of "an attorney under an enduring document"); the other reading is that they may resign as the general law allows. Asserted.
4. s 113(2), `the s 113 answer`: the grounds are reported in the text's order, the first that holds; for a document other than an enduring power of attorney, capacity is one input; the other reading reports every ground that holds.
5. Succession Act s 44(3)(b), `the s 44 answer`: "if notice ... has been received" is read as the claimant having given written notice before the distribution; the "unless" (notice of commencement, or service) is read as taking the protection away whenever it happened before the distribution. Asserted.
6. s 106(1), `the s 106 answer`: "may order ... to compensate for a loss caused by" is read as a grant limited in its own words, so a failure with neither loss nor profit answers that s 106 gives no order (`NOTHING`-kind wording); the other reading is a flat no.

## What the Act turns out to say (findings)

1. **Two deadlines for one sale of a willed house.** A will beneficiary whose gift the attorney sold has 6 months after the death for a s 61D order (s 61D(4)) but 9 months for s 107 compensation, because s 107(4) borrows the Succession Act's s 41(8) while s 61D(6) borrows only s 44(1)-(4). Asserted (14 February and 14 May 2027).
2. **The personal representative's protection starts on the s 61D deadline.** Under the Succession Act s 44(3)(a), applied by s 61D(6), a distribution properly made from 6 months after the death without notice is protected, and 6 months is also the last day for a s 61D application: on 14 February 2027 the application is in time and the distribution protected. A beneficiary who has not given written notice before then may find the property gone. Asserted.
3. **s 87 omits general powers of attorney but includes advance health directives.** The presumption of undue influence reaches an attorney under an enduring power of attorney or an advance health directive (whose attorney has only personal and health powers), not an attorney under a general power of attorney, who deals in financial transactions. Asserted.
4. **Part 3 protects only enduring powers of attorney.** By s 83, the investment limits, the separate-property offence, and the gift and dependant limits (ss 84, 86, 88, 89) do not reach an attorney under a general power of attorney, though s 73 does. Asserted.
5. **s 99(3)(b) runs from the making of the power, not its use or revocation.** A transaction completed within 1 year after the power of attorney was made is conclusively presumed, in a later purchaser's favour, to have been made without knowledge of the invalidity, even if it was made under a power revoked the week before. Asserted at the 1-year edge, including a power made on 29 February.
6. **s 106 has an application time only once someone has died.** While the principal and the attorney both live, s 106 sets none (other limitation law is not considered); when the attorney dies first, a living principal also has only 6 months (s 106(5)). Asserted.
7. **Two compensation powers overlap.** s 66(2) lets "the court" (the Supreme Court, schedule 3) order compensation for a failure to act honestly and diligently; s 106 lets "any court" or QCAT order compensation for any failure to comply with the Act, with its own time limits. The Act does not say whether the s 106 times apply to a s 66(2) order. Noted, not asserted.
8. **s 107 has no time of its own.** Its 9 months come only through s 107(4)'s borrowing of Succession Act s 41(8), whose "unless the court otherwise directs" replaces an express extension power. Asserted.

## Before relying on it

- Have a lawyer check the fork lines and findings 1, 2, 5 and 7.
- Deposit the Acts Interpretation Act 1954 (Qld) and check the date readings in `poa-dates.l4` and the status of examples (fork line 2).
- Add the making and revocation of documents (chapter 2 parts 2-3, chapter 3 parts 4-5) as a further layer, so that "revoked" and "does not comply with the requirements" are worked out rather than asked.
- Link to the Succession Act and Limitation of Actions Act encodings in a register when the language allows cross-folder links.
- An independent test pass, and the human gates.
