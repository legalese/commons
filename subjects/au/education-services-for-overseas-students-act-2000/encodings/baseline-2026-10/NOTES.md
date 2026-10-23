# Education Services for Overseas Students Act 2000 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it, and no question reaches a gap that needs a `not covered` answer. The refund *amounts*, which the Act leaves to an agreement or an instrument, are not asked for.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It satisfies `REQ-0080` in `subjects/au/requirements.jsonl` (a scheduled priority-2 entry for the 20 topics: education). There was no earlier encoding of this Act to keep. No scenario life raised it: the student in the case file (Priya, enrolling from India in a two-year diploma in Perth) and every date are the encoder's, hypothetical.

Ten questions are exported, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order.

## Edition

Compilation No. 45, compilation date 5 December 2025, includes amendments up to Act No. 74, 2025 (register id **C2025C00684**), as deposited at `../../registers/source-bundle/C2004A00757.txt`.

No instrument is deposited. Here is what that leaves open:

- **Refund amounts are not computed.** They are set by the student's written agreement (s 47D) or by the Minister's legislative instruments under ss 46D(7) and 47E(4).
- **Asked as facts:**
  - who holds a "student visa", and the kinds of student the regulations exclude (s 5);
  - providers exempted by the regulations (s 31(b), (c));
  - registration on the Register (s 14A);
  - the "suitable alternative course" criteria (s 49(6)).
- **Not deposited:** the national code (Part 4), which sets the requirements a s 47B agreement must meet.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `esos-student.l4` | `esos-cases-student.l4` | 46 written, 46 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-23). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the text.

## Seat

**The overseas student, or intending overseas student** (s 5). The questions are the ones that person asks:

- "Is this provider allowed to enrol me?"
- "How much can it make me pay up front, and is that money safe?"
- "What will it report about me, and when?"
- "My course didn't start, or the college closed: what happens to my fees?"
- "I withdrew, or didn't start: what do I get back, from whom, and by when?"

Nearly every duty in the Act falls on the registered provider, the TPS Director or the ESOS agency. Those duties are encoded as what they mean for the student.

The 2026-10-18 defaults:

- **The Act alone.** No instrument is deposited (see Edition).
- **The actors the text names:** the student, the registered provider, the TPS Director, the Overseas Students Tuition Fund (OSTF), the ESOS agency and the Immigration Minister.
- **Judgments left to others, answered conditionally:** the TPS Director's determinations (ss 49, 50A) and the provider's natural justice (s 47A(3)). The TPS Director's own determination is taken to follow the facts given.
- **The Act's own definitions worked out from facts:** overseas student, intending overseas student, provider default, student default, default day, agreed starting day and provider obligation period. **Borrowed terms asked as facts:** student visa, registration, and Commonwealth recurrent funding.
- **One case:** one student, one course and one location.
- **The Act's own terms,** quoted in the comment above each rule.
- **Machinery out:** registration, levies, the TPS Director's office, the Board, monitoring and enforcement.

## Scope

**In:**
- s 5: overseas student and intending overseas student.
- ss 8(1), (2) and 101(1): whether a provider may offer the course.
- s 27: the 50% limit on fees taken before the course begins.
- ss 28, 29(1)–(6) and 31: the protected account for prepaid fees.
- s 19(1), (1A): what the provider must report about me, and by when.
- ss 46A, 46D(2)–(6) and 46B(4): provider default, and the 14 days.
- s 49: the TPS Director's placement options, with 30 days to accept.
- ss 50A(2)–(5), 50B(1), (3), (4) and 50C(1): calls on the OSTF.
- ss 47A, 47B, 47D and 47E: student default and the refund owed.
- s 48: recovering the refund as a debt.

**Out:**
- Registration (Part 2), and the providers' other duties: ss 15–18, 21–21B and 26. Section 15 (no misleading or deceptive conduct) is enforced against the provider by the ESOS agency and gives the student no remedy in this Act.
- The national code (Part 4).
- Parts 5A and 5B: TPS levies, the OSTF's administration, the TPS Director and the Board.
- Parts 6 and 7: sanctions, suspension certificates beyond s 101, monitoring and enforcement.
- Part 7AA (review), which only an "affected provider" may seek.
- The offences' penalties, which are quoted in comments.
- Parts 1 and 8.

Business days (s 29(2), s 46B(2)) are not counted. A default day of 29 February would make the "12 months after" date invalid; no case uses one.

## What the Act turns out to say

