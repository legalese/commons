# Evidence Act 1995 — baseline encoding, the seat of the person bringing a civil claim

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its `references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
No REFUSE, no `#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. A claim in a State or Territory court answers `not covered`, asserted.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

This is a second encoding beside `../baseline-2026-10/` (the accused's seat, criminal proceedings), which is untouched. That encoding left civil proceedings out; this one takes the provisions a person bringing a civil claim meets: a claim for compensation or damages, an employment, discrimination or consumer claim, an insurance or superannuation claim, a class action, a claim on a deceased estate.

Three files:

- `ea95-claimant-days.l4`: the date helpers (plain days, working days for s 160), the only module that imports `daydate`;
- `ea95-claimant.l4`: 21 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order, with the situation in the heading where a group arises only in one ("if I want to rely on it", "if they have given me notice"); one regulative rule (ss 68, 168) run by EVALTRACE inside two questions that take only plain facts and dates;
- `ea95-cases-claimant.l4`: the cases.

Answers are enumerations worded from the text, as in the accused's encoding, not `MAYBE BOOLEAN`, so no `NOTHING-kind` tags are carried. The 2026-11-04 and 2026-11-05 rulings on negatives are followed in the wording: where the text itself says no (an "unless", an "if", "does not apply if"), the answer says "no"; where the case falls outside what a provision covers, the answer says the provision "does not reach it" or "gives no exception on these facts", and points to what else may apply.

## Edition

The compilation registered as **C2025C00340** (Compilation No. 35, compilation date 10 June 2025, including amendments up to Act No. 118, 2024), retrieved from the Federal Register of Legislation on 13 October 2026, as deposited at `../../registers/source-bundle/C2004A04858.txt`.

No other instrument is brought in. The provisions encoded take their numbers from the Act itself (21 days in ss 68, 168, 177; seven working days in s 160). Public and bank holidays (s 160(3)) are an input, a list of dates. Rules of court on the form of notices (ss 67(2), 99) are taken as given.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read (a deliberately wrong assertion, run once in a scratch file since deleted, showed as `DiagnosticSeverity_Error`, "assertion failed").

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `ea95-claimant-days.l4` | 0 | 0 | 0 | 0 |
| `ea95-claimant.l4` | 0 | 0 | 0 | 0 |
| `ea95-cases-claimant.l4` | 0 | 0 | 122 | 122 |

Every expected value was worked by hand from the text, with dates counted on a calendar: the 21 days of ss 68 and 168 on the last day and the day after, on the day of the notice, still open on the last day and too late the day after, and late with leave (s 168) and without any leave to give (s 68); s 177's 21 days before a hearing on 15 March 2027 (22 February 2027) served on that day and the day after, with a substituted period of 14 and 28 days; s 160's seventh working day from a Friday, from a Saturday, across a mid-week holiday, and across Christmas and New Year 2026–27 (6 January 2027); every branch of each question.

## Seat

**The person bringing a civil claim** (the plaintiff or applicant), in a court to which this Act applies. The questions are the ones that person asks: "Does this Act govern my claim?", "Can I use what the witness said?", "Can my specialist's letter go in without her?", "Can I use the driver's conviction?", "Can my expert's report go in by certificate?", "Can they see what I told my lawyer?", "Can my offer to settle be used against me?", "When is my posted notice taken to have arrived?", "By when must I object to their notice?". Where the other side is the one adducing (the s 68 objection, the s 168 requests, the s 177(5) notice, client legal privilege), the question is asked from the claimant's end of it.

The 2026-10-18 defaults:

- **The Act alone.** Who bears the burden of proof on each fact (for s 140) is for the law that gives the claim or defence, and is not asked.
- **The actors the text names:** the party, each other party, the person who made a previous representation, the expert, the client and lawyer, the persons in dispute, the court.
- **Judgments handed to the court are answered conditionally.** Every finding, satisfaction or discretion is an input worded "the court finds …" or "the court thinks …": undue expense or delay (s 64(2)), significant probative value (ss 97, 98), substantially outweighed (s 135), reasonable cause (ss 169, 177(7)), good reason for leave (s 168), another loss of privilege (ss 121, 123–126), another s 131(2) exception, not genuinely in dispute (s 190(3)), satisfaction on the balance of probabilities (s 140). None is guessed.
- **The Act's own definitions are worked out from facts:** "federal court" and "civil proceeding" (Dictionary), "not available" (Dictionary Part 2 cl 4, with (b)–(e) asked as one fact and (f), (g) as one), "working day" (s 160(3)), "business" (Dictionary Part 2 cl 1, in the `@desc`).
- **One case:** one claim, one piece of evidence (one statement, one record, one opinion, one communication, one letter or one notice).
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** ss 1–3, 8–11, regulation-making.

## Scope

**In:** s 4(1), (5), (5A) with the Dictionary's "federal court" and "civil proceeding"; s 140; ss 59, 60(1), 62, 63, 64, 66A, 67, 68 and Dictionary Part 2 cl 4; s 69; ss 76(1), 78, 79(1), 80; s 177; ss 91, 92(1)–(3); ss 94(1), (3), 97, 98, 100; ss 118, 119, 120(1), 122(1)–(3), (5) (ss 121, 123–126 as one fact); s 131(1), (2), (5)(b); ss 135, 136; ss 160, 161; ss 166–169; ss 190(1), (3), 191.

**Out, and why:**

- **Chapter 2** (witnesses, examination and cross-examination, documents, ss 12–58): the claimant meets it as a witness and in proving documents (ss 47–51 originals and copies); it is the next thing to add. Competence and compellability are in the accused's encoding for a criminal trial.
- **ss 61, 65, 66** (competence exception, criminal-only hearsay), **ss 70–75** (tags and labels, electronic communications, traditional laws, reputation, interlocutory proceedings): less often met; s 75 (hearsay in interlocutory proceedings if the source is given) would be a short addition.
- **Part 3.4 admissions (ss 81–90):** an admission by the defendant (an apology at the scene) is something a claimant meets often; ss 81, 82 and 87 apply in civil proceedings. Left out to keep this layer to the provisions without an equivalent in the accused's encoding; it is the first thing to add after Chapter 2.
- **Part 3.7 credibility, Part 3.8 character** (mostly criminal), **Part 3.9 identification** (criminal).
- **s 120(2), ss 121, 123–126 in detail, ss 126A–128A** (journalists, religious confessions, self-incrimination: the last is in the accused's encoding), **public interest immunity (ss 129–131A)**.
- **ss 137–139, 141** (criminal only), **s 142** (the standard for preliminary questions: always the balance of probabilities, asked within each finding).
- **Chapter 4 other than ss 160, 161, 166–169, 177:** judicial notice, other presumptions (s 162 lettergrams, s 163 Commonwealth letters), certificates other than expert certificates.
- **Chapter 5 other than ss 190(1), (3), 191:** s 190(2) (criminal), s 192 (terms of leave), s 192A (advance rulings), ss 185–187.
- **The Acts Interpretation Act 1901** (counting periods) is not brought in; see fork F1.

## Forks (one reading taken; the other for a reviewer to overrule)

- **F1. ss 68, 168: "within 21 days after" / "not later than 21 days after" the notice.** `I must take the step within 21 days`, `what became of my step`. Taken: the day of the notice is not counted, so the 21st day after it is the last day (notice 1 March 2027, last day 22 March 2027). Other reading: the Acts Interpretation Act 1901 s 36(2) also moves a last day that is not a working day to the next one; not encoded, so a last day on a weekend or holiday answers one day or more early.
- **F2. s 160: "on the seventh working day after having been posted".** `the working day … after …`. Taken: the day of posting is not counted, whether or not it is a working day (posted Saturday 7 November 2026 gives the same day as Friday 6 November: 17 November). Other reading: none apparent in the text.
- **F3. s 177(3): "not later than: (a) 21 days before the hearing".** `The last day to serve my expert certificate question`. Taken: the hearing day less 21 days is the last day (15 March 2027 → 22 February 2027). Other reading: 21 clear days, which would make it 21 February. "The hearing" is taken as its first day.
- **F4. The hearsay question's order.** `How can I use the statement question`. Taken: s 60 first, then s 66A, then first-hand hearsay (s 62) and the form of the evidence, then unavailability (s 63) before availability (s 64). A representation the maker is called to repeat (s 64(3)) is accepted even if the evidence of it would otherwise be second-hand, since the maker may give it. Other reading: s 64(3) only where the perceiver route is also met.
- **F5. s 68: notice "discloses" not calling the maker.** `By when can I object to their hearsay notice question`. Taken: no s 68 objection unless the notice gives the s 64(2) grounds. Other reading: an objection under the court's general powers; not in this Act.
- **F6. Client legal privilege when I do not object.** `Is it protected question`. Taken: "protected only if I object", since ss 118–120 operate "on objection by a client" or party.

## What the Act turns out to say

1. **This Act does not govern most claims for injury compensation.** It applies to proceedings in a federal court (s 4(1); Dictionary "federal court"): the High Court, the Federal Court, the Federal Circuit and Family Court. Most personal injury, motor accident, workers' compensation and estate claims are brought in State or Territory courts and tribunals, where that State's or Territory's evidence law applies (picked up by Judiciary Act 1903 s 79 for federal jurisdiction, s 4 Note 4). Such a claim answers `not covered`. Asserted. The Evidence Acts of NSW, Victoria, Tasmania, the ACT and the NT are largely in the same terms, which this encoding does not check; those of WA, SA and Queensland differ.
2. **An appeal from a State court is not governed at all** (s 4(5)), except a family law appeal from a court of summary jurisdiction to the Federal Circuit and Family Court (Division 1) (s 4(5A)). Asserted.
3. **A report obtained for the claim is not a business record.** Section 69(3)(a) takes out a representation "prepared or obtained for the purpose of conducting, or for or in contemplation of or in connection with" a proceeding, so a medico-legal report on an insurer's file cannot come in under s 69, though the same doctor's clinical notes can. Asserted.
4. **A party's conviction can be used against them; a stranger's cannot.** Section 92(2) lets the claimant use the conviction of "a party, or a person through or under whom a party claims", unless it is under appeal, quashed or pardoned. A claimant who sues the vehicle's owner or the driver's employer, but not the convicted driver, cannot use the conviction (s 91(1)). Asserted.
5. **The s 68 objection has no leave; the s 168 requests do.** After a s 64(2) notice, the 21 days to object are fixed: the Act gives no power to extend them. After a notice or a served copy, the 21 days to make a request may be extended by leave "if [the court] is satisfied that there is good reason" (s 168(2), (4), (7)). Asserted.
6. **Requiring an expert to be called has no time limit, but has a costs risk.** Section 177(5) sets no time for the notice requiring the expert to be called; s 177(7) allows costs against a party who did it "without reasonable cause". Asserted.
7. **An offer to settle is protected, except on costs.** Section 131(2)(h) lifts the protection for a communication "relevant to determining liability for costs". The rule protects only a civil settlement, not the settlement of a criminal proceeding (s 131(5)(b)). Asserted.
8. **A person who brings their claim without a lawyer has their own privilege.** Section 120 protects a confidential communication or document made or prepared for "the dominant purpose of preparing for or conducting the proceeding" by an unrepresented party, and stops protecting new ones once a lawyer is on the record. Asserted.
9. **A posted letter is presumed received on the seventh working day, counted at the address.** Section 160 counts holidays "in the place to which the postal article was addressed", not where it was posted. Asserted.
10. **In a civil claim tendency evidence needs notice and significant probative value, and nothing more.** Section 101's further test is for the prosecution in criminal proceedings; in a civil claim only the s 135 discretion remains. A civil party may apply to be excused from notice without notifying the others (s 100(4)). Asserted.
11. **Section 140 does not say who must prove what.** It sets the standard (the balance of probabilities, weighed against the gravity of what is alleged), but the burden comes from the law that gives the claim or defence. Asserted as the "no" answer's wording.
12. **The privilege sections govern adducing evidence at the hearing, not discovery.** Sections 118–120 say "evidence is not to be adduced"; they do not on their terms govern what must be produced before the hearing. Section 131A extends only Division 1C (journalists' informants) to court processes requiring disclosure. Pre-trial production is left to other law, not encoded. Noted, not asserted.
13. **Two hearsay routes need no notice.** A contemporaneous statement about one's own health, feelings or sensations (s 66A: "my back is killing me") and a statement by a maker who is called (s 64(3)) need no s 67 notice. Asserted.

## What would need doing before this is worth relying on

- **The State and Territory evidence law** for the courts where most claims are heard, linked through Judiciary Act s 79.
- **Chapter 2 and Part 3.4** (witnesses, documents, admissions), which a claimant meets in almost every claim.
- **Case law.** No case was read. Significant probative value, the s 135 balance, undue expense, dominant purpose and inconsistent conduct (s 122) are worked out by the courts; this encoding asks each as the court's finding.
- **The Acts Interpretation Act 1901 s 36** on counting periods (fork F1) and the Federal Court Rules on notices (ss 67(2), 99).
- An independent test pass and a human review.
