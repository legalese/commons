# NOTES: Companies Act 1967 (Singapore), Part 3 Division 2, ss 23 to 42A (part `sgi`)

Status, verified 2026-11-18 by running `check.sh` (its output is in the last section): every `sgi-*.l4` file runs with no error and no warning on the stable build 1.6.110, and every module reads the same on the second stable build 1.6.109.
The text is a rendering of the Act (the Singapore Statutes Online informal consolidation in force from 6 May 2026 to 20 October 2026, which carries the amendments up to Act 24 of 2025), and it is not the official text.
Ranges: lines 4175 to 6134 of `inputs/CoA1967.txt` (Part 3 Division 2, ss 23 to 42A).

## What this folder holds

- Layer 1, the law: `sgi-capacity`, `sgi-ultra-vires`, `sgi-director-transactions`, `sgi-alteration`, `sgi-objects`, `sgi-names`, `sgi-name-changes`, `sgi-conversion`, `sgi-constitution` and `sgi-contracts-seal`, each with a `sgi-tests-*` file beside it.
- Layer 2, the seat: `sgi-seat.l4` (232 questions, each with `@export` and `@desc` on every input) and `sgi-cases-seat.l4` (502 cases, each a case from the layer-1 tests asked through the seat question).
- The keel's modules (`sg-*.l4`), `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are the supplied read-only copies.
- `PROGRESS.md` is the working log.
- The `@desc` texts of the seat inputs are generated from the names of the facts (the question is the fact turned into a question), and the seat questions and cases are generated from the layer-1 functions by script, so the seat cannot differ from layer 1 on a rule.

**The seat.** An individual who is, or is about to become, a director, the company secretary or a member of a company incorporated under the Act, or of a foreign company registered under it, or who deals with one.
That is the brief's seat, and it is assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.
There is no seat for the Registrar, the Minister or the Court; their powers appear as what they mean to the individual (for example, "must the Registrar refuse my company this name" and "may the Court set this contract aside").

**Where `PLAN.md` and the brief differ, the brief governs.**
The differences met, each checked against the files:

1. PLAN section 6 lists, for this part, the keel names `s 4(1) "constitution"`, `"private company"`, `"public company"`, `"limited company"` and `"company limited by guarantee"`.
   The layer-1 files name `"limited company"` 5 times, `"company limited by guarantee"` 3 times, and also `"unlimited company"` 2 times and `"company limited by shares"` 3 times, which the row does not list.
   `"private company"` is named once in `sgi-conversion.l4`, in the header comment of the seam, and not called: this part gives the keel two of that function's inputs (section "Seams").
   `"constitution"` and `"public company"` are not used; the keel's `"constitution"` input about s 19 is for the part that encodes s 19.
2. PLAN section 6 says this part takes "the kind of resolution from the core".
   Four functions do (`s 26(1)` in `sgi-alteration`; `s 33(1)`, `s 34(1)` and `s 34(2)(b)` in `sgi-objects`), each taking the core's `Kind of resolution`.
   Five functions in `sgi-name-changes` instead take a yes/no input, `the resolution is a special resolution`.
   The text of all nine names a special resolution, so the two forms ask the same question two ways: this is an inconsistency in this part, not a reading of the text, and it departs from the plan.
   The lead may want one form throughout; changing the five touches only those functions, their tests and their seat questions.
3. PLAN section 6 says this part takes "what a general meeting is (sgl) as an input named for the fact".
   No function here needs the meaning of a general meeting: `s 24(2)` takes whether the constitution requires approval "in general meeting" as one plain input, and `s 25D(2)(b)(ii)` takes a percentage of the voting power "at any general meeting" as a number.

## Coverage (sgi)

Every non-blank line of lines 4175 to 6134 falls in exactly one row below; the check script (`work/units.py audit`) reports: `non-blank lines 1386 rows 380 problems []`.
The table has 380 rows and the script found 380 text units, so the counts before and after are the same.
Dispositions: encoded 129, fork 204, inert 1 28, inert 2 1, repealed or blank 18.
A row is `encoded` when a layer-1 rule with a test and an `@ref` implements it, and `fork` when the rule that implements it rests on a reading that the fork register lists (the entries are in the last column).
Where the only entry is a Guide ruling applied (F-I2, the grant ruling for "may" is the common one), the row is still a fork, because the answer depends on that ruling and the other reading is stated in the entry.
A paragraph or sub-paragraph row lists the rule of its subsection when one function implements them together; a lead-in row lists the rules of its paragraphs.
`inert 1` is a division or section title (not operative); `inert 2` is machinery; the text has no `inert 3` row because every row showing deleted text is `repealed or blank`, with what the text shows.

