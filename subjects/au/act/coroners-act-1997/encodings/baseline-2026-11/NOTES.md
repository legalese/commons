# Coroners Act 1997 (ACT) — baseline encoding: the family's, the witness's and the owner's seats

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18 and the `writing-l4-rules` skill.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
There is no REFUSE in it. A question that reaches a case the Act does not speak to answers a `not covered` constructor with a reason, and the cases assert it.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It was written as part of a run of baseline encodings of the Acts behind compensation and other civil claims. An inquest is often where a family first learns how a death at work, on the road, in hospital or in custody happened, and its findings, the evidence gathered and the people criticised all feed a later claim. The Act is of moderate size and is encoded across every Part that gives an individual a right, a duty or a deadline; the rest is listed below with reasons. There was no earlier encoding of this Act to keep. No ledger entry was open for it (the ACT has no requirement ledger).

Four modules:

- `coroners-dates.l4`: the date helpers (days, months and years after a day), on the prelude's date functions only;
- `coroners-family.l4`: the first seat, a member of the deceased's immediate family (29 questions);
- `coroners-witness.l4`: a witness, including a person the coroner may criticise, the treating doctor and the person in charge of records (15 questions);
- `coroners-owner.l4`: the owner or occupier of fire-damaged property, or of a place searched or made a coronial investigation scene (7 questions).

The three seat modules import only the date module, so their names never meet. Each question has `@export` and a `@desc` on every input, under `§§` headings in the Act's order; headings for situations the person may not be in say so ("only if a prosecution arises", "only if I have been served with one", and so on).

**Regulative rules.**

1. `s 64(5), (7) and s 90 -- what must happen after my request is passed on` (family module): `PARTY the coroner MUST respond WITHIN 14 HENCE (PARTY the Chief Coroner MUST give me notice that a hearing will be conducted WITHIN 14) ROR (PARTY the Chief Coroner MUST give me notice that a hearing will not be conducted WITHIN 14 HENCE PARTY I MAY apply to the Supreme Court WITHIN 30 LEST BREACH ... BECAUSE) LEST BREACH ... BECAUSE`. The seat questions take plain dates (`Last day for the coroner's response`, `Last day for the Chief Coroner's notice`, `Last day to apply to the Supreme Court`). The cases assert both duties kept on their last days, the application on the 30th day, not applying (a permission is never breached), the coroner one day late, and the Chief Coroner silent; the late response is `#TRACE`d.
2. `s 100 -- I must keep the records` (witness module): `PARTY I, the person in charge SHANT dispose of the records WITHIN <days> LEST BREACH ... BECAUSE`. The seat question `How long must I keep the records` gives the last day from the date of death. The cases assert disposal on the last day (a breach), the day after (kept), never (kept); a disposal on day 500 is `#TRACE`d.

## Edition

