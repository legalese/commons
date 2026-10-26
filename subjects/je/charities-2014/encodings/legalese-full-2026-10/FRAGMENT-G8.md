# FRAGMENT-G8: Articles 26 to 36 of the Charities (Jersey) Law 2014 (Part 7 Information and enforcement; Part 8 Appeals to Charity Tribunal)

Status: **draft, complete for its scope** (written 2026-10-26 by ENCODER G8).  Every provision of Articles 26 to 36 has a row below; none is `deferred`.  No domain expert has read it against the Law.
Sources: the Law's consolidated text (`charities-jersey-law-2014-2026-10-02.txt`, "RAW", the version from 2 October 2026), checked word for word against the official PDF text layer for these Articles: no difference except line-end hyphenation ("Non-Profit") and the position of the footnote marker 4 on 31(f).  Binary: the fleet's `l4` (sha256 `18bd5a72...`), `JL4_LIBRARY_PATH` unset.

## 0. What is in the deposit

| file | holds |
| --- | --- |
| `g8-nouns` | the nouns of G8 and nothing else: the 19 fork enumerations, the record `Interpretation of Articles 26 to 36`, the acts `Act under Article 26 to 31` and `Act under Article 32 to 36`, and the records the rule modules take as inputs |
| `g8-penalties` | the penalties of the three offences (26(7), 26(10), 29(1)) as data, the named refusals for the fines, and the unit of a term of imprisonment (F8.8) |
| `g8-art26-demand` | Article 26: who may be demanded of, the power, a lien, retaining and copying, the retention period, the copy, the two offences, privilege, the statement |
| `g8-art27-28-required-steps` | Articles 27 and 28: the five beliefs, the notice and its record (IP19), governor-directed steps, the Minister's Orders, organized religious charities (IP20), partial invalidity |
| `g8-art29-31-information` | Articles 29 to 31: the offence of disclosure and its exceptions, the duties of the Commissioner, the permitted disclosures |
| `g8-art32-36-appeals` | Articles 32 to 36: who may appeal what, the grounds, the powers of the Tribunal and the court, the time limit, a substituted decision |
| `g8-tests-art26`, `-art27-28`, `-art29-31`, `-art32-36` | tests from the source, one module per rule module |
| `g8-tests-fixtures` | the favoured interpretation and, for each fork, the favoured interpretation with the other reading of that fork alone (generated, with 399 assertions that each differs from the favoured in exactly its own field) |
| `g8-tests-red` | 19 assertions MEANT to fail, one per fork: the other reading's answer asked of the favoured interpretation |

Changes from the survey's group map: two modules were added, `g8-nouns` and `g8-penalties`, because the four rule modules share the fork record, the acts and the penalty helpers and a group module may import only `prelude`, `daydate`, `domain` and modules of its own group.  The four rule modules keep the PLAN's names.  The tests are in modules of their own (`g8-tests-*`).
Changes from the survey's readings: **the demand for information on an applicant answers FALSE, not REFUSE** (the survey's trap T23 suggested a refusal): 26(2) is a closed list, so the Law answers; a refusal is for what the sources do not answer.  **F8.7 is reformulated** (see its entry) because the survey's discriminating case depends on how the day of service is fixed, which is G7's fork.  **F8.2 has a third reading** (the request day counted).  **F8.15's default is the restrictive reading** (only (c) and (d) notices), the survey having left it unregistered.  Eleven forks are new (F8.9 to F8.19).  G8 is a producer of IP27 for Articles 26 and 27 (`Art 26 the decision of the Commissioner to impose a requirement`, `Art 27 the decision of the Commissioner to impose a requirement`), which the survey's section (c) names but section (b) does not list; each is tested round trip into `Art 33 the right of appeal`.  Export names are the survey's section (b) names; where the survey named a group of paragraphs I added the exact names (`Art 28(3) the required steps notice is invalid to the extent`, `Art 34(1) the appeal has a ground`, `Art 34(2) the tribunal may make interim orders and consider evidence`, `Art 34(3) the tribunal may determine the appeal`, `Art 35(3) the tribunal may refer a point of law`, `Art 36(2) the Minister may by Order set time limits`).  `Art 26(5) the Commissioner may keep the document until` returns an enumeration (a last day, or "until the proceedings conclude, and they have not"), not a bare `DATE`, because the extension has no end date until the proceedings conclude.

How the rules are shaped (so the register below can be read): a power is a `MAY` rule typed by who acts and what is done, with its preconditions as computable conditions (`IF ... THEN PARTY ... MAY ... ELSE FULFILLED`: no power leaves nothing to exercise); a duty is a `MUST`; an offence is a prohibition (`SHANT`) or a `MUST` whose breach is the offence, with the penalty as data (`Penalty provided`); a discretion ("reasonably requires", "reasonable excuse", "believes", "satisfied", "thinks fit", "appears") is a `GIVEN` named for what it decides.  Where a source provision is a plain test over facts it is a `BOOLEAN`.  Lazy evaluation is respected: every named refusal is returned, never stored.

## 1. Coverage

One row per provision of Articles 26 to 36, in the Law's numbering.  Dispositions: `encoded`, `inert`, `refused`, `out-of-scope`; none is `deferred`.  `Plan` is the survey's proposed disposition; where mine differs the last column says why.