| row | lines | disposition | L4 name | fork entries |
| --- | --- | --- | --- | --- |
| Division 2 heading | 4175-4176 | inert 1 | heading or section title: not operative | |
| section 23 | 4177-4178 | inert 1 | heading or section title: not operative | |
| subsection 23(1) | 4179-4181 | fork | `s 23(1)(a) the company has full capacity to carry on or undertake the business or activity, do the act or enter into the transaction`; `s 23(1)(b) the company has full rights, powers and privileges for the purposes of paragraph (a)` | F-I1 |
| paragraph 23(1)(a) | 4182-4187 | fork | `s 23(1)(a) the company has full capacity to carry on or undertake the business or activity, do the act or enter into the transaction`; `s 23(1)(b) the company has full rights, powers and privileges for the purposes of paragraph (a)` | F-I1 |
| paragraph 23(1)(b) | 4188-4192 | fork | `s 23(1)(b) the company has full rights, powers and privileges for the purposes of paragraph (a)` | F-I1 |
| subsection 23(1A) | 4193-4197 | encoded | `s 23(1A) the company may have its objects included in its constitution` |  |
| subsection 23(1B) | 4198-4202 | encoded | `s 23(1B) the constitution may contain the provision` |  |
| subsection 23(2) | 4203-4204 | repealed or blank | the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | |
| subsection 23(3) | 4205-4206 | repealed or blank | the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | |
| subsection 23(4) | 4207-4208 | repealed or blank | the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | |
| subsection 23(5) | 4209-4210 | repealed or blank | the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | |
| section 24 | 4211-4213 | inert 1 | heading or section title: not operative | |
| subsection 24(1) | 4214-4220 | encoded | `s 24(1) the powers of the company are deemed to include power to make the provision` |  |
| subsection 24(2) | 4221-4229 | encoded | `s 24(2) subsection (1) affects the constitution's provision on how the power is exercised` |  |
| section 25 | 4230-4231 | inert 1 | heading or section title: not operative | |
| subsection 25(1) | 4232-4244 | encoded | `s 25(1) the act is invalid by reason only of the company's lack of capacity or power` |  |
| subsection 25(2) | 4245-4247 | encoded | `s 25(2) the lack of capacity or power may be asserted or relied upon in the proceedings` |  |
| paragraph 25(2)(a) | 4248-4256 | encoded | `s 25(2) the lack of capacity or power may be asserted or relied upon in the proceedings` |  |
| paragraph 25(2)(b) | 4257-4260 | encoded | `s 25(2) the lack of capacity or power may be asserted or relied upon in the proceedings` |  |
| paragraph 25(2)(c) | 4261-4262 | encoded | `s 25(2) the lack of capacity or power may be asserted or relied upon in the proceedings` |  |
| subsection 25(3) | 4263-4275 | fork | `s 25(3) the Court may set aside and restrain the performance of the contract`; `s 25(3) the Court may allow the claimant compensation for the loss or damage`; `s 25(3) the Court may award the amount as a loss or damage sustained` | F-I2 |
| section 25A | 4276-4293 | encoded | `s 25A the person is affected by, or is deemed to have notice or knowledge of, the contents of the constitution or document` |  |
| section 25B | 4294-4295 | inert 1 | heading or section title: not operative | |
| subsection 25B(1) | 4296-4302 | fork | `s 25B(1) the power of the directors to bind the company is deemed to be free of the limitation in favour of the person` | F-I3 |
| subsection 25B(2) | 4303-4305 | encoded | `s 25B(2)(b) the person dealing with the company is presumed to have acted in good faith`; `s 25B(2)(a) the person dealing with the company is bound to enquire as to any limitation on the powers of the directors` |  |
| paragraph 25B(2)(a) | 4306-4309 | encoded | `s 25B(2)(b) the person dealing with the company is presumed to have acted in good faith`; `s 25B(2)(a) the person dealing with the company is bound to enquire as to any limitation on the powers of the directors` |  |
| paragraph 25B(2)(b) | 4310-4314 | encoded | `s 25B(2)(b) the person dealing with the company is presumed to have acted in good faith` |  |
| subsection 25B(3) | 4315-4318 | encoded | `s 25B(3) the limitation is within the limitations on the directors' powers under the company's constitution` |  |
| paragraph 25B(3)(a) | 4319-4321 | encoded | `s 25B(3) the limitation is within the limitations on the directors' powers under the company's constitution` |  |
| paragraph 25B(3)(b) | 4322-4326 | encoded | `s 25B(3) the limitation is within the limitations on the directors' powers under the company's constitution` |  |
| subsection 25B(4) | 4327-4337 | encoded | `s 25B(4) section 25B affects the member's right to bring the proceedings`; `s 25B(4) the proceedings lie in respect of the act` |  |
| subsection 25B(5) | 4338-4343 | encoded | `s 25B(5) section 25B affects the liability` |  |
| subsection 25B(6) | 4344-4347 | encoded | `s 25B(6) section 25B has effect subject to section 25C for the transaction` |  |
| section 25C | 4348-4350 | inert 1 | heading or section title: not operative | |
| subsection 25C(1) | 4351-4355 | fork | `s 25C(1) section 25C applies to the transaction` | F-I4 |
| subsection 25C(2) | 4356-4362 | encoded | `s 25C(2) section 25C excludes the operation of the other written law or rule of law` |  |
| subsection 25C(3) | 4363-4364 | fork | `s 25C(3) the transaction is voidable at the instance of the company` | F-I5 |
| paragraph 25C(3)(a) | 4365-4366 | fork | `s 25C(3) the transaction is voidable at the instance of the company` | F-I5 |
| paragraph 25C(3)(b) | 4367-4368 | fork | `s 25C(3) the transaction is voidable at the instance of the company` | F-I5 |
| sub-paragraph 25C(3)(b)(i) | 4369-4371 | fork | `s 25C(3) the transaction is voidable at the instance of the company` | F-I5 |
| sub-paragraph 25C(3)(b)(ii) | 4372-4377 | fork | `s 25C(3) the transaction is voidable at the instance of the company` | F-I5 |
| subsection 25C(4) | 4378-4381 | encoded | `s 25C(4) the person is liable to the company under subsection (4)`; `s 25C(4) and (6) the person is liable to the company`; `s 25C(4)(a) the amount the person must account to the company for`; `s 25C(4)(b) the person must indemnify the company for the loss or damage`; `s 25C(4)(b) the amount the person must indemnify the company for`; `s 25C(4)(a) the person liable under subsection (4) must account to the company for any gain`; `s 25C(4)(b) the person liable under subsection (4) must indemnify the company for any loss or damage` |  |
| paragraph 25C(4)(a) | 4382-4385 | encoded | `s 25C(4) the person is liable to the company under subsection (4)`; `s 25C(4) and (6) the person is liable to the company`; `s 25C(4)(a) the amount the person must account to the company for`; `s 25C(4)(b) the person must indemnify the company for the loss or damage`; `s 25C(4)(b) the amount the person must indemnify the company for`; `s 25C(4)(a) the person liable under subsection (4) must account to the company for any gain`; `s 25C(4)(b) the person liable under subsection (4) must indemnify the company for any loss or damage` |  |
| paragraph 25C(4)(b) | 4386-4393 | encoded | `s 25C(4) the person is liable to the company under subsection (4)`; `s 25C(4) and (6) the person is liable to the company`; `s 25C(4)(b) the person must indemnify the company for the loss or damage`; `s 25C(4)(b) the amount the person must indemnify the company for`; `s 25C(4)(b) the person liable under subsection (4) must indemnify the company for any loss or damage` |  |
| subsection 25C(5) | 4394-4395 | fork | `s 25C(5) the transaction ceases to be voidable` | F-I4 |
| paragraph 25C(5)(a) | 4396-4398 | fork | `s 25C(5) the transaction ceases to be voidable` | F-I4 |
| paragraph 25C(5)(b) | 4399-4401 | fork | `s 25C(5) the transaction ceases to be voidable` | F-I4 |
| paragraph 25C(5)(c) | 4402-4406 | fork | `s 25C(5) the transaction ceases to be voidable` | F-I4 |
| paragraph 25C(5)(d) | 4407-4410 | fork | `s 25C(5) the transaction ceases to be voidable` | F-I4 |
| subsection 25C(6) | 4411-4417 | encoded | `s 25C(6) the person other than a director is liable under subsection (4)` |  |
| subsection 25C(7) | 4418-4425 | fork | `s 25C(7) subsections (1) to (6) affect the rights of the party`; `s 25C(7) the court may make an order affirming, severing or setting aside the transaction` | F-I6 |
| subsection 25C(8) | 4426-4429 | encoded | `s 25C(8) the thing is within the word transaction` |  |
| section 25D | 4430-4431 | inert 1 | heading or section title: not operative | |
| subsection 25D(1) | 4432-4434 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| paragraph 25D(1)(a) | 4435-4436 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| paragraph 25D(1)(b) | 4437-4439 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| paragraph 25D(1)(c) | 4440-4445 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(c)(i) | 4446-4449 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(c)(ii) | 4450-4456 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| paragraph 25D(1)(d) | 4457-4458 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(d)(i) | 4459-4460 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(d)(ii) | 4461-4463 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| paragraph 25D(1)(e) | 4464-4466 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(e)(i) | 4467-4468 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(e)(ii) | 4469-4471 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| sub-paragraph 25D(1)(e)(iii) | 4472-4476 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| paragraph 25D(1)(f) | 4477-4482 | encoded | `s 25D(1) the person is a person connected with the director` |  |
| subsection 25D(2) | 4483-4484 | fork | `s 25D(2)(a) the person is a member of the director's family`; `s 25D(2)(b) the director is connected with the body corporate`; `s 25D(2)(c) the voting power counts as voting power the exercise of which is controlled by the director`; `s 25D(2)(d)(i) the body corporate is treated as connected with the director for the purposes of subsection (2)`; `s 25D(2)(d)(ii) the trustee is treated as connected with the director for the purposes of subsection (2)`; `s 25D(2)(e) the body is within the words body corporate`; `s 25D(1)(c) the person is within paragraph (c)`; `s 25D(1)(d) the person is within paragraph (d)`; `s 25D(1)(e) the person is within paragraph (e)` (the lead-in of its paragraphs; the rules are those of the paragraph rows) | F-I7 |
| paragraph 25D(2)(a) | 4485-4488 | encoded | `s 25D(2)(a) the person is a member of the director's family` |  |
| paragraph 25D(2)(b) | 4489-4495 | encoded | `s 25D(2)(b) the director is connected with the body corporate` |  |
| sub-paragraph 25D(2)(b)(i) | 4496-4498 | encoded | `s 25D(2)(b) the director is connected with the body corporate` |  |
| sub-paragraph 25D(2)(b)(ii) | 4499-4503 | encoded | `s 25D(2)(b) the director is connected with the body corporate` |  |
| paragraph 25D(2)(c) | 4504-4508 | encoded | `s 25D(2)(c) the voting power counts as voting power the exercise of which is controlled by the director` |  |
| paragraph 25D(2)(d) | 4509-4510 | fork | `s 25D(2)(d)(i) the body corporate is treated as connected with the director for the purposes of subsection (2)` | F-I7 |
| sub-paragraph 25D(2)(d)(i) | 4511-4516 | fork | `s 25D(2)(d)(i) the body corporate is treated as connected with the director for the purposes of subsection (2)` | F-I7 |
| sub-paragraph 25D(2)(d)(ii) | 4517-4522 | encoded | `s 25D(2)(d)(ii) the trustee is treated as connected with the director for the purposes of subsection (2)` |  |
| paragraph 25D(2)(e) | 4523-4525 | encoded | `s 25D(2)(e) the body is within the words body corporate`; `s 25D(1)(c) the person is within paragraph (c)`; `s 25D(1)(d) the person is within paragraph (d)`; `s 25D(1)(e) the person is within paragraph (e)` |  |
| sub-paragraph 25D(2)(e)(i) | 4526-4527 | encoded | `s 25D(2)(e) the body is within the words body corporate`; `s 25D(1)(c) the person is within paragraph (c)`; `s 25D(1)(d) the person is within paragraph (d)`; `s 25D(1)(e) the person is within paragraph (e)` |  |
| sub-paragraph 25D(2)(e)(ii) | 4528-4533 | encoded | `s 25D(2)(e) the body is within the words body corporate`; `s 25D(1)(c) the person is within paragraph (c)`; `s 25D(1)(d) the person is within paragraph (d)`; `s 25D(1)(e) the person is within paragraph (e)` |  |
| section 26 | 4534-4535 | inert 1 | heading or section title: not operative | |
| subsection 26(1) | 4536-4540 | fork | `s 26(1) the constitution may be altered or added to by the resolution` | F-I9 |
| subsection 26(1AA) | 4541-4551 | encoded | `s 26(1AA) the date on and from which the alteration or addition forms part of the original constitution` |  |
| subsection 26(1AB) | 4552-4560 | encoded | `s 26(1AB) the special resolution needs to set out the text of the model constitution adopted` |  |
| subsection 26(1A) | 4561-4566 | encoded | `s 26(1A) the power in subsection (1) is subject to an entrenching provision` |  |
| subsection 26(1B) | 4567-4574 | encoded | `s 26(1B) the provision may be altered` |  |
| subsection 26(2) | 4575-4586 | encoded | `s 26(2) the company has complied with the duty to lodge a copy of the resolution, order or other document`; `s 26(2) the company must lodge a copy within 14 days` |  |
| subsection 26(2A) | 4587-4593 | fork | `s 26(2A) the person is guilty of the offence`; `s 26(2A) the most the person may be sentenced to on conviction` | F-I10 |
| subsection 26(3) | 4594-4604 | encoded | `s 26(3) the Registrar must register the document`; `s 26(3) the Registrar must issue to the company a notice of the registration of the order` |  |
| subsection 26(4) | 4605-4606 | repealed or blank | the text shows [Deleted by Act 12 of 2002] | |
| subsection 26(5) | 4607-4609 | encoded | `s 26(5) the notice of the registration must be published in the manner directed` |  |
| subsection 26(6) | 4610-4615 | encoded | `s 26(6) the Registrar must issue a notice of incorporation in accordance with the alteration` |  |
| subsection 26(7) | 4616-4622 | fork | `s 26(7) the Registrar must issue to the company a certificate confirming the incorporation in accordance with the alteration` | F-I11 |
| section 26A | 4623-4624 | inert 1 | heading or section title: not operative | |
| subsection 26A(1) | 4625-4626 | encoded | `s 26A(1)(a) the entrenching provision may be included in the constitution with which the company is formed` |  |
| paragraph 26A(1)(a) | 4627-4629 | encoded | `s 26A(1)(a) the entrenching provision may be included in the constitution with which the company is formed` |  |
| paragraph 26A(1)(b) | 4630-4634 | encoded | `s 26A(1)(b) the entrenching provision may be inserted in the constitution` |  |
| subsection 26A(2) | 4635-4639 | encoded | `s 26A(2) the entrenching provision may be removed or altered` |  |
| subsection 26A(3) | 4640-4645 | encoded | `s 26A(3) the provisions of this Act on the alteration of the constitution are subject to the entrenching provision` |  |
| subsection 26A(4) | 4646-4649 | encoded | `s 26A(4) the provision is an entrenching provision` |  |
| paragraph 26A(4)(a) | 4650-4654 | encoded | `s 26A(4) the provision is an entrenching provision` |  |
| paragraph 26A(4)(b) | 4655-4656 | encoded | `s 26A(4) the provision is an entrenching provision` |  |
| sub-paragraph 26A(4)(b)(i) | 4657-4660 | encoded | `s 26A(4) the provision is an entrenching provision` |  |
| sub-paragraph 26A(4)(b)(ii) | 4661-4664 | encoded | `s 26A(4) the provision is an entrenching provision` |  |
| section 27 | 4665-4666 | inert 1 | heading or section title: not operative | |
| subsection 27(1) | 4667-4670 | fork | `s 27(1) the Registrar must refuse to register the company under the name` | F-I18 |
| paragraph 27(1)(a) | 4671-4672 | fork | `s 27(1) the Registrar must refuse to register the company under the name` | F-I18 |
| paragraph 27(1)(b) | 4673-4676 | fork | `s 27(1) the Registrar must refuse to register the company under the name` | F-I18 |
| paragraph 27(1)(c) | 4677-4686 | fork | `s 27(1) the Registrar must refuse to register the company under the name` | F-I18 |
| paragraph 27(1)(d) | 4687-4691 | fork | `s 27(1) the Registrar must refuse to register the company under the name` | F-I18 |
| subsection 27(1A) | 4692-4695 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| paragraph 27(1A)(a) | 4696-4698 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(a)(i) | 4699-4708 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(a)(ii) | 4709-4713 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| paragraph 27(1A)(b) | 4714-4720 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| paragraph 27(1A)(c) | 4721-4725 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| paragraph 27(1A)(d) | 4726-4728 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(d)(i) | 4729-4735 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(d)(ii) | 4736-4741 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| paragraph 27(1A)(e) | 4742-4744 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(e)(i) | 4745-4754 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(e)(ii) | 4755-4760 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| paragraph 27(1A)(f) | 4761-4762 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(f)(i) | 4763-4767 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| sub-paragraph 27(1A)(f)(ii) | 4768-4777 | fork | `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` | F-I4, F-I18 |
| subsection 27(1B) | 4778-4780 | fork | `s 27(1B) the Registrar may register the company under the name` | F-I2, F-I16 |
| paragraph 27(1B)(a) | 4781-4783 | fork | `s 27(1B) the Registrar may register the company under the name` | F-I2, F-I16 |
| sub-paragraph 27(1B)(a)(i) | 4784-4789 | fork | `s 27(1B) the Registrar may register the company under the name` | F-I2, F-I16 |
| sub-paragraph 27(1B)(a)(ii) | 4790-4794 | fork | `s 27(1B) the Registrar may register the company under the name` | F-I2, F-I16 |
| paragraph 27(1B)(b) | 4795-4807 | fork | `s 27(1B) the Registrar may register the company under the name` | F-I2, F-I16 |
| subsection 27(2) | 4808-4812 | fork | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` | F-I18, F-I19 |
| paragraph 27(2)(a) | 4813-4815 | fork | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` | F-I18, F-I19 |
| paragraph 27(2)(aa) | 4816-4819 | fork | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` | F-I18, F-I19 |
| paragraph 27(2)(ab) | 4820-4823 | fork | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` | F-I18, F-I19 |
| paragraph 27(2)(b) | 4824-4828 | fork | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` | F-I18, F-I19 |
| paragraph 27(2)(c) | 4829-4838 | fork | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` | F-I18, F-I19 |
| subsection 27(2A) | 4839-4845 | fork | `s 27(2A) the person may apply to the Registrar for a direction to the company`; `s 27(2A) the Registrar is barred from considering the application` | F-I2 |
| subsection 27(2B) | 4846-4854 | fork | `s 27(2B) the person is guilty of the offence`; `s 27(2B) the most the person may be sentenced to on conviction` | F-I10 |
| subsection 27(2C) | 4855-4856 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| subsection 27(2D) | 4857-4858 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| subsection 27(3) | 4859-4860 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| subsection 27(4) | 4861-4862 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| subsection 27(5) | 4863-4866 | encoded | `s 27(5) the person may appeal to the Minister against the decision` |  |
| paragraph 27(5)(a) | 4867-4870 | encoded | `s 27(5) the person may appeal to the Minister against the decision` |  |
| paragraph 27(5)(b) | 4871-4877 | encoded | `s 27(5) the person may appeal to the Minister against the decision` |  |
| subsection 27(5AA) | 4878-4882 | encoded | `s 27(5AA) the decision of the Minister on the appeal is final` |  |
| subsection 27(5A) | 4883-4887 | encoded | `s 27(5A) the Registrar or the Minister must accept as correct the decision of the Court to grant the injunction` |  |
| subsection 27(6) | 4888-4890 | encoded | `s 27(6) the Minister must cause the direction to be published in the Gazette` |  |
| subsection 27(7) | 4891-4893 | encoded | `s 27(7) the name of the limited company has the word Limited or Berhad as the subsection requires` |  |
| subsection 27(8) | 4894-4901 | encoded | `s 27(8) the name of the private company has the word Private or Sendirian as the subsection requires` |  |
| subsection 27(9) | 4902-4904 | encoded | `s 27(9) the use is lawful and does not make the description of the company inadequate or incorrect` |  |
| paragraph 27(9)(a) | 4905-4908 | encoded | `s 27(9) the use is lawful and does not make the description of the company inadequate or incorrect` |  |
| paragraph 27(9)(b) | 4909-4912 | encoded | `s 27(9) the use is lawful and does not make the description of the company inadequate or incorrect` |  |
| paragraph 27(9)(c) | 4913-4915 | encoded | `s 27(9) the use is lawful and does not make the description of the company inadequate or incorrect` |  |
| subsection 27(10) | 4916-4918 | fork | `s 27(10) the person may apply to the Registrar for the reservation of the name` | F-I2 |
| paragraph 27(10)(a) | 4919-4920 | fork | `s 27(10) the person may apply to the Registrar for the reservation of the name` | F-I2 |
| paragraph 27(10)(b) | 4921-4924 | fork | `s 27(10) the person may apply to the Registrar for the reservation of the name` | F-I2 |
| subsection 27(11) | 4925-4930 | fork | `s 27(11) the registration of the company, or the approval of the change of name, is barred` | F-I18 |
| subsection 27(12) | 4931-4933 | encoded | `s 27(12) the Registrar may approve the application` |  |
| paragraph 27(12)(a) | 4934-4935 | encoded | `s 27(12) the Registrar may approve the application` |  |
| paragraph 27(12)(b) | 4936-4941 | encoded | `s 27(12) the Registrar may approve the application` |  |
| subsection 27(12A) | 4942-4945 | fork | `s 27(12A) the Registrar must refuse to approve the application` | F-I4 |
| paragraph 27(12A)(a) | 4946-4952 | fork | `s 27(12A) the Registrar must refuse to approve the application` | F-I4 |
| paragraph 27(12A)(b) | 4953-4957 | fork | `s 27(12A) the Registrar must refuse to approve the application` | F-I4 |
| subsection 27(12B) | 4958-4962 | fork | `s 27(12B) the last day of the reservation`; `s 27(12B) the name is reserved on the day` | F-I20 |
| paragraph 27(12B)(a) | 4963-4968 | fork | `s 27(12B) the last day of the reservation`; `s 27(12B) the name is reserved on the day` | F-I20 |
| paragraph 27(12B)(b) | 4969-4974 | fork | `s 27(12B) the last day of the reservation`; `s 27(12B) the name is reserved on the day` | F-I20 |
| subsection 27(12C) | 4975-4976 | encoded | `s 27(12C) the person may appeal to the Minister against the decision` |  |
| paragraph 27(12C)(a) | 4977-4979 | encoded | `s 27(12C) the person may appeal to the Minister against the decision` |  |
| paragraph 27(12C)(b) | 4980-4987 | encoded | `s 27(12C) the person may appeal to the Minister against the decision` |  |
| subsection 27(13) | 4988-4994 | fork | `s 27(13) the Registrar may extend the period for a further period of 60 days` | F-I2 |
| subsection 27(14) | 4995-4996 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| subsection 27(15) | 4997-5006 | encoded | `s 27(15) the reservation in itself entitles the company to be registered by the name` |  |
| subsection 27(16) | 5007-5012 | encoded | `s 27(16) "registered business name" the name is a registered business name` |  |
| section 28 | 5013-5014 | inert 1 | heading or section title: not operative | |
| subsection 28(1) | 5015-5020 | fork | `s 28(1) the company may resolve that its name should be changed to the new name` | F-I2 |
| subsection 28(2) | 5021-5026 | fork | `s 28(2) the Registrar must register the company under the new name and issue the notice of incorporation`; `s 28(2) the change of name has become effective` | F-I21 |
| subsection 28(3) | 5027-5030 | fork | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` | F-I2, F-I18, F-I21 |
| paragraph 28(3)(a) | 5031-5033 | fork | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` | F-I2, F-I18, F-I21 |
| paragraph 28(3)(b) | 5034-5037 | fork | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` | F-I2, F-I18, F-I21 |
| paragraph 28(3)(c) | 5038-5041 | fork | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` | F-I2, F-I18, F-I21 |
| paragraph 28(3)(d) | 5042-5046 | fork | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` | F-I2, F-I18, F-I21 |
| paragraph 28(3)(e) | 5047-5061 | fork | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` | F-I2, F-I18, F-I21 |
| subsection 28(3AA) | 5062-5067 | encoded | `s 28(3AA) the Registrar is barred from directing a change of name under subsection (3) on the ground` |  |
| subsection 28(3A) | 5068-5076 | fork | `s 28(3A) the person may apply to the Registrar for a direction to the company`; `s 28(3A) the Registrar is barred from considering the application` | F-I2, F-I18 |
| subsection 28(3B) | 5077-5081 | fork | `s 28(3B) the person is guilty of the offence`; `s 28(3B) the most the person may be sentenced to on conviction` | F-I10 |
| subsection 28(3C) | 5082-5083 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| subsection 28(3D) | 5084-5087 | encoded | `s 28(3D) the person may appeal to the Minister against the decision` |  |
| paragraph 28(3D)(a) | 5088-5091 | encoded | `s 28(3D) the person may appeal to the Minister against the decision` |  |
| paragraph 28(3D)(b) | 5092-5098 | encoded | `s 28(3D) the person may appeal to the Minister against the decision` |  |
| subsection 28(3DA) | 5099-5103 | encoded | `s 28(3DA) the decision of the Minister on the appeal is final` |  |
| subsection 28(3E) | 5104-5115 | encoded | `s 28(3E) the Registrar or the Minister must accept as correct the decision of the Court to grant the injunction` |  |
| subsection 28(4) | 5116-5121 | fork | `s 28(4) the Registrar is barred from directing the company to change its name under subsection (3)` | F-I18, F-I21 |
| subsection 28(5) | 5122-5128 | fork | `s 28(5) the Registrar must issue to the company a certificate confirming the incorporation under the new name` | F-I11 |
| subsection 28(6) | 5129-5135 | fork | `s 28(6) the change of name affects the matter`; `s 28(6) the legal proceedings may be continued or commenced by or against the company by its new name` | F-I2 |
| section 29 | 5136-5139 | inert 1 | heading or section title: not operative | |
| subsection 29(1) | 5140-5161 | fork | `s 29(1) the Registrar may approve that the proposed limited company be registered without the word Limited or Berhad`; `s 29(1) the company may be registered without the word Limited or Berhad accordingly` | F-I2, F-I19 |
| subsection 29(2) | 5162-5163 | fork | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` | F-I19 |
| paragraph 29(2)(a) | 5164-5167 | fork | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` | F-I19 |
| paragraph 29(2)(b) | 5168-5170 | fork | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` | F-I19 |
| paragraph 29(2)(c) | 5171-5173 | fork | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` | F-I19 |
| paragraph 29(2)(d) | 5174-5183 | fork | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` | F-I19 |
| subsection 29(3) | 5184-5191 | fork | `s 29(3) the conditions are binding on the company`; `s 29(3) the company must insert the conditions in its constitution if the Registrar so directs`; `s 29(3) the conditions must be inserted in the constitution of the company`; `s 29(3) the constitution may be altered by special resolution to give effect to the direction` | F-I2, F-I21 |
| subsection 29(4) | 5192-5200 | fork | `s 29(4) the company may alter any provision of the constitution` | F-I19 |
| subsection 29(5) | 5201-5208 | fork | `s 29(5) the company is exempted from complying with the provisions of this Act relating to the use of the word Limited or Berhad` | F-I22 |
| subsection 29(6) | 5209-5219 | fork | `s 29(6) the Registrar may revoke the approval`; `s 29(6) before the revocation the Registrar must give the company written notice and afford it an opportunity to be heard`; `s 29(6) upon the revocation the Registrar must enter the word Limited or Berhad at the end of the name in the register`; `s 29(6) upon the revocation the company ceases to enjoy the exemption` | F-I11, F-I23 |
| subsection 29(6A) | 5220-5225 | fork | `s 29(6A) the Registrar may revoke the approval` | F-I2 |
| subsection 29(7) | 5226-5232 | fork | `s 29(7) the constitution may be altered by special resolution to remove the provision requiring the Minister's consent` | F-I2 |
| subsection 29(8) | 5233-5238 | fork | `s 29(8) the notice of the approval must be given to the person` | F-I21 |
| subsection 29(8A) | 5239-5242 | encoded | `s 29(8A) the person may appeal to the Minister against the decision` |  |
| paragraph 29(8A)(a) | 5243-5247 | encoded | `s 29(8A) the person may appeal to the Minister against the decision` |  |
| paragraph 29(8A)(b) | 5248-5253 | encoded | `s 29(8A) the person may appeal to the Minister against the decision` |  |
| subsection 29(9) | 5254-5261 | fork | `s 29(9) the Registrar must issue to the company a certificate confirming the approval` | F-I11 |
| subsection 29(10) | 5262-5266 | encoded | `s 29(10) section 29 applies to the company` |  |
| subsection 29(11) | 5267-5270 | fork | `s 29(11) the approval or condition is treated as the Registrar's approval and condition` | F-I24 |
| paragraph 29(11)(a) | 5271-5273 | fork | `s 29(11) the approval or condition is treated as the Registrar's approval and condition` | F-I24 |
| paragraph 29(11)(b) | 5274-5281 | fork | `s 29(11) the approval or condition is treated as the Registrar's approval and condition` | F-I24 |
| subsection 29(12) | 5282-5289 | fork | `s 29(12) the reference to the Minister's approval is read as a reference to the Registrar` | F-I24 |
| subsection 29(13) | 5290-5295 | fork | `s 29(13) the reference to a direction of the Minister is read as a direction of the Registrar` | F-I24 |
| section 29A | 5296-5298 | inert 1 | heading or section title: not operative | |
| subsection 29A(1) | 5299-5305 | fork | `s 29A(1) the charitable company may change its name to omit the word Limited or Berhad` | F-I2, F-I25 |
| subsection 29A(2) | 5306-5308 | fork | `s 29A(2)(a) the charitable company must alter its constitution to reflect the change of name`; `s 29A(2)(b) the charitable company must file the prescribed form with the Registrar and a copy of the special resolution`; `s 29A(2) the charitable company has met the requirements for the change of name` | F-I21 |
| paragraph 29A(2)(a) | 5309-5313 | fork | `s 29A(2)(a) the charitable company must alter its constitution to reflect the change of name`; `s 29A(2)(b) the charitable company must file the prescribed form with the Registrar and a copy of the special resolution`; `s 29A(2) the charitable company has met the requirements for the change of name` | F-I21 |
| paragraph 29A(2)(b) | 5314-5319 | fork | `s 29A(2)(a) the charitable company must alter its constitution to reflect the change of name`; `s 29A(2)(b) the charitable company must file the prescribed form with the Registrar and a copy of the special resolution`; `s 29A(2) the charitable company has met the requirements for the change of name` | F-I21 |
| subsection 29A(3) | 5320-5322 | fork | `s 29A(3) the Registrar must register the name of the charitable company with the omission and issue the notice of incorporation` | F-I11 |
| paragraph 29A(3)(a) | 5323-5326 | fork | `s 29A(3) the Registrar must register the name of the charitable company with the omission and issue the notice of incorporation` | F-I11 |
| paragraph 29A(3)(b) | 5327-5331 | fork | `s 29A(3) the Registrar must register the name of the charitable company with the omission and issue the notice of incorporation` | F-I11 |
| subsection 29A(4) | 5332-5333 | fork | `s 29A(4) the change of name has become effective and the charitable company is exempted` | F-I11 |
| paragraph 29A(4)(a) | 5334-5335 | fork | `s 29A(4) the change of name has become effective and the charitable company is exempted` | F-I11 |
| paragraph 29A(4)(b) | 5336-5341 | fork | `s 29A(4) the change of name has become effective and the charitable company is exempted` | F-I11 |
| subsection 29A(5) | 5342-5350 | fork | `s 29A(5) the Registrar must enter the word Limited or Berhad at the end of the name of the company`; `s 29A(5) the exemption under subsection (4)(b) has ceased` | F-I11, F-I21 |
| section 30 | 5351-5352 | inert 1 | heading or section title: not operative | |
| subsection 30(1) | 5353-5354 | fork | `s 30(1)(a) the unlimited company may convert to a limited company`; `s 30(1)(b) the limited company may convert to an unlimited company` (the lead-in of its paragraphs; the rules are those of the paragraph rows) | F-I2 |
| paragraph 30(1)(a) | 5355-5358 | fork | `s 30(1)(a) the unlimited company may convert to a limited company` | F-I2 |
| paragraph 30(1)(b) | 5359-5366 | fork | `s 30(1)(b) the limited company may convert to an unlimited company` | F-I2 |
| subsection 30(2) | 5367-5373 | fork | `s 30(2) the Registrar must issue to the company a notice of incorporation appropriate to the change of status`; `s 30(2) the company is deemed to be a company having the status specified in the notice` | F-I11, F-I21 |
| paragraph 30(2)(a) | 5374-5375 | fork | `s 30(2) the Registrar must issue to the company a notice of incorporation appropriate to the change of status`; `s 30(2) the company is deemed to be a company having the status specified in the notice` | F-I11, F-I21 |
| paragraph 30(2)(b) | 5376-5382 | fork | `s 30(2) the Registrar must issue to the company a notice of incorporation appropriate to the change of status`; `s 30(2) the company is deemed to be a company having the status specified in the notice` | F-I11, F-I21 |
| subsection 30(3) | 5383-5386 | fork | `s 30(3) the notice of the change of status must be published` | F-I21, F-I26 |
| subsection 30(3A) | 5387-5392 | fork | `s 30(3A) the Registrar must issue to the company a certificate confirming the incorporation with the new status` | F-I11 |
| subsection 30(4) | 5393-5395 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| paragraph 30(4)(a) | 5396-5397 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| sub-paragraph 30(4)(a)(i) | 5398-5400 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| sub-paragraph 30(4)(a)(ii) | 5401-5406 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| sub-paragraph 30(4)(a)(iii) | 5407-5408 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| sub-paragraph 30(4)(a)(iv) | 5409-5410 | repealed or blank | the text shows [Deleted by Act 36 of 2014] | |
| sub-paragraph 30(4)(a)(v) | 5411-5417 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| paragraph 30(4)(b) | 5418-5421 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| paragraph 30(4)(c) | 5422-5424 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| sub-paragraph 30(4)(c)(i) | 5425-5428 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| sub-paragraph 30(4)(c)(ii) | 5429-5443 | encoded | `s 30(4) the documents lodged are the prescribed documents` |  |
| subsection 30(5) | 5444-5447 | encoded | `s 30(5) section 26(2) to (6) applies to the matter` |  |
| subsection 30(6) | 5448-5452 | encoded | `s 30(6) the special resolution has taken effect` |  |
| subsection 30(7) | 5453-5458 | fork | `s 30(7) the provision of section 33 applies to the special resolution` | F-I27 |
| subsection 30(8) | 5459-5464 | fork | `s 30(8) the change in status operates on the matter`; `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` | F-I2 |
| paragraph 30(8)(a) | 5465-5466 | fork | `s 30(8) the change in status operates on the matter`; `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` | F-I2 |
| paragraph 30(8)(b) | 5467-5470 | fork | `s 30(8) the change in status operates on the matter`; `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` | F-I2 |
| paragraph 30(8)(c) | 5471-5473 | fork | `s 30(8) the change in status operates on the matter`; `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` | F-I2 |
| paragraph 30(8)(d) | 5474-5481 | fork | `s 30(8) the change in status operates on the matter`; `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` | F-I2 |
| section 31 | 5482-5483 | inert 1 | heading or section title: not operative | |
| subsection 31(1) | 5484-5486 | fork | `s 31(1) the public company may convert to a private company by lodging` | F-I2 |
| paragraph 31(1)(a) | 5487-5488 | fork | `s 31(1) the public company may convert to a private company by lodging` | F-I2 |
| sub-paragraph 31(1)(a)(i) | 5489-5491 | fork | `s 31(1) the public company may convert to a private company by lodging` | F-I2 |
| sub-paragraph 31(1)(a)(ii) | 5492-5495 | fork | `s 31(1) the public company may convert to a private company by lodging` | F-I2 |
| paragraph 31(1)(b) | 5496-5498 | fork | `s 31(1) the public company may convert to a private company by lodging` | F-I2 |
| paragraph 31(1)(c) | 5499-5503 | fork | `s 31(1) the public company may convert to a private company by lodging` | F-I2 |
| subsection 31(2) | 5504-5508 | fork | `s 31(2) the private company may convert to a public company by lodging`; `s 31(2) the restrictions and limitations referred to in section 18(1) cease to form part of the constitution` | F-I2, F-I11 |
| paragraph 31(2)(a) | 5509-5515 | fork | `s 31(2) the private company may convert to a public company by lodging`; `s 31(2) the restrictions and limitations referred to in section 18(1) cease to form part of the constitution` | F-I2, F-I11 |
| paragraph 31(2)(b) | 5516-5517 | fork | `s 31(2) the private company may convert to a public company by lodging`; `s 31(2) the restrictions and limitations referred to in section 18(1) cease to form part of the constitution` | F-I2, F-I11 |
| paragraph 31(2)(c) | 5518-5526 | fork | `s 31(2) the private company may convert to a public company by lodging`; `s 31(2) the restrictions and limitations referred to in section 18(1) cease to form part of the constitution` | F-I2, F-I11 |
| subsection 31(3) | 5527-5531 | fork | `s 31(3) the company has become a private company`; `s 31(3) the company has become a public company` | F-I11 |
| subsection 31(3A) | 5532-5538 | encoded | `s 31(3A) the company has complied with the duty to lodge the list of persons holding shares`; `s 31(3A) the company must lodge the list of persons holding shares within 14 days` |  |
| subsection 31(4) | 5539-5547 | fork | `s 31(4) the conversion affects the matter`; `s 31(4) the legal proceedings may be continued or commenced by or against the company after the conversion` | F-I2 |
| subsection 31(5) | 5548-5553 | fork | `s 31(5) the Registrar must issue to the company a certificate confirming the incorporation with the new status` | F-I11 |
| section 32 | 5554-5556 | inert 1 | heading or section title: not operative | |
| subsection 32(1) | 5557-5558 | repealed or blank | the text shows [Deleted by Act 5 of 2004] | |
| subsection 32(2) | 5559-5560 | fork | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` | F-I19 |
| paragraph 32(2)(a) | 5561-5569 | fork | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` | F-I19 |
| paragraph 32(2)(b) | 5570-5571 | repealed or blank | the text shows [Deleted by Act 5 of 2004] | |
| paragraph 32(2)(c) | 5572-5575 | fork | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` | F-I19 |
| paragraph 32(2)(d) | 5576-5583 | fork | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` | F-I19 |
| subsection 32(3) | 5584-5586 | fork | `s 32(3)(a) the company is a public company on and from the date specified`; `s 32(3)(b) the company is deemed to have changed its name by the omission of the word Private or Sendirian`; `s 32(3)(c) the company has complied with the duty to lodge the statement in lieu of prospectus and the declaration`; `s 32(3)(c) the company must lodge the statement in lieu of prospectus and the declaration within 14 days` (the lead-in of its paragraphs; the rules are those of the paragraph rows) | F-I21, F-I28 |
| paragraph 32(3)(a) | 5587-5590 | fork | `s 32(3)(a) the company is a public company on and from the date specified` | F-I21, F-I28 |
| paragraph 32(3)(b) | 5591-5595 | fork | `s 32(3)(b) the company is deemed to have changed its name by the omission of the word Private or Sendirian` | F-I21, F-I28 |
| paragraph 32(3)(c) | 5596-5598 | fork | `s 32(3)(c) the company has complied with the duty to lodge the statement in lieu of prospectus and the declaration`; `s 32(3)(c) the company must lodge the statement in lieu of prospectus and the declaration within 14 days` | F-I21 |
| sub-paragraph 32(3)(c)(i) | 5599-5600 | fork | `s 32(3)(c) the company has complied with the duty to lodge the statement in lieu of prospectus and the declaration`; `s 32(3)(c) the company must lodge the statement in lieu of prospectus and the declaration within 14 days` | F-I21 |
| sub-paragraph 32(3)(c)(ii) | 5601-5603 | fork | `s 32(3)(c) the company has complied with the duty to lodge the statement in lieu of prospectus and the declaration`; `s 32(3)(c) the company must lodge the statement in lieu of prospectus and the declaration within 14 days` | F-I21 |
| subsection 32(4) | 5604-5613 | fork | `s 32(4) the Court may determine that the company has not ceased to be a private company` | F-I19 |
| subsection 32(5) | 5614-5619 | fork | `s 32(5) the company may not convert to a private company` | F-I18 |
| subsection 32(6) | 5620-5624 | fork | `s 32(6) the person is guilty of the offence`; `s 32(6) the most the person may be sentenced to on conviction` | F-I10 |
| subsection 32(7) | 5625-5626 | repealed or blank | the text shows [Deleted by Act 5 of 2004] | |
| subsection 32(8) | 5627-5636 | fork | `s 32(8) the person is guilty of the offence`; `s 32(8) the most the person may be sentenced to on conviction` | F-I10 |
| section 33 | 5637-5638 | inert 1 | heading or section title: not operative | |
| subsection 33(1) | 5639-5644 | fork | `s 33(1) the company may alter the provisions of its constitution with respect to its objects by the resolution` | F-I9 |
| subsection 33(2) | 5645-5653 | fork | `s 33(2) the company has given the notice the subsection requires`; `s 33(2) the company must give 21 days' written notice` | F-I12 |
| subsection 33(3) | 5654-5658 | encoded | `s 33(3) the notice must be given to the person` |  |
| subsection 33(4) | 5659-5665 | fork | `s 33(4) the Court may dispense with the notice for the person or class of persons` | F-I13 |
| subsection 33(5) | 5666-5668 | fork | `s 33(5)(a) the applicants hold enough of the shares, or are enough of the members`; `s 33(5) the alteration does not have effect except so far as the Court confirms it` | F-I4 |
| paragraph 33(5)(a) | 5669-5673 | fork | `s 33(5)(a) the applicants hold enough of the shares, or are enough of the members`; `s 33(5) the alteration does not have effect except so far as the Court confirms it` | F-I4 |
| paragraph 33(5)(b) | 5674-5679 | fork | `s 33(5)(b) the applicants hold enough in nominal value of the company's debentures`; `s 33(5) the alteration does not have effect except so far as the Court confirms it` | F-I4 |
| subsection 33(5A) | 5680-5684 | encoded | `s 33(5A) the number of issued shares counted for subsection (5)` |  |
| subsection 33(6) | 5685-5690 | fork | `s 33(6) the application is made in time`; `s 33(6) the application may be made on behalf of the persons entitled by the applicants` | F-I13 |
| subsection 33(7) | 5691-5692 | fork | `s 33(7)(a) the Court must have regard to the rights and interests of the members and of the creditors`; `s 33(7)(b) the Court may adjourn the proceedings`; `s 33(7)(c) the Court may give the directions and make the orders`; `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` | F-I14 |
| paragraph 33(7)(a) | 5693-5696 | fork | `s 33(7)(a) the Court must have regard to the rights and interests of the members and of the creditors`; `s 33(7)(b) the Court may adjourn the proceedings`; `s 33(7)(c) the Court may give the directions and make the orders`; `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` | F-I14 |
| paragraph 33(7)(b) | 5697-5701 | fork | `s 33(7)(b) the Court may adjourn the proceedings`; `s 33(7)(c) the Court may give the directions and make the orders`; `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` | F-I14 |
| paragraph 33(7)(c) | 5702-5705 | fork | `s 33(7)(c) the Court may give the directions and make the orders`; `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` | F-I14 |
| paragraph 33(7)(d) | 5706-5709 | fork | `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` | F-I14 |
| subsection 33(8) | 5710-5720 | encoded | `s 33(8) lodging the copy of the resolution on the day is barred`; `s 33(8) the first day on which the copy may be lodged` |  |
| subsection 33(9) | 5721-5727 | encoded | `s 33(9) the company has complied with the duty to lodge the copy of the resolution`; `s 33(9) the company must lodge a copy of the resolution within 14 days` |  |
| subsection 33(10) | 5728-5730 | fork | `s 33(10) the alteration of the objects takes effect` | F-I4 |
| subsection 33(11) | 5731-5737 | encoded | `s 33(11) the thing is within the word alteration` |  |
| section 34 | 5738-5741 | inert 1 | heading or section title: not operative | |
| subsection 34(1) | 5742-5749 | fork | `s 34(1) the company may amend its constitution to remove the provision`; `s 34 the day 31 March 2006` | F-I9, F-I15 |
| subsection 34(2) | 5750-5755 | fork | `s 34(2)(a) the provision has ceased to have effect`; `s 34(2)(b) the company may amend its constitution to remove that provision` | F-I9, F-I15 |
| paragraph 34(2)(a) | 5756-5757 | fork | `s 34(2)(a) the provision has ceased to have effect`; `s 34(2)(b) the company may amend its constitution to remove that provision` | F-I9, F-I15 |
| paragraph 34(2)(b) | 5758-5765 | fork | `s 34(2)(b) the company may amend its constitution to remove that provision` | F-I9, F-I15 |
| section 35 | 5766-5767 | inert 1 | heading or section title: not operative | |
| subsection 35(1) | 5768-5772 | fork | `s 35(1) the constitution of the company must contain the regulations for the company` | F-I18 |
| subsection 35(2) | 5773-5777 | encoded | `s 35(2) subsection (1) does not apply to the company` |  |
| subsection 35(3) | 5778-5789 | fork | `s 35(3) the regulations are deemed to be the regulations for the company contained in its constitution` | F-I22 |
| section 36 | 5790-5791 | inert 1 | heading or section title: not operative | |
| subsection 36(1) | 5792-5793 | encoded | `s 36(1) the company is a specified company` |  |
| paragraph 36(1)(a) | 5794-5795 | encoded | `s 36(1) the company is a specified company` |  |
| paragraph 36(1)(b) | 5796-5801 | encoded | `s 36(1) the company is a specified company` |  |
| subsection 36(2) | 5802-5806 | inert 2 | machinery: the Minister's power to prescribe different model constitutions | |
| section 37 | 5807-5808 | inert 1 | heading or section title: not operative | |
| subsection 37(1) | 5809-5814 | fork | `s 37(1) the specified company may adopt the whole or any part of the model constitution as its constitution` | F-I2 |
| subsection 37(2) | 5815-5823 | fork | `s 37(2) the specified company may adopt the whole model constitution by reference to its title` | F-I2 |
| subsection 37(3) | 5824-5827 | fork | `s 37(3) the specified company may choose` | F-I2 |
| paragraph 37(3)(a) | 5828-5830 | fork | `s 37(3) the specified company may choose` | F-I2 |
| paragraph 37(3)(b) | 5831-5838 | fork | `s 37(3) the specified company may choose`; `s 37(3)(b) the model constitution for the time being in force is, so far as applicable, the constitution of the specified company` | F-I2, F-I21 |
| subsection 37(4) | 5839-5842 | fork | `s 37(4) a copy of the constitution of the specified company must be submitted to the Registrar`; `s 37(4) the specified company must submit a copy of its constitution to the Registrar` | F-I21 |
| paragraph 37(4)(a) | 5843-5845 | fork | `s 37(4) a copy of the constitution of the specified company must be submitted to the Registrar`; `s 37(4) the specified company must submit a copy of its constitution to the Registrar` | F-I21 |
| paragraph 37(4)(b) | 5846-5848 | fork | `s 37(4) a copy of the constitution of the specified company must be submitted to the Registrar`; `s 37(4) the specified company must submit a copy of its constitution to the Registrar` | F-I21 |
| paragraph 37(4)(c) | 5849-5852 | fork | `s 37(4) a copy of the constitution of the specified company must be submitted to the Registrar`; `s 37(4) the specified company must submit a copy of its constitution to the Registrar` | F-I21 |
| section 38 | 5853-5854 | inert 1 | heading or section title: not operative | |
| subsection 38(1) | 5855-5861 | fork | `s 38(1) the provision is void` | F-I32 |
| subsection 38(2) | 5862-5874 | encoded | `s 38(2) the provision is treated as a provision for a share capital` |  |
| section 39 | 5875-5876 | inert 1 | heading or section title: not operative | |
| subsection 39(1) | 5877-5884 | fork | `s 39(1) the constitution binds the person to the same extent as if signed and sealed by each member` | F-I21 |
| subsection 39(2) | 5885-5889 | encoded | `s 39(2) the money is a debt due from the member to the company` |  |
| subsection 39(3) | 5890-5903 | fork | `s 39(3) the member is bound by the alteration` | F-I18 |
| section 40 | 5904-5905 | inert 1 | heading or section title: not operative | |
| subsection 40(1) | 5906-5911 | fork | `s 40(1) the sum the member must pay for a copy of the constitution`; `s 40(1) the company must send the member a copy of the constitution`; `s 40(1) the company must send a copy of the constitution to the member who requires it` | F-I29 |
| subsection 40(2) | 5912-5915 | fork | `s 40(2) the company must not issue the copy of the constitution` | F-I18, F-I21 |
| paragraph 40(2)(a) | 5916-5917 | fork | `s 40(2) the company must not issue the copy of the constitution` | F-I18, F-I21 |
| paragraph 40(2)(b) | 5918-5928 | fork | `s 40(2) the company must not issue the copy of the constitution` | F-I18, F-I21 |
| subsection 40(3) | 5929-5930 | repealed or blank | the text shows [Omitted in 2006 Revised Edition] | |
| subsection 40(4) | 5931-5934 | fork | `s 40(4) the person is guilty of the offence` | F-I10 |
| section 41 | 5935-5937 | inert 1 | heading or section title: not operative | |
| subsection 41(1) | 5938-5944 | fork | `s 41(1) the contract or transaction may be ratified by the company`; `s 41(1) the company is bound by and entitled to the benefit of the contract or transaction` | F-I2, F-I11 |
| subsection 41(2) | 5945-5949 | fork | `s 41(2) the person is personally bound by the contract or transaction and entitled to the benefit of it` | F-I18, F-I30 |
| subsection 41(3) | 5950-5953 | fork | `s 41(3) the contract may be made on behalf of the corporation in the way` | F-I2 |
| paragraph 41(3)(a) | 5954-5958 | fork | `s 41(3) the contract may be made on behalf of the corporation in the way` | F-I2 |
| paragraph 41(3)(b) | 5959-5964 | fork | `s 41(3) the contract may be made on behalf of the corporation in the way` | F-I2 |
| paragraph 41(3)(c) | 5965-5977 | fork | `s 41(3) the contract may be made on behalf of the corporation in the way`; `s 41(3) the contract is effectual in law and binds the corporation and its successors and all other parties`; `s 41(3) the contract may be varied or discharged` | F-I2 |
| subsection 41(4) | 5978-5983 | fork | `s 41(4) the document or proceeding may be signed by an authorised officer of the corporation`; `s 41(4) the document or proceeding needs to be under the common seal` | F-I2 |
| subsection 41(5) | 5984-5993 | fork | `s 41(5) the corporation may empower the person as its agent or attorney to execute deeds on its behalf`; `s 41(5) the deed binds the corporation and has the same effect as if it were under its common seal` | F-I2 |
| subsection 41(6) | 5994-6000 | fork | `s 41(6) the authority of the agent or attorney continues as between the corporation and the person dealing with the agent or attorney` | F-I22 |
| subsection 41(7) | 6001-6016 | fork | `s 41(7) the corporation may have for use in a place outside Singapore an official seal`; `s 41(7) the official seal is as the subsection requires`; `s 41(7) the person affixing the official seal has certified the date and the place`; `s 41(7) the person affixing the official seal must certify the date and the place` | F-I2, F-I31 |
| subsection 41(8) | 6017-6030 | fork | `s 41(8) the instrument under seal is as valid as if the authority had been under seal`; `s 41(9) the day 15 May 1987` | F-I2 |
| subsection 41(9) | 6031-6037 | encoded | `s 41(9) subsection (8) applies to the instrument` |  |
| section 41A | 6038-6039 | inert 1 | heading or section title: not operative | |
| subsection 41A(1) | 6040-6044 | encoded | `s 41A(1) the company may have a common seal`; `s 41A(1) the company needs to have a common seal` |  |
| subsection 41A(2) | 6045-6049 | encoded | `s 41A(2) sections 41B and 41C apply to the company` |  |
| section 41B | 6050-6051 | inert 1 | heading or section title: not operative | |
| subsection 41B(1) | 6052-6055 | fork | `s 41B(1) the company may execute the document without affixing a common seal` | F-I2 |
| paragraph 41B(1)(a) | 6056-6058 | fork | `s 41B(1) the company may execute the document without affixing a common seal` | F-I2 |
| paragraph 41B(1)(b) | 6059-6064 | fork | `s 41B(1) the company may execute the document without affixing a common seal` | F-I2 |
| paragraph 41B(1)(c) | 6065-6069 | fork | `s 41B(1) the company may execute the document without affixing a common seal` | F-I2 |
| subsection 41B(2) | 6070-6076 | encoded | `s 41B(2) the document has the same effect as if it were executed under the common seal of the company` |  |
| subsection 41B(3) | 6077-6083 | fork | `s 41B(3) the document is considered to be signed by the person for the purposes of subsection (1) or (2)` | F-I18 |
| subsection 41B(4) | 6084-6090 | encoded | `s 41B(4) section 41B applies to the document` |  |
| section 41C | 6091-6100 | fork | `s 41C the document satisfies the written law or rule of law` | F-I2 |
| section 42 | 6101-6102 | repealed or blank | the text shows [Repealed by Act 5 of 2004] | |
| section 42A | 6103-6106 | inert 1 | heading or section title: not operative | |
| subsection 42A(1) | 6107-6109 | encoded | `s 42A(1) section 42A applies to the company or foreign company` |  |
| paragraph 42A(1)(a) | 6110-6111 | encoded | `s 42A(1) section 42A applies to the company or foreign company` |  |
| paragraph 42A(1)(b) | 6112-6118 | encoded | `s 42A(1) section 42A applies to the company or foreign company` |  |
| subsection 42A(2) | 6119-6130 | encoded | `s 42A(2) the company or foreign company is deemed to be used for purposes prejudicial to public welfare`; `s 42A(2) the company may be liable to be wound up by the Court under section 125(1)(n) of the Insolvency, Restructuring and Dissolution Act 2018`; `s 42A(2) the foreign company may be liable to have its name struck off the register by the Registrar under section 377(8)` |  |
| subsection 42A(3) | 6131-6134 | encoded | `s 42A(3) "charitable purpose" the purpose or object is a charitable purpose` |  |

