# NOTES: Fraud Act 2006 (2006 c. 35), encoding `legalese-sonnet-5.5`

Status: DRAFT, written by one Sonnet 5.5 agent (run `porridge-uk-fraud-b`) working alone from `BRIEF.md`.
No domain expert has read it against the text.
It was written without reading any existing encoding of this Act, and nothing outside the run's inputs and this folder.
The source is `ukpga-2006-35.txt`, a plain-text rendering made by a converter script from the legislation.gov.uk XML (version 2023-02-07, "point in time of the latest revised version").
It is not the official text and it is not marked up; nothing here is "verified against the official text".
Line numbers in `src:` locators are lines of that file.
`SOURCE-LICENSE.md` points at the subject-level licence note.
Numbers below are from the stable build named in `encoding.json` (1.6.98, sha256 recorded there), run at the end of this pass.

## Seat

The seat is **a person who may be accused of an offence under the Fraud Act 2006 (the person suspected or charged), asking what the Act makes of what they did or are alleged to have done, and the most that can follow.**
Why this seat: every operative provision of the Act is addressed to a person whom it makes liable (ss 1 to 4, 6, 7, 9, 11, 12), and the rest either measures that liability (the penalties, Schedule 2 paragraph 1) or takes a privilege away and replaces it with an immunity (s 13).
The operative provisions give no official a right or a power: the Secretary of State appears once, as the person who appoints a day (s 15(1)); an immigration officer's power of arrest appears only as a saving of another Act's power (Schedule 2 paragraph 11); and the court and the prosecutor are never named.
So there is one seat and no official's seat.
The company officer of s 12 is the same person in a different capacity, and is asked in its own group.