Republication No 51 (R51), effective 5 September 2026, retrieved from the ACT Legislation Register on 6 November 2026, as deposited at `../../registers/source-bundle/A1997-57.txt` (converted from the register's DOCX, which the register marks as an unauthorised version). No instrument is brought in: the regulation that s 68A(2) would prescribe (information for the family), the Court Procedures Rules 2006 schedule 4 (witness expenses, s 98) and the Legislation Act 2001 (penalty units s 133, counting time s 151, domestic partner s 169, client legal privilege s 171) are not deposited. Amounts of money are therefore not computed: penalties are given in penalty units, and witness expenses are a discretion with no amount.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `coroners-family.l4` | `coroners-cases-family.l4` | 151 written, 151 satisfied; 1 trace, as its `-- expect:` line says |
| `coroners-witness.l4` | `coroners-cases-witness.l4` | 61 written, 61 satisfied; 1 trace, as its `-- expect:` line says |
| `coroners-owner.l4` | `coroners-cases-owner.l4` | 24 written, 24 satisfied |
| `coroners-dates.l4` | (used by all three) | |

`l4 run` on all seven files: 0 errors, 0 warnings (2026-11-07). `l4 run` exits 0 even when an assertion fails, so the diagnostics were read. Every expected value was written by hand from the text. Edge cases: each s 13(1) paragraph alone; s 13(2) with and without another paragraph; deaths outside the ACT of residents and non-residents; each death-in-custody limb and the carer exception; the last day for public notice (in February and in a leap year); notice one day late; the s 58A days for each route, at month ends and in a leap year; the s 64 deadlines on the last day and one day late; the s 90 30th and 31st days; the s 55 period at 13, 14, 28 and 29 days and an extension of 28 and 29 days; s 100 periods from 29 February; a warrant issued on 31 January; a scene order at 30 and 31 days; a police declaration at 23 and 24 hours.

## Seats

**First seat: a member of the deceased's immediate family**, or that member's representative (`coroners-family.l4`). The dictionary's definition is worked out from the person's relationship and, for an Aboriginal or Torres Strait Islander person, the community's traditions. "Must there be an inquest? Can I see the body or stop the post-mortem? Will there be a hearing, and will I be told? Can I take part? Can I get the findings? When can a paused inquest go on? Can I ask for a hearing, a fresh inquest, or go to the Supreme Court? Must I report the death?"

**Second seat: a witness** (`coroners-witness.l4`): a person summoned or asked to give evidence, documents or information (a treating doctor or nurse, an employer or co-worker, a family member), including a person the findings may criticise, the doctor who treated the person who died, and the person in charge of a hospital, institution or agency holding the records. An employer that is a company is a "witness" too for ss 43 to 45, but cannot have a s 51B certificate (s 51B(11)); the cases assert that.

**Third seat: the owner or occupier of property** (`coroners-owner.l4`): property destroyed or damaged by fire (Division 3.2), or a place a coroner's search warrant or a coronial investigation scene reaches. The family module's s 64, s 67 and ss 90 to 93 questions also cover fire inquiries; they are not repeated.

No seat is written for a coroner, the Chief Coroner, the Attorney-General, the police, a custodial officer or the Supreme Court. Their duties appear as what the person in a seat must be given and by when.

The 2026-10-18 defaults:

- **The Act alone.** The Acts it names (Mental Health Act 2015, Crimes Act 1900, Crimes (Sentencing) Act 2005, Children and Young People Act 2008, Intoxicated People (Care and Protection) Act 1994, Voluntary Assisted Dying Act 2024, Births, Deaths and Marriages Registration Act 1997, Magistrates Court Act 1930, Court Procedures Rules 2006, Criminal Code, Legislation Act 2001) are named, not encoded; whether something happened under them is asked as a fact.
- **The actors the text names:** coroners, the Chief Coroner, the Attorney-General, the DPP, the agency, the Supreme Court, the person in the seat.
- **Judgments handed to others are answered conditionally:** every "in the opinion of", "is satisfied", "believes on reasonable grounds", "considers" and "sufficient interest" is an input.
- **The Act's own definitions are worked out from facts:** member of the immediate family; death in care (s 3BB); death in custody (s 3C); custodial officer (s 3D); operation or procedure (s 13(5), in the input's wording). **Borrowed terms are asked:** domestic partner; Aboriginal or Torres Strait Islander person (defined by the dictionary but asked as one fact); cause of death certificate; public servant.
- **One case:** one death (one fire, one place, one witness's evidence).
- **The Act's own terms**, quoted in the comment above each rule and glossed in the `@desc` lines.
- **Machinery out:** Part 2 (the court, the coroners, oaths, registrars), ss 1 to 3A, 12, 17, 100A to 103, schedule 1.

## Scope

**In.** Family: the dictionary definition of member of the immediate family; ss 3BB, 3C, 3D; s 13; s 15; s 20; ss 23, 24; s 34A; ss 37, 38; s 42 (with s 40(1)); s 49(2)(c); s 52(1), (4); s 54(1); s 57A; ss 58(3), (5), 58A; s 64(1) to (5) and (7); s 65; s 67; s 68; s 68A(1), (3), (4); ss 69, 70, 74, 75(2), 76(1), (4); s 77(1); the penalties of ss 40(3), 65(2), 77(1) and 83; ss 90 to 93. Witness: s 19B; s 25; s 43; s 44(3); s 45; s 48(2); s 51B; s 55; s 98 (with ss 44(2)(b), 46(2)); s 99B; s 100. Owner or occupier: s 18; s 54(2); s 66(4)(d), (5), (6); s 68C(2), (3); s 68F(3).

**Out, and why:**

- Machinery: ss 1 to 3A, 3BA (objects), Part 2 (ss 4 to 11A), s 12, s 17, s 101 to 103, schedule 1.
- The coroner's own powers, which give no individual a right, a deadline or a fact to state: ss 9, 17A (regard to cultural beliefs: a general duty, no answer turns on it), 19 (disasters, on the Attorney-General's request only), 19A, 19C, 21, 22, 27 to 29, 31, 33 to 36, 39 to 39B (counsel assisting; for deaths in care or custody s 72 makes it mandatory, mentioned only), 41, 42A, 46(1), 47, 48(1), (3), (4), 50 and 51 (the coroner "may" act at the request of a person with sufficient interest: a discretion with nothing to compute), 51A, 52(2), 53, 56, 57 (the Attorney-General's report: s 57(4) counts from "the first sitting week after the end of 6 months", which needs the Assembly's sitting calendar), 59 to 63, 66(1) to (3) and (7), 68B, 68D, 68E (listed in a comment), 68G, 68H, 71 to 73, 75(1), 76(2), (3), 99, 100A.
- Duties and offences of officials: s 77(2) (police), s 78 (custodial officers).
- s 30(2) (copy of a reinterment order to the family): exhumation is out as a whole.
- s 32: see finding 8.
- s 68A(2): the information it requires is prescribed by a regulation that is not deposited.
- s 76A, s 89, s 99A: how the Criminal Code, corporate responsibility and contempt apply; they change no answer here.