## Fork register (sgi)

One entry for each kind of site where the text can be read two ways with different outcomes.
Each entry gives the answer taken, the other reading, and the line of `inputs/ENCODING-GUIDE.md` or the dated ruling that licenses it, quoted.
Under each entry is one row for every site, which is the "one fork line each" the grant ruling asks for; the same line is in the comment on the function in the layer-1 file.
The site rows are found by script from the fork comments in the layer-1 files, so the tables and the code cannot disagree about which function cites which entry.
Line numbers of the Guide are those of `inputs/ENCODING-GUIDE.md`; line numbers of the text are those of `inputs/CoA1967.txt`.

### F-I1: s 23(1)(a) and (b): the capacity "Subject to" other provisions

- Answer taken: `NOTHING` where a limit (a provision of the Act, another written law, the constitution) applies, or the rights are not for the purposes of paragraph (a); `JUST TRUE` where none applies.
- The other reading: `JUST FALSE`: where a limit applies the capacity is not "full", so the text says no.
- Licence: ENCODING-GUIDE.md section 5, "In short" (lines 86-87): a function answers `JUST FALSE` only where the text itself says no "in its own words: a 'means' definition, a condition the text introduces with 'if', 'only if', 'as long as' or 'unless' (and plain variants such as 'while', 'until' and 'except'), a list the text closes with 'only', a flat negative"; "everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed"; the brief: "The company's capacity in s 23 is stated as a liberty with exceptions (\"Subject to ... a company has full capacity ...\"): encode it as the text says it."
- Sites: 2.