| id | provision | plan | disposition | module | rules | note |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | Article 26 | encoded | encoded | g8-art26-demand | `§§ Article 26`; every rule below |  |
| 26(1) | Article 26(1) | encoded | encoded | g8-art26-demand | `Art 26(1) the Commissioner has the power to demand`; `Art 26(1) the Commissioner may require the person to provide information or attend` (DEONTIC MAY); `Art 26 the decision of the Commissioner to impose a requirement` (IP27) | the purpose is limited to a required steps notice (T23); reasonably requires is an input |
| 26(1)(a) | Article 26(1)(a) | encoded | encoded | g8-art26-demand | same two rules; the time and place: `Art 26(1) the last day allowed by the notice` (F8.7) |  |
| 26(1)(b) | Article 26(1)(b) | encoded | encoded | g8-art26-demand | same two rules (one MAY covers both: information or a document, or attendance) |  |
| 26(2) | Article 26(2) | encoded | encoded | g8-art26-demand | `Art 26(2) the person falls within Article 26(2)` | an applicant for registration, or a governor of an applicant never registered, is NOT within it: answered FALSE, not REFUSE (the list is closed) |
| 26(2)(a) | Article 26(2)(a) | encoded | encoded | g8-art26-demand | `Art 26(2)(a) the person is a registered charity or an entity that was formerly one`; `Art 26(2) the entity is or was a registered charity` |  |
| 26(2)(b) | Article 26(2)(b) | encoded | encoded | g8-art26-demand | `Art 26(2)(b) the person is a governor or former governor of a registered charity or of a formerly registered entity`; readings A and B (F8.17) |  |
| 26(3) | Article 26(3) | encoded | encoded | g8-art26-demand | `Art 26(3) the effect on a lien of providing the document` | providing is without prejudice to the lien; a lien is not made an excuse (that is the 26(7) input) |
| 26(4) | Article 26(4) | encoded | encoded | g8-art26-demand | `Art 26(4)(a) ...`, `Art 26(4)(b) ...` |  |
| 26(4)(a) | Article 26(4)(a) | encoded | encoded | g8-art26-demand | `Art 26(4)(a) the Commissioner may retain or copy the document and require an explanation` (DEONTIC MAY); `Art 26(4)(a) an explanation of the document may be required of the person` (F8.19) |  |
| 26(4)(b) | Article 26(4)(b) | encoded | encoded | g8-art26-demand | `Art 26(4)(b) the Commissioner may require a statement of where the document is` (DEONTIC MAY) |  |
| 26(5) | Article 26(5) | encoded | encoded | g8-art26-demand | `Art 26(5) the Commissioner may keep the document until`; `Art 26(5) retention is permitted on` | period P23: F8.1, F8.9, F8.10 |
| 26(5)(a) | Article 26(5)(a) | encoded | encoded | g8-art26-demand | `Art 26(5)(a) the first day of the retention year`; `... the anniversary of the day the year starts`; `... the last day of the retention year` |  |
| 26(5)(b) | Article 26(5)(b) | encoded | encoded | g8-art26-demand | `Art 26(5)(b) proceedings were commenced within the retention year`; `Art 26(5)(b) the end of the retention when proceedings were commenced within the year` | proceedings commenced before the year starts, or after it ends, do not extend it |
| 26(6) | Article 26(6) | encoded | encoded | g8-art26-demand | `Art 26(6) the Commissioner must supply a copy of the retained document` (DEONTIC MUST); `Art 26(6) the copy was supplied as soon as practicable` | period P24: F8.2; the supplier is not named by the Law: typed on the Commissioner (open question) |
| 26(7) | Article 26(7) | encoded | encoded | g8-art26-demand; g8-penalties | `Art 26(7) the person must comply with the requirement` (DEONTIC MUST); `Art 26(7) the person commits an offence`; `Art 26(7) the penalty the person is liable to`; `Art 26(7) the penalty provided for the offence`; `Art 26(7) the amount of a fine of level 3 on the standard scale` (named refusal); `Art 26 and 29 a term of imprisonment is within the maximum` | periods P25: F8.8; the time to comply: F8.7; reasonable excuse is an input |
| 26(8) | Article 26(8) | encoded | encoded | g8-art26-demand | `Art 26(8) a requirement under Article 26 extends to what is withheld`; read by `Art 26(7) the person commits an offence` | legal professional privilege is an input |
| 26(9) | Article 26(9) | encoded | encoded | g8-art26-demand | `Art 26(9) the prosecution is barred from using the statement`; `Art 26(9) the statement may be used by the prosecution` | TRUE of 'may be used' means only that Article 26(9) does not bar it |
| 26(10) | Article 26(10) | encoded | encoded | g8-art26-demand; g8-penalties | `Art 26(10) the person must not give false information` (DEONTIC SHANT); `Art 26(10) the person commits an offence`; `Art 26(10) the penalty the person is liable to`; `Art 26(10) the penalty provided for the offence`; `Art 26(10) the maximum fine` (named refusal) | period P26: F8.8; the Law states no maximum fine |
| 26(11) | Article 26(11) | encoded | encoded | g8-art26-demand | `Art 26(10) the person commits an offence` reads neither fact of (a) and (b); four tests show it |  |
| 26(11)(a) | Article 26(11)(a) | encoded | encoded | g8-art26-demand | field `contained in a document` of `Facts of providing information under Article 26(10)`, deliberately not read |  |
| 26(11)(b) | Article 26(11)(b) | encoded | encoded | g8-art26-demand | field `provided under Article 26` of the same record, deliberately not read |  |
| 27 | Article 27 | encoded | encoded | g8-art27-28-required-steps | `§§ Article 27`; every rule below |  |
| 27(1) | Article 27(1) | encoded | encoded | g8-art27-28-required-steps | `Art 27(1) the Commissioner has a ground to serve a required steps notice`; `Art 27(1) paragraph (2) applies`; `Art 27(1) the belief is borne out` | the Commissioner's belief is an input; F8.14 |
| 27(1)(a) | Article 27(1)(a) | encoded | encoded | g8-art27-28-required-steps | `Art 27(1) the belief is borne out` arm 1 (IP12 `the conduct is misconduct within Article 2(10)`) |  |
| 27(1)(b) | Article 27(1)(b) | encoded | encoded | g8-art27-28-required-steps | arm 2 (IP8 `the entity meets the charity test`) |  |
| 27(1)(c) | Article 27(1)(c) | encoded | encoded | g8-art27-28-required-steps | arm 3 (IP14 `the governor has engaged in misconduct within Article 18(4)`) |  |
| 27(1)(d) | Article 27(1)(d) | encoded | encoded | g8-art27-28-required-steps | arm 4 (IP21 through `the entity`'s governors; the unfitness is an input) |  |
| 27(1)(e) | Article 27(1)(e) | encoded | encoded | g8-art27-28-required-steps | arm 5 (IP15, IP16) |  |
| 27(2) | Article 27(2) | encoded | encoded | g8-art27-28-required-steps | `Art 27(2) the Commissioner may serve a required steps notice` (DEONTIC MAY); `Art 27(2) the required steps notice served` (IP19 record); `Art 27 the decision of the Commissioner to impose a requirement` (IP27) | time specified: F8.7; steps and Order are inputs |
| 27(3) | Article 27(3) | encoded | encoded | g8-art27-28-required-steps | `Art 27(3) the person is a relevant person` |  |
| 27(3)(a) | Article 27(3)(a) | encoded | encoded | g8-art27-28-required-steps | first disjunct of `Art 27(3) the person is a relevant person`; constructor `the registered charity` |  |
| 27(3)(b) | Article 27(3)(b) | encoded | encoded | g8-art27-28-required-steps | second disjunct; constructor `a governor of the registered charity` |  |
| 27(4) | Article 27(4) | encoded | encoded | g8-art27-28-required-steps | `Art 27(4) the steps may include suspension, removal or replacement`; `Art 27(4) the requirement is to suspend, remove or replace a governor` | F8.15; barred for an organized religious charity (Article 28) |
| 27(5) | Article 27(5) | encoded | encoded | g8-art27-28-required-steps | `Art 27(5) the Minister may by Order make further provision` (DEONTIC MAY) | the content of the Order is an input read by `Art 27(2)` |
| 28 | Article 28 | encoded | encoded | g8-art27-28-required-steps | `§§ Article 28`; every rule below |  |
| 28(1) | Article 28(1) | encoded | encoded | g8-art27-28-required-steps | `Art 28(1) the Minister may by Order provide for the charity to be categorized` (DEONTIC MAY); `Art 28(1) the charity is eligible to be categorized as an organized religious charity` | content of the Order is an input |
| 28(1)(a) | Article 28(1)(a) | encoded | encoded | g8-art27-28-required-steps | `Art 28(1)(a) the charity meets the charity test by virtue of Article 6(1)(c)`; readings A and B (F8.3) | uses IP8, IP11 |
| 28(1)(b) | Article 28(1)(b) | encoded | encoded | g8-art27-28-required-steps | `Art 28(1)(b) the supervision and discipline of the governors is adequate to justify Article 28(3)` | the Minister's appearance is an input |
| 28(2) | Article 28(2) | encoded | encoded | g8-art27-28-required-steps | `§§§ 28(2)`; the rules of (a) below | a limit on the content of the Order, carried by the inputs of `Art 28 the entity is an organized religious charity` |
| 28(2)(a) | Article 28(2)(a) | encoded | encoded | g8-art27-28-required-steps | `Art 28(2)(a) the Commissioner may grant or withdraw the status` (DEONTIC MAY); `Art 28 the entity is an organized religious charity` |  |
| 28(2)(b) | Article 28(2)(b) | inert | inert | g8-art27-28-required-steps | quoted (src:658-661), no rule | what an Order does with the three statuses is the Order's content |
| 28(2)(b)(i) | Article 28(2)(b)(i) | out-of-scope | out-of-scope | g8-art27-28-required-steps | quoted with 28(2)(b), no rule | the Charities and Trustee Investment (Scotland) Act 2005 is not among the sources; a designated religious charity is an input to the Order |
| 28(2)(b)(ii) | Article 28(2)(b)(ii) | out-of-scope | out-of-scope | g8-art27-28-required-steps | quoted with 28(2)(b), no rule | section 10(2) of the Charities Act 2011 (UK) is not among the sources |
| 28(2)(b)(iii) | Article 28(2)(b)(iii) | inert | inert | g8-art27-28-required-steps | quoted with 28(2)(b), no rule | an entity in Jersey similar to those: the Order's content |
| 28(3) | Article 28(3) | encoded | encoded | g8-art27-28-required-steps | `Art 28(3) the required steps notice is invalid to the extent`; `Art 28(3) the requirements of the notice that remain valid` | partial invalidity; T11 collides with 19(9)(e)(i) (G6) |
| 29 | Article 29 | encoded | encoded | g8-art29-31-information | `§§ Article 29`; every rule below |  |
| 29(1) | Article 29(1) | encoded | encoded | g8-art29-31-information; g8-penalties | `Art 29(1) the person must not disclose the information` (DEONTIC SHANT); `Art 29(1) the person commits an offence`; `Art 29(1) the person received information within Article 29(1)`; `Art 29(1) the disclosure has the consent Article 29(1) requires` (F8.11); `Art 29(1) the penalty the person is liable to`; `Art 29(1) the penalty provided for the offence`; `Art 29(1) the maximum fine` (named refusal) | subject to (2), 30 and 31; period P26: F8.8; the consent structure: F8.11 |
| 29(1)(a) | Article 29(1)(a) | encoded | encoded | g8-art29-31-information | `Art 29(1) the person received information within Article 29(1)` (field `received under or for the purposes of this Law`) |  |
| 29(1)(b) | Article 29(1)(b) | encoded | encoded | g8-art29-31-information | same rule (field `received directly or indirectly from a person who so received it`); the consent of the source is read only where this applies (`Art 29(1) reading A: both consents given`) |  |
| 29(2) | Article 29(2) | encoded | encoded | g8-art29-31-information | `Art 29(2) this Article does not apply to the information` |  |
| 29(2)(a) | Article 29(2)(a) | encoded | encoded | g8-art29-31-information | `Art 29(2)(a) the information is registered in the public parts of the register` (IP25 `the information is registered in a public part of the register`) |  |
| 29(2)(b) | Article 29(2)(b) | encoded | encoded | g8-art29-31-information | `Art 29(2)(b) the information is or has already been made available to the public from other sources` |  |
| 29(2)(c) | Article 29(2)(c) | encoded | encoded | g8-art29-31-information | `Art 29(2)(c) the information is in a form that identifies no particular person` |  |
| 30 | Article 30 | encoded | encoded | g8-art29-31-information | `§§ Article 30`; `Art 30 the disclosure is one the Commissioner must make` |  |
| 30(1) | Article 30(1) | encoded | encoded | g8-art29-31-information | `Art 30(1) the Commissioner must disclose information to the Comptroller` (DEONTIC MUST) | the Comptroller's requirement is an input; no time is stated, so no WITHIN |
| 30(2) | Article 30(2) | encoded | encoded | g8-art29-31-information | `Art 30(2) the Commissioner must disclose information to the JFSC` (DEONTIC MUST) | the JFSC's requirement is an input; no time is stated, so no WITHIN |
| 31 | Article 31 | encoded | encoded | g8-art29-31-information | `§§ Article 31`; `Art 31 the disclosure is permitted`; `Art 31 the provisions that permit the disclosure` |  |
| 31(a) | Article 31(a) | encoded | encoded | g8-art29-31-information | `Art 31(a) by or on behalf of the Commissioner, to enable the Commissioner to discharge a function` |  |
| 31(b) | Article 31(b) | encoded | encoded | g8-art29-31-information | `Art 31(b) to the Comptroller, to enable the Comptroller to discharge a function` | wider than the duty in 30(1): any function |
| 31(c) | Article 31(c) | encoded | encoded | g8-art29-31-information | `Art 31(c) to the JFSC, to enable it to discharge a function` | endnote [4] is an editorial change to these words; its marker stands on (f) in the text (contradictions) |
| 31(d) | Article 31(d) | encoded | encoded | g8-art29-31-information | `Art 31(d) to the Attorney General, the Bailiff or the court, to enable them to discharge a function in relation to charities` |  |
| 31(e) | Article 31(e) | encoded | encoded | g8-art29-31-information | `Art 31(e) to any person, for the investigation or prosecution of an offence or for taking or deciding whether to take proceedings under this Law` |  |
| 31(f) | Article 31(f) | encoded | encoded | g8-art29-31-information | `Art 31(f) in other circumstances prescribed by the States by Regulations`; `Art 31(f) the States may by Regulations prescribe other circumstances` (DEONTIC MAY) | the content of the Regulations is an input |
| 32 | Article 32 | inert | inert | g8-art32-36-appeals | `§§ Article 32`; quoted (src:685-688), no rule | constitutive; the Tribunal is the actor `the Charity Tribunal` of the rules of Articles 34 and 35 |
| 32(1) | Article 32(1) | inert | inert | g8-art32-36-appeals | quoted (src:686), no rule | establishes a body; nothing to compute |
| 32(2) | Article 32(2) | inert | inert | g8-art32-36-appeals | quoted (src:687), no rule | declares the Tribunal's function; the appeal rights are encoded at 33 to 35 |
| 32(3) | Article 32(3) | inert | inert | g8-art32-36-appeals | quoted (src:688), no rule | pointer to Schedule 2 (G9) |
| 33 | Article 33 | encoded | encoded | g8-art32-36-appeals | `Art 33 the right of appeal`; `Art 33 the person may appeal the decision` | closed list: F8.4; the answer 'no appeal is given by Part 8' is not a statement that no other remedy exists |
| 33(1) | Article 33(1) | encoded | encoded | g8-art32-36-appeals | `Art 33(1)(a) ...`, `Art 33(1)(b) ...` |  |
| 33(1)(a) | Article 33(1)(a) | encoded | encoded | g8-art32-36-appeals | `Art 33(1)(a) an applicant for registration appeals a refusal to register the applicant` |  |
| 33(1)(b) | Article 33(1)(b) | encoded | encoded | g8-art32-36-appeals | `Art 33(1)(b) an applicant for registration appeals a refusal to register the applicant in the restricted section` | a general-section charity's refused request (9(7)) is not within it: F8.4 |
| 33(2) | Article 33(2) | encoded | encoded | g8-art32-36-appeals | `Art 33(2)(a)` to `Art 33(2)(e)`; the analogies of reading B of F8.4 | a closed list: trap T12, F8.4 |
| 33(2)(a) | Article 33(2)(a) | encoded | encoded | g8-art32-36-appeals | `Art 33(2)(a) a registered charity appeals a decision to deregister the charity` | a refusal to deregister (15(3)(b)) is not a decision to deregister; a deregistration on the charity's own application: F8.16 |
| 33(2)(b) | Article 33(2)(b) | encoded | encoded | g8-art32-36-appeals | `Art 33(2)(b) a registered charity appeals a refusal of permission to change or add a registered name` |  |
| 33(2)(c) | Article 33(2)(c) | encoded | encoded | g8-art32-36-appeals | `Art 33(2)(c) a registered charity appeals a requirement to apply to change its registered name` |  |
| 33(2)(d) | Article 33(2)(d) | encoded | encoded | g8-art32-36-appeals | `Art 33(2)(d) a registered charity appeals a refusal of approval of an amendment of its purposes` |  |
| 33(2)(e) | Article 33(2)(e) | encoded | encoded | g8-art32-36-appeals | `Art 33(2)(e) a registered charity appeals a refusal to approve an amendment of its registered public benefit statement` |  |
| 33(3) | Article 33(3) | encoded | encoded | g8-art32-36-appeals | `Art 33(3) a person served with the notice appeals the decision to impose a requirement in it` |  |
| 33(4) | Article 33(4) | encoded | encoded | g8-art32-36-appeals | `Art 33(4) the Attorney General appeals a decision of the Commissioner` |  |
| 33(5) | Article 33(5) | encoded | encoded | g8-art32-36-appeals | `Art 33(5) a person other than the applicant, a registered charity or the Attorney General appeals a decision to register an applicant`; `Art 33(5) the appellant is a person other than those excluded`; `Art 33(5) a ground holds at the two times`; `Art 33(5) which ground` | who is excluded: F8.13; the 'both times' structure: F8.18 |
| 33(5)(a) | Article 33(5)(a) | encoded | encoded | g8-art32-36-appeals | `Art 33(5)(a) the applicant did not meet the charity test at both times` (IP9) |  |
| 33(5)(b) | Article 33(5)(b) | encoded | encoded | g8-art32-36-appeals | `Art 33(5)(b) the appellant has an interest in the name and it was undesirable at both times` (IP18) | open only to an appellant with an interest in the name |
| 34 | Article 34 | encoded | encoded | g8-art32-36-appeals | `§§ Article 34`; every rule below |  |
| 34(1) | Article 34(1) | encoded | encoded | g8-art32-36-appeals | `Art 34(1) the appeal has a ground` | wider than 35(1): F8.5 |
| 34(2) | Article 34(2) | encoded | encoded | g8-art32-36-appeals | `Art 34(2) the tribunal may make interim orders and consider evidence` (DEONTIC MAY RAND MAY); `Art 34(2)(a) ...`, `Art 34(2)(b) ...` |  |
| 34(2)(a) | Article 34(2)(a) | encoded | encoded | g8-art32-36-appeals | `Art 34(2)(a) the tribunal may make an interim order` (DEONTIC MAY) | 'as it thinks fit' is the Tribunal's judgement, not modelled |
| 34(2)(b) | Article 34(2)(b) | encoded | encoded | g8-art32-36-appeals | `Art 34(2)(b) the tribunal may consider evidence` (DEONTIC MAY) |  |
| 34(3) | Article 34(3) | encoded | encoded | g8-art32-36-appeals | `Art 34(3)(a)` to `Art 34(3)(c)` |  |
| 34(3)(a) | Article 34(3)(a) | encoded | encoded | g8-art32-36-appeals | `Art 34(3) the tribunal may determine the appeal` (DEONTIC MAY); `Art 34(3)(a) the way is one the tribunal may use` |  |
| 34(3)(b) | Article 34(3)(b) | encoded | encoded | g8-art32-36-appeals | `Art 34(3)(b) the tribunal may award costs` (DEONTIC MAY) | against whom is unstated (open question); the Tribunal's satisfaction is an input |
| 34(3)(c) | Article 34(3)(c) | encoded | encoded | g8-art32-36-appeals | `Art 34(3)(c) the tribunal may make a recommendation to the Commissioner` (DEONTIC MAY) | 'appears to be called for' is an input |
| 35 | Article 35 | encoded | encoded | g8-art32-36-appeals | `§§ Article 35`; every rule below |  |
| 35(1) | Article 35(1) | encoded | encoded | g8-art32-36-appeals | `Art 35(1) the party may appeal to the court`; `Art 35(1) reading A: ...`; `Art 35(1) reading B: ...` | F8.5 |
| 35(2) | Article 35(2) | encoded | encoded | g8-art32-36-appeals | `Art 35(2) the court may determine the appeal` (DEONTIC MAY); `Art 35(2) the way is one the court may use` |  |
| 35(3) | Article 35(3) | encoded | encoded | g8-art32-36-appeals | `Art 35(3) the tribunal may refer a point of law` (DEONTIC MAY) |  |
| 35(4) | Article 35(4) | encoded | encoded | g8-art32-36-appeals | `Art 35(4) the court may make an interim order` (DEONTIC MAY) |  |
| 36 | Article 36 | encoded | encoded | g8-art32-36-appeals | `§§ Article 36`; every rule below |  |
| 36(1) | Article 36(1) | encoded | encoded | g8-art32-36-appeals | `Art 36(1) the Commissioner may reconsider a decision` (DEONTIC MAY) | reads no fact about an appeal: Part 8 does not limit the power |
| 36(2) | Article 36(2) | encoded | encoded | g8-art32-36-appeals | `Art 36(2)(a)`, `Art 36(2)(b)`; `Art 36(2) the appeal is in time`; `Art 36(2) the last day to bring the appeal` | no Order is in the sources: 'in time' refuses when the Order is not supplied (P27: F8.6, F8.12) |
| 36(2)(a) | Article 36(2)(a) | encoded | encoded | g8-art32-36-appeals | `Art 36(2) the Minister may by Order set time limits` (DEONTIC MAY); `Art 36(2)(a) the last day of the time limit`; `Art 36(2) the day the time limit runs from` | anchor: F8.6; counting: F8.12 |
| 36(2)(b) | Article 36(2)(b) | encoded | encoded | g8-art32-36-appeals | `Art 36(2)(b) the Minister may by Order provide for notice of decisions and of reasons` (DEONTIC MAY) | 'appears to the Minister to be expedient' is an input |
| 36(3) | Article 36(3) | encoded | encoded | g8-art32-36-appeals | `Art 36(3) the court or tribunal may order the date from which the substituted decision takes effect` (DEONTIC MAY); `Art 36(3) the date from which the substituted decision takes effect`; `Art 36(3) the substituted decision takes effect from a date before the date of the order` | when no date is ordered the Law does not say: named refusal |
| 36(4) | Article 36(4) | encoded | encoded | g8-art32-36-appeals | `Art 36(4) the act is protected from the operation of the order`; `Art 36(4) the act is an offence in the light of the order` | parallel of 17(4) (G6) |

Totals: 104 rows; 96 encoded, 6 inert, 2 out-of-scope; not yet encoded: 0.  Dispositions changed from the plan: none.

## 2. Fork register

Record: `Interpretation of Articles 26 to 36` (declared in `g8-nouns`), one field per fork, each `TYPICALLY` the reading taken; 19 forks, ids F8.1 to F8.19 (F8.1 to F8.8 are the survey's, F8.9 to F8.19 are new).  The survey's F8.7 is reformulated and F8.2 has a third reading; see below.  The favoured interpretation and, for each fork, the favoured interpretation with the other reading of that fork alone are the fixtures of `g8-tests-fixtures` (generated by `genfix.py`).  Every public decision that depends on a fork takes the record as an ordinary `GIVEN` and delegates by `CONSIDER` to one private implementation per reading.  Every kind of period of G8 has a fork: P23 (F8.1, F8.9, F8.10), P24 (F8.2), P25 and P26 (F8.8), P27 (F8.6, F8.12), P28 (F8.7).

| id | field of the record | reading taken | other reading |
| --- | --- | --- | --- |
| F8.1 | `when the retention year of Article 26(5) starts` | `the year of Article 26(5) runs from the day the document is provided or retained` | `the year of Article 26(5) runs from the day of the notice` |
| F8.2 | `how promptness under Article 26(6) is judged` | `promptness under Article 26(6) is a judgement the caller supplies` | `promptness under Article 26(6) is a number of days from the request` ; `promptness under Article 26(6) is a number of days counting the day of the request as the first` |
| F8.3 | `whether Article 28(1)(a) reaches a philosophical belief purpose` | `only a purpose within Article 6(1)(c) counts under Article 28(1)(a)` | `a philosophical belief purpose also counts under Article 28(1)(a)` |
| F8.4 | `whether the list of appealable decisions in Article 33 is closed` | `the list of appealable decisions in Article 33 is closed` | `a decision unlisted in Article 33 is appealable by analogy with a listed one` |
| F8.5 | `on what ground a decision of the tribunal is appealed to the court` | `a decision of the tribunal is appealed to the court only on the ground in Article 35(1)` | `a decision of the tribunal is appealed to the court on any ground in Article 34(1)` |
| F8.6 | `from when an appeal time limit under Article 36(2) runs` | `an appeal time limit under Article 36(2) runs from the notice of the decision` | `an appeal time limit under Article 36(2) runs from the decision` |
| F8.7 | `how a period fixed by a notice under Article 26 or 27 is counted` | `the day of service is not counted in a period fixed by a notice` | `the day of service is the first day of a period fixed by a notice` |
| F8.8 | `unit of the terms of imprisonment in Articles 26 and 29` | `calendar months` | `days` |
| F8.9 | `where the retention year of Article 26(5) ends` | `the year of Article 26(5) ends on the anniversary of the day it starts` | `the year of Article 26(5) ends on the day before the anniversary of the day it starts` |
| F8.10 | `how a year is added to 29 February under Article 26(5)` | `a year of Article 26(5) from 29 February ends on 28 February` | `a year of Article 26(5) from 29 February ends on 1 March` |
| F8.11 | `which consents Article 29(1) requires` | `Article 29(1) requires both consents` | `Article 29(1) is met by either consent` |
| F8.12 | `whether the first day counts in an appeal time limit under Article 36(2)` | `the day of the anchor is not counted in an appeal time limit` | `the day of the anchor is the first day of an appeal time limit` |
| F8.13 | `who is excluded from appealing under Article 33(5)` | `any applicant for registration or registered charity is excluded from appealing under Article 33(5)` | `only the applicant concerned and the charity it became are excluded from appealing under Article 33(5)` |
| F8.14 | `what Article 27(1) requires of the Commissioner's belief` | `the Commissioner's belief alone is the ground under Article 27(1)` | `the Commissioner's belief must also be borne out under Article 27(1)` |
| F8.15 | `which notices may require a governor to be suspended, removed or replaced` | `only a notice under Article 27(1)(c) or (d) may require a governor to be suspended, removed or replaced` | `a notice on any ground in Article 27(1) may require a governor to be suspended, removed or replaced` |
| F8.16 | `whether Article 33(2)(a) reaches a deregistration on the charity's own application` | `Article 33(2)(a) reaches a deregistration granted on the charity's own application` | `Article 33(2)(a) does not reach a deregistration granted on the charity's own application` |
| F8.17 | `when a person must have been a governor to fall within Article 26(2)(b)` | `a governor at any time of an entity registered at any time falls within Article 26(2)(b)` | `a person falls within Article 26(2)(b) only if a governor while the entity was registered` |
| F8.18 | `how the two grounds of Article 33(5) combine with the two times` | `each ground of Article 33(5) must hold at both times` | `some ground of Article 33(5) must hold at each of the two times` |
| F8.19 | `which charity Article 26(4)(a) speaks of` | `the registered charity of Article 26(4)(a) is a charity registered now` | `the registered charity of Article 26(4)(a) is the charity or formerly registered entity demanded of` |

### F8.1 -- when does the one year of Article 26(5)(a) start?

- **Provision:** 26(5)(a), (b) (src:628-630); 26(4)(a) (src:626); 26(1) (src:618-619).
- **Kind of period / note:** P23: a retention period (a year, extended to the end of proceedings commenced within it).
- **Field and constructors:** field `when the retention year of Article 26(5) starts`; reading taken `the year of Article 26(5) runs from the day the document is provided or retained`; other reading `the year of Article 26(5) runs from the day of the notice`.
- **Reading taken (A) and the text that licenses it:** The year runs from the day the document, copy or extract is provided or retained under 26(4)(a).  Licensed by the opening words of 26(5), "A document, copy or extract retained or taken under paragraph (4)(a) may be retained for ...": what is retained or taken is retained for a period, and retention begins when it is retained.
- **Other reading (B) and the text that licenses it:** The year runs from the day of the notice under 26(1).  Licensed by 26(4) ("If the Commissioner exercises a power under paragraph (1) to require a document ..."): the notice is the one date in the chain that 26(5) can be read to refer back to, and 26(5) names no other start.
- **Why A:** The period is one of RETENTION; it cannot start before the Commissioner has the thing.  Under B the year could end before a late-provided document had been held for any time at all.
- **Implementation:** `Art 26(5)(a) the first day of the retention year` (CONSIDER arms); read by `Art 26(5)(b) proceedings were commenced within the retention year` and `Art 26(5) the Commissioner may keep the document until`.
- **Discriminating case:** Notice 2026-02-01, document provided 2026-02-20, proceedings commenced 2027-02-10 and not concluded.  A: the year is 2026-02-20 to 2027-02-20, the proceedings were commenced inside it, so the document is kept until they conclude.  B: the year is 2026-02-01 to 2027-02-01, the proceedings began after it, so the document may be kept only to 2027-02-01.  A second case: proceedings commenced 2026-02-10 (after the notice, before the document arrived) are inside the year on B and before it on A.
- **Test:** `g8-tests-art26`, section 26(5): the fixtures `T26 retention, proceedings commenced on 10 February 2027 and not concluded` and `T26 retention, proceedings commenced between the notice and the provision`, each under both readings; red: `g8-tests-red`, F8.1.

### F8.2 -- what is "as soon as practicable" in Article 26(6)?

- **Provision:** 26(6) (src:631).
- **Kind of period / note:** P24: a standard of promptness (no number; it starts with the request).
- **Field and constructors:** field `how promptness under Article 26(6) is judged`; reading taken `promptness under Article 26(6) is a judgement the caller supplies`; other reading `promptness under Article 26(6) is a number of days from the request`; third reading `promptness under Article 26(6) is a number of days counting the day of the request as the first`.
- **Reading taken (A) and the text that licenses it:** A judgement the caller supplies.  Licensed by the words themselves: "as soon as practicable" is an evaluative standard like "a reasonable time", and the Law gives no number.  The duty carries no WITHIN.
- **Other reading (B and C) and the text that licenses it:** B: a number of days from the request, the day of the request not counted; C: the same number counted with the day of the request as its first day.  Licensed only by the practice of measuring promptness against a period; the Law fixes none, so the number is an extra input.
- **Why A:** A number would be a period Parliament did not enact; the brief and the skill say a missing period is not invented.
- **Implementation:** `Art 26(6) the Commissioner must supply a copy of the retained document` and `Art 26(6) the copy was supplied as soon as practicable` (CONSIDER arms; private rules `Art 26(6) reading A: ...`, `reading B: ...`, `reading C: ...`).
- **Discriminating case:** Request 2026-05-01, copy supplied 2026-05-20, seven days.  A: the caller's judgement decides.  B and C: 19 days is over seven.  B against C: a copy supplied on 2026-05-08 (7 days after) is in time on B and late on C.
- **Test:** `g8-tests-art26`, section 26(6): the fixtures `T26 a request for a copy, copy supplied on ...` (7, 8, 9 and 20 May) under the three readings, and the traces with WITHIN 7 and WITHIN 6; red: F8.2.

### F8.3 -- does Article 28(1)(a) "by virtue of Article 6(1)(c)" reach a philosophical-belief purpose?

- **Provision:** 28(1)(a) (src:654); 6(1)(c) (src:170); 6(1)(p) (src:183); 6(2)(f) (src:194); trap T27.
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `whether Article 28(1)(a) reaches a philosophical belief purpose`; reading taken `only a purpose within Article 6(1)(c) counts under Article 28(1)(a)`; other reading `a philosophical belief purpose also counts under Article 28(1)(a)`.
- **Reading taken (A) and the text that licenses it:** No: only a purpose within Article 6(1)(c) itself (IP11) counts.  Licensed by the words "by virtue of Article 6(1)(c)" and by 6(2)(f), which makes a philosophical-belief purpose "analogous to" (c) "for the purposes of paragraph (1)(p)" - that is, a (p) purpose, not a (c) purpose.
- **Other reading (B) and the text that licenses it:** Yes: a philosophical-belief purpose counts.  Licensed by 6(2)(f)'s statement that such a purpose is analogous to (c): the Minister may regard it as within the same policy.
- **Why A:** The text names (c), not (p), and 6(2)(f) is drafted as an analogy, which is what puts the purpose under (p).
- **Implementation:** `Art 28(1)(a) the charity meets the charity test by virtue of Article 6(1)(c)` (CONSIDER arms; private rules reading A and reading B); read by `Art 28(1) the charity is eligible to be categorized as an organized religious charity`.
- **Discriminating case:** A humanist association that meets the charity test through 6(1)(p): A - not eligible to be categorized as an organized religious charity; B - eligible.
- **Test:** `g8-tests-art27-28`, section 28(1): `T28 a humanist association` and `T28 a church`; red: F8.3.

### F8.4 -- is the list of appealable decisions in Article 33 closed?

- **Provision:** 33(1) to (5) (src:690-703); 9(7) (src:284-286); 15(3)(b) (src:434); trap T12.
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `whether the list of appealable decisions in Article 33 is closed`; reading taken `the list of appealable decisions in Article 33 is closed`; other reading `a decision unlisted in Article 33 is appealable by analogy with a listed one`.
- **Reading taken (A) and the text that licenses it:** Closed.  The Attorney General alone may appeal any decision (33(4)); an unlisted decision gets "no appeal is given by Part 8" - which is not a statement that no other remedy exists (40(1) preserves independent powers).  Licensed by the form of 33(1) to (3), which lists decisions by kind.
- **Other reading (B) and the text that licenses it:** An unlisted decision of the same kind as a listed one is appealable by analogy.  The two the survey names, and the only two this reading adds: a registered charity's refused request for entry in the restricted section (9(7)), by analogy with 33(1)(b), and a charity's refused application to deregister (15(3)(b)), by analogy with 33(2)(a).  Licensed by 9(7)(a), which treats the refused request of a charity and of an applicant alike ("to the applicant or charity").
- **Why A:** A closed list is what the drafter wrote; an analogy would add rights of appeal the text does not give.
- **Implementation:** `Art 33 the right of appeal` (the BRANCH ends with the two analogy arms, each guarded by the reading), `Art 33(2) by analogy with Article 33(1)(b): ...` and `... Article 33(2)(a): ...`.
- **Discriminating case:** A charity in the general section asks for the restricted section and is refused (9(7)): A - no appeal; B - an appeal by analogy with 33(1)(b).  A charity's refused application to deregister (15(3)(b)): A - none; B - by analogy with 33(2)(a).
- **Test:** `g8-tests-art32-36`, sections 33(2) (the closed list and the F8.4 other reading) and 33(1); red: F8.4.

### F8.5 -- on what ground is a decision of the tribunal appealed to the court?

- **Provision:** 35(1) (src:714); 34(1) (src:705); 35(3) (src:716).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `on what ground a decision of the tribunal is appealed to the court`; reading taken `a decision of the tribunal is appealed to the court only on the ground in Article 35(1)`; other reading `a decision of the tribunal is appealed to the court on any ground in Article 34(1)`.
- **Reading taken (A) and the text that licenses it:** Only that the decision "was unreasonable having regard to all the circumstances of the case".  Licensed by the words of 35(1); a point of law reaches the court through the tribunal's own reference (35(3)).
- **Other reading (B) and the text that licenses it:** Any ground Article 34(1) allows for the tribunal, as well as that one.  Licensed by the parallel of the two appeals.
- **Why A:** The Law states two different grounds for two different appeals; reading 34(1) into 35(1) erases the difference.
- **Implementation:** `Art 35(1) the party may appeal to the court` (CONSIDER arms; private rules `Art 35(1) reading A: ...` and `reading B: ...`).
- **Discriminating case:** A party's complaint is that the tribunal's decision was wrong in law but not unreasonable: A - not a ground; B - a ground.
- **Test:** `g8-tests-art32-36`, section 35 (F8.5); red: F8.5.

### F8.6 -- from when does an appeal time limit under Article 36(2) run?

- **Provision:** 36(2)(a), (b) (src:721-722).
- **Kind of period / note:** P27: a deadline (the number of days is the content of an Order that is not in the sources; the Law fixes none).
- **Field and constructors:** field `from when an appeal time limit under Article 36(2) runs`; reading taken `an appeal time limit under Article 36(2) runs from the notice of the decision`; other reading `an appeal time limit under Article 36(2) runs from the decision`.
- **Reading taken (A) and the text that licenses it:** From the giving of notice of the decision.  Licensed by 36(2)(b), which provides for notice of decisions and reasons "for the purpose of enabling appeals to be brought within any time limits".  If notice has not been given the function refuses.
- **Other reading (B) and the text that licenses it:** From the decision itself.  Licensed by the plain meaning of a limit "within which appeals ... are to be brought" against a decision.
- **Why A:** The Law ties notice to the time limits in the same sentence.
- **Implementation:** `Art 36(2) the day the time limit runs from` (CONSIDER arms), read by `Art 36(2) the last day to bring the appeal` and `Art 36(2) the appeal is in time`.
- **Discriminating case:** Decision 2026-01-01, notice 2026-01-10, a limit of 30 days, appeal lodged 2026-02-05: A - in time (last day 2026-02-09); B - late (last day 2026-01-31).
- **Test:** `g8-tests-art32-36`, section 36(2): the lodging dates 31 January, 1 February, 5, 8, 9 and 10 February under both readings, and the case where no notice has been given; red: F8.6.

### F8.7 -- how is a period fixed by a notice counted (Articles 26(1)(a), (b) and 27(2))?

- **Provision:** 26(1)(a), (b) (src:619-620); 27(2) (src:646).
- **Kind of period / note:** P28: a deadline set by the Commissioner in a notice (a date, or a period running from service).
- **Field and constructors:** field `how a period fixed by a notice under Article 26 or 27 is counted`; reading taken `the day of service is not counted in a period fixed by a notice`; other reading `the day of service is the first day of a period fixed by a notice`.
- **Reading taken (A) and the text that licenses it:** A date fixed by the notice is the deadline.  A period of days fixed by the notice does not count the day of service: 14 days from service on 2026-06-01 end on 2026-06-15.  Licensed by the ordinary rule for a period running from an event.
- **Other reading (B) and the text that licenses it:** A period of days counts the day of service as its first day: it ends on 2026-06-14.  Licensed by reading "in a time specified" as running from the moment of service.
- **Why A:** As for F8.9.  (Changed from the survey: its discriminating case, a notice served by post on 2026-06-01 and received on 2026-06-03, turns on how the day of service is itself fixed, which is G7's fork F7.7 and Article 38.  Here the day of service is an input, IP34, and the fork is only whether that day is counted.)
- **Implementation:** `Art 26(1) the last day allowed by the notice`, `Art 26(1) the days allowed by the notice` (CONSIDER arms); read by `Art 26(7) the person must comply with the requirement` and `Art 27(2) the required steps notice served`.
- **Discriminating case:** A notice served 2026-06-01 fixing 14 days.  A: the last day is 2026-06-15, so compliance on day 14 and day 15 is in time; B: 2026-06-14, so compliance on day 14 is in time and day 15 is late (the trace is WITHIN 14 on A and WITHIN 13 on B).
- **Test:** `g8-tests-art26`, sections 26(1)(a), (b) and 26(7): date and period fixtures under both readings, the month-end case (14 days from 25 June, 28 days from 31 January), and the four traces; red: F8.7.

### F8.8 -- in what unit is a term of imprisonment measured in Articles 26(7), 26(10) and 29(1)?

- **Provision:** 26(7) "a term of 3 months" (src:632); 26(10) "2 years" (src:635); 29(1) "2 years" (src:667).
- **Kind of period / note:** P25, P26: a sentence.  IP35: the field is typed with the domain's `Unit of a term of imprisonment`, and the integrator sets it from one value for G6 (F6.16), G7 (F7.8), G8 (F8.8) and G9 (F9.13)..
- **Field and constructors:** field `unit of the terms of imprisonment in Articles 26 and 29`; reading taken `calendar months`; other reading `days`.
- **Reading taken (A) and the text that licenses it:** Calendar months: 3 months and 24 months (2 years).  A term starting on a day may last until the day that many calendar months on, clamped at a month end by `add months`.  Licensed by the Law's own units, months and years.
- **Other reading (B) and the text that licenses it:** Days: 3 months is 90 days and 2 years is 730 days.  Licensed by counting a month as 30 days and a year as 365.  The Law does not say so; the constants belong to this reading alone.
- **Why A:** The Law writes months and years, which are calendar units.
- **Implementation:** `Art 26 and 29 a term of imprisonment is within the maximum` (CONSIDER arms; private rules `Art 26 and 29 reading A: ...` and `reading B: ...`); the maxima are `Art 26 and 29 the maximum term in calendar months` and `... in days on the days reading`.
- **Discriminating case:** A term starting 2027-11-30 under 26(7): 91 days is within three calendar months (to 2028-02-29, clamped) on A and over 90 days on B.  The other way: from 2027-02-01 three calendar months are 89 days, so 90 days is within on B and over on A.  Two years from 2026-03-01 are 731 days (the second year holds 29 February 2028): within on A, over 730 on B.
- **Test:** `g8-tests-art26`, section "Tests of the penalties (F8.8)"; red: F8.8.

### F8.9 -- does the one year end on the anniversary of the day it starts, or on the day before?

- **Provision:** 26(5)(a) (src:629).
- **Kind of period / note:** P23 (counting: is the day of the event inside the period?).
- **Field and constructors:** field `where the retention year of Article 26(5) ends`; reading taken `the year of Article 26(5) ends on the anniversary of the day it starts`; other reading `the year of Article 26(5) ends on the day before the anniversary of the day it starts`.
- **Reading taken (A) and the text that licenses it:** The year ends on the anniversary of its start (a year from 20 February 2026 ends on 20 February 2027).  Licensed by counting a period "of one year" from a day without counting that day, and by the library's `add years`.
- **Other reading (B) and the text that licenses it:** The year ends on the day before the anniversary (19 February 2027): the start day is its first day.  Licensed by counting the start day, as a period expressed "beginning with" a day is counted.
- **Why A:** The Law does not say "beginning with", which is the drafter's way of making the anchor day the first day, so the day of the event is not counted in the ordinary way.
- **Implementation:** `Art 26(5)(a) the last day of the retention year` (CONSIDER arms).
- **Discriminating case:** Start 2026-02-20, proceedings commenced 2027-02-20 (the anniversary).  A: the last day is 2027-02-20, so they were commenced within the year and the document is kept until they conclude.  B: the last day is 2027-02-19, so they were commenced after it.
- **Test:** `g8-tests-art26`, section 26(5): `T26 retention, proceedings commenced on the anniversary` on both readings, and the edge assertions on `Art 26(5) retention is permitted on` (2027-02-19, 2027-02-20, 2027-02-21); red: F8.9.

### F8.10 -- what is a year from 29 February in Article 26(5)(a)?

- **Provision:** 26(5)(a) (src:629).
- **Kind of period / note:** P23 (how a year is added at the end of February).
- **Field and constructors:** field `how a year is added to 29 February under Article 26(5)`; reading taken `a year of Article 26(5) from 29 February ends on 28 February`; other reading `a year of Article 26(5) from 29 February ends on 1 March`.
- **Reading taken (A) and the text that licenses it:** 28 February of the next year.  Licensed by `daydate`'s `add years`, which uses the last day of the month when the day does not exist (as Excel's EDATE does).
- **Other reading (B) and the text that licenses it:** 1 March of the next year.  Licensed by the lenient `Date` constructor, which rolls a day that does not exist into the next month.
- **Why A:** The year ends in the same month it began; rolling into March makes a year from 29 February a year and a day.
- **Implementation:** `Art 26(5)(a) the anniversary of the day the year starts` (CONSIDER arms).
- **Discriminating case:** Document provided 2028-02-29, proceedings commenced 2029-03-01.  A: the last day is 2029-02-28, so the proceedings were commenced after the year; the document may be kept to 2029-02-28.  B: the last day is 2029-03-01, so they were commenced within it.
- **Test:** `g8-tests-art26`, section 26(5): `T26 retention from 29 February 2028, proceedings commenced on 1 March 2029` and `... no proceedings`; red: F8.10.

### F8.11 -- which consents does Article 29(1) require?

- **Provision:** 29(1) (src:667).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `which consents Article 29(1) requires`; reading taken `Article 29(1) requires both consents`; other reading `Article 29(1) is met by either consent`.
- **Reading taken (A) and the text that licenses it:** Both: the consent of the person to whom the information relates, and, where 29(1)(b) applies, the consent of the person from whom it was received; a disclosure lacking either is an offence.  Licensed by "without the consent of the person to whom it relates and ... the person from whom it was received" read as one requirement for both consents.
- **Other reading (B) and the text that licenses it:** Either consent suffices: it is an offence only if neither was given.  Licensed by reading "without the consent of A and B" as "without A's consent and without B's consent".
- **Why A:** The two persons have separate interests - the confidence of the person the information is about, and of the person who passed it on - and a disclosure needs the leave of both.
- **Implementation:** `Art 29(1) the disclosure has the consent Article 29(1) requires` (CONSIDER arms; private rules `Art 29(1) reading A: both consents given` and `reading B: either consent given`).
- **Discriminating case:** Information received from another recipient (29(1)(b)) and disclosed with the consent of the person it relates to only: A - an offence; B - none.  Where (b) does not apply the two readings agree.
- **Test:** `g8-tests-art29-31`, section "29(1) -- the offence, and the consent (F8.11)", every consent combination for each way of receiving; red: F8.11.

### F8.12 -- is the first day counted in an appeal time limit under Article 36(2)?

- **Provision:** 36(2)(a) (src:721).
- **Kind of period / note:** P27 (counting: is the day of the event inside the period?).
- **Field and constructors:** field `whether the first day counts in an appeal time limit under Article 36(2)`; reading taken `the day of the anchor is not counted in an appeal time limit`; other reading `the day of the anchor is the first day of an appeal time limit`.
- **Reading taken (A) and the text that licenses it:** The day the limit runs from is not counted: 30 days from 2026-01-10 end on 2026-02-09, and an appeal lodged on that day is in time.  Licensed by the ordinary rule.
- **Other reading (B) and the text that licenses it:** That day is the first day: the limit ends on 2026-02-08.
- **Why A:** As for F8.9.
- **Implementation:** `Art 36(2)(a) the last day of the time limit` (CONSIDER arms).
- **Discriminating case:** A limit of 30 days from a notice of 2026-01-10, appeal lodged 2026-02-09: A - in time; B - late.  Month end: 28 days from 2026-01-31 end on 2026-02-28 (A) or 2026-02-27 (B).
- **Test:** `g8-tests-art32-36`, section 36(2); red: F8.12.

### F8.13 -- who is excluded from appealing under Article 33(5)?

- **Provision:** 33(5) (src:701); 33(1), (2), (4).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `who is excluded from appealing under Article 33(5)`; reading taken `any applicant for registration or registered charity is excluded from appealing under Article 33(5)`; other reading `only the applicant concerned and the charity it became are excluded from appealing under Article 33(5)`.
- **Reading taken (A) and the text that licenses it:** Any applicant for registration and any registered charity, and the Attorney General: the three classes already have appeals under 33(1), (2) and (4).  A registered charity with an interest in a similar name therefore cannot use 33(5).  Licensed by the words "other than an applicant for registration, a registered charity, or the Attorney General".
- **Other reading (B) and the text that licenses it:** Only the applicant whose application is decided, the charity it became, and the Attorney General.  Licensed by the purpose: the person most likely to have an interest in a registered name is another charity.
- **Why A:** The words are general ("an applicant", "a registered charity"), where 33(1) and (2) are specific ("the applicant", "the charity").
- **Implementation:** `Art 33(5) the appellant is a person other than those excluded` (CONSIDER arms).
- **Discriminating case:** Another registered charity, with an interest in the name, appeals the registration of an applicant whose name was undesirable at both times: A - excluded; B - may appeal under 33(5)(b).  The applicant concerned, and the charity it became, are excluded on both.
- **Test:** `g8-tests-art32-36`, section 33(5); red: F8.13.

### F8.14 -- does Article 27(1) "if the Commissioner believes that" make the belief alone the ground?

- **Provision:** 27(1)(a) to (e) (src:640-645); 34(1) (src:705).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `what Article 27(1) requires of the Commissioner's belief`; reading taken `the Commissioner's belief alone is the ground under Article 27(1)`; other reading `the Commissioner's belief must also be borne out under Article 27(1)`.
- **Reading taken (A) and the text that licenses it:** The belief alone is the ground.  Licensed by the words "if the Commissioner believes that"; a belief that proves wrong is corrected on appeal, where 34(1) allows the ground that the decision was wrong or unreasonable "on the facts".
- **Other reading (B) and the text that licenses it:** The belief must also be borne out by the facts the other groups decide (IP8, IP12, IP14, IP15, IP16, IP21).  Licensed by the standard inputs the survey designated for 27(1) and by the expectation that a power conditioned on a belief about a charity's misconduct is conditioned on the misconduct.
- **Why A:** Belief is the statutory trigger; making truth the trigger replaces what the Law wrote.
- **Implementation:** `Art 27(1) the Commissioner has a ground to serve a required steps notice` (CONSIDER arms) with `Art 27(1) the belief is borne out`.
- **Discriminating case:** The Commissioner believes the registered charity has been guilty of misconduct but the facts show none (IP12 false): A - a ground; B - none.  Limb by limb for (b) to (e).
- **Test:** `g8-tests-art27-28`, section 27(1): all five limbs on both readings, the unregistered entity, and two beliefs of which one is borne out; red: F8.14.

### F8.15 -- may a notice on any ground of Article 27(1) require a governor to be suspended, removed or replaced?

- **Provision:** 27(4) (src:650); 27(2) (src:646); 28(3) (src:662).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `which notices may require a governor to be suspended, removed or replaced`; reading taken `only a notice under Article 27(1)(c) or (d) may require a governor to be suspended, removed or replaced`; other reading `a notice on any ground in Article 27(1) may require a governor to be suspended, removed or replaced`.
- **Reading taken (A) and the text that licenses it:** Only a notice under 27(1)(c) or (d).  Licensed by 27(4): "If the notice is served by virtue of paragraph (1)(c) or (d), the steps required may include ... the suspension, removal or replacement of the governor referred to in that paragraph" - only those paragraphs refer to a governor.
- **Other reading (B) and the text that licenses it:** A notice on any ground may, 27(4) only confirming what 27(2) ("steps ... appropriate to remedy the matter") already allows.  Licensed by the generality of 27(2), and by 28(3), which speaks of a notice that "purports to impose a requirement to suspend, remove or replace a governor" without limiting it to (c) and (d) notices.
- **Why A:** The one provision that names the governor-directed steps names the grounds that concern a governor; and 28(3) voids such a requirement on an organized religious charity whatever the ground of the notice, which says nothing about whether a non-(c)/(d) notice on another charity may require removal. 
- **Implementation:** `Art 27(4) the steps may include suspension, removal or replacement` (CONSIDER arms); the bar of Article 28 is applied first under both readings.
- **Discriminating case:** A notice under 27(1)(a) (the charity's own misconduct) on a charity that is not an organized religious charity: A - its steps may not include removing a governor; B - they may.  On an organized religious charity: never, on either.
- **Test:** `g8-tests-art27-28`, section 27(4); red: F8.15.

### F8.16 -- does Article 33(2)(a) "a decision to deregister the charity" reach a deregistration granted on the charity's own application?

- **Provision:** 33(2)(a) (src:694); 15(3)(a) (src:433); IP32.
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `whether Article 33(2)(a) reaches a deregistration on the charity's own application`; reading taken `Article 33(2)(a) reaches a deregistration granted on the charity's own application`; other reading `Article 33(2)(a) does not reach a deregistration granted on the charity's own application`.
- **Reading taken (A) and the text that licenses it:** Yes.  Licensed by the words, which do not distinguish why the Commissioner deregisters; a refusal to deregister under 15(3)(b) is not a decision to deregister on either reading.
- **Other reading (B) and the text that licenses it:** No: a charity cannot be aggrieved by what it asked for.  Licensed by the purpose of an appeal.
- **Why A:** The text distinguishes decisions by what the Commissioner does ("to deregister", "to refuse"), not by who asked; an appeal against a grant may still be on the ground that the decision was wrong in its terms.
- **Implementation:** `Art 33(2)(a) a registered charity appeals a decision to deregister the charity` (the decision's subject carries Article 15(3) or Article 16; IP32 `the basis of deregistration` is not needed).
- **Discriminating case:** A charity applies to deregister and the Commissioner deregisters it under 15(3)(a): A - it may appeal; B - it may not.
- **Test:** `g8-tests-art32-36`, section 33(2); red: F8.16.

### F8.17 -- when must a person have been a governor to fall within Article 26(2)(b)?

- **Provision:** 26(2)(b) (src:623); 2(7) (src:91-96).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `when a person must have been a governor to fall within Article 26(2)(b)`; reading taken `a governor at any time of an entity registered at any time falls within Article 26(2)(b)`; other reading `a person falls within Article 26(2)(b) only if a governor while the entity was registered`.
- **Reading taken (A) and the text that licenses it:** A governor or former governor of an entity that is, or was at some time, a registered charity falls within it, with no overlap in time required.  Licensed by the text, which pairs "a governor or former governor" with "a registered charity or ... an entity that was formerly a registered charity" and asks for no overlap.
- **Other reading (B) and the text that licenses it:** The person must have been a governor while the entity was registered.  Licensed by the purpose: the power to demand information serves a decision whether to serve a required steps notice, which only a registered charity's affairs prompt.
- **Why A:** No overlap is asked for in the text.
- **Implementation:** `Art 26(2)(b) the person is a governor or former governor of a registered charity or of a formerly registered entity` (CONSIDER arms; private rules `Art 26(2)(b) reading A: ...` and `reading B: ...`).
- **Discriminating case:** X was a governor of E only before E was registered; E is registered now: A - within 26(2)(b); B - not.
- **Test:** `g8-tests-art26`, section 26(2); red: F8.17.

### F8.18 -- how do the two grounds of Article 33(5) combine with the two times?

- **Provision:** 33(5), (5)(a), (5)(b) (src:701-703); IP9; IP18.
- **Kind of period / note:** (not a period: two points of time).
- **Field and constructors:** field `how the two grounds of Article 33(5) combine with the two times`; reading taken `each ground of Article 33(5) must hold at both times`; other reading `some ground of Article 33(5) must hold at each of the two times`.
- **Reading taken (A) and the text that licenses it:** Each ground must hold at both times: (a) at both, or (b) at both.  Licensed by the grammar of "on the ground that, at both the time of the application and the time of the appeal - (a) ...; or (b) ...", where "at both" qualifies each ground.
- **Other reading (B) and the text that licenses it:** Some ground must hold at each time: (a) or (b) at the application, and (a) or (b) at the appeal.  Licensed by reading "at both" as qualifying the disjunction.
- **Why A:** "At both the time of the application and the time of the appeal" attaches to the clause that introduces the grounds, and each ground is then stated of both times.
- **Implementation:** `Art 33(5) a ground holds at the two times` (CONSIDER arms) and `Art 33(5) which ground` (names (a), (b), or on B a mixture).
- **Discriminating case:** The charity test failed at the application but is met at the appeal; the name was acceptable at the application but undesirable at the appeal; the appellant has an interest: A - no ground; B - an appeal on grounds that differ between the two times.
- **Test:** `g8-tests-art32-36`, section 33(5); red: F8.18.

### F8.19 -- which charity does Article 26(4)(a) speak of?

- **Provision:** 26(4)(a) (src:626); 26(2)(a), (b) (src:622-623); Article 1 "registered charity" (src:34).
- **Kind of period / note:** (not a period).
- **Field and constructors:** field `which charity Article 26(4)(a) speaks of`; reading taken `the registered charity of Article 26(4)(a) is a charity registered now`; other reading `the registered charity of Article 26(4)(a) is the charity or formerly registered entity demanded of`.
- **Reading taken (A) and the text that licenses it:** A charity registered now.  Licensed by the Article 1 definition of the defined term "registered charity" (an entity entered for the time being in the general or the restricted section), and by 26(2), which shows the drafter knows how to say "formerly".
- **Other reading (B) and the text that licenses it:** The charity or formerly registered entity demanded of.  Licensed by the purpose: the explanation serves the demand, and 26(2) lets the demand reach a formerly registered entity.
- **Why A:** A defined term means what it defines; 26(2) says "formerly" where it means it.
- **Implementation:** `Art 26(4)(a) an explanation of the document may be required of the person` (CONSIDER arms).
- **Discriminating case:** The Commissioner demanded a document of a formerly registered entity and asks a person who appears to be an employee of it for an explanation: A - may not; B - may.  The person who provided the document may be asked on either.
- **Test:** `g8-tests-art26`, section 26(4); red: F8.19.

## 3. Answer table

The headline scenarios, each with the Article that decides it, the exact export and the test that asserts it.  Every answer is on the readings taken (the favoured interpretation) unless a reading is named.  Dates are the tests' own.

| scenario | answer | Article | export | test (module, section) |
| --- | --- | --- | --- | --- |
| A registered charity in the general section; the demand is for determining whether to serve a required steps notice; the Commissioner reasonably requires it | the Commissioner has the power, and the MAY stands | 26(1), 26(2)(a) | `Art 26(1) the Commissioner has the power to demand`; `Art 26(1) the Commissioner may require the person to provide information or attend` | `g8-tests-art26`, 26(1) |
| An applicant for registration that was never registered, same demand | no power (the answer is FALSE; 26(2) is a closed list, so this is not a gap) | 26(2) | same | `g8-tests-art26`, 26(2) and 26(1) |
| A registered charity, but the demand is for an application for registration | no power under 26(1) (the purpose of 26(1) is the notice; 26(10) names two) | 26(1), T23 | same | `g8-tests-art26`, 26(1) |
| An applicant that was once a registered charity; a former governor of an entity in the historic section | within 26(2) | 26(2)(a), (b) | `Art 26(2) the person falls within Article 26(2)` | `g8-tests-art26`, 26(2) |
| A notice served on 2026-06-01 fixing 14 days | the last day is 2026-06-15 (day of service not counted); 2026-06-14 on the other reading of F8.7; compliance on day 14 is in time on the first, late on the second | 26(1), 27(2), 26(7) | `Art 26(1) the last day allowed by the notice`; `Art 26(7) the person must comply with the requirement` | `g8-tests-art26`, 26(1)(a),(b) and 26(7) |
| A document provided on 2026-02-20 under a notice of 2026-02-01, no proceedings | may be retained up to and including 2027-02-20; with proceedings commenced 2027-02-10 and not concluded, until they conclude | 26(5) | `Art 26(5) the Commissioner may keep the document until` | `g8-tests-art26`, 26(5) |
| A copy requested on 2026-05-01 and supplied on 2026-05-20 | "as soon as practicable" is the caller's judgement; with a seven-day number it was late | 26(6) | `Art 26(6) the copy was supplied as soon as practicable` | `g8-tests-art26`, 26(6) |
| A valid requirement not complied with, no privilege, no reasonable excuse | an offence: 3 months and a fine of level 3 on the standard scale (the amount of level 3 is not in the sources: a named refusal) | 26(7), 26(8) | `Art 26(7) the person commits an offence`; `Art 26(7) the penalty the person is liable to` | `g8-tests-art26`, 26(7) and 26(8) |
| Information known to be false in a material particular, intended for an application for registration or for deciding whether to serve a required steps notice | an offence: 2 years and a fine with no maximum stated; whether it is in a document or provided under Article 26 is irrelevant | 26(10), 26(11) | `Art 26(10) the person commits an offence`; `Art 26(10) the person must not give false information` | `g8-tests-art26`, 26(10) and 26(11) |
| A statement made in compliance with a requirement, tendered by the prosecution against its maker | barred in criminal proceedings other than under 26(7) or (10); not barred otherwise (TRUE of "may be used" means only that Article 26(9) does not bar it) | 26(9) | `Art 26(9) the statement may be used by the prosecution` | `g8-tests-art26`, 26(9) |
| The Commissioner believes a governor has engaged in misconduct; the entity is a registered charity | a ground under 27(1)(c); on the other reading only if IP14 bears it out | 27(1) | `Art 27(1) the Commissioner has a ground to serve a required steps notice` | `g8-tests-art27-28`, 27(1) |
| A notice on the ground of a governor's misconduct, on a charity that is not an organized religious charity | its steps may include suspension, removal or replacement of a governor; for a notice on the charity's own misconduct, not (default); never for an organized religious charity | 27(4), 28(3) | `Art 27(4) the steps may include suspension, removal or replacement` | `g8-tests-art27-28`, 27(4) |
| A notice on an organized religious charity requiring removal of a governor of it, and a report | the removal requirement is invalid, the report stands | 28(3) | `Art 28(3) the required steps notice is invalid to the extent`; `Art 28(3) the requirements of the notice that remain valid` | `g8-tests-art27-28`, 28(3) |
| A humanist association whose charity test is met through 6(1)(p) | not eligible to be categorized as an organized religious charity (default); eligible on the other reading of F8.3 | 28(1)(a), 6(2)(f) | `Art 28(1) the charity is eligible to be categorized as an organized religious charity` | `g8-tests-art27-28`, 28(1) |
| Information received under the Law, disclosed to a stranger with no consent | an offence: 2 years and a fine with no maximum stated | 29(1) | `Art 29(1) the person commits an offence` | `g8-tests-art29-31`, 29(1) |
| The same information registered in a public part of the register, or already public, or in a summary identifying no one | no offence | 29(2) | `Art 29(2) this Article does not apply to the information` | `g8-tests-art29-31`, 29(2) |
| The same disclosure to the Comptroller to enable the Comptroller to discharge a function; or by the Commissioner because the Comptroller requires it | no offence | 31(b); 30(1) | `Art 31 the disclosure is permitted`; `Art 30 the disclosure is one the Commissioner must make` | `g8-tests-art29-31`, 29(1) with Articles 30 and 31 |
| Information received from another recipient, disclosed with the consent of the person it relates to only | an offence (default: both consents are required); none on the other reading | 29(1), F8.11 | `Art 29(1) the person commits an offence` | `g8-tests-art29-31`, 29(1) consent |
| An applicant refused registration | may appeal | 33(1)(a) | `Art 33 the person may appeal the decision`; `Art 33 the right of appeal` | `g8-tests-art32-36`, 33(1) |
| A registered charity in the general section refused entry in the restricted section; a charity refused deregistration on its own application | no appeal is given by Part 8 (the list is closed; not a statement that no other remedy exists); an appeal by analogy on the other reading of F8.4 | 33, T12 | `Art 33 the right of appeal` | `g8-tests-art32-36`, 33(2) |
| A registered charity refused permission to change its name (12(4)); required to apply to change it (12(6)); refused approval of a purposes amendment (13(3)) or of a public benefit statement amendment (13(4)(b)); deregistered (16) | may appeal, under 33(2)(b), (c), (d), (e), (a) respectively | 33(2) | same | `g8-tests-art32-36`, 33(2) |
| The Attorney General, any decision of the Commissioner | may appeal | 33(4) | same | `g8-tests-art32-36`, 33(4) |
| A stranger against the registration of an applicant whose charity test failed at the application and fails at the appeal | may appeal under 33(5)(a); not if it failed at one time only (default) | 33(5)(a), F8.18 | same | `g8-tests-art32-36`, 33(5) |
| A decision of the tribunal that is wrong in law but not unreasonable | not a ground of appeal to the court (default); a ground on the other reading of F8.5 | 35(1), 34(1) | `Art 35(1) the party may appeal to the court` | `g8-tests-art32-36`, 35 |
| Decision 2026-01-01, notice 2026-01-10, a limit of 30 days, lodged 2026-02-05 | in time (the last day is 2026-02-09); late if the limit runs from the decision (last day 2026-01-31) | 36(2) | `Art 36(2) the appeal is in time` | `g8-tests-art32-36`, 36(2) |
| The same appeal, no Order supplied | refuses (no Order is among the sources); TRUE if the caller says no Order has prescribed a limit | 36(2) | same | `g8-tests-art32-36`, 36(2) |
| An act before the date of an order that takes effect from an earlier date, made an offence only by the order's operation | not an offence | 36(4) | `Art 36(4) the act is an offence in the light of the order` | `g8-tests-art32-36`, 36(3) and 36(4) |

## 4. Nouns requests for the INTEGRATOR

`domain.l4` is read-only to G8, and every noun G8 needed beyond it is defined in `g8-nouns` (its own group).  What the integrator may want to do about them, and about three things in `domain.l4` itself:

1. **A name collision in `domain.l4`.**  The constructor `the registered charity` of `Recipient of a required steps notice` has the same name as the standard `GIVEN` of IP7, `the registered charity` : `Registered charity`.  A module that declares the `GIVEN` and also names the constructor sees the parameter and not the constructor (the parameter shadows it).  G8 uses the constructor as a value (`g8-tests-art27-28`, `Art 27(2) the required steps notice served`), and declares no `GIVEN` of that name.  Suggest renaming the constructor (for example `the registered charity itself`), or the standard `GIVEN`.
2. **Field names in `domain.l4` that begin with "is" or "has"** (`is a natural person`, `is resident in Jersey`, `is itself a Jersey entity by virtue of Article 2(3)(a)`, `is a Jersey entity`, `is purely ancillary or incidental to a charitable purpose of the entity`, `is advancing a political party or promoting a candidate for election`, `is advancing a philosophical belief`, `is an organized religious charity`, `has been complied with`).  The repository's naming ruling asks for a noun phrase, since the genitive supplies the verb.  They are not G8's to rename.  `g8-art27-28-required-steps` reads one of them (`is advancing a philosophical belief`, in `Art 28(1)(a) reading B`), so a rename there needs one line changed here.
3. **Two nouns that G6 or G7 may want to share.**  `Time specified in a notice` (a date, or a number of days after the day of service) and `Requirement in a required steps notice` (a kind of requirement, and whether it is about a governor of the charity concerned) are defined in `g8-nouns`.  G6's Article 16(1) notice ("a reasonable time specified in the notice") and Article 19(9)(e)(i) (a required steps notice "requiring the charity to suspend or remove the governor", the trap T11) read the same shapes.  If G6 needs them, the integrator should move them to `domain.l4`; their names carry no Article number that would mislead.
4. **`Required steps notice.steps to be taken by` is a `MAYBE DATE`** in `domain.l4`.  Article 27(2) requires the notice to specify a time, so `Art 27(2) the required steps notice served` always fills it with `JUST`; the `MAYBE` costs a consumer a match that never reaches `NOTHING` for a notice built by G8.
5. **`Penalty provided` stores months only.**  The days reading of F8.8 needs the Law's own unit (3 months, 2 years), which the record loses.  G8 keeps the days equivalents (90 and 730) as constants of reading B in `g8-penalties` and does not touch the record.  G6, G7 and G9 may need the same treatment (IP35).
6. **IP32 is not consumed by G8.**  The decision's subject (`Article 15(3)` or `Article 16`) already carries the distinction that 33(2)(a) turns on (F8.16), so `the basis of deregistration` is not needed here.
7. **IP7 is not consumed by G8** (no rule of Articles 26 to 36 reads a field of `the registered charity`); IP20 is produced by `Art 28 the entity is an organized religious charity` and consumed by `Art 27(4) ...` and `Art 28(3) ...` through a `GIVEN` of the standard name, as PLAN section (c) says, so the integrator wires the producer to those two consumers.
8. **IP11 is read by `Art 28(1)(a) ...` and not by `Art 28 the entity is an organized religious charity`.**  The Minister's appearance that a charity meets the test by virtue of 6(1)(c) bears on the Minister's POWER to categorize (`Art 28(1) the charity is eligible to be categorized as an organized religious charity`); the status itself is the Order's categorization plus any grant or withdrawal under 28(2)(a).
9. **The outcome constructors that Article 33 expects from the producers of IP27 (wire by name).**  G8 produces the decisions of Articles 26 and 27 (`Art 26 the decision of the Commissioner to impose a requirement`, `Art 27 the decision of the Commissioner to impose a requirement`).  For the decisions the other groups produce, `Art 33 the right of appeal` reads the outcome as follows, and a producer that picks the other constructor silently turns an appealable decision into "no appeal is given by Part 8":
   - `the Commissioner does what was sought or proposed` for a decision to ACT: to deregister (33(2)(a), subject `whether to deregister a charity in other cases, Article 16`, or `... on its own application, Article 15(3)`), to REQUIRE a charity to apply to change its registered name (33(2)(c), subject `whether to require a charity to apply to change its registered name, Article 12(6)`: a requirement, not a request, so "sought or proposed" is read as "the Commissioner's own proposal, carried out"), to impose a requirement in a notice (33(3)), and to register an applicant (33(5), subject `whether to register an applicant, Article 11`);
   - `the Commissioner refuses` for a decision to REFUSE: to refuse registration (33(1)(a)), to refuse the restricted section (33(1)(b)), to refuse permission for a name (33(2)(b), 12(4)), to refuse approval of a purposes amendment (33(2)(d), 13(3)) or of a public benefit statement amendment (33(2)(e), 13(4)(b)), and (reading B of F8.4 only) a refused request for the restricted section by a charity (9(7)) or a refused application to deregister (15(3)(b)).
   A decision that does not belong to one of these subjects is `any other matter`, which only the Attorney General may appeal (33(4)).

## 5. Standard inputs consumed, and functions exported

Generated from the `@export` blocks of the four rule modules and `g8-penalties` by `work/g8/mkexports.py`, so the names are exactly the modules' own.  Every parameter is an ordinary `GIVEN` with a `@desc`.  A parameter whose name is a standard name of PLAN section (c) is marked with its integration point; every other parameter is a fact (or discretion) local to G8 and has no producer in another group.

### 5.1 The functions exported (exact names)

| module | export (exact name) | takes (name : type [IP]) | gives |
| --- | --- | --- | --- |
| g8-art26-demand | `Art 26(2) the person falls within Article 26(2)` | `interp` : `Interpretation of Articles 26 to 36`; `person` : `Person addressed by a notice under Article 26` | `BOOLEAN` |
| g8-art26-demand | `Art 26(1) the Commissioner has the power to demand` | `interp` : `Interpretation of Articles 26 to 36`; `person` : `Person addressed by a notice under Article 26`; `demand` : `Demand for information under Article 26(1)` | `BOOLEAN` |
| g8-art26-demand | `Art 26(1) the Commissioner may require the person to provide information or attend` | `interp` : `Interpretation of Articles 26 to 36`; `person` : `Person addressed by a notice under Article 26`; `demand` : `Demand for information under Article 26(1)` | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art26-demand | `Art 26 the decision of the Commissioner to impose a requirement` | `the Commissioner imposes the requirement` : BOOLEAN | `Decision of the Commissioner` |
| g8-art26-demand | `Art 26(1) the last day allowed by the notice` | `interp` : `Interpretation of Articles 26 to 36`; `spec` : `Time specified in a notice`; `the date on which the notice was served` : DATE [IP34] | `DATE` |
| g8-art26-demand | `Art 26(4)(a) the Commissioner may retain or copy the document and require an explanation` | `the Commissioner has exercised the power under Article 26(1) to require the document` : BOOLEAN; `the document is provided` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art26-demand | `Art 26(4)(a) an explanation of the document may be required of the person` | `interp` : `Interpretation of Articles 26 to 36`; `person` : `Person asked for an explanation of a document` | `BOOLEAN` |
| g8-art26-demand | `Art 26(4)(b) the Commissioner may require a statement of where the document is` | `the Commissioner has exercised the power under Article 26(1) to require the document` : BOOLEAN; `the document is provided` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art26-demand | `Art 26(5) the Commissioner may keep the document until` | `interp` : `Interpretation of Articles 26 to 36`; `facts` : `Facts of the retention of a document under Article 26(5)` | `End of the retention of a document under Article 26(5)` |
| g8-art26-demand | `Art 26(5) retention is permitted on` | `interp` : `Interpretation of Articles 26 to 36`; `facts` : `Facts of the retention of a document under Article 26(5)`; `day` : DATE | `BOOLEAN` |
| g8-art26-demand | `Art 26(6) the Commissioner must supply a copy of the retained document` | `interp` : `Interpretation of Articles 26 to 36`; `request` : `Request for a copy of a retained document`; `days` : MAYBE NUMBER | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art26-demand | `Art 26(6) the copy was supplied as soon as practicable` | `interp` : `Interpretation of Articles 26 to 36`; `request` : `Request for a copy of a retained document`; `days` : MAYBE NUMBER; `the copy was supplied as soon as practicable in the caller's judgement` : BOOLEAN | `BOOLEAN` |
| g8-art26-demand | `Art 26(7) the person must comply with the requirement` | `interp` : `Interpretation of Articles 26 to 36`; `spec` : `Time specified in a notice`; `the date on which the notice was served` : DATE [IP34] | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art26-demand | `Art 26(7) the person commits an offence` | `facts` : `Facts of a contravention under Article 26(7)` | `BOOLEAN` |
| g8-art26-demand | `Art 26(9) the statement may be used by the prosecution` | `statement` : `Statement made under Article 26` | `BOOLEAN` |
| g8-art26-demand | `Art 26(10) the person must not give false information` | (none) | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art26-demand | `Art 26(10) the person commits an offence` | `facts` : `Facts of providing information under Article 26(10)` | `BOOLEAN` |
| g8-art27-28-required-steps | `Art 27(1) the Commissioner has a ground to serve a required steps notice` | `interp` : `Interpretation of Articles 26 to 36`; `the entity is a registered charity` : BOOLEAN [IP6]; `the Commissioner's beliefs` : LIST OF `Belief that prompts a required steps notice`; `the conduct is misconduct within Article 2(10)` : BOOLEAN [IP12]; `the entity meets the charity test` : BOOLEAN [IP8]; `the governor has engaged in misconduct within Article 18(4)` : BOOLEAN [IP14]; `the entity` : Entity [IP5 (and IP21 through its governors)]; `a governor is unfit by reason of a reportable matter` : BOOLEAN; `the requirement of Article 11(4)(c) is met` : BOOLEAN [IP15]; `the requirement of Article 11(4)(d) is met` : BOOLEAN [IP16] | `LIST OF Belief that prompts a required steps notice` |
| g8-art27-28-required-steps | `Art 27(2) the Commissioner may serve a required steps notice` | `grounds` : LIST OF `Belief that prompts a required steps notice`; `belief` : `Belief that prompts a required steps notice`; `the person is a relevant person` : BOOLEAN; `the notice specifies the steps and a time for them` : BOOLEAN; `the steps are in the Commissioner's opinion appropriate to remedy the matter` : BOOLEAN; `the procedure and restrictions of any Order under Article 27(5) are met` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art27-28-required-steps | `Art 27 the decision of the Commissioner to impose a requirement` | `the Commissioner imposes the requirement` : BOOLEAN | `Decision of the Commissioner` |
| g8-art27-28-required-steps | `Art 27(2) the required steps notice served` | `interp` : `Interpretation of Articles 26 to 36`; `recipient` : `Recipient of a required steps notice`; `belief` : `Belief that prompts a required steps notice`; `the date on which the notice was served` : DATE [IP34]; `spec` : `Time specified in a notice`; `requirements` : LIST OF `Requirement in a required steps notice`; `the steps required have been taken` : BOOLEAN | `Required steps notice` |
| g8-art27-28-required-steps | `Art 27(4) the steps may include suspension, removal or replacement` | `interp` : `Interpretation of Articles 26 to 36`; `belief` : `Belief that prompts a required steps notice`; `the entity is an organized religious charity` : BOOLEAN [IP20] | `BOOLEAN` |
| g8-art27-28-required-steps | `Art 27(5) the Minister may by Order make further provision` | (none) | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art27-28-required-steps | `Art 28(1)(a) the charity meets the charity test by virtue of Article 6(1)(c)` | `interp` : `Interpretation of Articles 26 to 36`; `the entity meets the charity test` : BOOLEAN [IP8]; `the entity has a purpose within Article 6(1)(c)` : BOOLEAN [IP11]; `the entity` : Entity [IP5 (and IP21 through its governors)] | `BOOLEAN` |
| g8-art27-28-required-steps | `Art 28(1) the charity is eligible to be categorized as an organized religious charity` | `interp` : `Interpretation of Articles 26 to 36`; `the entity is a registered charity` : BOOLEAN [IP6]; `the entity meets the charity test` : BOOLEAN [IP8]; `the entity has a purpose within Article 6(1)(c)` : BOOLEAN [IP11]; `the entity` : Entity [IP5 (and IP21 through its governors)]; `it appears to the Minister that the charity is organized so that the supervision and discipline of its governors in respect of its activities in Jersey is adequate` : BOOLEAN | `BOOLEAN` |
| g8-art27-28-required-steps | `Art 28(1) the Minister may by Order provide for the charity to be categorized` | `the charity is eligible to be categorized` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art27-28-required-steps | `Art 28(2)(a) the Commissioner may grant or withdraw the status` | `the Order gives the Commissioner discretion to grant or withdraw the status` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art27-28-required-steps | `Art 28 the entity is an organized religious charity` | `the entity is a registered charity` : BOOLEAN [IP6]; `order` : `Order under Article 28 as it applies to a charity` | `BOOLEAN` |
| g8-art27-28-required-steps | `Art 28(3) the required steps notice is invalid to the extent` | `the entity is an organized religious charity` : BOOLEAN [IP20]; `requirement` : `Requirement in a required steps notice` | `BOOLEAN` |
| g8-art27-28-required-steps | `Art 28(3) the requirements of the notice that remain valid` | `the entity is an organized religious charity` : BOOLEAN [IP20]; `requirements` : LIST OF `Requirement in a required steps notice` | `LIST OF Requirement in a required steps notice` |
| g8-art29-31-information | `Art 29(1) the person commits an offence` | `interp` : `Interpretation of Articles 26 to 36`; `the information is registered in a public part of the register` : BOOLEAN [IP25]; `info` : `Information received and its character`; `disclosure` : `Disclosure of information` | `BOOLEAN` |
| g8-art29-31-information | `Art 29(1) the person must not disclose the information` | `interp` : `Interpretation of Articles 26 to 36`; `the information is registered in a public part of the register` : BOOLEAN [IP25]; `info` : `Information received and its character`; `disclosure` : `Disclosure of information` | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art29-31-information | `Art 29(2) this Article does not apply to the information` | `the information is registered in a public part of the register` : BOOLEAN [IP25]; `info` : `Information received and its character` | `BOOLEAN` |
| g8-art29-31-information | `Art 30(1) the Commissioner must disclose information to the Comptroller` | `the Comptroller requires the information for its functions in relation to the taxation of registered charities or other entities with charitable purposes` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art29-31-information | `Art 30(2) the Commissioner must disclose information to the JFSC` | `the JFSC requires the information for its functions under the Non-Profit Organizations (Jersey) Law 2008` : BOOLEAN | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art29-31-information | `Art 31(f) the States may by Regulations prescribe other circumstances` | (none) | `DEONTIC Legal actor Act under Article 26 to 31` |
| g8-art29-31-information | `Art 31 the disclosure is permitted` | `disclosure` : `Disclosure of information` | `BOOLEAN` |
| g8-art32-36-appeals | `Art 33 the right of appeal` | `interp` : `Interpretation of Articles 26 to 36`; `appeal` : `Appeal under Article 33`; `the entity met the charity test at the time of the application` : BOOLEAN [IP9]; `the entity meets the charity test at the time of the appeal` : BOOLEAN [IP9]; `the name is undesirable under Article 12(1) at the time of the application` : BOOLEAN [IP18]; `the name is undesirable under Article 12(1) at the time of the appeal` : BOOLEAN [IP18] | `Right of appeal under Article 33` |
| g8-art32-36-appeals | `Art 33 the person may appeal the decision` | `interp` : `Interpretation of Articles 26 to 36`; `appeal` : `Appeal under Article 33`; `the entity met the charity test at the time of the application` : BOOLEAN [IP9]; `the entity meets the charity test at the time of the appeal` : BOOLEAN [IP9]; `the name is undesirable under Article 12(1) at the time of the application` : BOOLEAN [IP18]; `the name is undesirable under Article 12(1) at the time of the appeal` : BOOLEAN [IP18] | `BOOLEAN` |
| g8-art32-36-appeals | `Art 34(1) the appeal has a ground` | `ground` : `Ground alleged in an appeal` | `BOOLEAN` |
| g8-art32-36-appeals | `Art 34(2)(a) the tribunal may make an interim order` | `an appeal is before the tribunal` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 34(2)(b) the tribunal may consider evidence` | `an appeal is before the tribunal` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 34(2) the tribunal may make interim orders and consider evidence` | `an appeal is before the tribunal` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 34(3) the tribunal may determine the appeal` | `an appeal is before the tribunal` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 34(3)(b) the tribunal may award costs` | `the tribunal is satisfied that the appeal was vexatious or otherwise grossly unreasonable` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 34(3)(c) the tribunal may make a recommendation to the Commissioner` | `a recommendation appears to the tribunal to be called for in the circumstances of the case` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 35(1) the party may appeal to the court` | `interp` : `Interpretation of Articles 26 to 36`; `the person is a party to the appeal to the tribunal` : BOOLEAN; `the person is the Attorney General` : BOOLEAN; `ground` : `Ground alleged in an appeal` | `BOOLEAN` |
| g8-art32-36-appeals | `Art 35(2) the court may determine the appeal` | `an appeal is before the court` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 35(3) the tribunal may refer a point of law` | `an appeal is before the tribunal` : BOOLEAN; `a point of law arises` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 35(4) the court may make an interim order` | `an appeal or reference is before the court` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 36(1) the Commissioner may reconsider a decision` | `the decision is a decision of the Commissioner or of the Commissioner's staff` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 36(2) the Minister may by Order set time limits` | (none) | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 36(2)(b) the Minister may by Order provide for notice of decisions and of reasons` | `it appears to the Minister to be expedient for the purpose of enabling appeals to be brought within any time limits` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 36(2) the last day to bring the appeal` | `interp` : `Interpretation of Articles 26 to 36`; `dates` : `Dates of an appeal under Article 36(2)`; `days` : NUMBER | `DATE` |
| g8-art32-36-appeals | `Art 36(2) the appeal is in time` | `interp` : `Interpretation of Articles 26 to 36`; `dates` : `Dates of an appeal under Article 36(2)`; `limit` : MAYBE `Time limit prescribed under Article 36(2)(a)` | `BOOLEAN` |
| g8-art32-36-appeals | `Art 36(3) the court or tribunal may order the date from which the substituted decision takes effect` | `the court or the tribunal` : `Legal actor`; `it substitutes its decision for another decision` : BOOLEAN; `the date appears to it to be appropriate` : BOOLEAN | `DEONTIC Legal actor Act under Article 32 to 36` |
| g8-art32-36-appeals | `Art 36(3) the date from which the substituted decision takes effect` | `the date ordered` : MAYBE DATE | `DATE` |
| g8-art32-36-appeals | `Art 36(4) the act is an offence in the light of the order` | `the substituted decision takes effect from a date before the date of the order` : BOOLEAN; `the act occurred before the date of the order` : BOOLEAN; `the act is an offence apart from the order` : BOOLEAN; `the act is an offence only by the operation of the order` : BOOLEAN | `BOOLEAN` |
| g8-penalties | `Art 26 and 29 a term of imprisonment is within the maximum` | `interp` : `Interpretation of Articles 26 to 36`; `offence` : `Offence under Article 26 or 29`; `start` : DATE; `length` : NUMBER | `BOOLEAN` |

### 5.2 The standard inputs G8 consumes

| IP | standard name (exact, as a GIVEN) | consumed by |
| --- | --- | --- |
| IP5 | `the entity` | `Art 27(1) the Commissioner has a ground to serve a required steps notice`; `Art 28(1) the charity is eligible to be categorized as an organized religious charity`; `Art 28(1)(a) the charity meets the charity test by virtue of Article 6(1)(c)` |
| IP6 | `the entity is a registered charity` | `Art 27(1) the Commissioner has a ground to serve a required steps notice`; `Art 28 the entity is an organized religious charity`; `Art 28(1) the charity is eligible to be categorized as an organized religious charity` |
| IP8 | `the entity meets the charity test` | `Art 27(1) the Commissioner has a ground to serve a required steps notice`; `Art 28(1) the charity is eligible to be categorized as an organized religious charity`; `Art 28(1)(a) the charity meets the charity test by virtue of Article 6(1)(c)` |
| IP9 | `the entity met the charity test at the time of the application` | `Art 33 the person may appeal the decision`; `Art 33 the right of appeal` |
| IP9 | `the entity meets the charity test at the time of the appeal` | `Art 33 the person may appeal the decision`; `Art 33 the right of appeal` |
| IP11 | `the entity has a purpose within Article 6(1)(c)` | `Art 28(1) the charity is eligible to be categorized as an organized religious charity`; `Art 28(1)(a) the charity meets the charity test by virtue of Article 6(1)(c)` |
| IP12 | `the conduct is misconduct within Article 2(10)` | `Art 27(1) the Commissioner has a ground to serve a required steps notice` |
| IP14 | `the governor has engaged in misconduct within Article 18(4)` | `Art 27(1) the Commissioner has a ground to serve a required steps notice` |
| IP15 | `the requirement of Article 11(4)(c) is met` | `Art 27(1) the Commissioner has a ground to serve a required steps notice` |
| IP16 | `the requirement of Article 11(4)(d) is met` | `Art 27(1) the Commissioner has a ground to serve a required steps notice` |
| IP18 | `the name is undesirable under Article 12(1) at the time of the application` | `Art 33 the person may appeal the decision`; `Art 33 the right of appeal` |
| IP18 | `the name is undesirable under Article 12(1) at the time of the appeal` | `Art 33 the person may appeal the decision`; `Art 33 the right of appeal` |
| IP20 | `the entity is an organized religious charity` | `Art 27(4) the steps may include suspension, removal or replacement`; `Art 28(3) the required steps notice is invalid to the extent`; `Art 28(3) the requirements of the notice that remain valid` |
| IP25 | `the information is registered in a public part of the register` | `Art 29(1) the person commits an offence`; `Art 29(1) the person must not disclose the information`; `Art 29(2) this Article does not apply to the information` |
| IP34 | `the date on which the notice was served` | `Art 26(1) the last day allowed by the notice`; `Art 26(7) the person must comply with the requirement`; `Art 27(2) the required steps notice served` |

### 5.3 What G8 produces for other groups, and how it consumes what it does not take as a bare `GIVEN`

| IP | what | G8's name | how |
| --- | --- | --- | --- |
| IP19 | the required steps notices served | `Art 27(2) the required steps notice served` | one record per service (`Required steps notice`); the caller builds the `LIST OF` by mapping it over the recipients |
| IP20 | whether the charity is an organized religious charity | `Art 28 the entity is an organized religious charity` | consumed inside G8 by `Art 27(4) ...` and `Art 28(3) ...` through `GIVEN` `the entity is an organized religious charity`; the integrator wires producer to those two consumers |
| IP27 | the Commissioner's decisions (subject and outcome) | `Art 26 the decision of the Commissioner to impose a requirement`; `Art 27 the decision of the Commissioner to impose a requirement` | G8 produces these two; it CONSUMES the decisions of G3 to G6 as the field `decision appealed` of `Appeal under Article 33` (not as a bare `GIVEN` `the decision of the Commissioner`), so the integrator builds one `Appeal under Article 33` per appeal; see the nouns request on the outcome constructors |
| IP30 | the penalty an offence carries | `Art 26(7) the penalty provided for the offence`; `Art 26(10) the penalty provided for the offence`; `Art 29(1) the penalty provided for the offence` (g8-penalties) | constants of type `Penalty provided`; G7's Article 37(1) takes them as `the penalty provided for the offence` |
| IP35 | the unit of a term of imprisonment | field `unit of the terms of imprisonment in Articles 26 and 29` of `Interpretation of Articles 26 to 36` | typed with `Unit of a term of imprisonment`; the integrator sets it from the same value as G6, G7 and G9 |
| IP21 | reportable matters of the persons concerned | field `reportable matters` of each `Governor` in `the entity`'s `governors` | consumed by `Art 27(1) the Commissioner has a ground to serve a required steps notice` through `the entity` |

Standard names G8 does not consume: IP7 (`the registered charity` : `Registered charity` - no rule of Articles 26 to 36 reads a field of it), IP32 (`the basis of deregistration` - the decision's subject carries the Article 15 / Article 16 distinction), and IP27 as a bare `GIVEN`.

## 6. Contradictions, gaps and oddities found in a separate pass over the source

A deliberate pass, made after every module was green, reading Articles 26 to 36 against each other and against the Articles they cite (1, 2, 5, 6, 9 to 13, 15 to 20, 38, 40).  Each item says what the two provisions say, the case that tells them apart, and where the alternative reading is callable.  Items marked **fork** are registered in section 2; the others are reported and left as noted.

1. **Article 26(4)(a) "the registered charity" against Article 26(2) and the Article 1 definition (fork F8.19).**  Article 1 defines "registered charity" as an entity entered "for the time being" in the general or restricted section.  26(2) reaches "an entity that was formerly a registered charity" and a governor of one, and says so in terms.  26(4)(a), which lets the Commissioner require an explanation from a person who appears to be "a governor or employee of the registered charity", uses the defined term.  A definition and its use disagree in reach.  Case: a document demanded of a formerly registered entity, an employee of which is asked for an explanation.  Taken: a charity registered now (the defined term); callable: `Art 26(4)(a) the person appears to be a governor or employee of a charity registered now or formerly`.
2. **Article 33(5) excludes "a registered charity" (fork F8.13).**  A registered charity has appeals about its own affairs under 33(2) and none about a competitor's registration, yet the charity most likely to have "an interest in the registered name of the applicant" (33(5)(b)) is a registered charity with a similar name, and 33(5) excludes it.  Taken: the exclusion is general; callable: only the applicant concerned and the charity it became.
3. **Article 33(5) "at both the time of the application and the time of the appeal - (a) ... or (b) ..." (fork F8.18).**  Two groupings of the same words give different answers when the charity test failed at one time and the name was undesirable at the other.  Callable: `Art 33(5) a ground holds at the two times`.
4. **Article 34(1) against Article 35(1) (fork F8.5).**  Two statements of "the ground" of two appeals; the second is narrower.  A decision wrong in law but not unreasonable can be appealed to the tribunal and, on the taken reading, not to the court (35(3) is the route for a point of law).
5. **Article 33(1)(b) against Article 9(2) and 9(7) (fork F8.4).**  9(2) lets "an applicant for registration, or a charity registered in the general section" request entry in the restricted section, and 9(7)(a) requires written notice of a refusal "to the applicant or charity".  33(1)(b) gives an appeal against a refusal to register "the applicant" in the restricted section and 33(2) does not list a charity's refused request.  A cross-reference that stops short of the provision it serves.  Likewise a refusal to deregister on application (15(3)(b)) against the listed decision "to deregister" (33(2)(a)).  Taken: closed; callable: the two analogies.
6. **Article 33(2)(a) "to deregister the charity" against Article 15(3)(a) (fork F8.16).**  A deregistration the charity itself applied for is "a decision of the Commissioner to deregister the charity".
7. **Article 27(4) against Article 27(2) and Article 28(3) (fork F8.15).**  27(4) names (1)(c) and (d) as the notices whose steps "may include" the suspension, removal or replacement of a governor; 27(2) lets any notice require steps "appropriate to remedy the matter"; 28(3) voids such a requirement "to the extent that it purports to impose" it without limiting it to (c) and (d) notices.  Taken: only (c) and (d); callable: any ground.
8. **Article 28(3) against Article 19(9)(e)(i) (trap T11; G6's fork F6.15).**  19(9)(e)(i) has the Commissioner, determining a governor's fitness, "serve a required steps notice requiring the charity to suspend or remove the governor"; 28(3) makes that requirement invalid for an organized religious charity.  The Commissioner's duty in 19(9)(e) is "(i) ... or (ii)", and (ii) (permission) remains.  Case: the governor of an organized religious charity has a reportable matter the Commissioner finds disqualifying.  G8's side: `Art 28(3) the required steps notice is invalid to the extent` is TRUE for that requirement and `Art 27(4) the steps may include suspension, removal or replacement` is FALSE; the court route (19(9)(b), 20(1)(d)) is not touched by 28(3).  G6 owns the reading.
9. **Article 26(1) against Article 26(10) (trap T23).**  The power to demand serves one purpose (determining whether to serve a required steps notice); the offence of false information serves two (it adds an application for registration).  Information for an application is requested under 11(2)(f)(ii), which creates no offence of its own, and applicants and their governors are not within 26(2).  Case: false information given in an application: an offence under 26(10) with no 26(1) demand behind it.  Encoded as the Law reads (the power is limited, the offence is not); not a fork, because the text is plain on both.
10. **Endnote [4] against Article 31.**  The Table of Endnote References says "Article 31 editorial change, in sub-paragraph (c), 'for purpose of' deleted, 'for the purpose of' inserted instead", but the marker 4 stands at the end of 31(f) (src:682).  The text of (c) reads "for the purpose of" (src:679) and (a) and (b) still read "for purpose of" (src:677-678); (d) reads "for the purpose of".  A cross-reference that points at the wrong sub-paragraph, and an editorial change applied to one of three alike.  No effect on meaning; no rule reads the words.
11. **Article 30 against Article 31 (not a contradiction).**  31(b) and (c) permit disclosure to the Comptroller and the JFSC for "any" of their functions, while 30(1) and (2) oblige it only for taxation functions and functions under the Non-Profit Organizations (Jersey) Law 2008.  The permission is wider than the duty; both encoded as written.
12. **Article 36(2)(b) against Article 11(8)(a)(ii).**  Both let the Minister make an Order about notification of decisions (and reasons) to applicants; 36(2)(b) is limited to what is expedient for enabling appeals within time limits.  Two Order-making powers over one subject; which governs if the Orders differ is not answered.  No case can be written without the Orders.
13. **Article 33(5)(b) "the registered name of the applicant" "at the time of the application".**  12(2)(a) defines the "registered name" as the name the Commissioner enters when it registers the entity, so at the time of the application there is none.  The only coherent reading is the name the applicant proposed; IP18 supplies the undesirability at each time, and the encoding takes the name to be that name at the first time.  Not registered as a fork: no second reading has a case.
14. **Article 27(1)(d) "unfit to be a governor" against Article 20(4) "unfit to be concerned in the management".**  Two phrasings of unfitness, neither defined, one decided by the Commissioner's belief and the other by the court's satisfaction.  Encoded as the caller's determination (`a governor is unfit by reason of a reportable matter`).
15. **Article 28(1) "categorized" against Article 28(2)(a) "status".**  The Order provides for charities "to be categorized as organized religious charities"; the Commissioner may be given discretion "to grant or withdraw status as an organized religious charity".  Taken as one thing.
16. **Article 26(9) excepts "proceedings under paragraph (7)".**  A statement "made in compliance with a requirement" cannot itself be the contravention; the exception can only reach a statement made in compliance with one requirement and used to prove contravention of another.  Encoded as written.
17. **Article 31(d) lists "the Attorney General, the Bailiff or the court"** and Article 1 defines "the court" as the Royal Court, over which the Bailiff presides: a redundancy of no effect.
18. **Article 27(2) "in Commissioner's opinion"** lacks "the" before "Commissioner's"; a typographical slip of no effect.

## 7. Open questions for a domain expert

1. Who must supply the copy under 26(6)?  The sentence is passive ("must be supplied with a copy"); only the Commissioner retains the document under 26(4)(a), so the duty is typed on the Commissioner (`PARTY the Commissioner`).  It has no second candidate party, so it is not a fork, but a reader may think a member of staff acting for the Commissioner (Schedule 1 paragraph 4(3), G9) is meant.
2. Is a claimed lien (26(3)) a "reasonable excuse" under 26(7)?  26(3) says only that providing the document is without prejudice to the lien; the encoding makes a lien no excuse by itself and leaves the excuse to the caller's judgement.
3. Against whom may the tribunal award costs under 34(3)(b)?  The text says "award costs if satisfied that the appeal was vexatious or otherwise grossly unreasonable", so the appellant is the natural reading, but a Commissioner whose decision was grossly unreasonable is not excluded in terms.  Not modelled; the act is `award costs`.
4. Does an appeal suspend the decision appealed?  Nothing in Part 8 says it does or does not (34(2)(a) lets the tribunal make an interim order).
5. What happens if the Commissioner never decides an application (no "decision to refuse")?  33(1)(a) gives an appeal only against a refusal; 11(8)(a)(i) lets an Order fix the period for a decision.  No deemed refusal is provided.
6. What are the time limits and the provisions on notice that the Minister may prescribe under 36(2)?  No Order is among the sources; `Art 36(2) the appeal is in time` refuses until a limit is supplied.  Which of the two readings of F8.6 an Order, if made, would displace.
7. May a notice under 27(2) specify a period, or only a date?  "in a time specified in the notice" (27(2)) against "at such time and place as may be specified" (26(1)); both forms are accepted.
8. When the status of an organized religious charity is lost (a charity that stops meeting 28(1)(a) or (b)) is not said; the encoding takes the status from the Order and the Commissioner's grant or withdrawal only.
9. What the Law means by an "employee" of a registered charity in 26(4)(a).
10. A ruling on each fork, F8.1 to F8.19, in particular F8.11 (which consents), F8.13 (who is excluded from 33(5)) and F8.18 (the two grounds and the two times), where the text could be read either way and the consequence is who may sue or who commits an offence.

## 8. What the sources do not answer

Each is a place where the encoding gives a named refusal or an input and never a plausible value.

1. **The amount of "level 3 on the standard scale"** (26(7)).  Not in the sources: `Art 26(7) the amount of a fine of level 3 on the standard scale` refuses.  The fines of 26(10) and 29(1) are "a fine" with no maximum stated, so `Art 26(10) the maximum fine` and `Art 29(1) the maximum fine` refuse with that reason; no figure is invented.
2. **Every Order and set of Regulations Articles 26 to 36 empower:** the procedure and restrictions of 27(5) (an input `the procedure and restrictions of any Order under Article 27(5) are met`), the categorization of 28(1) and the Commissioner's discretion of 28(2)(a) (the record `Order under Article 28 as it applies to a charity`), the circumstances of 31(f) (the field `in circumstances prescribed by Regulations`), and the time limits and notice of 36(2) (`Art 36(2) the appeal is in time` refuses until a limit is supplied).  Orders and Regulations have been made under the Law; they are separate instruments and are not among the inputs.
3. **When a substituted decision takes effect if no date is ordered** (36(3)): `Art 36(3) the date from which the substituted decision takes effect` refuses.
4. **The Interpretation (Jersey) Law 1954**, which would settle how a period is counted: not among the inputs, so every period is a fork (F8.1, F8.2, F8.6, F8.7, F8.8, F8.9, F8.10, F8.12).
5. **How a notice is served** (Article 38 is a power to make an Order) and **which day a notice is served on**: an input (IP34); G7's fork F7.7.
6. **The text of Articles 26 to 36 before 1 January 2019.**  Part 7 (26 to 31) and Part 8 other than Article 32 (33 to 36) came into force on 1 May 2018 (R&O.17/2018) and Article 32 on 21 November 2014 (the Table of Legislation History); the first consolidated version is 1 January 2019.  The nine consolidated texts differ, so far as the BRIEF's list of amendments shows, in Article 1, Article 2(1)(ba) and Schedule 1 only (endnote [4] records one undated editorial change to 31(c), item 7), so Articles 26 to 36 read the same in all nine in substance - but **who "the Minister" is** (27(5), 28(1), 36(2)) and **which Law defines "the Comptroller"** (30, 31(b)) depend on the vintage: those are G1's rules (`Art 1 the Minister under the text of`, `Art 1 the Law that defines the Comptroller`) and the roles `the Minister` and `the Comptroller` are `Legal actor` constructors here.  The integrator's commencement wrapper is what makes a function of Part 7 or Part 8 answer on a given day (stage 2) and refuse before 1 May 2018.
7. **Endnote [4]**, an editorial change to 31(c): the Table of Endnote References gives no date and no instrument, so which of the nine vintages carried "for purpose of" in (c) is not in the sources.  No meaning turns on it.
8. **Who prosecutes** the offences, and any procedure beyond the penalties stated; what a court or tribunal "thinks fit" to order; the Commissioner's, the Minister's, the Tribunal's and the court's judgement wherever the text says "opinion", "satisfied", "reasonably requires", "appears" or "believes" - all inputs.
9. **The status of the statements of 26(9) outside criminal proceedings and against someone else:** Article 26(9) is silent, so `Art 26(9) the statement may be used by the prosecution` means only that Article 26(9) does not bar it.
10. **Anything after 2 October 2026**, and whether the consolidated text is exactly the enacted text.