## Fork register (questions with no convention, decided case by case)

Answers are enumerations whose wording carries the reach of each "no". The rulings of 2026-11-04 and 2026-11-05 in `docs/ENCODING-GUIDE.md` §5 were followed in choosing between "no" and `not covered`; each site below is a choice the reviewer may overrule.

- **s 13, no paragraph applies:** `not covered` (s 13(1) is a list with no "only", and s 12(2) keeps the coroner's older jurisdiction). The other reading: "no inquest".
- **s 13(3), resident, death outside the ACT:** "may hold, not required" (s 13(3) gives jurisdiction, not a duty). The other reading: s 13(1)'s "must" reaches it (finding 1).
- **s 13(2):** "no" where (i) is the only ground (a flat negative).
- **s 3C(1)(g), escape from an Intoxicated People Act carer:** not a death in custody (the definition "means"; the specific exclusion governs). The other reading: (f) "after being taken into ... custody" catches it (finding 4).
- **ss 23, 70, a family member asking to inspect the scene of another event in a care or custody death:** `not covered` (s 23 excludes the death and s 70 omits the request). The other reading: "no".
- **s 24 for a refusal under s 70:** "no" (s 24 is limited in its own words to s 23(1) refusals, a "where" condition).
- **s 42 for a person neither summoned nor with sufficient interest:** `not covered` (a grant limited in its own words).
- **ss 54, 75 for a person they do not name:** `not covered`. **s 54(2) for an occupier:** `not covered`.
- **s 51B(7) for a proceeding outside the ACT:** `not covered`.
- **s 55(3) for a statement where the comment is in a finding:** `not covered` (finding 9).
- **s 43(2):** read as a production-only subpoena (finding 7).
- **s 58A:** the day each subparagraph names is counted as written, "on a day after" it (finding 5).
- **Counting time:** "n days after" a day is that day plus n; a month or year on is the same day number, or the month's last day where there is none; "not less than 28 days before" a hearing allows notice on the 28th day before; "kept for at least 3 years after the day of the death" runs to the end of the day 3 years on. The Legislation Act 2001, which governs counting time in ACT laws, is not deposited and was not read.

## What the Act turns out to say

1. **Section 13(1) has no words of place.** "A coroner must hold an inquest into the manner and cause of death of a person who …" names no territory. It is read as deaths in the ACT, because s 13(3) then gives only jurisdiction ("has jurisdiction"), not a duty, for a death outside the ACT of an ACT resident. On that reading an ACT resident killed interstate need not have an ACT inquest. Asserted.
2. **The voluntary assisted dying carve-out is narrow.** Section 13(2) takes out only paragraph (i) (death in care or custody), and the s 13(5) definition takes the administration of the substance out of "operation or procedure". A voluntary assisted death of a person in care with no cause of death certificate (paragraph (e)) still needs an inquest. Asserted.
3. **Families in care and custody deaths get less on two points.** Section 70, the stronger "must authorise" rule for deaths in care or custody, has no counterpart to s 23(1)(c) (inspecting the scene of an event that may have caused the death), and s 23 excludes those deaths. So that request is in neither section. And the s 24 route to the Chief Coroner is limited to refusals under s 23(1); a family refused under s 70 gets written reasons (and, for an Aboriginal or Torres Strait Islander deceased, the legal service gets them too) but no s 24 reconsideration. Asserted.
4. **Section 3C's carer exception may not bite.** Paragraph (g) excludes escaping from "a carer under the Intoxicated People (Care and Protection) Act 1994", but a carer is a custodial officer (s 3D(h)) and paragraph (f) covers a death "while in, being taken into, or after being taken into, the custody of a custodial officer". Read literally, "after being taken into" custody reaches a person escaping from it, which would make the exclusion empty. Encoded on the narrower reading. Asserted.
5. **Section 58A counts its days awkwardly.** Under paragraph (b) the inquest may go on "on a day after" the day each subparagraph names. Subparagraph (iii) names "the day after the day the director of public prosecutions gives notice", so the earliest day is the second day after the notice. Subparagraphs (ii) and (iv) name "30 days after" the discharge or the final decision, so the earliest day is the 31st. Paragraph (a) asks whether a prosecution is started "on or before the day after the day that is 3 months after" the notice, so the inquest may go on from the second day after the 3-month mark. Encoded literally; the other reading (the named day itself) would make each answer one day earlier. Asserted.
6. **The 30-day Supreme Court route is not the only one, and the statement of it is not always given.** Section 90 allows 30 days after receipt of a Chief Coroner's notice that there will be no hearing, but s 91 (interests of justice) and s 92 (public interest or interests of justice where the coroner does not intend to hold a hearing) set no time limit. And s 64(8) puts the statement about the 30 days only in the explanation under s 64(7)(b)(ii), which is given only "if the coroner was available to reconsider". An applicant whose coroner was unavailable is not told of the s 90 period. Also, s 64(6) speaks of reconsidering "the original finding" where s 64(2) speaks of a decision to dispense with or conclude a hearing. Asserted (the first point).
7. **Section 43(2) points to the wrong paragraph.** It deems compliance with "a subpoena under subsection (1) (a)", but paragraph (a) is a ground for issuing a subpoena, not a kind of subpoena; the kinds are paragraphs (c) to (e). Read as a production-only subpoena (paragraph (e)), since delivering a document cannot satisfy a subpoena to give evidence. Asserted.
8. **Section 32(b) refers to a request that s 71 does not provide for.** Section 32(b) requires a report to "the person who made the request" "if a request has been made under section 71", but s 71 (post-mortems by experienced pathologists in care and custody deaths) provides for no request. Left out of the encoding; it changes no answer.
9. **Section 55's protection is wider than its remedy.** Section 55(1) covers an adverse comment "in a finding or report", but s 55(3), the duty to include the person's written statement, speaks only of "the report". A person criticised in the findings of an inquest has no right on the text to have their statement included. Asserted.
10. **Fire findings go to the owner, not the occupier.** Section 18 lets "the owner or occupier" ask for an inquiry, and s 18(3) gives each of them reasons if it is refused, but s 54(2) gives a copy of the findings only to "the owner". A tenant whose belongings burned is not named. Asserted.
11. **A witness's right to the findings depends on the kind of death.** Section 75(2)(b) gives a witness who appeared a copy of the findings in a care or custody death; s 54(1) gives a witness nothing in any other inquest. Asserted.
12. **The Aboriginal legal service is notified only in care and custody deaths.** Section 69(1) bars a hearing into a death in care or custody until the local Aboriginal legal service has been notified; s 37 has no such requirement for other deaths of Aboriginal or Torres Strait Islander people. Asserted.
13. **Different triggers for "care or custody".** Section 34A(2) turns on the coroner having "reasonable grounds for believing" that the death is a death in care or custody; ss 69 to 75 turn on whether it is one. The encoding asks the two as separate inputs.
14. **Certificates protect only in the ACT.** A s 51B certificate stops use of the evidence "in any proceeding in an ACT court or before any entity authorised by a territory law"; nothing in the Act reaches a court elsewhere. Whether the Evidence Act 2011 or Commonwealth law adds protection was not examined. Asserted as `not covered`.

## Raised in the ledger

Nothing. The ACT keeps no requirement ledger, and no scenario life cites this Act.

## What would need doing before this is worth relying on

- **The Legislation Act 2001** for counting time (months, "not less than 28 days before", days after), penalty units and client legal privilege; the dates here rest on stated readings.
- **The Coroners Regulation** (if any) prescribing the s 68A(2) information, and the **Court Procedures Rules 2006** schedule 4 for witness expenses.
- **Case law** on "sufficient interest", on the s 13 paragraphs (for example what makes a death "unnatural"), and on s 58A.
- The Acts the definitions borrow from, if the death-in-care and death-in-custody questions are to be asked in more detail.
- An independent test pass and a human review.