| provision | function |
| --- | --- |
| s 23(1)(a) | `s 23(1)(a) the company has full capacity to carry on or undertake the business or activity, do the act or enter into the transaction` |
| s 23(1)(b) | `s 23(1)(b) the company has full rights, powers and privileges for the purposes of paragraph (a)` |

### F-I2: A permission or power ("may") whose conditions are not met

- Answer taken: `NOTHING`: the text names no outcome where a condition of a permission is not met.
- The other reading: `JUST FALSE`: reading (a) for a lawyer, a failed "if" is the text's no.
- Licence: the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed". Each site is one row of the table below.
- Sites: 33.

| provision | function |
| --- | --- |
| s 25(3) | `s 25(3) the Court may set aside and restrain the performance of the contract` |
| s 25(3) | `s 25(3) the Court may allow the claimant compensation for the loss or damage` |
| s 27(1B) | `s 27(1B) the Registrar may register the company under the name` |
| s 27(2A) | `s 27(2A) the person may apply to the Registrar for a direction to the company` |
| s 27(10) | `s 27(10) the person may apply to the Registrar for the reservation of the name` |
| s 27(13) | `s 27(13) the Registrar may extend the period for a further period of 60 days` |
| s 28(1) | `s 28(1) the company may resolve that its name should be changed to the new name` |
| s 28(3) | `s 28(3) the company may by special resolution change its name` |
| s 28(3A) | `s 28(3A) the person may apply to the Registrar for a direction to the company` |
| s 28(6) | `s 28(6) the legal proceedings may be continued or commenced by or against the company by its new name` |
| s 29(1) | `s 29(1) the company may be registered without the word Limited or Berhad accordingly` |
| s 29(3) | `s 29(3) the constitution may be altered by special resolution to give effect to the direction` |
| s 29(6A) | `s 29(6A) the Registrar may revoke the approval` |
| s 29(7) | `s 29(7) the constitution may be altered by special resolution to remove the provision requiring the Minister's consent` |
| s 29A(1) | `s 29A(1) the charitable company may change its name to omit the word Limited or Berhad` |
| s 30(1)(a) | `s 30(1)(a) the unlimited company may convert to a limited company` |
| s 30(1)(b) | `s 30(1)(b) the limited company may convert to an unlimited company` |
| s 30(8) | `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` |
| s 31(1) | `s 31(1) the public company may convert to a private company by lodging` |
| s 31(2) | `s 31(2) the private company may convert to a public company by lodging` |
| s 31(4) | `s 31(4) the legal proceedings may be continued or commenced by or against the company after the conversion` |
| s 37(1) | `s 37(1) the specified company may adopt the whole or any part of the model constitution as its constitution` |
| s 37(2) | `s 37(2) the specified company may adopt the whole model constitution by reference to its title` |
| s 37(3) | `s 37(3) the specified company may choose` |
| s 41(1) | `s 41(1) the contract or transaction may be ratified by the company` |
| s 41(3) | `s 41(3) the contract may be made on behalf of the corporation in the way` |
| s 41(3) | `s 41(3) the contract may be varied or discharged` |
| s 41(4) | `s 41(4) the document or proceeding may be signed by an authorised officer of the corporation` |
| s 41(5) | `s 41(5) the corporation may empower the person as its agent or attorney to execute deeds on its behalf` |
| s 41(7) | `s 41(7) the corporation may have for use in a place outside Singapore an official seal` |
| s 41(8) | `s 41(8) the instrument under seal is as valid as if the authority had been under seal` |
| s 41B(1) | `s 41B(1) the company may execute the document without affixing a common seal` |
| s 41C | `s 41C the document satisfies the written law or rule of law` |

### F-I3: s 25B(1): the deeming is limited to a person in good faith and to limitations under the constitution

- Answer taken: `NOTHING` outside the limit.
- The other reading: `JUST FALSE`: the power of the directors is not deemed free of the limitation.
- Licence: ENCODING-GUIDE.md section 5, "In short" (lines 86-87): a function answers `JUST FALSE` only where the text itself says no "in its own words: a 'means' definition, a condition the text introduces with 'if', 'only if', 'as long as' or 'unless' (and plain variants such as 'while', 'until' and 'except'), a list the text closes with 'only', a flat negative"; "everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit".
- Sites: 1.

| provision | function |
| --- | --- |
| s 25B(1) | `s 25B(1) the power of the directors to bind the company is deemed to be free of the limitation in favour of the person` |

### F-I4: A failed "if" the text introduces, on an applicability clause or a duty (ss 25C(1), 27(1A), 27(12A))

- Answer taken: `JUST FALSE`.
- The other reading: `NOTHING`: "if A then B" does not itself say "if not A then not B" (the brief's reading (a), marked "for a lawyer").
- Licence: ENCODING-GUIDE.md section 5, "In short" (lines 86-87): a function answers `JUST FALSE` only where the text itself says no "in its own words: a 'means' definition, a condition the text introduces with 'if', 'only if', 'as long as' or 'unless' (and plain variants such as 'while', 'until' and 'except'), a list the text closes with 'only', a flat negative"; "everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit" ("a condition the text introduces with 'if'") and the brief's status-quo reading (a).
- Sites: 8.

| provision | function |
| --- | --- |
| s 25C(1) | `s 25C(1) section 25C applies to the transaction` |
| s 25C(5) | `s 25C(5) the transaction ceases to be voidable` |
| s 33(5)(a) | `s 33(5)(a) the applicants hold enough of the shares, or are enough of the members` |
| s 33(5)(b) | `s 33(5)(b) the applicants hold enough in nominal value of the company's debentures` |
| s 33(5) | `s 33(5) the alteration does not have effect except so far as the Court confirms it` |
| s 33(10) | `s 33(10) the alteration of the objects takes effect` |
| s 27(1A) | `s 27(1A) the Registrar must refuse to register the company under the name` |
| s 27(12A) | `s 27(12A) the Registrar must refuse to approve the application` |

### F-I5: s 25C(3): a status ("voidable") gated by "Where"

- Answer taken: `JUST FALSE` when the "Where" fails.
- The other reading: `NOTHING`: the section is silent where the parties are not those it names.
- Licence: the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)".
- Sites: 1.

| provision | function |
| --- | --- |
| s 25C(3) | `s 25C(3) the transaction is voidable at the instance of the company` |

### F-I6: s 25C(7): the court "may, on the application of"

- Answer taken: `NOTHING` where there is no such application (split site (ii)).
- The other reading: `JUST FALSE`: "on the application" counts as "where" and a failed "where" is `JUST FALSE`.
- Licence: the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed"; the other reading is the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)". The grant ruling's limit 3 (line 99) says: "do not change, but list in the row's fork register for the maintainer or a lawyer, a \"may\" function whose gate is \"where\", \"when\" or \"upon\"" and that ruling (b) of the periods ruling "says `JUST FALSE`, and the \"In short\" line on grants points the other way". The brief makes this a split site to be decided site by site, so this part took `NOTHING` here and lists the site in the section "Split sites (sgi)"; a reader who takes limit 3 to keep the periods ruling's `JUST FALSE` flips the `ELSE` branch of the function and its tests.
- Sites: 1.

| provision | function |
| --- | --- |
| s 25C(7) | `s 25C(7) the court may make an order affirming, severing or setting aside the transaction` |

### F-I7: s 25D(2)(d): an "unless" once met

- Answer taken: `NOTHING`: the paragraph is then silent (the answer comes from s 25D(1)(c) or (d)).
- The other reading: `JUST TRUE` or `JUST FALSE`, inverted.
- Licence: the case-by-case ruling of 2026-11-05T10:25:24Z (line 95): "Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an \"unless\" or \"except\" once it is met; a bare \"must\" not done; ... a duty whose \"if\" or \"where\" is unmet; ...".
- Sites: 1.

| provision | function |
| --- | --- |
| s 25D(2)(d)(i) | `s 25D(2)(d)(i) the body corporate is treated as connected with the director for the purposes of subsection (2)` |

### F-I8: "within N days after X" (ss 26(2), 31(3A), 32(3)(c), 33(9))

- Answer taken: Met by an act on any day up to and including the last day (sg-periods P2, `the date is not later than the end of a period after`).
- The other reading: Met only before the last day (sg-periods `the date is within a period after`).
- Licence: sg-periods.l4 P1 (the day of the event is not counted) and P2 ("within" against "not later than"); the brief's rule that periods are counted only by sg-periods.l4.
- Sites: 0.

### F-I9: ss 26(1), 33(1), 29(3), 29(7): "may by special resolution", and "Unless otherwise provided in this Act"

- Answer taken: `NOTHING` for a resolution of another kind (the text does not say no other resolution will do) and where the Act otherwise provides (points outside this subsection).
- The other reading: `JUST FALSE` for another kind of resolution (an implied "only").
- Licence: ENCODING-GUIDE.md section 5, "In short" (lines 86-87): a function answers `JUST FALSE` only where the text itself says no "in its own words: a 'means' definition, a condition the text introduces with 'if', 'only if', 'as long as' or 'unless' (and plain variants such as 'while', 'until' and 'except'), a list the text closes with 'only', a flat negative"; "everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit" ("is silent, points outside the sources").
- Sites: 4.

| provision | function |
| --- | --- |
| s 26(1) | `s 26(1) the constitution may be altered or added to by the resolution` |
| s 33(1) | `s 33(1) the company may alter the provisions of its constitution with respect to its objects by the resolution` |
| s 34(1) | `s 34(1) the company may amend its constitution to remove the provision` |
| s 34(2)(b) | `s 34(2)(b) the company may amend its constitution to remove that provision` |

### F-I10: Split site (i): an unmet element of an offence

- Answer taken: `JUST FALSE`, for the offence provision's own question.
- The other reading: `NOTHING`: the text does not say what the position is of one who is not within the offence.
- Licence: the grant ruling of 2026-11-12, limit 2 (line 98): "keep `JUST FALSE` where the text closes the gate itself (\"only if\", \"only where\", \"may not ... unless\", a list closed with \"only\"), and for a bar, a duty or the provision's own question" (the provision's own question); N2 (line 92): "flat negatives count as a no".
- Sites: 6.

| provision | function |
| --- | --- |
| s 26(2A) | `s 26(2A) the person is guilty of the offence` |
| s 27(2B) | `s 27(2B) the person is guilty of the offence` |
| s 28(3B) | `s 28(3B) the person is guilty of the offence` |
| s 32(6) | `s 32(6) the person is guilty of the offence` |
| s 32(8) | `s 32(8) the person is guilty of the offence` |
| s 40(4) | `s 40(4) the person is guilty of the offence` |

### F-I11: A duty or status gated by "Upon", "On" or "thereupon"

- Answer taken: `JUST FALSE` where the gate fails.
- The other reading: `NOTHING`.
- Licence: the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)"; the grant ruling of 2026-11-12, limit 2 (line 98): "keep `JUST FALSE` where the text closes the gate itself (\"only if\", \"only where\", \"may not ... unless\", a list closed with \"only\"), and for a bar, a duty or the provision's own question".
- Sites: 15.

| provision | function |
| --- | --- |
| s 26(7) | `s 26(7) the Registrar must issue to the company a certificate confirming the incorporation in accordance with the alteration` |
| s 28(5) | `s 28(5) the Registrar must issue to the company a certificate confirming the incorporation under the new name` |
| s 29(6) | `s 29(6) upon the revocation the Registrar must enter the word Limited or Berhad at the end of the name in the register` |
| s 29(6) | `s 29(6) upon the revocation the company ceases to enjoy the exemption` |
| s 29(9) | `s 29(9) the Registrar must issue to the company a certificate confirming the approval` |
| s 29A(3) | `s 29A(3) the Registrar must register the name of the charitable company with the omission and issue the notice of incorporation` |
| s 29A(4) | `s 29A(4) the change of name has become effective and the charitable company is exempted` |
| s 29A(5) | `s 29A(5) the exemption under subsection (4)(b) has ceased` |
| s 30(2) | `s 30(2) the company is deemed to be a company having the status specified in the notice` |
| s 30(3A) | `s 30(3A) the Registrar must issue to the company a certificate confirming the incorporation with the new status` |
| s 31(2) | `s 31(2) the restrictions and limitations referred to in section 18(1) cease to form part of the constitution` |
| s 31(3) | `s 31(3) the company has become a private company` |
| s 31(3) | `s 31(3) the company has become a public company` |
| s 31(5) | `s 31(5) the Registrar must issue to the company a certificate confirming the incorporation with the new status` |
| s 41(1) | `s 41(1) the company is bound by and entitled to the benefit of the contract or transaction` |

### F-I12: s 33(2): "21 days' written notice"

- Answer taken: The notice is given not later than 21 days before the meeting (sg-periods P5).
- The other reading: Twenty-one clear days (sg-periods P7).
- Licence: sg-periods.l4 P5 and P7.
- Sites: 1.

| provision | function |
| --- | --- |
| s 33(2) | `s 33(2) the company has given the notice the subsection requires` |

### F-I13: ss 33(4) and 33(6): a power or permission whose gate failed

- Answer taken: `NOTHING`.
- The other reading: `JUST FALSE`.
- Licence: the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed".
- Sites: 2.

| provision | function |
| --- | --- |
| s 33(4) | `s 33(4) the Court may dispense with the notice for the person or class of persons` |
| s 33(6) | `s 33(6) the application may be made on behalf of the persons entitled by the applicants` |

### F-I14: s 33(7): the Court "On the application"

- Answer taken: (a) a duty: `JUST FALSE` where there is no application; (b) to (d) powers: `NOTHING`.
- The other reading: (a) `NOTHING`; (b) to (d) `JUST FALSE` ("On" counts as "where").
- Licence: the grant ruling of 2026-11-12, limit 2 (line 98): "keep `JUST FALSE` where the text closes the gate itself (\"only if\", \"only where\", \"may not ... unless\", a list closed with \"only\"), and for a bar, a duty or the provision's own question" for (a); the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed" for (b) to (d); the other readings rest on the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)". The grant ruling's limit 3 (line 99) says: "do not change, but list in the row's fork register for the maintainer or a lawyer, a \"may\" function whose gate is \"where\", \"when\" or \"upon\"" and that ruling (b) of the periods ruling "says `JUST FALSE`, and the \"In short\" line on grants points the other way". The brief makes this a split site to be decided site by site, so this part took `NOTHING` here and lists the site in the section "Split sites (sgi)"; a reader who takes limit 3 to keep the periods ruling's `JUST FALSE` flips the `ELSE` branch of the function and its tests.
- Sites: 4.

| provision | function |
| --- | --- |
| s 33(7)(a) | `s 33(7)(a) the Court must have regard to the rights and interests of the members and of the creditors` |
| s 33(7)(b) | `s 33(7)(b) the Court may adjourn the proceedings` |
| s 33(7)(c) | `s 33(7)(c) the Court may give the directions and make the orders` |
| s 33(7)(d) | `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` |

### F-I15: s 34(1) and (2)(b): a power gated by "Where" (split site (ii))

- Answer taken: `NOTHING`.
- The other reading: `JUST FALSE`.
- Licence: the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed"; the other reading is the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)". The grant ruling's limit 3 (line 99) says: "do not change, but list in the row's fork register for the maintainer or a lawyer, a \"may\" function whose gate is \"where\", \"when\" or \"upon\"" and that ruling (b) of the periods ruling "says `JUST FALSE`, and the \"In short\" line on grants points the other way". The brief makes this a split site to be decided site by site, so this part took `NOTHING` here and lists the site in the section "Split sites (sgi)"; a reader who takes limit 3 to keep the periods ruling's `JUST FALSE` flips the `ELSE` branch of the function and its tests.
- Sites: 2.

| provision | function |
| --- | --- |
| s 34(1) | `s 34(1) the company may amend its constitution to remove the provision` |
| s 34(2)(b) | `s 34(2)(b) the company may amend its constitution to remove that provision` |

### F-I16: s 27(1B)(a)(i) and (ii): joined by "and"

- Answer taken: Both limbs must hold (the literal "and"): the foreign company's cessation notice and three months, and its name struck off and six years.
- The other reading: Either limb suffices ("or").
- Licence: The text of s 27(1B)(a)(i), which ends "; and" before (ii) (CoA1967.txt lines 4778-4804).
- Sites: 1.

| provision | function |
| --- | --- |
| s 27(1B) | `s 27(1B) the Registrar may register the company under the name` |

### F-I17: s 27(1A), (1B): "a period of at least N years has passed after the date"

- Answer taken: The day asked is after the last day of the N years (sg-periods P1, P2): on the anniversary itself the period has not yet passed.
- The other reading: The period has passed on the anniversary.
- Licence: sg-periods.l4 P1 and P2; the text's "after the date" (CoA1967.txt lines 4692-4776).
- Sites: 0.

### F-I18: An "unless", "except" or "in the absence of" once it is met

- Answer taken: `NOTHING`: the text then says nothing of the case.
- The other reading: The opposite of the answer given before the exception is met.
- Licence: the case-by-case ruling of 2026-11-05T10:25:24Z (line 95): "Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an \"unless\" or \"except\" once it is met; a bare \"must\" not done; ... a duty whose \"if\" or \"where\" is unmet; ...".
- Sites: 13.

| provision | function |
| --- | --- |
| s 27(1) | `s 27(1) the Registrar must refuse to register the company under the name` |
| s 27(1A) | `s 27(1A) the Registrar must refuse to register the company under the name` |
| s 27(2) | `s 27(2) the company has complied with the direction` |
| s 27(11) | `s 27(11) the registration of the company, or the approval of the change of name, is barred` |
| s 28(3) | `s 28(3) the company must change its name within 6 weeks after the direction` |
| s 28(3A) | `s 28(3A) the Registrar is barred from considering the application` |
| s 28(4) | `s 28(4) the Registrar is barred from directing the company to change its name under subsection (3)` |
| s 32(5) | `s 32(5) the company may not convert to a private company` |
| s 35(1) | `s 35(1) the constitution of the company must contain the regulations for the company` |
| s 39(3) | `s 39(3) the member is bound by the alteration` |
| s 40(2) | `s 40(2) the company must not issue the copy of the constitution` |
| s 41(2) | `s 41(2) the person is personally bound by the contract or transaction and entitled to the benefit of it` |
| s 41B(3) | `s 41B(3) the document is considered to be signed by the person for the purposes of subsection (1) or (2)` |

### F-I19: A "may" gated by "where" (ss 27(2), 29(1), 29(2), 29(4), 32(2), 32(4)): split site (ii)

- Answer taken: `NOTHING` where the gate fails.
- The other reading: `JUST FALSE` ("where ..." fails).
- Licence: the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed"; the other reading is the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)". The grant ruling's limit 3 (line 99) says: "do not change, but list in the row's fork register for the maintainer or a lawyer, a \"may\" function whose gate is \"where\", \"when\" or \"upon\"" and that ruling (b) of the periods ruling "says `JUST FALSE`, and the \"In short\" line on grants points the other way". The brief makes this a split site to be decided site by site, so this part took `NOTHING` here and lists the site in the section "Split sites (sgi)"; a reader who takes limit 3 to keep the periods ruling's `JUST FALSE` flips the `ELSE` branch of the function and its tests.
- Sites: 6.

| provision | function |
| --- | --- |
| s 27(2) | `s 27(2) the Registrar may direct the company to change its name` |
| s 29(1) | `s 29(1) the Registrar may approve that the proposed limited company be registered without the word Limited or Berhad` |
| s 29(2) | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` |
| s 29(4) | `s 29(4) the company may alter any provision of the constitution` |
| s 32(2) | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` |
| s 32(4) | `s 32(4) the Court may determine that the company has not ceased to be a private company` |

### F-I20: s 27(12B)(a) and (13): "such further period of 60 days" and "a further period of 60 days"

- Answer taken: The number of further 60-day periods is a plain input.
- The other reading: Only one extension is allowed.
- Licence: The text does not say whether the Registrar may extend more than once (CoA1967.txt lines 4958-4971 and 4988-4991).
- Sites: 1.

| provision | function |
| --- | --- |
| s 27(12B) | `s 27(12B) the last day of the reservation` |

### F-I21: A duty, bar or status gated by "If", "Where" or "that proposes" that is unmet

- Answer taken: `JUST FALSE`.
- The other reading: `NOTHING`: a duty's "if" is a limit in its own wording.
- Licence: the grant ruling of 2026-11-12, limit 2 (line 98): "keep `JUST FALSE` where the text closes the gate itself (\"only if\", \"only where\", \"may not ... unless\", a list closed with \"only\"), and for a bar, a duty or the provision's own question"; the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)".
- Sites: 17.