`fraud-seat.l4` has 17 questions under `§§` headings in the text's order.
Each takes plain inputs (yes or no, a choice from the module's list, a date), builds the layer-1 records inside its `WHERE`, and calls the same layer-1 rule; it restates no rule.
A field that no rule reads, or that cannot change an answer, takes a fixed placeholder with a comment (the form of a representation, s 2(4); act or omission, s 4(2); temporary or permanent, s 5(2)(b); getting or keeping, losing or not getting, s 5(3) and (4)).
The Act's two loss limbs "to cause loss to another" and "to expose another to a risk of loss" lead to the same result, so the seat asks them as one question and fills both fields from the answer (fork F20).
Layer 1 keeps them apart.

An answer of TRUE to "am I guilty" or "am I in breach" means every element is made out on the facts the person states; it is not a verdict.
Words the Act leaves undefined (dishonestly, a legal duty to disclose, expected to safeguard) are put to the person as facts to state.

| # | Question (as the person asks it) | Layer-1 rule it calls |
| --- | --- | --- |
| 1 | On what I have said, am I guilty of fraud under section 1, in any of the three ways in sections 2 to 4? | `section 1(1) and (2): a person is guilty of fraud` |
| 2 | Am I in breach of section 2 (fraud by false representation)? | `section 2(1): a person is in breach of section 2` |
| 3 | Am I in breach of section 3 (fraud by failing to disclose information)? | `section 3: a person is in breach of section 3` |
| 4 | Am I in breach of section 4 (fraud by abuse of position)? | `section 4(1): a person is in breach of section 4` |
| 5 | Am I guilty of an offence under section 6 by having this article? | `section 6(1): the elements of the offence are made out` |
| 6 | Am I guilty of an offence under section 7 by making, adapting, supplying or offering to supply this article? | `section 7(1): the elements of the offence are made out` |
| 7 | Am I guilty of an offence under section 9 by taking part in this business? | `section 9(1): the elements of the offence are made out` |
| 8 | Am I guilty of an offence under section 11 by obtaining these services? | `section 11(1): the elements of the offence are made out` |
| 9 | What is the longest prison term I can be given if I am convicted on indictment? | the penalty rule of the section (`section 1(3)` ... `section 11(3)`) |
| 10 | What is the longest prison term I can be given if I am convicted by a magistrates' court? | the same, through `the longest term on summary conviction` |
| 11 | What is the most I can be fined if I am convicted? | the same |
| 12 | If a company I am an officer of committed an offence under this Act, am I guilty of it too? | `section 12(2): the person is guilty ...` |
| 13 | Am I excused from answering a question, or obeying an order, in proceedings about property because it might incriminate me or my spouse or civil partner? | `section 13(1): whether the person is excused ...` |
| 14 | Can what I said in answering that question, or obeying that order, be used in evidence against me or my spouse or civil partner? | `section 13(2): whether the statement or admission is admissible ...` |
| 15 | Does the Fraud Act extend to the place where I did it? | `section 15(2): sections 1 to 9 and 11 to 13 extend to` |
| 16 | Was the Fraud Act in force on the day I did it? | `section 15(1): the Act is in force for a purpose on` |
| 17 | Can I still be prosecuted for an old deception offence that the Fraud Act abolished? | `Schedule 2 paragraph 3(1): what becomes of liability ...` |

Provisions kept out of the seat, and why: Schedule 2 paragraphs 4 to 10 and 11 (savings for provisions of other Acts, whose conditions the person could not state without those Acts; they are in layer 1), `section 13(3)` and `(4)` and the definitions of ss 2, 5, 8 and 9 (they are parts of the questions above, not questions).

## Jural relations

The Act names no holder of a right against the person: it says who is "guilty" and "liable", never who may sue or prosecute.
Where the text names no correlative party the table says so rather than inventing one.

| Provision | Holder (right, privilege, power, immunity) | Bearer (duty, no-right, liability, disability) | Relation | L4 rule |
| --- | --- | --- | --- | --- |
| s 1(1), (2) with ss 2, 3, 4 | not named in the text (the power to prosecute is outside this Act) | the person: liable to be convicted of fraud | liability | `section 1(1) and (2): a person is guilty of fraud`, `section 2(1): a person is in breach of section 2`, `section 3: a person is in breach of section 3`, `section 4(1): a person is in breach of section 4` |
| s 1(3), 6(2), 7(2), 9(6), 11(3) | the court that convicts (not named in the text) | the person: liable to the stated ceiling | liability | `section 1(3): the penalty for fraud` and its four twins, through `the penalty subsection: what may follow conviction` |
| s 1(4), 6(3), 7(3), 9(7), 11(4); Sch 2 para 1 | none | none: they change a limit inside the liability above | none (counting rules) | `sections 1(4), 6(3), 7(3), 9(7) and 11(4) ...`, `Schedule 2 paragraph 1 ...`, `sections 1(3)(a) ... the longest term on summary conviction` |
| s 2(2) to (5), 4(2), 5, 8(1), 9(2), (3), (5), 13(3), (4) | none | none | none (definitions) | the rules of those names |
| s 6(1) | not named in the text | the person: liable for having an article for use in fraud | liability | `section 6(1): the elements of the offence are made out` |
| s 7(1) | not named in the text | the person: liable for making, adapting, supplying or offering to supply | liability | `section 7(1): the elements of the offence are made out` |
| s 9(1) | not named in the text | the person: liable for taking part knowingly in a fraudulent business | liability | `section 9(1): the elements of the offence are made out` |
| s 11(1), (2) | not named in the text (the provider of the services is the victim but the text gives it no right) | the person: liable for obtaining services dishonestly | liability | `section 11(1): the elements of the offence are made out` |
| s 12(2), (3) | not named in the text | the officer, or the member treated as a director: liable with the body corporate | liability | `section 12(2): the person is guilty of the offence as well as the body corporate` |
| s 13(1) | the party asking, or the court ordering (not named) | the person: no privilege to refuse on the ground of self-incrimination, in proceedings relating to property | no-privilege (duty to answer or comply) | `section 13(1): whether the person is excused ...` |
| s 13(2) | the person, and the spouse or civil partner (unless married or partnered after the statement) | whoever would use the statement: disabled from using it in evidence | immunity / disability | `section 13(2): whether the statement or admission is admissible ...` |
| s 15(1) | the Secretary of State: power to appoint a day by order | everyone the Act binds: liable to its coming into force on that day | power / liability | `section 15(1): the Act is in force for a purpose on` (the day is an input) |
| s 15(2), (3) | none | none | none (extent) | `section 15(2): ...`, `section 15(3): ...` |
| Sch 1 para 1 with Sch 2 para 3 | the person: immunity from the abolished deception offences for what is wholly done after abolition | whoever would prosecute: disabled, except for offences partly committed before (para 3) | immunity / saving | `Schedule 2 paragraph 3(1): what becomes of liability for an old deception offence` |
| Sch 2 paras 4 to 10 | those holding the saved provisions of other Acts | the persons those provisions bind | saving of relations arising under other Acts | the rules `Schedule 2 paragraph 4` to `paragraph 10`, through `Schedule 2 paragraphs 4 to 10: the saving applies` |
| Sch 2 para 11 | an immigration officer: power of arrest (saved) | the person arrested: liability | power / liability | `Schedule 2 paragraph 11(1): ...` |

## What is and is not encoded

Encoded: ss 1 to 9 (with s 9(4) blank in this text), 11 to 13, 15(1) to (3), the date of enactment, Schedule 1 paragraph 1 (its effect on liability), Schedule 2 paragraphs 1 and 3 to 11.
Not encoded, with reasons, in the coverage table: s 8(2) (stop and search powers in other Acts), s 10 (blank), s 14, s 15(4), s 16, Schedule 1 paragraphs 2 to 38 (amendments of other Acts), Schedule 2 paragraph 2, Schedule 3 (a table of repeals).
Not in the sources, so asked or named and never decided: dishonesty; the Companies Act 2006 (s 1(1), s 993); the general limit in a magistrates' court; the statutory maximum; whether a duty to disclose exists; the day the Act was brought into force; where the Armed Forces Act 2001 extends; the circumstances described in the Theft Acts, the Limitation Acts and the Terrorism Act 2000 that Schedule 2 paragraphs 4 to 10 refer to.
Penalties are ceilings, never sentences, and carry no figure the Act does not give.

## Coverage table

Dispositions: `encoded`, `inert` (reason given), `repealed or blank in this text`, `not applicable`.
None is `deferred`.

| Provision (src lines) | Heading | Disposition | Where / why |
| --- | --- | --- | --- |
| Title, chapter, long title (1-3) | | inert | The long title states the Act's purpose ("criminal liability for fraud and obtaining services dishonestly"); it decides nothing and creates no relation. |
| Date of enactment (4) | [8th November 2006] | encoded | `fraud-dates.l4` (fork F17). |
| Enacting formula (5) | | inert | The words of enactment; they decide nothing about any person. |
| s 1 (7-16) | Fraud | encoded | `fraud-s01-s05.l4` for (1) and (2); (3) through `fraud-penalty.l4`; (4) in `fraud-penalty.l4` (fork F2). |
| s 2 (17-30) | Fraud by false representation | encoded | `fraud-s01-s05.l4`. |
| s 3 (31-36) | Fraud by failing to disclose information | encoded | `fraud-s01-s05.l4`. |
| s 4 (37-44) | Fraud by abuse of position | encoded | `fraud-s01-s05.l4`. |
| s 5 (45-52) | "Gain" and "loss" | encoded | `fraud-s01-s05.l4`, worked out from facts (the thing, the way, the permanence). |
| s 6 (53-58) | Possession etc. of articles for use in frauds | encoded | `fraud-s06-s08.l4`; (2) through `fraud-penalty.l4`; (3) in `fraud-penalty.l4`. |
| s 7 (59-66) | Making or supplying articles for use in frauds | encoded | `fraud-s06-s08.l4`; (2) and (3) as for s 6. |
| s 8(1) (67-71) | "Article" | encoded | `fraud-s06-s08.l4`. |
| s 8(2) (72-76) | "Article" | inert | Lists three stop-and-search provisions of other Acts (PACE 1984 s 1(7)(b), Armed Forces Act 2001 s 2(8)(b), the Northern Ireland PACE Order Art 3(7)(b)) to which the extended meaning of "article" also applies; they give powers to constables and are not among the sources. |
| s 9 (77-91, except (4)) | Participating in fraudulent business carried on by sole trader etc. | encoded | `fraud-s09.l4`; (6) through `fraud-penalty.l4`; (7) in `fraud-penalty.l4`. |
| s 9(4) (86) | | repealed or blank in this text | The text shows `(4)` followed by a row of dots. |
| s 10 (92-93) | Participating in fraudulent business carried on by company etc.: penalty | repealed or blank in this text | The text shows the heading and then a row of dots; no wording is left. |
| s 11 (95-109) | Obtaining services dishonestly | encoded | `fraud-s11.l4`; (3) through `fraud-penalty.l4`; (4) in `fraud-penalty.l4`. |
| s 12 (111-117) | Liability of company officers for offences by company | encoded | `fraud-s12-s13.l4`. |
| s 13 (118-134) | Evidence | encoded | `fraud-s12-s13.l4`. |
| s 14 (135-138) | Minor and consequential amendments etc. | inert | Says only that Schedules 1, 2 and 3 contain amendments, savings and repeals; it creates no relation. What the Schedules do is under their own rows. |
| s 15(1) (139-140) | Commencement and extent | encoded | `fraud-s15.l4`; the day appointed is an input (finding 17). |
| s 15(2), (3) (141-142) | Commencement and extent | encoded | `fraud-s15.l4` (fork F18). |
| s 15(4) (143) | Commencement and extent | inert | Says where the amendments in s 10 and Schedule 1 extend: to any place to which the provision amended extends. Those are provisions of other Acts, not among the sources, and s 10 is blank. |
| s 16 (144-145) | Short title | inert | The Act's name; it creates no relation. |
| Sch 1 para 1 (150-166) | Abolition of various deception offences | encoded | Its effect on liability, in `fraud-sch2.l4` (`Schedule 2 paragraph 3(1)`). The abolished offences of the Theft Acts are not encoded; their elements are not in the sources. |
| Sch 1 paras 2-38 (167-340) | amendments of other Acts | inert | Each paragraph amends an Act that is not among the sources (the Visiting Forces Act 1952, the Theft Acts, the Criminal Justice Act 1993, the Terrorism Act 2000, the Gambling Act 2005 and others) and gives the person nothing under this Act. Some of them bear on the person through those Acts (paragraph 24 lists ss 1, 6, 7, 9 and 11 as Group A offences in s 1(2) of the Criminal Justice Act 1993, and paragraph 25 amends that Act's jurisdiction rule); those effects are not encoded. |
| Sch 2 para 1 (343-344) | Maximum term of imprisonment | encoded | `fraud-penalty.l4`, with `fraud-dates.l4` for the date. |
| Sch 2 para 2 (345-346) | Increase in penalty for fraudulent trading | inert | Says s 10 does not affect the penalty for an offence committed before it comes into force; s 10 is blank in this text and its penalty belongs to the Companies Act 2006, which is not among the sources, so the paragraph decides nothing here. |
| Sch 2 para 3 (347-352) | Abolition of deception offences | encoded | `fraud-sch2.l4`. |
| Sch 2 paras 4-10 (353-366) | savings for other Acts | encoded | `fraud-sch2.l4`, as one shape with the circumstances taken as a fact (finding 19). |
| Sch 2 para 11 (367-372) | Powers of arrest | encoded | `fraud-sch2.l4`. |
| Sch 3 (373-387) | Repeals and revocations (table) | inert | A table of provisions of other Acts repealed or revoked; it gives the person nothing under this Act. |

Summary: 31 rows: 20 encoded, 9 inert, 2 repealed or blank in this text, 0 not applicable, 0 deferred.

## Fork register

Where the text leaves a choice, this is the reading taken and the reason.
Each is an assumption, not a ruling.

| Fork | Provision | Readings seen | Taken | Licensed by |
| --- | --- | --- | --- | --- |
| F1 | ss 2(1)(a), 3(a), 4(1)(b), 11(1)(a) "dishonestly", "dishonest act" | the Act defines it; a test is borrowed from case law; the person's honest belief decides | A bare yes-or-no fact the person states. | The Act does not define "dishonestly" (searched the whole text). |
| F2 | ss 1(4), 6(3), 7(3), 9(7), 11(4) | the instruction "as if the reference to 12 months were a reference to 6 months" has no "12 months" to act on, so it does nothing and Northern Ireland follows "the general limit"; or its evident effect is six months in Northern Ireland | Six months in Northern Ireland, at any date. | The five subsections each say 6 months for Northern Ireland; the subsections they modify now read "the general limit in a magistrates' court", which suggests an earlier text said 12 months (an inference, not stated). |
| F3 | ss 1(3)(b), 6(2)(b), 7(2)(b), 9(6)(b), 11(3)(b) "or to a fine" | an unlimited fine; a fine up to some figure elsewhere | `no limit is stated`. | The text gives no ceiling for the fine on indictment, and none is imported. |
| F4 | "the general limit in a magistrates' court", "the statutory maximum" | give the usual figures | Named values with no number. | Neither figure is in the sources; Schedule 2 para 1 gives 6 months only for offences before 2 May 2022. |
| F5 | s 1(1), (2) | three offences; one offence committed in three ways | One offence, in breach of any of ss 2, 3 or 4. | s 1(1): "guilty of fraud if he is in breach of any of the sections listed in subsection (2) (which provide for different ways of committing the offence)". |
| F6 | s 11(2)(c) "(i) ... or (ii) that they might be, but intends that payment will not be made" | the intention qualifies only (ii); the intention qualifies both | Both: either knowledge, and the intention, are required. | The comma and "but" follow the two limbs together; the other reading would make anyone who knows services are paid for guilty whatever they meant to do. |
| F7 | s 2(2)(b) "knows that it is, or might be, untrue or misleading" | actual knowledge only; awareness of the possibility suffices | Awareness that it might be untrue or misleading suffices. | The words "or might be". |
| F8 | s 2(5) "may be regarded as made" | the court has a discretion; it counts | It counts, when submitted to a system or device; a representation made to nobody is not made. | The word "may" makes it permissible, and a discretion cannot be tested with facts; the alternative is unencodable. |
| F9 | s 6(1) | a mental element is implied (knowledge, or intent to use); none is stated | None added; whose fraud, and whose use, are not required to be the person's. | The text states no mental element and no owner for the fraud. |
| F10 | s 7(1)(a) "knowing that it is designed or adapted" | by whom designed is unstated | The person's knowledge is a fact the person states. | The text. |
| F11 | s 9(2)(a), (3), (5) | the Act's own list decides who is within s 993 | Who carries on the business is a choice (company; a person treated as one; a person exempted; a person outside) and "fraudulent purpose" is a fact. | s 993 and s 1(1) of the Companies Act 2006 are not among the sources. |
| F12 | s 8(1) "includes" | the electronic extension is the whole meaning; it adds to an ordinary meaning | It adds: an ordinary article is asked as a fact, plus a program, plus data. | "Includes", and the Act defines no ordinary sense. |
| F13 | s 4(1)(a) "expected" | by the other person, by the law, by a reasonable person | A fact the person states. | The text does not say. |
| F14 | s 12(2) "proved to have been committed with the consent or connivance" | the module decides proof; proof is a fact about the proceedings | A fact the person is asked about. | A module cannot decide proof. |
| F15 | s 13(1), (2) outside their conditions | the privilege stays; the privilege goes everywhere; unknown | A named value `section 13(1) does not apply` / `section 13(2) does not apply`, the Act's silence. | The text states the rule only for proceedings relating to property and offences under the Act or related offences. |
| F16 | s 13(4)(b) "any other offence involving any form of fraudulent conduct or purpose" | a closed list; any offence with a fraudulent aspect | A choice in the module's list the person makes. | The text does not list them. |
| F17 | the bracketed date under the title | Royal Assent; date of enactment | Carried as the date of enactment. | The text does not label the date. |
| F18 | s 15(2) | the Act applies to conduct in Scotland or abroad that a court in England and Wales or Northern Ireland could try; it does not | The Act states no penalty for another place: the answer is `NOTHING`, and the extent question says so. | s 15(2) says "extend to"; extent is not application, and this Act says nothing about conduct abroad. Sch 1 paras 24 and 25 show that jurisdiction over such offences is dealt with in the Criminal Justice Act 1993, which is not among the sources. |
| F19 | s 2(3) | a promise or an opinion is a representation as to state of mind; it is not | The person classifies what they said (fact, law, a state of mind, or none of these). | The text. |
| F20 | seat only: ss 2(1)(b)(ii), 3(b)(ii), 4(1)(c)(ii) | one question or two | One question, answer copied into both limbs. | Both limbs lead to the same result in every rule. |

Where I looked and found no ambiguity worth a fork: s 1(2) (the list is closed); s 5(3) and (4) (keeping and not getting are named and both count); s 7(1)'s four verbs (alternatives joined by "or"); s 12(3) (a member counts as a director for acts and defaults in connection with management).

## Findings: what the text turns out to say

1. Each of the offences in ss 2, 3 and 4 is complete on the intention alone: no gain, no loss, and no person deceived is needed. Asserted.
2. A free service is outside ss 2 to 4, because "gain" and "loss" extend only to money or other property (s 5(2)(a)); it can be inside s 11 only if it was made available on a payment basis and the person meant not to pay. A service not offered on a payment basis is outside both. Asserted.
3. Section 6 has no mental element and does not say whose fraud the article is for. On the text, having an article for use in connection with another person's fraud is enough. Asserted (fork F9).
4. Section 7 has two mental limbs, knowing and intending, and either suffices; there are four ways of dealing with the article, and any one suffices. Asserted.
5. Section 2(2)(b) is satisfied by awareness of a possibility ("or might be"); a representation that is untrue but neither known nor suspected to be so is not false within the section. Asserted.
6. A representation submitted to a system or device counts as made (s 2(5)); one made to nobody and nothing does not. Asserted.
7. An omission can be an abuse of position (s 4(2)); the form of the conduct never changes the answer. Asserted.
8. The penalties are ceilings with no figures for the general limit, the statutory maximum and the fine on indictment, and the encoding returns those words, not numbers. Asserted.
9. The Northern Ireland clauses (ss 1(4), 6(3), 7(3), 9(7), 11(4)) speak of "the reference to 12 months", which the subsections they modify do not now contain; their effect on an offence committed on or after 2 May 2022 is therefore unclear (fork F2). The encoding takes six months; a court could read the clauses as doing nothing. Asserted (as the reading taken).
10. Schedule 2 paragraph 1 says "committed before 2 May 2022". An offence committed on 2 May 2022 is not before it, so the general limit applies from that day. Asserted.
11. Section 9 does not reach a business carried on by a company, by a person treated as a company, or by a person exempted from s 993; those are within s 993 of the Companies Act 2006, which is not among the sources. Section 9(4) and section 10 are blank in this text. Asserted for the first sentence.
12. Section 11(2)(c): "but intends" is read as qualifying both knowledge limbs (fork F6); under the other reading a person who knows the services are paid for would be liable regardless of their intention. Asserted.
13. Section 12 reaches an officer only on proof of consent or connivance. The text does not mention neglect, so the position alone is not enough. Asserted.
14. Section 13(2) protects the person who made the statement without exception, and the spouse or civil partner unless they married or became civil partners after the statement was made; the exception does not apply to the person. Its protection is limited to proceedings for an offence under the Act or a related offence: the text is silent on any other use. Asserted.
15. Section 13(1) removes the excuse only in proceedings relating to property (s 13(3)), and only for an answer or compliance that may incriminate the person or their spouse or civil partner of an offence under the Act or a related offence; outside those conditions the text says nothing. Asserted.
16. Section 15(2) extends ss 1 to 9 and 11 to 13 to England and Wales and Northern Ireland only; for Scotland or anywhere else the Act states no penalty. Asserted.
17. The Act comes into force on a day appointed by order, and different days may be appointed for different purposes (s 15(1)); the day is not in the text, so every question about being in force takes it as an input. Asserted.
18. Schedule 2 paragraph 3 saves liability only for an offence partly committed before the abolition; an offence whose every relevant event was before the abolition is left unaddressed by the text, as is an offence with no relevant events given. Asserted.
19. Schedule 2 paragraphs 4 to 10 each preserve an operation of another Act where the circumstances described in that Act apply and the deception or credit came before the commencement of the relevant paragraph of Schedule 1; "before" is strict. Asserted (the shape; the circumstances are a fact).
20. The text of s 13(4) lists conspiracy to defraud as a "related offence" but this Act creates no such offence; the penalty questions therefore return `NOTHING` for it. Asserted.

## What the stable binary does not accept

The brief lists these as unavailable on the stable build 1.6.98: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, section `GIVEN`, `TYPICALLY`, `SET OF`, an unparenthesised `NOT`, an `#ASSERT` over more than one line, and `IMPORT` of a module outside the same folder.
I used none of them, and I did not test each; the list is the brief's, not my measurement.
"Not covered" is a constructor (`the Act does not say (...)`, `section 13(1) does not apply`) or `NOTHING`, and each is asserted.
What I hit and fixed in this run:

- Comparing two `DATE`s with `AT LEAST` or `LESS THAN` needed `IMPORT daydate`; without it the checker reported multiple definitions of the comparison operator (`fraud-s15.l4`).
- `GIVEN a IS A LIST OF DATE, b IS A DATE` on one line is a parse error; each parameter takes its own line.
- The prelude has no `YMD`, so `fraud-dates.l4` defines a local one over `Date`, which takes the day first.

## What `check.sh` prints

Command: `L4=<L4_BIN> L4_TARGET=unstable ./check.sh`, from this folder, at the end of the pass.

```
module                                    errors satisfied  failed  refused  expected
fraud-cases-seat.l4                            0       109       0        0         0
fraud-dates.l4                                 0         0       0        0         0
fraud-nouns.l4                                 0         0       0        0         0
fraud-penalty.l4                               0         0       0        0         0
fraud-s01-s05.l4                               0         0       0        0         0
fraud-s06-s08.l4                               0         0       0        0         0
fraud-s09.l4                                   0         0       0        0         0
fraud-s11.l4                                   0         0       0        0         0
fraud-s12-s13.l4                               0         0       0        0         0
fraud-s15.l4                                   0         0       0        0         0
fraud-sch2.l4                                  0         0       0        0         0
fraud-seat.l4                                  0         0       0        0         0
fraud-tests-penalty-s15.l4                     0        43       0        0         0
fraud-tests-s01-s05.l4                         0        71       0        0         0
fraud-tests-s06-s09.l4                         0        37       0        0         0
fraud-tests-s11-s13.l4                         0        53       0        0         0
fraud-tests-sch2.l4                            0        30       0        0         0
TOTAL (17 modules)                             0       343       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Every case file has assertions written equal to assertions satisfied.
A control run with two deliberately false assertions appended to a scratch copy of `fraud-cases-seat.l4` counted `failed 2` and left `satisfied` at 109, so the script does count failures; the scratch copy was deleted.
`python3 -I srcrefs.py check --refs <the text> fraud-*.l4` reports: `srcrefs check: 196 src: lines, 40 runs, 96 locators, 0 problems`.

## Owed before this is relied on

- A lawyer who practises criminal law in England and Wales or Northern Ireland to read it against the text, and to rule on forks F2 (Northern Ireland six months), F6 (s 11), F7 and F9.
- The instruments the Act points to, which are not among the sources: the Companies Act 2006 ss 1(1) and 993 (for s 9); the Sentencing Act 2020 or its predecessors for the "general limit" and the statutory maximum; the order bringing the Act into force; the Theft Acts, the Limitation Acts, the Terrorism Act 2000 and the 2004 Act for Schedule 2 paragraphs 4 to 11. With them, borrowed terms become rules rather than inputs.
- The text is the revised text at 2023-02-07; whether any provision was prospective or amended since is not known here.
- Whether the "dishonestly" test and the limits of "a legal duty to disclose" should stay inputs, or be encoded from case law, which is outside the Act alone.
- The seat's wording of each `@desc` has not been tried on a real person.