1. **An intending student is protected before the visa.** Section 5 covers a person who "intends to become, or ... has taken any steps towards becoming" a student visa holder. The default and refund rules (Part 5) apply to "an overseas student or intending overseas student" alike. So a student whose visa is refused is still protected (finding 7). Asserted.
2. **Only a registered provider, or someone working under its arrangement, may offer the course.** That means a provider registered for that course at that location (s 8). Breach is an offence carrying 2 years' imprisonment. While an Immigration Minister's suspension certificate is in effect, no one may offer or invite students to the provider's courses, though it stays registered for other purposes (s 101). Asserted.
3. **A provider may take at most half the fees before the course starts, with two exceptions.** The limit (s 27) does not apply if the student (or whoever pays) chooses to pay more, or if the course lasts 25 weeks or less. So a 25-week course has no limit, and a 26-week course has the 50% limit. Asserted.
4. **Prepaid fees are ring-fenced, except at public providers.** Fees paid before the course starts must go into an Australian ADI account within 5 business days (s 29). The account must always hold enough to repay every student who has not yet started, and that money "is not available for the payment of a debt of any creditor". Exempt (s 31) are providers run by a State education authority, those with Commonwealth recurrent funding (most public universities), and any the regulations name. Once the student begins, the fees leave the protection. Asserted.
5. **The provider has 14 days after a default.** On a provider default (s 46A), the provider must, within 14 days after the default day, do one of two things (s 46D):
   - arrange a place in another course at its expense, which the student accepts in writing; or
   - refund the "unspent tuition fees", by the Minister's method.

   If it does neither, the TPS Director must offer suitable alternatives where any exist, and the student has 30 days after the 14 to accept in writing (s 49(5)). The Fund then pays the new provider, or refunds the student (ss 50A(2), (3), 50B). For a 1 March 2027 default, that is 15 March for the provider and 14 April for the student. Asserted.
6. **The Fund's protection lapses after 12 months, and payment ends the claim.** No call is made on the Fund if the TPS Director "becomes aware" of the failure "more than 12 months after the relevant default day" (s 50A(5)). This turns on when the TPS Director learns, not on when the student claims. Once the Fund pays, the student's claim against the provider ends (s 50C(1)), and the provider owes the TPS Director instead. Asserted (a 1 March 2027 default first known on 1 March 2028 still qualifies; on 2 March 2028 it does not).
7. **A student who withdraws is owed a refund too.** Withdrawing, not turning up on the agreed day, or being refused for non-payment, a visa breach or misbehaviour (after natural justice) is a *student* default (s 47A). The provider must still refund:
   - **under the written agreement** (s 47D): within 4 weeks of the student's written claim, to the student or the person the agreement names; or
   - **under the Minister's method** (s 47E): within 4 weeks of the default day. This applies if there is no compliant agreement, or if a refused visa caused the default.

   If the provider does not pay in time, the Fund does (s 50A(4)). The student may also sue for the refund as a debt (s 48). Asserted (dates; the amount is the agreement's or the instrument's).
8. **Who defaults when the course never starts decides which rules apply.** If the course did not start because of the provider, the student has not defaulted (s 47A(2)). If the student was refused for non-payment, a visa breach or misbehaviour, the provider has not defaulted (s 46A(3)). A refusal for misbehaviour counts as the student's default only after natural justice (s 47A(3)). Asserted.
9. **The provider's report clock is shorter for minors.** The provider must report a student who does not begin, or whose studies end early, within 14 days if the student is under 18, and 31 days otherwise (s 19(1A)). Every other report is 31 days. This report is what the student visa system acts on. Asserted.
10. **Students have no review right in this Act.** Part 7AA's reviewable decisions are applied for by "the affected provider". The student's remedies are the refund duties, the Fund, and an action in court (s 48). Not asserted (no question turns on it).

## What would need doing before this is worth relying on

- **The Minister's instruments**: the refund methods under ss 46D(7) and 47E(4) (unspent tuition fees, and refunds without an agreement); the suitable-alternative-course criteria under s 49(6); and the payment requirements under s 50B(5). Also the **national code** (Part 4), which a s 47B agreement must meet. With those, the refund amounts could be computed. Raised as `REQ-0102`.
- **The ESOS Regulations**: "student visa", excluded students, s 31 exemptions and the prescribed s 19 details.
- **Business-day counting** for s 29(2) (fees into the account in 5 business days) and s 46B(2), against the public holidays of the provider's State.
- **Wider sources.** No guidance, TPS policy or case was read.