| provision | function |
| --- | --- |
| s 28(2) | `s 28(2) the Registrar must register the company under the new name and issue the notice of incorporation` |
| s 28(2) | `s 28(2) the change of name has become effective` |
| s 28(3) | `s 28(3) the company must change its name within 6 weeks after the direction` |
| s 28(4) | `s 28(4) the Registrar is barred from directing the company to change its name under subsection (3)` |
| s 29(3) | `s 29(3) the conditions must be inserted in the constitution of the company` |
| s 29(8) | `s 29(8) the notice of the approval must be given to the person` |
| s 29A(2) | `s 29A(2) the charitable company has met the requirements for the change of name` |
| s 29A(5) | `s 29A(5) the Registrar must enter the word Limited or Berhad at the end of the name of the company` |
| s 30(2) | `s 30(2) the Registrar must issue to the company a notice of incorporation appropriate to the change of status` |
| s 30(3) | `s 30(3) the notice of the change of status must be published` |
| s 32(3)(a) | `s 32(3)(a) the company is a public company on and from the date specified` |
| s 32(3)(b) | `s 32(3)(b) the company is deemed to have changed its name by the omission of the word Private or Sendirian` |
| s 32(3)(c) | `s 32(3)(c) the company has complied with the duty to lodge the statement in lieu of prospectus and the declaration` |
| s 37(3)(b) | `s 37(3)(b) the model constitution for the time being in force is, so far as applicable, the constitution of the specified company` |
| s 37(4) | `s 37(4) a copy of the constitution of the specified company must be submitted to the Registrar` |
| s 39(1) | `s 39(1) the constitution binds the person to the same extent as if signed and sealed by each member` |
| s 40(2) | `s 40(2) the company must not issue the copy of the constitution` |

### F-I22: A status "while" or "until" an event (s 29(5) while an approval is in force; s 35(3) until the constitution is amended; s 41(6) during the period mentioned, or until notice)

- Answer taken: `JUST FALSE` outside the period the text fixes.
- The other reading: `NOTHING`: the end is an event, not a period of days.
- Licence: the periods ruling of 2026-11-05, item (a) (line 93): "a period the text fixes in its own words (\"within one month\", \"begins from ... until the employee attains the age\", \"on the last day of employment\"): outside the period the answer is `JUST FALSE`"; ENCODING-GUIDE.md section 5, "In short" (lines 86-87): a function answers `JUST FALSE` only where the text itself says no "in its own words: a 'means' definition, a condition the text introduces with 'if', 'only if', 'as long as' or 'unless' (and plain variants such as 'while', 'until' and 'except'), a list the text closes with 'only', a flat negative"; "everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit" ("plain variants such as 'while', 'until'").
- Sites: 3.

| provision | function |
| --- | --- |
| s 29(5) | `s 29(5) the company is exempted from complying with the provisions of this Act relating to the use of the word Limited or Berhad` |
| s 35(3) | `s 35(3) the regulations are deemed to be the regulations for the company contained in its constitution` |
| s 41(6) | `s 41(6) the authority of the agent or attorney continues as between the corporation and the person dealing with the agent or attorney` |

### F-I23: s 29(6): the precondition of a revocation is phrased as a duty ("but before the approval is so revoked the Registrar must give ... notice")

- Answer taken: `NOTHING` where it is not met.
- The other reading: `JUST FALSE` (the revocation is not within the power without notice).
- Licence: the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed" (the text does not say "only after"): marginal.
- Sites: 1.

| provision | function |
| --- | --- |
| s 29(6) | `s 29(6) the Registrar may revoke the approval` |

### F-I24: ss 29(11), (12), (13): a transitional rule fixed on 3 January 2016

- Answer taken: `JUST FALSE` before that date; `NOTHING` where no such approval, condition or reference existed.
- The other reading: `NOTHING` before that date.
- Licence: the periods ruling of 2026-11-05, item (a) (line 93): "a period the text fixes in its own words (\"within one month\", \"begins from ... until the employee attains the age\", \"on the last day of employment\"): outside the period the answer is `JUST FALSE`" (a date the text fixes in its own words).
- Sites: 3.

| provision | function |
| --- | --- |
| s 29(11) | `s 29(11) the approval or condition is treated as the Registrar's approval and condition` |
| s 29(12) | `s 29(12) the reference to the Minister's approval is read as a reference to the Registrar` |
| s 29(13) | `s 29(13) the reference to a direction of the Minister is read as a direction of the Registrar` |

### F-I25: s 29A(1): "subject to section 28(3) to (6)"

- Answer taken: The function answers on the subsection's own gate (a limited company registered as a charity); the limits of s 28(3) to (6) are answered by their own functions.
- The other reading: The function takes the limits as inputs.
- Licence: The text points to other provisions of the Act, which this module encodes in their own functions.
- Sites: 1.

| provision | function |
| --- | --- |
| s 29A(1) | `s 29A(1) the charitable company may change its name to omit the word Limited or Berhad` |

### F-I26: s 30(3): "in such manner (if any) as the Registrar may direct"

- Answer taken: `NOTHING` where the Registrar directs no manner: the text does not say whether notice must still be published.
- The other reading: `JUST TRUE`: notice must be published in some manner, or `JUST FALSE`: no publication.
- Licence: ENCODING-GUIDE.md section 5, "In short" (lines 86-87): a function answers `JUST FALSE` only where the text itself says no "in its own words: a 'means' definition, a condition the text introduces with 'if', 'only if', 'as long as' or 'unless' (and plain variants such as 'while', 'until' and 'except'), a list the text closes with 'only', a flat negative"; "everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit" ("is silent").
- Sites: 1.

| provision | function |
| --- | --- |
| s 30(3) | `s 30(3) the notice of the change of status must be published` |

### F-I27: s 30(7): "With such modifications as may be necessary"

- Answer taken: The function answers whether the provision of s 33 applies; it does not say what the modifications are.
- The other reading: The function takes the modified provision as an input.
- Licence: The text does not list the modifications (CoA1967.txt lines 5453-5458).
- Sites: 1.

| provision | function |
| --- | --- |
| s 30(7) | `s 30(7) the provision of section 33 applies to the special resolution` |

### F-I28: s 32(3)(a), (b): "on and from the date specified in the order or notice"

- Answer taken: `JUST FALSE` before the date specified; `JUST TRUE` on and from it.
- The other reading: `JUST TRUE` from the determination, with the status relating back.
- Licence: the periods ruling of 2026-11-05, item (a) (line 93): "a period the text fixes in its own words (\"within one month\", \"begins from ... until the employee attains the age\", \"on the last day of employment\"): outside the period the answer is `JUST FALSE`"; the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)".
- Sites: 2.

| provision | function |
| --- | --- |
| s 32(3)(a) | `s 32(3)(a) the company is a public company on and from the date specified` |
| s 32(3)(b) | `s 32(3)(b) the company is deemed to have changed its name by the omission of the word Private or Sendirian` |

### F-I29: s 40(1): the duty is gated by the member's requirement, "(if any)" and payment

- Answer taken: `JUST FALSE` where a gate fails.
- The other reading: `NOTHING`.
- Licence: the grant ruling of 2026-11-12, limit 2 (line 98): "keep `JUST FALSE` where the text closes the gate itself (\"only if\", \"only where\", \"may not ... unless\", a list closed with \"only\"), and for a bar, a duty or the provision's own question"; the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; item (c) of the delegated-definitions ruling of the same day (line 94): "'when', 'upon' and 'whenever' count as 'where' under rule (b)".
- Sites: 1.

| provision | function |
| --- | --- |
| s 40(1) | `s 40(1) the company must send the member a copy of the constitution` |

### F-I30: s 41(2): after ratification

- Answer taken: `NOTHING`: the subsection speaks of the time "Prior to ratification", and s 41(1) does not say the person is released.
- The other reading: `JUST FALSE`: outside the period the text fixes.
- Licence: the periods ruling of 2026-11-05, item (a) (line 93): "a period the text fixes in its own words (\"within one month\", \"begins from ... until the employee attains the age\", \"on the last day of employment\"): outside the period the answer is `JUST FALSE`" read against s 41(1): the end of the period is an event, not a stated period.
- Sites: 1.

| provision | function |
| --- | --- |
| s 41(2) | `s 41(2) the person is personally bound by the contract or transaction and entitled to the benefit of it` |

### F-I31: A "must" with no time fixed, not yet done (s 29A(2), s 41(7))

- Answer taken: `NOTHING`: the text fixes no time, so a person who has not yet done it has not failed.
- The other reading: `JUST FALSE`: the duty is unmet.
- Licence: the case-by-case ruling of 2026-11-05T10:25:24Z (line 95): "Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an \"unless\" or \"except\" once it is met; a bare \"must\" not done; ... a duty whose \"if\" or \"where\" is unmet; ..." ("a bare 'must' not done").
- Sites: 1.

| provision | function |
| --- | --- |
| s 41(7) | `s 41(7) the person affixing the official seal has certified the date and the place` |

### F-I32: s 38(1): a provision outside the avoidance (a company not limited by guarantee, or a provision that gives no right to the divisible profits)

- Answer taken: `NOTHING`: the subsection voids provisions of that kind in that kind of company and says nothing of any other.
- The other reading: `JUST FALSE`: the earlier pass (`inputs/NAIVE-EVIDENCE/coa-formation-shares-buyback.l4`, `the provision is void under section 38(1)`) is a plain BOOLEAN that answers FALSE whenever either limb fails.
- Licence: the periods ruling of 2026-11-05, item (c) (line 93): "a scope limit with no \"only\" (for example \"below\" the minimum age): outside the scope the answer is `NOTHING`" ("In the case of a company limited by guarantee"); ENCODING-GUIDE.md section 5, "In short" (line 87): `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit".
- Sites: 1.

| provision | function |
| --- | --- |
| s 38(1) | `s 38(1) the provision is void` |

### Functions named for an entitlement (the grant ruling's limit 3, line 99)

The ruling says an "entitled"-named function is listed and not changed: "an entitlement is a claim, not a power, and this guide does not settle it".
Whether such a function should answer `NOTHING` where its gate fails is for the maintainer or a lawyer.

There are 3 functions here named for an entitlement (`s 33(6)` says "persons entitled" but is named for a power, so it is not among them):

| provision | function |
| --- | --- |
| s 27(15) | `s 27(15) the reservation in itself entitles the company to be registered by the name` |
| s 41(1) | `s 41(1) the company is bound by and entitled to the benefit of the contract or transaction` |
| s 41(2) | `s 41(2) the person is personally bound by the contract or transaction and entitled to the benefit of it` |

Their answers: `s 27(15)` is `JUST FALSE` where a name is reserved (the text says the reservation "does not in itself entitle") and `NOTHING` otherwise; `s 41(1)` and `s 41(2)` are as the fork entries F-I11, F-I18 and F-I30 describe.

## Jural relations (sgi)

One row for each provision that creates a right, privilege, power or immunity, with its correlative (Hohfeld): a right is the other party's duty, a privilege is the other party's no-right, a power is the other party's liability (being subject to it, not an obligation), and an immunity is the other party's disability.
A provision that creates no such relation (a definition, a counting rule, an effect rule) is listed once as `none`, with what it is; a provision the text shows deleted is `none` too.
The last column lists the L4 rules that encode the row, found by script (a function belongs to the row with the longest key that is a prefix of its label); where it is empty the row has no rule of its own.
Where the text names no holder or no bearer, the row says so and does not supply one.
N2 (Guide line 92) keeps the Hohfeld kinds in this table and does not type the answers to the questions in layer 2.

| provision | holder: right, privilege, power or immunity | bearer: correlative duty, no-right, liability or disability | L4 rules |
| --- | --- | --- | --- |
| s 23(1) | Company: power and privilege (full capacity to carry on business, do acts and enter transactions; full rights, powers and privileges), "subject to" the Act, other written law and its constitution | Persons dealing with the company: liability to its acts and no-right to stop them | `s 23(1)(a) the company has full capacity to carry on or undertake the business or activity, do the act or enter into the transaction`; `s 23(1)(b) the company has full rights, powers and privileges for the purposes of paragraph (a)` |
| s 23(1A), s 23(1B) | Company: privilege to have its objects, and a provision restricting its capacity, rights, powers or privileges, in its constitution | Others: no-right to object | `s 23(1A) the company may have its objects included in its constitution`; `s 23(1B) the constitution may contain the provision` |
| s 23(2) | none: the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | none |  |
| s 23(3) | none: the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | none |  |
| s 23(4) | none: the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | none |  |
| s 23(5) | none: the text shows [Deleted by Act 17 of 2023 wef 01/07/2023] | none |  |
| s 24(1) | Company: power to make provision, on a cessation of the whole or part of its or a subsidiary's business, for persons employed or formerly employed (an employee gets no claim from the subsection) | Members and others affected: liability to the exercise of the power | `s 24(1) the powers of the company are deemed to include power to make the provision` |
| s 24(2) | none: limits (1) to the company's capacity and leaves the constitution's approval requirement in place | none | `s 24(2) subsection (1) affects the constitution's provision on how the power is exercised` |
| s 25(1) | Company and the other party to an act, conveyance or transfer: immunity from invalidity by reason only of the company's lack of capacity or power | Anyone who would say the act is invalid for that reason: disability | `s 25(1) the act is invalid by reason only of the company's lack of capacity or power` |
| s 25(2) | A member (and a floating-charge debenture holder or trustee) against the company, the company or a member against present or former officers, and the Minister on an application to wind up: power to assert the lack of capacity or power, in those proceedings only | The company and its officers: liability; everyone else in any other proceedings: disability | `s 25(2) the lack of capacity or power may be asserted or relied upon in the proceedings` |
| s 25(3) | Court: power, if all parties to the contract are before it and it is just and equitable, to set aside and restrain the contract and to allow compensation (not anticipated profits) | The company and the other parties: liability to the order; a party's claim to compensation arises only once the Court allows it | `s 25(3) the Court may set aside and restrain the performance of the contract`; `s 25(3) the Court may allow the claimant compensation for the loss or damage`; `s 25(3) the Court may award the amount as a loss or damage sustained` |
| s 25A | Any person: immunity from being affected by, or deemed to know, the contents of the constitution or other documents merely because registered or open for inspection at the registered office | The company: disability to rely on constructive notice | `s 25A the person is affected by, or is deemed to have notice or knowledge of, the contents of the constitution or document` |
| s 25B(1) | Person dealing with the company in good faith: immunity from any limitation, under the constitution, on the directors' power to bind the company or authorise others | The company: disability to plead the limitation | `s 25B(1) the power of the directors to bind the company is deemed to be free of the limitation in favour of the person` |
| s 25B(2) | Person dealing with the company: privilege not to enquire into limitations on the directors' powers, and a presumption of good faith unless the contrary is proved | The company: no-right to an enquiry; it carries the burden of proving bad faith | `s 25B(2)(b) the person dealing with the company is presumed to have acted in good faith`; `s 25B(2)(a) the person dealing with the company is bound to enquire as to any limitation on the powers of the directors` |
| s 25B(3) | none: says what counts as a limitation under the constitution | none | `s 25B(3) the limitation is within the limitations on the directors' powers under the company's constitution` |
| s 25B(4) | A member: preserved power to bring proceedings to restrain an act beyond the directors' powers, except an act to be done in fulfilment of a legal obligation from a previous act of the company | The company and its directors: liability; the member: disability for an act done in fulfilment of such an obligation | `s 25B(4) section 25B affects the member's right to bring the proceedings`; `s 25B(4) the proceedings lie in respect of the act` |
| s 25B(5) | The company and anyone wronged: preserved claim against directors or others for exceeding their powers | Directors and other persons: preserved liability | `s 25B(5) section 25B affects the liability` |
| s 25B(6) | none: ranks s 25B below s 25C | none | `s 25B(6) section 25B has effect subject to section 25C for the transaction` |
| s 25C(1), s 25C(2), s 25C(8) | none: scope, saving of other written law and rules of law, and the meaning of "transaction" | none | `s 25C(1) section 25C applies to the transaction`; `s 25C(2) section 25C excludes the operation of the other written law or rule of law`; `s 25C(8) the thing is within the word transaction` |
| s 25C(3) | Company: power to avoid a transaction to which a director of the company or its holding company, or a person connected with such a director, is a party | That director or connected person, and the other parties: liability | `s 25C(3) the transaction is voidable at the instance of the company` |
| s 25C(4), s 25C(6) | Company: claim, whether or not it avoids, to an account of any gain and an indemnity for any loss or damage; a person other than a director: immunity from that liability on showing that the person did not know the directors were exceeding their powers | A party within s 25C(3)(b), and any director who authorised the transaction: duty (no time fixed); the company: disability against the non-director who did not know | `s 25C(4) the person is liable to the company under subsection (4)`; `s 25C(6) the person other than a director is liable under subsection (4)`; `s 25C(4) and (6) the person is liable to the company`; `s 25C(4)(a) the amount the person must account to the company for`; `s 25C(4)(b) the person must indemnify the company for the loss or damage`; `s 25C(4)(b) the amount the person must indemnify the company for`; `s 25C(4)(a) the person liable under subsection (4) must account to the company for any gain`; `s 25C(4)(b) the person liable under subsection (4) must indemnify the company for any loss or damage` |
| s 25C(5) | The other party: immunity from avoidance once restitution is impossible, the company is indemnified, bona fide rights acquired for value would be affected, or the company affirms | Company: disability to avoid | `s 25C(5) the transaction ceases to be voidable` |
| s 25C(7) | A party not within s 25C(3)(b): preserved rights; Court: power, on the application of the company or such a party, to affirm, sever or set aside the transaction on just terms | The parties: liability to the order | `s 25C(7) subsections (1) to (6) affect the rights of the party`; `s 25C(7) the court may make an order affirming, severing or setting aside the transaction` |
| s 25D | none: defines a person connected with a director (the family, bodies corporate, trustees, partners and firms it names, and the 20% tests) | none | `s 25D(2)(a) the person is a member of the director's family`; `s 25D(2)(b) the director is connected with the body corporate`; `s 25D(2)(c) the voting power counts as voting power the exercise of which is controlled by the director`; `s 25D(2)(d)(i) the body corporate is treated as connected with the director for the purposes of subsection (2)`; `s 25D(2)(d)(ii) the trustee is treated as connected with the director for the purposes of subsection (2)`; `s 25D(2)(e) the body is within the words body corporate`; `s 25D(1)(c) the person is within paragraph (c)`; `s 25D(1)(d) the person is within paragraph (d)`; `s 25D(1)(e) the person is within paragraph (e)`; `s 25D(1) the person is a person connected with the director` |
| s 26(1) | Company: power to alter or add to its constitution by special resolution, unless the Act provides otherwise | Members, including those who voted against: liability to the alteration | `s 26(1) the constitution may be altered or added to by the resolution` |
| s 26(1AA) | none: counting rule (the alteration forms part of the original constitution from the date of the resolution or the later date it specifies) | none | `s 26(1AA) the date on and from which the alteration or addition forms part of the original constitution` |
| s 26(1AB) | Company: privilege to adopt a model constitution by its title or the numbers of its regulations without setting out the text | none | `s 26(1AB) the special resolution needs to set out the text of the model constitution adopted` |
| s 26(1A) | none: makes the power in (1) subject to s 26A and to any entrenching provision | none | `s 26(1A) the power in subsection (1) is subject to an entrenching provision` |
| s 26(1B) | Each member: power to withhold agreement to the alteration of a provision that could not be altered before 1 April 2004 (it may be altered only if all members agree) | Company: disability to alter it without all the members | `s 26(1B) the provision may be altered` |
| s 26(2) | Registrar: claim to lodging, within 14 days, of a copy of the resolution, order or other document, with a copy of the constitution unless the Registrar dispenses with it | Company: duty (regulative rule with a deadline) | `s 26(2) the company has complied with the duty to lodge a copy of the resolution, order or other document`; `s 26(2) the company must lodge a copy within 14 days` |
| s 26(2A) | State: power to prosecute | Company and each officer in default: liability to a fine of up to $1,000 and a default penalty | `s 26(2A) the person is guilty of the offence`; `s 26(2A) the most the person may be sentenced to on conviction` |
| s 26(3) | Company: claim to registration of what it lodged and, for an order, to a notice of the registration | Registrar: duty | `s 26(3) the Registrar must register the document`; `s 26(3) the Registrar must issue to the company a notice of the registration of the order` |
| s 26(4) | none: the text shows [Deleted by Act 12 of 2002] | none |  |
| s 26(5) | none: no holder or bearer is named (the notice is to be published "in such manner (if any)" as the Court or the Registrar directs) | none | `s 26(5) the notice of the registration must be published in the manner directed` |
| s 26(6) | Company: claim to a notice of incorporation in accordance with the alteration, where appropriate | Registrar: duty | `s 26(6) the Registrar must issue a notice of incorporation in accordance with the alteration` |
| s 26(7) | Company: claim, on application and payment of the prescribed fee, to a certificate confirming the incorporation in accordance with the alteration | Registrar: duty | `s 26(7) the Registrar must issue to the company a certificate confirming the incorporation in accordance with the alteration` |
| s 26A(1) | Company: privilege to include an entrenching provision in the constitution it is formed with; each member: power to withhold agreement to inserting one later (only if all agree) | Company: disability to insert one later without all the members | `s 26A(1)(a) the entrenching provision may be included in the constitution with which the company is formed`; `s 26A(1)(b) the entrenching provision may be inserted in the constitution` |
| s 26A(2), s 26A(3) | Each member: power to withhold agreement to removing or altering an entrenching provision (only if all agree); the protected provisions: immunity from alteration by the ordinary route | Company: disability to alter in the manner the entrenching provision bars | `s 26A(2) the entrenching provision may be removed or altered`; `s 26A(3) the provisions of this Act on the alteration of the constitution are subject to the entrenching provision` |
| s 26A(4) | none: defines "entrenching provision" | none | `s 26A(4) the provision is an entrenching provision` |
| s 27(1), s 27(1A) | Registrar: duty to refuse to register a company under a name that is undesirable, identical, reserved, of a kind the Minister has directed against, or (1A) identical to a dissolved or cancelled name within the stated period; Minister: power to consent | Applicant: no-right to the name unless the Minister consents | `s 27(1) the Registrar must refuse to register the company under the name`; `s 27(1A) the years that must pass after the date of dissolution, cancellation or cessation`; `s 27(1A) the Registrar must refuse to register the company under the name` |
| s 27(1B) | Registrar: privilege, on or after 3 January 2016 and despite (1), to register a company under a name identical to a foreign company's or a limited partnership's, once the stated time has passed | Applicant: no claim to the name; others: no-right to stop the registration | `s 27(1B) the Registrar may register the company under the name` |
| s 27(2) | Registrar: power, where satisfied that a company was registered by a name within (a), (aa), (ab), (b) or (c), to direct it to change its name; Minister: power to annul the direction | Company: liability to the direction, and duty to comply within 6 weeks of the direction (or a longer period the Registrar allows) unless the Minister annuls it | `s 27(2) the Registrar may direct the company to change its name`; `s 27(2) the company has complied with the direction`; `s 27(2) the last day for compliance`; `s 27(2) the company must change its name within 6 weeks of the direction` |
| s 27(2A) | Any person: privilege to apply in writing for a direction | Registrar: barred from considering an application on the (2)(b) ground received more than 12 months after incorporation; the applicant: no-right to a decision then | `s 27(2A) the person may apply to the Registrar for a direction to the company`; `s 27(2A) the Registrar is barred from considering the application` |
| s 27(2B) | State: power to prosecute | Company and its officers: liability to a fine of up to $2,000 and a default penalty | `s 27(2B) the person is guilty of the offence`; `s 27(2B) the most the person may be sentenced to on conviction` |
| s 27(2C) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 27(2D) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 27(3) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 27(4) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 27(5) | A company aggrieved by a decision under (2): power to appeal to the Minister within 30 days after the decision; an applicant aggrieved by a refusal to direct: power to appeal within 30 days after being informed | The Registrar's decision: liability to review | `s 27(5) the person may appeal to the Minister against the decision` |
| s 27(5AA) | Minister: immunity of the decision on an appeal (final) | Appellant: disability to reopen it | `s 27(5AA) the decision of the Minister on the appeal is final` |
| s 27(5A) | none for the individual: the Registrar and the Minister must accept as correct a Court's grant of an injunction | Registrar and Minister: duty | `s 27(5A) the Registrar or the Minister must accept as correct the decision of the Court to grant the injunction` |
| s 27(6) | none for the individual: the Minister must cause a direction under (1) to be published in the Gazette | Minister: duty | `s 27(6) the Minister must cause the direction to be published in the Gazette` |
| s 27(7), s 27(8) | The text names no holder: a limited company must have "Limited" or "Berhad" at the end of its name (subject to s 29), and a private company "Private" or "Sendirian" in it | Company: duty | `s 27(7) the name of the limited company has the word Limited or Berhad as the subsection requires`; `s 27(8) the name of the private company has the word Private or Sendirian as the subsection requires` |
| s 27(9) | Company: privilege to use the abbreviations "Pte.", "Sdn.", "Ltd." and "Bhd." or the full words; immunity: no description is deemed inadequate or incorrect for that use | Others: no-right; disability | `s 27(9) the use is lawful and does not make the description of the company inadequate or incorrect` |
| s 27(10) | Person: privilege to apply in the prescribed form for the reservation of a name | none: the application is decided under (12) and (12A) | `s 27(10) the person may apply to the Registrar for the reservation of the name` |
| s 27(11) | Registrar: bar against registering under s 19(3), or approving a change of name under s 28(2), unless the name has been reserved under (12) | Company: no-right to registration or change under an unreserved name | `s 27(11) the registration of the company, or the approval of the change of name, is barred` |
| s 27(12) | Registrar: power to approve a reservation only if satisfied that the application is in good faith and the name is registrable | Applicant: liability; no claim unless the Registrar is satisfied | `s 27(12) the Registrar may approve the application` |
| s 27(12A) | Registrar: duty to refuse a reservation for a company likely to be used for an unlawful purpose or contrary to national security | Applicant: no-right | `s 27(12A) the Registrar must refuse to approve the application` |
| s 27(12B) | Applicant: claim to the reservation of the proposed name from receipt of the application until 60 days after notice of approval (or a further 60 days), or until notice of refusal | Registrar: duty to reserve; others: disability to be registered under the name meanwhile (s 27(1)(c)) | `s 27(12B) the last day of the reservation`; `s 27(12B) the name is reserved on the day` |
| s 27(12C) | A person aggrieved by a refusal to approve or to extend: power to appeal to the Minister within 30 days after being informed; Minister: decision final | The Registrar's decision: liability to review; the appellant: disability to challenge the Minister's decision | `s 27(12C) the person may appeal to the Minister against the decision` |
| s 27(13) | Registrar: power, on a bona fide application during the reservation, to extend it for a further 60 days | Applicant: no claim to an extension | `s 27(13) the Registrar may extend the period for a further period of 60 days` |
| s 27(14) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 27(15) | none: a reservation "does not in itself entitle" the company to be registered by the name (the company has no right to the registration from it; the Registrar keeps the privilege to refuse) | none | `s 27(15) the reservation in itself entitles the company to be registered by the name` |
| s 27(16) | none: defines "registered business name" | none | `s 27(16) "registered business name" the name is a registered business name` |
| s 28(1) | Company: power to resolve by special resolution that its name be changed to a name that could be registered under s 27(1), (1A) or (1B) | Members: liability to the resolution | `s 28(1) the company may resolve that its name should be changed to the new name` |
| s 28(2) | Company: claim to registration under the new name and a notice of incorporation, on which the change of name becomes effective | Registrar: duty, once the Registrar approves the name | `s 28(2) the Registrar must register the company under the new name and issue the notice of incorporation`; `s 28(2) the change of name has become effective` |
| s 28(3) | Company: power to change its name by special resolution to a name not within paragraphs (a) to (e); Registrar: the power the text calls "the Registrar's power under subsection (3)" to direct a change (s 28(4)), granted in the words "if the Registrar so directs"; Minister: power to annul | Company: liability to the direction, and duty to change its name within 6 weeks of the direction (or a longer period the Registrar allows) unless the Minister annuls it | `s 28(3) the company may by special resolution change its name`; `s 28(3) the company must change its name within 6 weeks after the direction`; `s 28(3) the last day for compliance`; `s 28(3) the company has complied with the direction`; `s 28(3) the company must change its name within 6 weeks of the direction` |
| s 28(3AA) | Company: immunity from a direction on the ground that its name could not be registered without contravening s 27(1)(c) | Registrar: disability | `s 28(3AA) the Registrar is barred from directing a change of name under subsection (3) on the ground` |
| s 28(3A) | Any person: privilege to apply in writing for a direction | Registrar: barred from considering an application on the (3)(d) ground received more than 12 months after the change of name; the applicant: no-right to a decision then | `s 28(3A) the person may apply to the Registrar for a direction to the company`; `s 28(3A) the Registrar is barred from considering the application` |
| s 28(3B) | State: power to prosecute | Company and its officers: liability to a fine of up to $2,000 and a default penalty | `s 28(3B) the person is guilty of the offence`; `s 28(3B) the most the person may be sentenced to on conviction` |
| s 28(3C) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 28(3D) | A company aggrieved by a decision under (3): power to appeal to the Minister within 30 days after the decision; an applicant aggrieved by a refusal to direct: power to appeal within 30 days after being informed | The Registrar's decision: liability to review | `s 28(3D) the person may appeal to the Minister against the decision` |
| s 28(3DA) | Minister: immunity of the decision on an appeal (final) | Appellant: disability to reopen it | `s 28(3DA) the decision of the Minister on the appeal is final` |
| s 28(3E) | none for the individual: the Registrar and the Minister must accept as correct a Court's grant of an injunction | Registrar and Minister: duty | `s 28(3E) the Registrar or the Minister must accept as correct the decision of the Court to grant the injunction` |
| s 28(4) | A company incorporated under a corresponding previous written law whose name is unchanged since 29 December 1967: immunity from a direction, except with the Minister's approval | Registrar: disability | `s 28(4) the Registrar is barred from directing the company to change its name under subsection (3)` |
| s 28(5) | Company: claim, on application and fee, to a certificate confirming incorporation under the new name | Registrar: duty | `s 28(5) the Registrar must issue to the company a certificate confirming the incorporation under the new name` |
| s 28(6) | Company, and anyone with proceedings by or against it: immunity (identity, rights, obligations and proceedings are unaffected by a change of name) | Others: disability to treat the change as affecting them | `s 28(6) the change of name affects the matter`; `s 28(6) the legal proceedings may be continued or commenced by or against the company by its new name` |
| s 29(1) | Registrar: power, on proof of the stated purposes and finances, to approve that a proposed limited company be registered without "Limited" or "Berhad"; the company: power to be registered accordingly | Promoter: no claim to approval | `s 29(1) the Registrar may approve that the proposed limited company be registered without the word Limited or Berhad`; `s 29(1) the company may be registered without the word Limited or Berhad accordingly` |
| s 29(2) | Registrar: power, on proof of the four stated matters, to approve a change of name to one without "Limited" or "Berhad" | Company: liability; no claim to approval | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` |
| s 29(3) | Registrar: power to attach conditions to an approval, binding on the company, and to direct their insertion in the constitution; company: power to alter the constitution by special resolution to give effect to the direction | Company: liability to the conditions, and duty to insert them if directed (no time fixed) | `s 29(3) the conditions are binding on the company`; `s 29(3) the company must insert the conditions in its constitution if the Registrar so directs`; `s 29(3) the conditions must be inserted in the constitution of the company`; `s 29(3) the constitution may be altered by special resolution to give effect to the direction` |
| s 29(4) | Company whose constitution bars alteration except with the Minister's consent: power, with that consent, to alter any provision by special resolution; Minister: power of consent | Members: liability to the alteration | `s 29(4) the company may alter any provision of the constitution` |
| s 29(5) | Company: immunity from the Act's provisions on the use of "Limited" or "Berhad" while an approval is in force | Registrar: disability to require the word | `s 29(5) the company is exempted from complying with the provisions of this Act relating to the use of the word Limited or Berhad` |
| s 29(6) | Registrar: power to revoke an approval at any time, after written notice of intention and an opportunity to be heard, and to enter the word on revocation; company: claim to that notice and hearing | Company: liability to revocation, and loses the exemption on revocation; Registrar: duty to give notice and a hearing | `s 29(6) the Registrar may revoke the approval`; `s 29(6) before the revocation the Registrar must give the company written notice and afford it an opportunity to be heard`; `s 29(6) upon the revocation the Registrar must enter the word Limited or Berhad at the end of the name in the register`; `s 29(6) upon the revocation the company ceases to enjoy the exemption` |
| s 29(6A) | Registrar: power to revoke an approval where the company has ceased to satisfy the conditions of approval | Company: liability | `s 29(6A) the Registrar may revoke the approval` |
| s 29(7) | Company: power, after revocation, to alter its constitution by special resolution to remove a provision that it may be altered only with the Minister's consent | Members: liability | `s 29(7) the constitution may be altered by special resolution to remove the provision requiring the Minister's consent` |
| s 29(8) | Company (or the applicant for a proposed limited company): claim to notice of an approval | Registrar: duty | `s 29(8) the notice of the approval must be given to the person` |
| s 29(8A) | Promoter (decision under (1)) and company (decision under (2)): power to appeal to the Minister within 30 days after the notice under (8) | The Registrar's decision: liability to review | `s 29(8A) the person may appeal to the Minister against the decision` |
| s 29(9) | Company or proposed limited company: claim, on application and fee, to a certificate confirming the approval | Registrar: duty | `s 29(9) the Registrar must issue to the company a certificate confirming the approval` |
| s 29(10) | A limited company registered as a charity under the Charities Act 1994: immunity from s 29 (it does not apply to it) | Registrar: disability under s 29 | `s 29(10) section 29 applies to the company` |
| s 29(11), s 29(12), s 29(13) | A company with a Minister's approval, condition, reference or direction in force immediately before 3 January 2016: its standing is kept (read as the Registrar's) on or after that date | Registrar: liability to be treated as the maker; others: disability | `s 29(11) the approval or condition is treated as the Registrar's approval and condition`; `s 29(12) the reference to the Minister's approval is read as a reference to the Registrar`; `s 29(13) the reference to a direction of the Minister is read as a direction of the Registrar` |
| s 29A(1) | Charitable company: power to change its name to omit "Limited" or "Berhad" (despite s 28(1) and (2), subject to s 28(3) to (6)) | Members: liability | `s 29A(1) the charitable company may change its name to omit the word Limited or Berhad` |
| s 29A(2) | Registrar: claim that the charitable company alter its constitution to reflect the change and file the prescribed form with a copy of the special resolution | Charitable company: duty (no time fixed) | `s 29A(2)(a) the charitable company must alter its constitution to reflect the change of name`; `s 29A(2)(b) the charitable company must file the prescribed form with the Registrar and a copy of the special resolution`; `s 29A(2) the charitable company has met the requirements for the change of name` |
| s 29A(3) | Charitable company: claim, on receipt of the form, to registration of the name and a notice of incorporation | Registrar: duty | `s 29A(3) the Registrar must register the name of the charitable company with the omission and issue the notice of incorporation` |
| s 29A(4) | Charitable company: immunity, from issue of the notice, from the Act's provisions on the use of "Limited" or "Berhad" | Registrar: disability | `s 29A(4) the change of name has become effective and the charitable company is exempted` |
| s 29A(5) | Registrar: duty to re-enter the word when satisfied that the company has ceased to be a charitable company; the exemption ends on notice to the company | Company: liability; loses the exemption | `s 29A(5) the Registrar must enter the word Limited or Berhad at the end of the name of the company`; `s 29A(5) the exemption under subsection (4)(b) has ceased` |
| s 30(1) | Unlimited company (not previously a limited company that became unlimited) and limited company (not previously an unlimited company that became limited): power to change status | Members: liability to the change | `s 30(1)(a) the unlimited company may convert to a limited company`; `s 30(1)(b) the limited company may convert to an unlimited company` |
| s 30(2) | Company: claim, on application and lodging of the prescribed documents, to a notice of incorporation appropriate to the change of status; it is deemed to have the new status on issue | Registrar: duty | `s 30(2) the Registrar must issue to the company a notice of incorporation appropriate to the change of status`; `s 30(2) the company is deemed to be a company having the status specified in the notice` |
| s 30(3) | none: no holder or bearer is named (notice of the change is to be published "in such manner (if any)" as the Registrar directs) | none | `s 30(3) the notice of the change of status must be published` |
| s 30(3A) | Company: claim, on application and fee, to a certificate confirming the incorporation with the new status | Registrar: duty | `s 30(3A) the Registrar must issue to the company a certificate confirming the incorporation with the new status` |
| s 30(4) | none: defines the prescribed documents | none | `s 30(4) the documents lodged are the prescribed documents` |
| s 30(4)(a)(iii) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 30(4)(a)(iv) | none: the text shows [Deleted by Act 36 of 2014] | none |  |
| s 30(5) | Company: immunity from s 26(2) to (6) for an application under s 30 | Registrar: disability to apply them | `s 30(5) section 26(2) to (6) applies to the matter` |
| s 30(6) | none: timing rule (the special resolution takes effect only on issue of the notice of incorporation) | none | `s 30(6) the special resolution has taken effect` |
| s 30(7) | Holders of enough shares, members or debentures: power to apply to the Court under s 33 (with the modifications the text leaves unlisted) | Company: liability to the Court's cancellation or confirmation | `s 30(7) the provision of section 33 applies to the special resolution` |
| s 30(8) | Company and anyone with proceedings by or against it: immunity (no new entity; identity, property, rights, obligations and proceedings unaffected) | Others: disability | `s 30(8) the change in status operates on the matter`; `s 30(8) the legal proceedings may be continued or commenced by or against the company after the change in its status` |
| s 31(1) | Public company having a share capital: power to convert to a private company by lodging the documents | Members: liability to the conversion | `s 31(1) the public company may convert to a private company by lodging` |
| s 31(2) | Private company, subject to its constitution: power to convert to a public company by lodging the documents | Members: liability to the conversion | `s 31(2) the private company may convert to a public company by lodging`; `s 31(2) the restrictions and limitations referred to in section 18(1) cease to form part of the constitution` |
| s 31(3) | none: effect rule (on compliance and on issue of the altered notice of incorporation, the company becomes private or public) | none | `s 31(3) the company has become a private company`; `s 31(3) the company has become a public company` |
| s 31(3A) | Registrar: claim to a list of persons holding shares, within 14 days after the notice of incorporation | The converted public company: duty (regulative rule with a deadline) | `s 31(3A) the company has complied with the duty to lodge the list of persons holding shares`; `s 31(3A) the company must lodge the list of persons holding shares within 14 days` |
| s 31(4) | Company and anyone with proceedings by or against it: immunity from the conversion (identity, rights, obligations and proceedings unaffected) | Others: disability | `s 31(4) the conversion affects the matter`; `s 31(4) the legal proceedings may be continued or commenced by or against the company after the conversion` |
| s 31(5) | Company: claim, on application and fee, to a certificate confirming the incorporation with the new status | Registrar: duty | `s 31(5) the Registrar must issue to the company a certificate confirming the incorporation with the new status` |
| s 32(1) | none: the text shows [Deleted by Act 5 of 2004] | none |  |
| s 32(2) | Registrar: power, by notice served on the company, to determine that on the specified date it ceased to be a private company (default in a s 18(1)(b) limitation, alteration dropping the s 18(1) restrictions, or no share capital) | Company: liability to the determination | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` |
| s 32(2)(b) | none: the text shows [Deleted by Act 5 of 2004] | none |  |
| s 32(3)(a), s 32(3)(b) | none: effect rules (a public company from the date specified; name deemed changed on that date) | none | `s 32(3)(a) the company is a public company on and from the date specified`; `s 32(3)(b) the company is deemed to have changed its name by the omission of the word Private or Sendirian` |
| s 32(3)(c) | Registrar: claim to a statement in lieu of prospectus and a declaration, within 14 days after the date of the order or notice | Company: duty (regulative rule with a deadline) | `s 32(3)(c) the company has complied with the duty to lodge the statement in lieu of prospectus and the declaration`; `s 32(3)(c) the company must lodge the statement in lieu of prospectus and the declaration within 14 days` |
| s 32(4) | Court: power, where a default or alteration was accidental, due to inadvertence or other sufficient cause, or relief is just and equitable, to determine on terms that the company has not ceased to be private | Company: liability to the Court's terms; no claim to relief | `s 32(4) the Court may determine that the company has not ceased to be a private company` |
| s 32(5) | Court: power to give permission | Company that became public by a determination: disability to convert to private without that permission | `s 32(5) the company may not convert to a private company` |
| s 32(6) | State: power to prosecute | Company and each officer in default under (3)(c): liability to a fine of up to $2,000 and a default penalty | `s 32(6) the person is guilty of the offence`; `s 32(6) the most the person may be sentenced to on conviction` |
| s 32(7) | none: the text shows [Deleted by Act 5 of 2004] | none |  |
| s 32(8) | State: power to prosecute | Company and each officer in default of a s 18(1) restriction: liability to a fine of up to $5,000 or imprisonment of up to 12 months | `s 32(8) the person is guilty of the offence`; `s 32(8) the most the person may be sentenced to on conviction` |
| s 33(1) | Company: power to alter its objects by special resolution | Members: liability to the alteration | `s 33(1) the company may alter the provisions of its constitution with respect to its objects by the resolution` |
| s 33(2), s 33(3) | Members, trustees for debenture holders (or the debenture holders of a class that has none): claim to 21 days' written notice of the intention to propose the special resolution | Company: duty (regulative rule with a deadline) | `s 33(2) the company has given the notice the subsection requires`; `s 33(2) the company must give 21 days' written notice`; `s 33(3) the notice must be given to the person` |
| s 33(4) | Court: power to dispense with the notice for a person or class | The person or class: loses the claim to notice | `s 33(4) the Court may dispense with the notice for the person or class of persons` |
| s 33(5) | Holders of not less than 5% of the issued shares (or of the members) or of 5% in nominal value of the debentures: power to apply for cancellation; the alteration does not have effect except so far as the Court confirms it | Company: liability | `s 33(5)(a) the applicants hold enough of the shares, or are enough of the members`; `s 33(5)(b) the applicants hold enough in nominal value of the company's debentures`; `s 33(5) the alteration does not have effect except so far as the Court confirms it` |
| s 33(5A) | none: counting rule (treasury shares are disregarded) | none | `s 33(5A) the number of issued shares counted for subsection (5)` |
| s 33(6) | Applicants: power to apply within 21 days after the resolution, through persons they appoint in writing | Company: liability | `s 33(6) the application is made in time`; `s 33(6) the application may be made on behalf of the persons entitled by the applicants` |
| s 33(7) | Court: duty to have regard to the rights and interests of members and creditors; powers to adjourn, direct and order, and to cancel or confirm the alteration wholly or in part | Applicants and company: liability to the order | `s 33(7)(a) the Court must have regard to the rights and interests of the members and of the creditors`; `s 33(7)(b) the Court may adjourn the proceedings`; `s 33(7)(c) the Court may give the directions and make the orders`; `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` |
| s 33(8) | The text names no holder: a copy of a resolution altering the objects must not be lodged before 21 days after the resolution has passed, or if an application to the Court has been made, before the Court has determined it, whichever is later | Company: disability | `s 33(8) lodging the copy of the resolution on the day is barred`; `s 33(8) the first day on which the copy may be lodged` |
| s 33(9) | Registrar: claim to lodging of the copy within 14 days after the 21 days (or, with a copy of the order, after the Court's decision) | Company: duty (regulative rule with a deadline) | `s 33(9) the company has complied with the duty to lodge the copy of the resolution`; `s 33(9) the company must lodge a copy of the resolution within 14 days` |
| s 33(10) | none: effect rule (the alteration of the objects takes effect on compliance with (9)) | none | `s 33(10) the alteration of the objects takes effect` |
| s 33(11) | none: definition (alteration includes removal) | none | `s 33(11) the thing is within the word alteration` |
| s 34(1), s 34(2) | Company: power to amend its constitution by special resolution to remove a provision referred to in s 10(1) of the Residential Property Act 1976; a provision that it may not be altered except under that Act ceases to have effect | Members: liability to the amendment | `s 34(1) the company may amend its constitution to remove the provision`; `s 34(2)(a) the provision has ceased to have effect`; `s 34(2)(b) the company may amend its constitution to remove that provision` |
| s 35(1) | The text names no holder: the constitution must contain the regulations for the company | Company: duty | `s 35(1) the constitution of the company must contain the regulations for the company` |
| s 35(2) | Company limited by shares incorporated before 3 January 2016: immunity from (1) | Registrar and others: disability | `s 35(2) subsection (1) does not apply to the company` |
| s 35(3) | none: effect rule (regulations in force before 3 January 2016 are deemed the company's regulations until the constitution is amended) | none | `s 35(3) the regulations are deemed to be the regulations for the company contained in its constitution` |
| s 36(1) | none: defines "specified companies" | none | `s 36(1) the company is a specified company` |
| s 36(2) | none for the individual: Minister's power to prescribe different model constitutions for different descriptions of specified company | none |  |
| s 37(1), s 37(2), s 37(3) | Specified company: power to adopt the whole or part of the model constitution, by reference to its title, as in force at adoption or as in force from time to time | Members: liability to the adoption | `s 37(1) the specified company may adopt the whole or any part of the model constitution as its constitution`; `s 37(2) the specified company may adopt the whole model constitution by reference to its title`; `s 37(3) the specified company may choose`; `s 37(3)(b) the model constitution for the time being in force is, so far as applicable, the constitution of the specified company` |
| s 37(4) | Registrar: claim to a copy of the constitution, in accordance with s 19(1), where the company adopts only part of the model, adds provisions or includes object clauses | Specified company: duty (the time is fixed by s 19(1), outside this range) | `s 37(4) a copy of the constitution of the specified company must be submitted to the Registrar`; `s 37(4) the specified company must submit a copy of its constitution to the Registrar` |
| s 38(1) | Company limited by guarantee: immunity from provisions giving a person a right to participate in the divisible profits otherwise than as a member (void) | Anyone who would rely on such a provision: disability | `s 38(1) the provision is void` |
| s 38(2) | none: deeming rule (a provision dividing the undertaking into shares or interests is treated as a provision for a share capital) | none | `s 38(2) the provision is treated as a provision for a share capital` |
| s 39(1) | Company and members: claim against each other to the constitution's observance (it binds as if signed and sealed by each member) | Members and company: duty | `s 39(1) the constitution binds the person to the same extent as if signed and sealed by each member` |
| s 39(2) | Company: claim to money payable by a member under the constitution (a debt) | Member: duty | `s 39(2) the money is a debt due from the member to the company` |
| s 39(3) | Member who has not agreed in writing: immunity from an alteration made after joining that requires more shares or increases liability to pay the company | Company: disability | `s 39(3) the member is bound by the alteration` |
| s 40(1) | Member who requires it: claim to a copy of the constitution (if any) on payment of $5 or less | Company: duty (no time fixed) | `s 40(1) the sum the member must pay for a copy of the constitution`; `s 40(1) the company must send the member a copy of the constitution`; `s 40(1) the company must send a copy of the constitution to the member who requires it` |
| s 40(2) | The text names no holder: after an alteration, a copy of the constitution must not be issued unless it is in accordance with the alteration or the order or resolution is annexed and the clauses affected are indicated | Company: duty not to issue otherwise | `s 40(2) the company must not issue the copy of the constitution` |
| s 40(3) | none: the text shows [Omitted in 2006 Revised Edition] | none |  |
| s 40(4) | State: power to prosecute | Company and each officer in default: liability to an offence (the section names no penalty) | `s 40(4) the person is guilty of the offence` |
| s 41(1) | Company: power to ratify a pre-incorporation contract or transaction; on ratification it is bound by and entitled to the benefit of it | The other party: liability | `s 41(1) the contract or transaction may be ratified by the company`; `s 41(1) the company is bound by and entitled to the benefit of the contract or transaction` |
| s 41(2) | The other party: claim against the person who purported to act, before ratification and absent express agreement to the contrary; that person: claim to the benefit of the contract | That person: duty (personally bound); the other party: duty to give the benefit | `s 41(2) the person is personally bound by the contract or transaction and entitled to the benefit of it` |
| s 41(3) | Corporation: power to contract in writing under the common seal, in writing signed, or by parol, as private persons could; the contract binds it, its successors and all other parties and may be varied or discharged in the manner authorised | Other parties: liability | `s 41(3) the contract may be made on behalf of the corporation in the way`; `s 41(3) the contract is effectual in law and binds the corporation and its successors and all other parties`; `s 41(3) the contract may be varied or discharged` |
| s 41(4) | Corporation: privilege to authenticate a document or proceeding by an authorised officer's signature without the common seal | Others: no-right to insist on the seal | `s 41(4) the document or proceeding may be signed by an authorised officer of the corporation`; `s 41(4) the document or proceeding needs to be under the common seal` |
| s 41(5) | Corporation: power, by writing under its common seal, to empower an agent or attorney to execute deeds binding it | Agent and those dealing with the agent: liability to the deed | `s 41(5) the corporation may empower the person as its agent or attorney to execute deeds on its behalf`; `s 41(5) the deed binds the corporation and has the same effect as if it were under its common seal` |
| s 41(6) | Person dealing with the agent or attorney: immunity (the authority continues for the period mentioned, or until notice of revocation or determination) | Corporation: disability | `s 41(6) the authority of the agent or attorney continues as between the corporation and the person dealing with the agent or attorney` |
| s 41(7) | Corporation whose objects require or comprise business outside Singapore, if authorised by its constitution: privilege to have an official seal for use abroad; the text names no holder of the claim to the certificate | Person affixing the official seal: duty to certify in writing the date and place (no time fixed); others: no-right | `s 41(7) the corporation may have for use in a place outside Singapore an official seal`; `s 41(7) the official seal is as the subsection requires`; `s 41(7) the person affixing the official seal has certified the date and the place`; `s 41(7) the person affixing the official seal must certify the date and the place` |
| s 41(8), s 41(9) | Corporation and those relying on an instrument executed by its donee of a power or agent: immunity (the instrument is as valid as if the authority had been under seal; also for instruments executed before 15 May 1987) | Others: disability to impeach it | `s 41(8) the instrument under seal is as valid as if the authority had been under seal`; `s 41(9) the day 15 May 1987`; `s 41(9) subsection (8) applies to the instrument` |
| s 41A | Company: privilege to have or not have a common seal; ss 41B and 41C apply either way | Others: no-right | `s 41A(1) the company may have a common seal`; `s 41A(1) the company needs to have a common seal`; `s 41A(2) sections 41B and 41C apply to the company` |
| s 41B(1), s 41B(2) | Company: power to execute a deed without affixing a common seal, by signature of a director and a secretary, of at least 2 directors, or of a director before an attesting witness, with the same effect as under the common seal | Other parties: liability | `s 41B(1) the company may execute the document without affixing a common seal`; `s 41B(2) the document has the same effect as if it were executed under the common seal of the company` |
| s 41B(3), s 41B(4) | none: s 41B(3) a signing rule for a person signing for more than one company (signature must be separate in each capacity); s 41B(4) extends s 41B to a document executed in another person's name | none | `s 41B(3) the document is considered to be signed by the person for the purposes of subsection (1) or (2)`; `s 41B(4) section 41B applies to the document` |
| s 41C | Company: immunity of a document signed as s 41B(1)(a), (b) or (c) and (3) provide from any written law or rule of law requiring the common seal | Others: disability | `s 41C the document satisfies the written law or rule of law` |
| s 42 | none: the text shows [Repealed by Act 5 of 2004] | none |  |
| s 42A(1) | none: scope (a company or foreign company registered under the Charities Act 1994, or with a charitable purpose connected with persons, events or objects outside Singapore) | none | `s 42A(1) section 42A applies to the company or foreign company` |
| s 42A(2) | Court (winding up) and Registrar (striking off a foreign company's name): power | Convicted company or foreign company: liability (it "may be liable") | `s 42A(2) the company or foreign company is deemed to be used for purposes prejudicial to public welfare`; `s 42A(2) the company may be liable to be wound up by the Court under section 125(1)(n) of the Insolvency, Restructuring and Dissolution Act 2018`; `s 42A(2) the foreign company may be liable to have its name struck off the register by the Registrar under section 377(8)` |
| s 42A(3) | none: defines "charitable purpose" | none | `s 42A(3) "charitable purpose" the purpose or object is a charitable purpose` |

## Marginal readings for a lawyer (sgi)

The brief's two status-quo readings are taken as the status quo, and every branch resting on one is listed here with the other reading; the sites are the rows of the fork tables above.

- **Reading (a): a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (and a flat negative counts as the text saying no).** 55 functions answer `JUST FALSE` on it, in the entries F-I4, F-I5, F-I10, F-I11, F-I21, F-I22, F-I24, F-I28, F-I29, and the duty of s 33(7)(a) in F-I14.
  The other reading answers `NOTHING` at each, because "if A then B" does not itself say "if not A then not B".
- **Reading (b): a prohibition or grant limited by its own wording does not give the text's no.** 54 functions answer `NOTHING` on it (counting each function once, and not again where it is also in (a)), in the entries F-I1, F-I2, F-I3, F-I6, F-I9, F-I13, F-I15, F-I19, F-I23, F-I26, F-I32, and the powers of s 33(7)(b) to (d) in F-I14.
  The other reading answers `JUST FALSE` at each.
- **Decided case by case under the Guide's line 95** (an "unless" or "except" once it is met; a bare "must" not done): 15 functions in the entries F-I7, F-I18, F-I30, F-I31. The other reading is in each entry.
- **Readings of the text that are not about FALSE and NOTHING** (a count of days, "and" against "or", a reference outside the range): 5 functions in the entries F-I8, F-I12, F-I16, F-I17, F-I20, F-I25, F-I27.

The sites that fit the Guide's lines least well, and so the ones to read first:

- F-I22 (s 29(5), s 35(3), s 41(6)): the periods ruling's item (a) speaks of "a period the text fixes in its own words", and these end on an event (an approval revoked, an amendment made, a notice given), not on a stated number of days.
- F-I23 (s 29(6)): the precondition of a revocation is phrased as the Registrar's duty, with no "only after" (the fork line itself says "marginal").
- F-I30 (s 41(2)): "Prior to ratification" ends on an event, and s 41(1) does not say that the person is released.
- F-I24 and F-I28 (s 29(11) to (13), s 32(3)(a) and (b)): a date the text fixes (3 January 2016; "the date specified"), where the text says nothing of the time before it.

### Reading a result: FALSE and NOTHING (sgi)

In this part, `JUST TRUE` is yes: the test of the section is met on the facts given.
`JUST FALSE` is the text's own no: a "means" definition the facts do not satisfy; a condition the text introduces with "if", "only if", "unless", "while", "until", "where", "when" or "upon" that fails, where the section's own question is a duty, a bar or a status (not a permission); a flat negative ("does not", "is not bound"); a period or a date the text fixes in its own words that has not begun or has run out; or the offence provision's own question when an element is unmet.
`NOTHING` is "the text does not say", and it carries one of six tags in the code (`-- NOTHING-kind (...)`): silent, list not closed, includes, undefined term, points outside the text, or limited by its own wording.
In this part it usually means one of three things: a permission ("may") whose conditions are not met, so the text names no outcome; an exception ("unless", "except", "in the absence of") that is met, after which the text is silent; or a case the section does not address (a resolution of another kind, another person, another decision).
A caller never turns `NOTHING` into `FALSE`: in a seat question `NOTHING` is the answer "the Act, in these sections, does not say", which is not "no".

## Seams (sgi)

**Given.** PLAN.md section 4, table A, asks this part to answer the keel's `s 4(1) "private company"` (`sg-definitions.l4`), which takes three facts: incorporated as private by s 18, converted under s 31, ceased to be private under s 31 or 32.
This part answers two of them, in `sgi-conversion.l4`; the first is for the part that encodes s 18.

| the keel's input | answered by | how |
| --- | --- | --- |
| `the company was converted into a private company pursuant to section 31(1)` | `s 31(3) the company has become a private company` | `JUST TRUE` |
| `the company has ceased to be a private company under section 31 or 32` | `s 31(3) the company has become a public company` or `s 32(3)(a) the company is a public company on and from the date specified` | `JUST TRUE` of either |

**Taken from the keel and the core** (the part imports them): the functions `s 4(1) "limited company"`, `"unlimited company"`, `"company limited by shares"` and `"company limited by guarantee"` (`sg-definitions.l4`); the types `Liability of members`, `Kind of resolution`, `Party` and `Penalty` and the constant `the day 3 January 2016` (`sg-core.l4`); and the `period:` functions (`sg-periods.l4`).

**Passed through.** The keel's `s 4(1) "limited company"` takes the input `the period of 2 years specified in section 17(6) has expired` (table A: the answer is for the part that encodes s 17(6)).
`sgi-conversion`, `sgi-names` and `sgi-name-changes` take it as an input of the same name, with the same type, and pass it on.

**Taken as plain inputs: facts of other sections and other Acts that no part of this range answers.**
Tables A and B of the plan do not list these, so each is a seam the plan lacks; the part that encodes the section can answer it under the same name.

| input | in |
| --- | --- |
| `the notice is in writing and is given by post or by electronic communications in accordance with section 387A or 387C` | sgi-objects |
| `the constitution contains a provision referred to in section 10(1) of the Residential Property Act 1976 as in force immediately before 31 March 2006` | sgi-objects |
| `the constitution contains a provision to the effect that it must not be altered to remove any of the provisions referred to in section 10(1) of the Residential Property Act 1976 except in accordance with the requirements of that Act` | sgi-objects |
| `the name is identical to the name of a foreign company registered under Division 2 of Part 11` | sgi-names |
| `notice was lodged under section 377(1) that the foreign company has ceased to have a place of business in Singapore or ceased to carry on business in Singapore` | sgi-names |
| `the name of the foreign company was struck off the register under section 377(8), (9) or (10)` | sgi-names |
| `notice was lodged under section 19(1) of the Limited Partnerships Act 2008 that the limited partnership ceased to carry on business in Singapore` | sgi-names |
| `the Registrar is satisfied that the company has been registered by a name the use of which has been restrained by an injunction granted under the Trade Marks Act 1998` | sgi-names |
| `the name is a registered business name as section 2(1) of the Business Names Registration Act 2014 gives that meaning` | sgi-names |
| `the use of the name of the company has been restrained by an injunction granted under the Trade Marks Act 1998` | sgi-name-changes |
| `the company is registered as a charity under the Charities Act 1994` | sgi-name-changes |
| `the special resolution alters the provisions of its constitution so far as is necessary to impose the restrictions and limitations referred to in section 18(1)` | sgi-conversion |
| `the company lodges a declaration in the prescribed form verifying that section 61(2)(b) has been complied with` | sgi-conversion |
| `default has been made in relation to a private company in complying with a limitation of a kind specified in section 18(1)(b) that is included or deemed to be included in its constitution` | sgi-conversion |
| `the constitution of the private company has been so altered that it no longer includes restrictions or limitations of the kinds specified in section 18(1)` | sgi-conversion |
| `default is made in relation to a private company in complying with a restriction or limitation of a kind specified in section 18(1) that is included or deemed to be included in its constitution` | sgi-conversion |
| `the company or foreign company is registered under the Charities Act 1994` | sgi-contracts-seal |
| `the company or foreign company is convicted of an offence under the Charities Act 1994 or any regulations made thereunder` | sgi-contracts-seal |
| `the company is convicted of an offence under the Charities Act 1994 or any regulations made thereunder` | sgi-contracts-seal |
| `the foreign company is convicted of an offence under the Charities Act 1994 or any regulations made thereunder` | sgi-contracts-seal |

That is 20 inputs.
The other Acts named (the Charities Act 1994, the Trade Marks Act 1998, the Limited Partnerships Act 2008, the Business Names Registration Act 2014, the Residential Property Act 1976) are not sources here, so each of their facts is a supplied fact.

## Split sites (sgi)

The brief asks for the count of the sites of two kinds that the Guide leaves open, each with the answer taken and a pointer to its fork line.

### (i) An unmet element of an offence or a contravention: 6 sites, `JUST FALSE` at all 6

Fork entry F-I10.
The answer relies on the grant ruling of 2026-11-12, limit 2 (line 98): "keep `JUST FALSE` where the text closes the gate itself (\"only if\", \"only where\", \"may not ... unless\", a list closed with \"only\"), and for a bar, a duty or the provision's own question" (the offence provision's own question), and on N2 (line 92): "flat negatives count as a no".
The other reading is `NOTHING`: the text does not say what the position is of one whose conduct is not within the offence.

| provision | function |
| --- | --- |
| s 26(2A) | `s 26(2A) the person is guilty of the offence` |
| s 27(2B) | `s 27(2B) the person is guilty of the offence` |
| s 28(3B) | `s 28(3B) the person is guilty of the offence` |
| s 32(6) | `s 32(6) the person is guilty of the offence` |
| s 32(8) | `s 32(8) the person is guilty of the offence` |
| s 40(4) | `s 40(4) the person is guilty of the offence` |

### (ii) A "may" gated by "where", "when", "upon", "on application" or "with the consent of": 12 sites, `NOTHING` at all 12; one more site, a duty, answers `JUST FALSE`

The answer relies on the grant ruling of 2026-11-12, limit 1 (line 97): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power (\"may\", \"is permitted to\", \"has power to\") whose `if` gate failed", and on the Guide's "In short" (line 87): `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit".
The other reading is `JUST FALSE`, from the periods ruling of 2026-11-05, item (b) (line 93): "a \"where ...\" condition: when it fails the answer is `JUST FALSE`", with "when", "upon" and "whenever" counting as "where" (line 94, item (c)).
The grant ruling's limit 3 (line 99) says to list these and not to change them; they are listed here and in the fork entries F-I6, F-I14, F-I15 and F-I19.

| fork entry | provision | function | answer taken |
| --- | --- | --- | --- |
| F-I6 | s 25C(7) | `s 25C(7) the court may make an order affirming, severing or setting aside the transaction` | `NOTHING` |
| F-I15 | s 34(1) | `s 34(1) the company may amend its constitution to remove the provision` | `NOTHING` |
| F-I15 | s 34(2)(b) | `s 34(2)(b) the company may amend its constitution to remove that provision` | `NOTHING` |
| F-I19 | s 27(2) | `s 27(2) the Registrar may direct the company to change its name` | `NOTHING` |
| F-I19 | s 29(1) | `s 29(1) the Registrar may approve that the proposed limited company be registered without the word Limited or Berhad` | `NOTHING` |
| F-I19 | s 29(2) | `s 29(2) the Registrar may grant approval to the company to change its name to a name without the word Limited or Berhad` | `NOTHING` |
| F-I19 | s 29(4) | `s 29(4) the company may alter any provision of the constitution` | `NOTHING` |
| F-I19 | s 32(2) | `s 32(2) the Registrar may by notice served on the company determine that it ceased to be a private company` | `NOTHING` |
| F-I19 | s 32(4) | `s 32(4) the Court may determine that the company has not ceased to be a private company` | `NOTHING` |
| F-I14 | s 33(7)(b) | `s 33(7)(b) the Court may adjourn the proceedings` | `NOTHING` |
| F-I14 | s 33(7)(c) | `s 33(7)(c) the Court may give the directions and make the orders` | `NOTHING` |
| F-I14 | s 33(7)(d) | `s 33(7)(d) the Court may make an order cancelling the alteration or confirming it, wholly or in part` | `NOTHING` |
| F-I14 | s 33(7)(a) | `s 33(7)(a) the Court must have regard to the rights and interests of the members and of the creditors` | `JUST FALSE` (a duty gated by "On the application") |

Gated "may" functions that the count leaves out, because the gate is an "if" or a plain condition and not a where, when, upon, application or consent, are the sites of F-I2 and F-I13.

## Rules with no breach path (sgi)

These 8 regulative rules have a `MUST` with no time limit and no stated consequence, so no trace can show them breached: a late action still reads `FULFILLED`.
Each has a trace that reaches `FULFILLED` and one that stays `RESIDUAL`, and none has a `BREACH` trace.

- s 25C(4)(a): `s 25C(4)(a) the person liable under subsection (4) must account to the company for any gain`
- s 25C(4)(b): `s 25C(4)(b) the person liable under subsection (4) must indemnify the company for any loss or damage`
- s 29(3): `s 29(3) the company must insert the conditions in its constitution if the Registrar so directs`
- s 29A(2)(a): `s 29A(2)(a) the charitable company must alter its constitution to reflect the change of name`
- s 29A(2)(b): `s 29A(2)(b) the charitable company must file the prescribed form with the Registrar and a copy of the special resolution`
- s 37(4): `s 37(4) the specified company must submit a copy of its constitution to the Registrar`
- s 40(1): `s 40(1) the company must send a copy of the constitution to the member who requires it`
- s 41(7): `s 41(7) the person affixing the official seal must certify the date and the place`

The other 7 regulative rules have a deadline, and each has traces that reach `BREACH`: s 26(2), s 33(2), s 33(9), s 27(2), s 28(3), s 31(3A), s 32(3)(c).
Across the tests files there are 43 traces (15 `FULFILLED`, 14 `BREACH`, 14 `RESIDUAL`), each carrying an `-- EXPECT` comment, and `work/traces.py` compared every one with its expectation on both builds.

## Compared with the earlier pass

`inputs/NAIVE-EVIDENCE/` holds two files, `coa-formation-shares-buyback.l4` and its cases, written for one scenario: a private company is incorporated, shares are issued to an investor, the investor's holding is a substantial shareholding and a significant interest, a selective buy-back follows, and a company limited by guarantee is incorporated.
Its header lists the sections it reads: ss 17 to 22, 38(1), 63, 76B to 76F, 79 to 84, 145, 146, 157, 161, 171, 184 and 386AB to 386AF.
One provision of this range is among them, s 38(1).

The earlier pass has a plain BOOLEAN, `the provision is void under section 38(1)` (line 585 of its file), that is true when the company is limited by guarantee and the provision gives a right to profits otherwise than as a member, and false otherwise.
This part's `s 38(1) the provision is void` (`sgi-constitution.l4`) is `JUST TRUE` in that case and `NOTHING` otherwise, because the subsection voids provisions of that kind in that kind of company and says nothing of any other; this is the fork entry F-I32, which names the readings and the text that licenses each.
The earlier pass's cases assert only the first row below (line 483 of its cases file); the three rows that differ are asserted here in `sgi-tests-constitution.l4`.

| the company is limited by guarantee | the provision gives a right to profits otherwise than as a member | earlier pass | this part | differs |
| --- | --- | --- | --- | --- |
| yes | yes | TRUE | `JUST TRUE` | no |
| yes | no | FALSE | `NOTHING` | yes |
| no | yes | FALSE | `NOTHING` | yes |
| no | no | FALSE | `NOTHING` | yes |

The earlier pass also encodes s 18(1), which is outside this range; its conditions are the facts that `s 31(1)(a)(ii)` and `s 32(2)` take as inputs here (section "Seams"), so there is no case to compare.

## What the text turns out to say

1. s 27(1B)(a) joins its two limbs, (i) a cessation notice with at least 3 months passed and (ii) a name struck off with at least 6 years passed, with "and", and the next paragraph with "or" (lines 4778-4804).
   The literal reading needs both limbs; this is F-I16.
2. s 27(2A) bars the Registrar from considering an application on the (2)(b) ground, "so nearly resembles", unless it is received within 12 months from the date of incorporation (lines 4839-4844).
   s 28(3A) does the same for the (3)(d) ground within 12 months from the date of change of name (lines 5068-5073).
   Neither names a time limit for the other grounds.
3. s 27(2) gives the Registrar the power to direct a change of name in the words "the Registrar may direct" (lines 4832-4835).
   s 28(3) never says "may direct": it says the company "if the Registrar so directs, must so change it" (lines 5050-5058), and subsections (3A), (3AA) and (4) then speak of a direction "under subsection (3)" and of "the Registrar's power under subsection (3)" (lines 5068-5070, 5062-5064, 5118-5120).
   The company's duty to comply within 6 weeks is therefore stated twice, once in each section, and is encoded twice (`s 27(2)` and `s 28(3)`).
4. s 28(3AA) bars a direction on the s 27(1)(c) ground, and s 28(4) bars a direction against the name of a company incorporated under a corresponding previous written law and not changed since 29 December 1967, except with the Minister's approval (lines 5062-5064, 5116-5120).
5. s 29(6) states the Registrar's duty to enter the word "Limited" or "Berhad" on revocation first, and then adds that "before the approval is so revoked" the Registrar must give written notice and an opportunity to be heard (lines 5209-5216).
   Both are encoded; the second is a precondition phrased as a duty, not as "only after" (F-I23).
6. s 29(11) to (13) read the Minister's former approvals, conditions, references and directions as the Registrar's "on or after" 3 January 2016 (lines 5267-5292) and say nothing of the time before (F-I24).
7. s 30(3) leaves open whether notice of a change of status must be published when the Registrar directs no manner: "in such manner (if any) as the Registrar may direct" (lines 5383-5385; F-I26).
8. s 30(2) makes the lodging of the prescribed documents "subject to section 33(8) and (9) as applied by subsection (7)" (lines 5367-5372), and s 30(5) excludes s 26(2) to (6) (lines 5444-5446).
9. s 32(2) gives only the Registrar the power to determine, by notice, that a company ceased to be private (lines 5559-5580).
   s 32(3) speaks of the Court or the Registrar determining, and of "the order or the notice" (lines 5584-5589, 5596-5597).
   The only Court determination in the range is in s 32(4), and it is a determination that the company has not ceased to be private (lines 5604-5609).
   The functions take "the Court or the Registrar has determined" as one plain input.
10. s 32(3)(a) says the company "is deemed to have been a public company on and from the date specified in the order or notice" (lines 5587-5589): the status is tied to that date (F-I28).
11. The offences differ in their penalties: s 26(2A) a fine of up to $1,000 and a default penalty (lines 4587-4590); ss 27(2B), 28(3B) and 32(6) up to $2,000 and a default penalty (lines 4846-4853, 5077-5080, 5620-5623); s 32(8) up to $5,000 or up to 12 months' imprisonment, with no default penalty (lines 5627-5633).
12. s 27(12B)(a) lets the Registrar extend a reservation by "such further period of 60 days" on an application made in good faith, and s 27(13) by "a further period of 60 days" where the Registrar is satisfied of the bona fides (lines 4963-4967, 4988-4991).
   Neither says whether the extension can be made more than once; the number of 60-day periods is a plain input (F-I20).
13. s 34(2)(a) says the provision "ceases to have effect as from that date", and the only date in the subsection is 31 March 2006 (lines 5750-5756); the function reads "that date" as 31 March 2006.
14. s 35(2) takes a company limited by shares incorporated before 3 January 2016 out of s 35(1).
   s 35(3) then deems regulations in force for a company immediately before that date to be the regulations in its constitution "until such time as the constitution of the company is amended to replace or amend those regulations" (lines 5773-5786).
15. s 37(4) requires a copy of the constitution to be submitted "in accordance with section 19(1)" in three cases and gives no time of its own (lines 5839-5849); the time is in a part of the Act outside this range.
16. s 39(3) protects a member who has not agreed in writing from an alteration, made after the member became a member, that requires more shares or increases the member's liability to pay (lines 5892-5900); it limits who is bound, not the company's power to alter.
17. s 40(4) makes default in complying with s 40 an offence but names no penalty (lines 5931-5933), and s 40(3) reads "[Omitted in 2006 Revised Edition]" (line 5929); no penalty function is written for s 40(4).
18. s 41(2) makes the person who purported to act for a company before its formation personally bound, "Prior to ratification" and "in the absence of express agreement to the contrary" (lines 5945-5948); the text does not say what happens to that liability on ratification (F-I30).
19. s 41B(1) lets a company execute a deed by (a) a director and a secretary, (b) at least 2 directors, or (c) a director in the presence of a witness who attests the signature (lines 6052-6066).
   The text does not say whether one individual who is both a director and the secretary can sign under (a) alone; the function takes the number of directors who sign and whether a secretary signs as two separate facts.
20. s 42A(2) says a convicted company or foreign company is deemed to be used for purposes prejudicial to public welfare and "may be liable" to be wound up or struck off (lines 6119-6127): the text says only that it may be liable to the step, and does not order the step.

## What the stable binary does not accept (sgi)

Each item was run against the stable build 1.6.110 on 2026-11-18, in a scratch file.
Loud failures name the error code; the silent one is listed first.

- **Silent at the definition: two top-level functions of the same name and different result types** (a `MAYBE BOOLEAN` and a `NUMBER` in the probe) are both accepted with no message.
  The failure comes at the first call, `check/ambiguous-identifier` ("There are multiple definitions for the identifier ... I do not have sufficient information to make a choice").
  This part kept every top-level name unique (the script that writes this file asserts it), and renamed the regulative rule of s 40(1) after it shared a name with the decision function.
- **Silent in reading: `NOT a OR b` is read as `NOT (a OR b)`.** In the probe, `NOT TRUE OR TRUE` evaluates to `FALSE` and `(NOT TRUE) OR TRUE` to `TRUE`, with no message; every `NOT` here is parenthesised.
- **Loud: `x NOT EQUALS y`** is a parse error, `parse/unexpected-NOT`; write `(NOT (x EQUALS y))`.
- **Loud: two `EQUALS` in one expression**, such as `a EQUALS 1 EQUALS TRUE`, is `check/type-mismatch` (the second `EQUALS` is given a BOOLEAN where it expects a NUMBER); assert `NOT (a EQUALS b)` or keep one comparison in the assertion.
- **Loud: a call with more arguments than the function's `GIVEN` has** is `check/wrong-argument-count` ("expects 1 argument, but you are applying it to 2").

## What `check.sh` prints

Baseline: the eight keel modules print 0 errors and 0 assertions in the run below (the keel's own tests are not in this folder), so the whole of the total is this part's.
With this part: 30 modules, 0 errors, 1336 assertions satisfied (834 in the ten layer-1 test files and 502 in `sgi-cases-seat.l4`), 0 failed, 0 refused, and every module has the same four counts on the main build 1.6.109 as on the stable 1.6.110.
Traces are not counted by `check.sh`: `work/traces.py` compared all 43 with their `-- EXPECT` comments on both builds, with no mismatch.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgi-alteration.l4                              0         0       0        0         0 |      0         0       0        0  same
sgi-capacity.l4                                0         0       0        0         0 |      0         0       0        0  same
sgi-cases-seat.l4                              0       502       0        0         0 |      0       502       0        0  same
sgi-constitution.l4                            0         0       0        0         0 |      0         0       0        0  same
sgi-contracts-seal.l4                          0         0       0        0         0 |      0         0       0        0  same
sgi-conversion.l4                              0         0       0        0         0 |      0         0       0        0  same
sgi-director-transactions.l4                   0         0       0        0         0 |      0         0       0        0  same
sgi-name-changes.l4                            0         0       0        0         0 |      0         0       0        0  same
sgi-names.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgi-objects.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgi-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgi-tests-alteration.l4                        0        58       0        0         0 |      0        58       0        0  same
sgi-tests-capacity.l4                          0        20       0        0         0 |      0        20       0        0  same
sgi-tests-constitution.l4                      0        65       0        0         0 |      0        65       0        0  same
sgi-tests-contracts-seal.l4                    0        93       0        0         0 |      0        93       0        0  same
sgi-tests-conversion.l4                        0       116       0        0         0 |      0       116       0        0  same
sgi-tests-director-transactions.l4             0        78       0        0         0 |      0        78       0        0  same
sgi-tests-name-changes.l4                      0       153       0        0         0 |      0       153       0        0  same
sgi-tests-names.l4                             0       130       0        0         0 |      0       130       0        0  same
sgi-tests-objects.l4                           0        73       0        0         0 |      0        73       0        0  same
sgi-tests-ultra-vires.l4                       0        48       0        0         0 |      0        48       0        0  same
sgi-ultra-vires.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (30 modules)                             0      1336       0        0           |      0      1336       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

