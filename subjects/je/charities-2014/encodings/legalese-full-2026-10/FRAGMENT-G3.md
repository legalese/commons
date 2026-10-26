# FRAGMENT-G3: Articles 8 to 10 (the register, the restricted section, public access)

**Role:** ENCODER for group G3. **Scope:** Articles 8 to 10 (Part 4: the register, the restricted section, public access). **Module prefix:** `g3-`.
**Status (2026-10-26):** Articles 8, 9 and 10 are encoded and tested; the group's `check.sh` printed GREEN on 2026-10-26 after the last edit (verbatim in section 9); the coverage has no `deferred` row.
Nothing is left over: no stop at a boundary was needed.

**Files** (all in `deposit/`):

| file | what it holds |
| --- | --- |
| `g3-nouns.l4` | nouns of the group; the fork enumerations; the record `Interpretation of Articles 8 to 10` |
| `g3-art8-register.l4` | Article 8(1) to 8(6), and the Minister's powers of 8(3)(n), 8(5)(e), 8(6)(d) |
| `g3-art9-restricted-section.l4` | Article 9(1) to 9(7), and the Minister's powers of 9(1)(d), 9(2)(a), 9(2)(b) |
| `g3-art10-public-access.l4` | Article 10(1) to 10(5), and the Minister's power of 10(2) |
| `g3-fixtures.l4` | named cases for the tests (generated: one interpretation per other reading) |
| `g3-tests-art8-register.l4`, `g3-tests-art8-address.l4`, `g3-tests-art8-historic.l4`, `g3-tests-art8-time.l4`, `g3-tests-art8-retention.l4`, `g3-tests-art9-restricted-section.l4`, `g3-tests-art10-public-access.l4` | the tests, with expected values decided from the source |
| `g3-tests-readings.l4` | each reading of each fork called directly, without the record (the R4 shape: one callable function per reading, each with its own test) |
| `g3-tests-red.l4` | twelve assertions that are MEANT to fail, and why |
| `FRAGMENT-G3.md` | this file |

No module starts with `@lang en`; every module imports only `prelude`, `daydate`, `domain` and modules of group G3.


## 1. Coverage

One row for each of the 82 provisions of the scope (the survey's rows, `phase1/coverage.tsv`, group G3), in the Law's numbering.
**Dispositions: 82 `encoded`, 0 `inert`, 0 `refused`, 0 `out-of-scope`, 0 `deferred`.** No disposition is changed from the survey's PLAN.
A row is `encoded` where the provision decides an outcome; the sub-paragraph rows of lists (8(2)(a) to (c), 8(6)(a) to (d), 9(5)(a)(i) to (b)(ii), 10(2)(a), (b), 10(3)(a) to (c)) are carried by the constructors or the arms of the rule that holds the list.
Every rule of the three rule modules has an `@ref`. The rules that decide an outcome in the Article's own words quote the source and carry `src:` locators that `srcrefs.py check --refs` verifies; the private helpers (the readings of the forks, the list builders, the named refusals) cite by Article number and fork id only, with no locator (legal, and ignored by the gate).

| id | provision | disposition | module | rule or noun | note |
| --- | --- | --- | --- | --- | --- |
| 8 | Article 8 | encoded | `g3-art8-register` | the whole Article: the rules of 8(1) to 8(6) below |  |
| 8(1) | Article 8(1) | encoded | `g3-art8-register` | `Art 8(1) the Commissioner must establish and maintain a register of charities` (MUST) | stands until done; the Article states no time, so no WITHIN |
| 8(2) | Article 8(2) | encoded | `g3-art8-register` | `Art 8(2) the register must be kept so as to distinguish between the general, restricted and historic sections` (MUST); `Art 8(2) the section in which the entity is entered on` (the section as a function of dated entries and of the day; F3.6); `the section named by the standing` | the passive 'must be kept' names no actor; the Commissioner, by 8(1). The historic section is not defined in Article 1 (T7): it is the section 8(5) describes |
| 8(2)(a) | Article 8(2)(a) | encoded | `g3-nouns` | `Section of the register`: `the general section`; used by `Art 8(2) the section in which the entity is entered on` |  |
| 8(2)(b) | Article 8(2)(b) | encoded | `g3-nouns` | `Section of the register`: `the restricted section` |  |
| 8(2)(c) | Article 8(2)(c) | encoded | `g3-nouns` | `Section of the register`: `the historic section` |  |
| 8(3) | Article 8(3) | encoded | `g3-art8-register` | `Art 8(3) the entries required for the registered charity` (the list); `Art 8(3) the Commissioner must enter in the register the entries required for the registered charity` (MUST, one duty per item, RAND); `Art 8(3) the items missing from the register entry` | empty list / FULFILLED if the standing is not that of a registered charity |
| 8(3)(a) | Article 8(3)(a) | encoded | `g3-art8-register` | `Art 8(3)(a) the note of the status of the entity`; `the recorded note of status is as Article 8(3)(a) requires` |  |
| 8(3)(a)(i) | Article 8(3)(a)(i) | encoded | `g3-art8-register` | `Art 8(3)(a) the note of the status of the entity`: fields `sub-paragraphs of Article 2(1) within which the entity falls` and `whether it also falls within sub-paragraph (a)`; `the kind is one of sub-paragraphs (f) to (j) of Article 2(1)` | by constructor, never by position; (ba) is not within '(f) to (j)': F3.13 |
| 8(3)(a)(ii) | Article 8(3)(a)(ii) | encoded | `g3-art8-register` | `Art 8(3)(a) the note of the status of the entity`: field `sub-paragraphs for which details of the enactment or foreign law are required`; `the kind is one of sub-paragraphs (e), (g), (h) and (j) of Article 2(1)` | (ba) is not listed (T5): F3.13. The details themselves are an input |
| 8(3)(b) | Article 8(3)(b) | encoded | `g3-art8-register` | `Art 8(3)(b) the names of each of the governors to be entered` |  |
| 8(3)(c) | Article 8(3)(c) | encoded | `g3-art8-register` | `Art 8(4) the addresses that may be entered as the principal address`; the item `the principal address` of `Entry required by Article 8(3)` |  |
| 8(3)(d) | Article 8(3)(d) | encoded | `g3-art8-register` | `Art 8(3)(d) the addresses of other premises in Jersey to be entered` | the principal address premises are not 'other' |
| 8(3)(e) | Article 8(3)(e) | encoded | `g3-art8-register` | the item `the registered charitable purposes` (always required); `the register entry holds the item` (non-empty and approved by the Commissioner) | the Commissioner's approval is an input |
| 8(3)(f) | Article 8(3)(f) | encoded | `g3-art8-register` | the item `the registered public benefit statement` (always required); `the register entry holds the item` (non-empty and approved by the Commissioner) | the Commissioner's approval is an input |
| 8(3)(g) | Article 8(3)(g) | encoded | `g3-art8-register` | the item `the date on which the charity was registered` (always required); field `date registered` of `Registered charity` |  |
| 8(3)(h) | Article 8(3)(h) | encoded | `g3-art8-register` | `Art 8(3)(h) a note that the charity is an organized religious charity is required` | IP20: field `is an organized religious charity` |
| 8(3)(i) | Article 8(3)(i) | encoded | `g3-art8-register` | `Art 8(3)(i) the text of the provision in the constitution is required` | IP10 |
| 8(3)(j) | Article 8(3)(j) | encoded | `g3-art8-register` | `Art 8(3)(j) the registered charity has sent its annual return for the most recent year` | periods P3: F3.2, F3.5, F3.7; refuses where no year has ended since registration or the financial-year end is not given |
| 8(3)(k) | Article 8(3)(k) | encoded | `g3-art8-register` | `Art 8(3)(k) the required steps notices to be noted` | IP19, IP34; F3.8 |
| 8(3)(l) | Article 8(3)(l) | encoded | `g3-art8-register` | `Art 8(3)(l) the previous registered names to be entered` |  |
| 8(3)(m) | Article 8(3)(m) | encoded | `g3-art8-register` | `Art 8(3)(m) the details or statement under the Order are required` | IP29 |
| 8(3)(n) | Article 8(3)(n) | encoded | `g3-art8-register` | `Art 8(3)(n) other information prescribed by the Minister by Order is required`; `Art 8(3)(n) the Minister may by Order prescribe other information to be entered in the register` (MAY) | the content of the Order is an input |
| 8(4) | Article 8(4) | encoded | `g3-art8-register` | `Art 8(4) the addresses that may be entered as the principal address`; `Art 8(4) the entity has a principal address in Jersey` (IP17); `Art 8(4) the address is a principal address of the registered charity` | the cascade returns the set of permitted addresses: 'one of the governors' is not a choice the Law makes |
| 8(4)(a) | Article 8(4)(a) | encoded | `g3-art8-register` | `Art 8(4)(a) the registered charity is an entity within sub-paragraph (a)` | F3.9; where Article 2(5) names no constitutional Law (T6) the requirement is FALSE |
| 8(4)(b) | Article 8(4)(b) | encoded | `g3-art8-register` | `the addresses under Article 8(4)(b) and (c)` | F3.10 |
| 8(4)(c) | Article 8(4)(c) | encoded | `g3-art8-register` | `the addresses under Article 8(4)(b) and (c)` |  |
| 8(5) | Article 8(5) | encoded | `g3-art8-register` | `Art 8(5) the entries required in the historic section` (the list); `Art 8(5) the Commissioner must enter in the historic section the entries required for the formerly registered charity` (MUST, one duty per item, RAND) | empty list / FULFILLED if the standing is not historic |
| 8(5)(a) | Article 8(5)(a) | encoded | `g3-art8-register` | the item `the entity's former registered number` (always required) |  |
| 8(5)(b) | Article 8(5)(b) | encoded | `g3-art8-register` | `Art 8(5)(b) the entity was registered in the general section`; `Art 8(5)(b) the names to be entered in the historic section` | F3.11; refuses if no earlier entry of the entity in a section is recorded |
| 8(5)(c) | Article 8(5)(c) | encoded | `g3-art8-register` | the item `a summary of the reason why the entity was deregistered` (always required); `Art 8(5)(c) the summary must include the reason for the service of the notice` | IP32 |
| 8(5)(d) | Article 8(5)(d) | encoded | `g3-art8-register` | the item `the dates on which the entity was registered and deregistered` (always required); fields `date registered` and `date deregistered` |  |
| 8(5)(e) | Article 8(5)(e) | encoded | `g3-art8-register` | `Art 8(5)(e) other matters prescribed by the Minister by Order are required`; `Art 8(5)(e) the Minister may by Order prescribe other matters to be entered in the historic section` (MAY) | the content of the Order is an input |
| 8(6) | Article 8(6) | encoded | `g3-art8-register` | `Art 8(6) the Commissioner may discard the copy on` (the first day); `Art 8(6) the Commissioner must retain the copy for 10 years` (SHANT discard BEFORE the last day) | period P4: F3.1, F3.4, F3.5. 'Must retain' is the contrapositive of 'must not discard': a prohibition that sunsets |
| 8(6)(a) | Article 8(6)(a) | encoded | `g3-nouns` | `Document of a kind within Article 8(6)`: `the constitution of the charity, or an amendment to it` |  |
| 8(6)(b) | Article 8(6)(b) | encoded | `g3-nouns` | `Document of a kind within Article 8(6)`: `an annual return of the charity` |  |
| 8(6)(c) | Article 8(6)(c) | encoded | `g3-nouns` | `Document of a kind within Article 8(6)`: `a notice served on the charity under this Law`; a notice served on a governor is `a document of a kind that Article 8(6) does not list` | 8(3)(k) notes a notice served on a governor; 8(6)(c) keeps only a notice served on the charity |
| 8(6)(d) | Article 8(6)(d) | encoded | `g3-nouns` | `Document of a kind within Article 8(6)`: `a document prescribed by the Minister by Order`; `Art 8(6)(d) the Minister may by Order prescribe other documents to be retained` (MAY, in g3-art8-register) | the content of the Order is an input |
| 9 | Article 9 | encoded | `g3-art9-restricted-section` | the whole Article: the rules of 9(1) to 9(7) below |  |
| 9(1) | Article 9(1) | encoded | `g3-art9-restricted-section` | `Art 9(1) the public elements of the restricted section` (the list); `Art 9(1) the matter is a public element of the restricted section` | empty list for a charity not in the restricted section |
| 9(1)(a) | Article 9(1)(a) | encoded | `g3-art9-restricted-section` | element `the registration number, but not the registered name`; the matter `the registered name` is not a public element |  |
| 9(1)(b) | Article 9(1)(b) | encoded | `g3-art9-restricted-section` | elements `the note of status registered under Article 8(3)(a)`, `...(e)`, `...(f)`, `...(j)`, `...(k)` | (k) is an element only if a notice is to be noted (F3.8) |
| 9(1)(c) | Article 9(1)(c) | encoded | `g3-art9-restricted-section` | element `a summary of the reasons for registration in the restricted section`; field `a summary of the reasons has been produced by the charity to the satisfaction of the Commissioner` | the Commissioner's satisfaction is an input |
| 9(1)(d) | Article 9(1)(d) | encoded | `g3-art9-restricted-section` | element `another element prescribed by the Minister by Order`; `Art 9(1)(d) the Minister may by Order prescribe other elements of the restricted section that are public` (MAY) | the content of the Order is an input |
| 9(2) | Article 9(2) | encoded | `g3-art9-restricted-section` | `Art 9(2) the request for entry in the restricted section may be made` | F3.12 |
| 9(2)(a) | Article 9(2)(a) | encoded | `g3-art9-restricted-section` | input `the funding condition prescribed under Article 9(2)(a) is met`; `Art 9(2)(a) the Minister may by Order prescribe the funding condition for entry in the restricted section` (MAY) | the funding condition is the content of an Order: an input; 'solicit' and 'donation' (Article 1) are construed by that Order |
| 9(2)(b) | Article 9(2)(b) | encoded | `g3-art9-restricted-section` | input `another condition prescribed under Article 9(2)(b) is met`; `Art 9(2)(b) the Minister may by Order prescribe other conditions for entry in the restricted section` (MAY) | an input |
| 9(3) | Article 9(3) | encoded | `g3-art9-restricted-section` | `Art 9(3) the Order contains what Article 9(3) requires` (a limit on the content of the Order, over `Content of an Order under Article 9`) |  |
| 9(3)(a) | Article 9(3)(a) | encoded | `g3-art9-restricted-section` | `Art 9(3)(a) the Order prescribes grounds on which the Commissioner may accept or refuse a request` |  |
| 9(3)(b) | Article 9(3)(b) | encoded | `g3-art9-restricted-section` | `Art 9(3)(b) the Order specifies, for the purpose of paragraph (2)(a), what soliciting, a donation and the general public are` |  |
| 9(3)(b)(i) | Article 9(3)(b)(i) | encoded | `g3-art9-restricted-section` | `Art 9(3)(b)(i) the Order specifies what constitutes soliciting` | defines 'solicit' (Article 1) by the Order: the meaning is an input |
| 9(3)(b)(ii) | Article 9(3)(b)(ii) | encoded | `g3-art9-restricted-section` | `Art 9(3)(b)(ii) the Order specifies what constitutes a donation` | defines 'donation' (Article 1) by the Order: the meaning is an input |
| 9(3)(b)(iii) | Article 9(3)(b)(iii) | encoded | `g3-art9-restricted-section` | `Art 9(3)(b)(iii) the Order specifies what constitutes the general public, where it prescribes no description of persons` | required only where no description of persons is prescribed |
| 9(3)(c) | Article 9(3)(c) | encoded | `g3-art9-restricted-section` | `Art 9(3)(c) a provision under sub-paragraph (b) of that manner is permitted` | a permission about the content of the Order; excludes nothing |
| 9(4) | Article 9(4) | encoded | `g3-art9-restricted-section` | `Art 9(4) the request is in the published form and supported to the Commissioner's satisfaction` |  |
| 9(4)(a) | Article 9(4)(a) | encoded | `g3-art9-restricted-section` | field `made in the form published by the Commissioner` of `Request for entry in the restricted section (Article 9)` |  |
| 9(4)(b) | Article 9(4)(b) | encoded | `g3-art9-restricted-section` | field `supported by information and evidence to the satisfaction of the Commissioner` | the Commissioner's satisfaction is an input |
| 9(5) | Article 9(5) | encoded | `g3-art9-restricted-section` | `Art 9(5) the request is accompanied by a statement of intention that Article 9(5) allows`; `Art 9(4) and (5) the request complied` |  |
| 9(5)(a) | Article 9(5)(a) | encoded | `g3-art9-restricted-section` | the branch of `Art 9(5)...` for `an applicant for registration` |  |
| 9(5)(a)(i) | Article 9(5)(a)(i) | encoded | `g3-nouns` | `Intention stated with a request (Article 9(5))`: `that the application should be treated as withdrawn` |  |
| 9(5)(a)(ii) | Article 9(5)(a)(ii) | encoded | `g3-nouns` | `Intention stated with a request (Article 9(5))`: `that the application should be treated as an application for entry in the general section, on provision of any further information and evidence required` |  |
| 9(5)(b) | Article 9(5)(b) | encoded | `g3-art9-restricted-section` | the branch of `Art 9(5)...` for `entered in the general section` | ties to Article 15 |
| 9(5)(b)(i) | Article 9(5)(b)(i) | encoded | `g3-nouns` | `Intention stated with a request (Article 9(5))`: `that the charity should remain so registered` |  |
| 9(5)(b)(ii) | Article 9(5)(b)(ii) | encoded | `g3-nouns` | `Intention stated with a request (Article 9(5))`: `that the charity should be treated as applying to be deregistered, on provision of any further information and evidence required` | ties to Article 15 |
| 9(6) | Article 9(6) | encoded | `g3-art9-restricted-section` | `Art 9(6) the Commissioner may enter the charity in the restricted section` (the three satisfactions); `Art 9(6) the Commissioner must not enter the charity in the restricted section unless satisfied` (SHANT, biting only where not satisfied); `Art 9(6) the decision of the Commissioner on the request for the restricted section` (IP27) |  |
| 9(6)(a) | Article 9(6)(a) | encoded | `g3-art9-restricted-section` | field `satisfied that the request complied with paragraphs (4) and (5)` of `Satisfaction of the Commissioner under Article 9(6)`; the fact it is about: `Art 9(4) and (5) the request complied` | the Commissioner's satisfaction is an input |
| 9(6)(b) | Article 9(6)(b) | encoded | `g3-art9-restricted-section` | field `satisfied that one of the conditions prescribed under paragraph (2) is met` | feeds 13(5)(a): the condition the Commissioner was satisfied of |
| 9(6)(c) | Article 9(6)(c) | encoded | `g3-art9-restricted-section` | field `satisfied that there is no ground ...`; the fact: `Art 9(6)(c) there is no ground on which the request must be refused or should be refused` | the Commissioner's consideration of a discretionary ground is an input |
| 9(7) | Article 9(7) | encoded | `g3-art9-restricted-section` | `Art 9(7)(a) ...` and `Art 9(7)(b) ...` |  |
| 9(7)(a) | Article 9(7)(a) | encoded | `g3-art9-restricted-section` | `Art 9(7)(a) the Commissioner must give written notice of the refusal` (MUST, no WITHIN) | no time limit is stated, and none is invented |
| 9(7)(b) | Article 9(7)(b) | encoded | `g3-art9-restricted-section` | `Art 9(7)(b) the Commissioner may proceed on the intention stated with the request` (MAY); `Art 9(7)(b) the consequence of proceeding on the intention` |  |
| 10 | Article 10 | encoded | `g3-art10-public-access` | the whole Article: the rules of 10(1) to 10(5) below |  |
| 10(1) | Article 10(1) | encoded | `g3-art10-public-access` | `Art 10(1) the Commissioner must make the public parts of the register available on a website` (MUST, no WITHIN) | no time is stated |
| 10(2) | Article 10(2) | encoded | `g3-art10-public-access` | `Art 10(2) the Minister may by Order provide for other access to the public parts of the register` (MAY); `Art 10(2) the Order provides for another specified manner of access on payment of a charge within (a) or (b)` | the charge and the manner are the content of an Order: inputs |
| 10(2)(a) | Article 10(2)(a) | encoded | `g3-art10-public-access` | `Art 10(2)(a) the Order requires payment of a specified charge`; `Charge for access to the public parts of the register (Article 10(2))`: `a specified charge` |  |
| 10(2)(b) | Article 10(2)(b) | encoded | `g3-art10-public-access` | `Art 10(2)(b) the Order requires payment of a charge determined and published by the Commissioner`; `Charge for access ...`: `a charge determined and published by the Commissioner` |  |
| 10(3) | Article 10(3) | encoded | `g3-art10-public-access` | `Art 10(3) the matter is in a public part of the register` (IP25) | subject to (5): a valid designation takes the matter out |
| 10(3)(a) | Article 10(3)(a) | encoded | `g3-art10-public-access` | `Art 10(3) ...`: the arm for `the general section` |  |
| 10(3)(b) | Article 10(3)(b) | encoded | `g3-art10-public-access` | `Art 10(3) ...`: the arm for `the restricted section`, via `Art 9(1) the matter is a public element of the restricted section` |  |
| 10(3)(c) | Article 10(3)(c) | encoded | `g3-art10-public-access` | `Art 10(3) ...`: the arm for `the historic section` |  |
| 10(4) | Article 10(4) | encoded | `g3-art10-public-access` | `Art 10(4) paragraph (5) applies`; `the standing is within Article 10(4)'s reach` | F3.3: the Commissioner's consideration is an input |
| 10(5) | Article 10(5) | encoded | `g3-art10-public-access` | `Art 10(5) the Commissioner may designate the matter as not a public part of the register` (MAY, only where 10(4) applies) | a permission, so not designating is no breach |

## 2. Fork register

The record is `Interpretation of Articles 8 to 10` (`g3-nouns`); its thirteen fields map one-to-one to the thirteen forks below, each `TYPICALLY` the reading taken.
Every public decision that depends on a reading takes the record as an ordinary `GIVEN` named `interp` and delegates by `CONSIDER` to one function per reading.
The test fixtures `the favoured interpretation of Articles 8 to 10` and one `interpretation F3.n reading X` per other reading are in `g3-fixtures` (generated, and each differs from the favoured in exactly one field, except the two combined ones the tests name).
"Reading A" is always the reading taken.

### F3.1  Article 8(6): from when do the ten years of retention run?

- **Provision:** 8(6) `src:249`; compare 17(1)(a) `src:444` (G6, F6.5); trap T14.
- **Record field and enumeration:** `start of the ten years of retention` : `When the ten years of retention under Article 8(6) begin`.
- **Readings and the text that licenses each.**
  - A (taken) `from the day the Commissioner receives or makes each copy`: "retain for 10 years, in respect of each registered charity, a copy of" four kinds of document; the only event the Article itself names for a copy is its being a copy the Commissioner holds, and the period is attached to the copy.
  - B `from the day the charity is deregistered`: Article 17(1)(a), the only other ten-year retention in the Law, runs "After deregistering an entity", and a register would not discard a registered charity's constitution while the charity is registered.
  - C `from the day the copy ceases to be operative`: "a copy of the constitution of the charity, and any amendments to it" reads as keeping each version for ten years after it is superseded; a copy that is still the operative one is not yet discardable.
- **Why A is taken.** It is the only reading computable from the copy alone (a receipt date) and the only one whose start is an event the Article itself mentions; B and C each need a further fact (a deregistration date, a supersession date) that the Article does not mention. It is a stipulation, not a finding.
- **A reading the survey proposed and this register drops.** The survey's third reading, "a rolling window: at any time the Commissioner must hold the copies of the preceding 10 years", answers "may this copy be discarded on this day" exactly as A does (a copy outside the window is one received more than ten years ago), so no case separates them and it is not a fork. The third constructor here is the reading that does differ (C). The survey's own discriminating case, run against C as defined here, is kept in `g3-tests-red` as an expected failure.
- **Discriminating cases (tests in `g3-tests-art8-retention`).**
  1. A constitution received 1 March 2019, never amended, the charity still registered: A may discard from 2 March 2029; B and C: not while the charity remains registered.
  2. The same constitution amended on 15 June 2021: A from 2 March 2029; C from 16 June 2031.
  3. The charity deregistered on 1 June 2024: B from 2 June 2034.

### F3.2  Article 8(3)(j): which year is "the most recent year"?

- **Provision:** 8(3)(j) `src:234`; 13(7) `src:392`, 13(9)(a) `src:395` (G5, F5.2); trap T24; integration point IP33.
- **Record field and enumeration:** `meaning of the year of an annual return` : `Meaning of the year of an annual return` (the enumeration is declared in `domain.l4`; the integrator sets this field and G5's from one value).
- **Readings.**
  - A (taken) `the calendar year`: "year" is not defined; the calendar year is the ordinary meaning.
  - B `the charity's own financial year`: 13(7) says "the year to which the return relates", which a charity with its own accounting year would read as its financial year.
  - C `the twelve months from each anniversary of registration`: a year of the charity's registration.
- **Why A is taken.** It needs no fact beyond the date. The text cuts both ways: Schedule 1 paragraph 4(8) (`src:807`) and Schedule 2 paragraph 3(3) (`src:842`) say "calendar year" where a calendar year is meant, which is some evidence that the unqualified "year" of Part 4 is not meant to be one. That is why it is a fork.
- **Discriminating case (test in `g3-tests-art8-time`).** A charity with a 30 June year-end that sent its return for the year to 30 June 2026 on 1 September 2026, asked on 1 February 2027: A has not sent its return for the most recent year (calendar 2026); B has.
- **Period (P3).** Kind: look-back. The year is identified by its last day. The counting conventions of the period are F3.5 (a year added to a date that does not exist) and F3.7 (which year is the most recent).

### F3.3  Article 10(4): does "a particular registered charity" include a deregistered entity?

- **Provision:** 10(4) `src:296`, 10(3)(c) `src:295`, Article 1 "registered charity" `src:34`, 8(5) `src:243`; trap T16.
- **Record field and enumeration:** `reach of Article 10(4)` : `Reach of Article 10(4) to an entity that has been deregistered`.
- **Readings.**
  - A (taken) `a registered charity is an entity entered in the general or the restricted section only`: Article 1 defines "registered charity" as an entity "entered for the time being in the general section or the restricted section".
  - B `a registered charity includes an entity formerly registered and entered in the historic section`: 10(4) speaks of "a matter entered on any section of the register in respect of that charity", and the historic section is a section, and is public under 10(3)(c).
- **Why A is taken.** The defined term. On A the Commissioner cannot protect a matter in the historic section by a designation; a person endangered by the publication of a historic-section summary of reasons has no remedy under 10(5).
- **Discriminating case (test in `g3-tests-art10-public-access`).** A deregistered entity whose historic-section summary of the reasons for deregistration would significantly endanger a person: A, the Commissioner may not designate it as non-public; B, the Commissioner may.

### F3.4  Every period of years: is the day of the event counted?

- **Provision:** 8(6) "for 10 years" (P4). The Interpretation (Jersey) Law 1954, which would settle it, is not among the sources.
- **Record field and enumeration:** `counting the day of an event in a period of years` : `Whether the day of an event is counted in a period of years`.
- **Readings.**
  - A (taken) `the day of the event is not counted, so the last day of the period is the anniversary`: a period "for 10 years" from an event runs from the day after it; the copy may be discarded on the day after the tenth anniversary.
  - B `the day of the event is the first day, so the last day of the period is the day before the anniversary`: the day of the event is day one, as British drafting says in "beginning with"; the copy may be discarded on the anniversary.
- **Discriminating case (test in `g3-tests-art8-retention`).** A copy received 1 March 2019 (F3.1 reading A): A may discard it on 2 March 2029, B on 1 March 2029.

### F3.5  Adding a year to a date that does not exist in the target year

- **Provision:** 8(6) (P4) for a copy received on 29 February; 8(3)(j) (P3) for a year of the charity that starts on 29 February.
- **Record field and enumeration:** `adding a year to a date that does not exist` : `How a year is added to a date that does not exist in the target year`.
- **Readings.**
  - A (taken) `the date moves back to the last day of the month`: `daydate`'s `add years` (as a spreadsheet's EDATE does): 29 February 2016 plus ten years is 28 February 2026.
  - B `the date rolls forward into the next month`: the lenient `Date` constructor: 1 March 2026.
- **Discriminating cases (tests in `g3-tests-art8-retention` and `g3-tests-art8-time`).** A copy received 29 February 2016: A may discard it from 1 March 2026 (day of the event not counted), B from 2 March 2026. A charity registered on 29 February 2020 under the anniversary-year meaning: A's first year ends on 27 February 2021, B's on 28 February 2021.

### F3.6  The day on which an entry in a section takes effect

- **Provision:** 8(2); 8(3)(g) `src:231` "the date on which the charity was registered"; 8(5)(d) `src:247` "the dates on which the entity was registered and deregistered".
- **Record field and enumeration:** `day on which an entry takes effect` : `The day on which an entry in a section of the register takes effect`.
- **Readings.** A (taken) `on the day of the entry`: the register's own wording gives the date on which the charity "was registered". B `on the day after the entry`: an entry made on a day is a record of that day's close.
- **Discriminating case (test in `g3-tests-art8-register`).** An entity entered in the general section on 1 March 2019, asked on 1 March 2019: A, it is in the general section; B, it is in no section yet. Likewise the day of the entry in the restricted section and the day of deregistration.

### F3.7  Article 8(3)(j): which year is the most recent, on the day asked?

- **Provision:** 8(3)(j) `src:234` (P3, a look-back period).
- **Record field and enumeration:** `the most recent year` : `Which year is the most recent year`.
- **Readings.** A (taken) `the latest year that has ended before the day asked`: a return reports "any matter ... arising during the year to which the return relates" (13(7)), so the year must be over, and a year is not over on its own last day. B `the year in progress on the day asked`: the register can show whether the return for the current year has been sent.
- **Discriminating cases (test in `g3-tests-art8-time`).** Asked on 30 June 2026, calendar years: A the year 2025, B the year 2026. Asked on 31 December 2026: A still 2025, B 2026. Asked on 1 January 2027: A 2026, B 2027.

### F3.8  Article 8(3)(k): is a notice noted once it has been complied with?

- **Provision:** 8(3)(k) `src:235` "if a required steps notice has been served ... a note of that fact (or a copy of the notice) and of the date on which the notice was served"; 9(1)(b) makes the item public for a restricted-section charity.
- **Record field and enumeration:** `required steps notices noted` : `Which required steps notices Article 8(3)(k) notes`.
- **Readings.** A (taken) `every notice that has been served`: "has been served" says nothing of compliance, and the note is of the fact and date of service. B `only a notice that has not been complied with`: the register is a current record, and a notice complied with is spent.
- **Discriminating case (test in `g3-tests-art8-register`).** A notice served on the charity on 10 January 2024 and complied with: A, item (k) is required; B, it is not (a second notice, served on a governor on 5 March 2025 and not complied with, is noted on both).

### F3.9  Article 8(4)(a): which entities are within "a company, foundation, or other entity required by its constitutional Law to have a registered office or business address in Jersey"?

- **Provision:** 8(4)(a) `src:240`; trap T6 (Article 2(5) names a constitutional Law for five kinds only).
- **Record field and enumeration:** `entities within Article 8(4)(a)` : `Which entities fall within Article 8(4)(a)`.
- **Readings.** A (taken) `an entity that its constitutional Law requires to have a registered office or business address in Jersey`: the participial phrase governs the whole list, and (b) refers back to "such an entity". B `every company and foundation, and any other entity that its constitutional Law so requires`: a company and a foundation are named and are within (a) whatever the Law says.
- **Why A is taken.** Limb (b) is "if the charity is not such an entity", and "such" points to the requirement. Whether a Law requires an office is a fact about another enactment (the Companies (Jersey) Law 1991 and the Foundations (Jersey) Law 2009 are not among the sources), so it is an input.
- **Discriminating case (test in `g3-tests-art8-address`).** A foundation whose constitutional Law (as given) does not require an office in Jersey, though it has one at "2 Bath Street" and its main premises are "5 Pier Road": A, the principal address is 5 Pier Road; B, 2 Bath Street.

### F3.10  Article 8(4)(b), (c): main premises that are a private dwelling house

- **Provision:** 8(4)(b) `src:241`, "unless the premises are a private dwelling house"; 8(4)(c) `src:242`, "if neither sub-paragraph (a) nor (b) applies".
- **Record field and enumeration:** `main premises that are a private dwelling house` : `What follows when the main premises are a private dwelling house`.
- **Readings.** A (taken) `Article 8(4)(b) does not apply, so Article 8(4)(c) is reached`: the proviso takes the premises out of (b), and (c) is the fallback. B `Article 8(4)(b) applies and gives no address`: (b) applies to every entity not within (a); the proviso removes only the address.
- **Why A is taken.** On B a charity run from a private home could never have a principal address in Jersey and so could never be registered (Article 11(4)(d)); (c) exists for exactly this.
- **Discriminating case (test in `g3-tests-art8-address`).** An unincorporated body whose main premises are a flat at "7 Elm Close", with governors in Jersey: A, the governors' addresses are allowed; B, no address is.

### F3.11  Article 8(5)(b): "if the entity was registered in the general section"

- **Provision:** 8(5)(b) `src:245`.
- **Record field and enumeration:** `section that decides Article 8(5)(b)` : `The section that decides Article 8(5)(b)`.
- **Readings.** A (taken) `the section the entity was entered in immediately before deregistration`: the sentence goes on "the name under which the entity was registered immediately before deregistration", and the point of the restricted section (9(1)(a)) is that the name is not public. B `any section the entity was ever entered in`: the entity was, at some time, registered in the general section.
- **Discriminating case (test in `g3-tests-art8-historic`).** A charity entered in the general section on 1 March 2019, moved to the restricted section on 1 June 2021 and then deregistered: A, the name is not entered; B, it is.

### F3.12  Article 9(2): who must meet the condition?

- **Provision:** 9(2) `src:260-262`; 11(1) `src:299` (defines "the applicant" as the entity that applies to be registered); 9(7) `src:285`.
- **Record field and enumeration:** `who must meet a condition under Article 9(2)` : `Who must meet a condition prescribed under Article 9(2)`.
- **Readings.** A (taken) `whoever makes the request, an applicant for registration or a registered charity`: the lead-in lets "a charity registered in the general section" request entry, and (a) and (b) say "the applicant meets"; the only reading that gives the lead-in any work is that "the applicant" there means the one who requests. B `only an applicant for registration`: the defined term "the applicant" (11(1)) is an entity applying to be registered; on it a general-section charity can never meet (a) or (b), so the lead-in confers a right it can never use.
- **Reported also as a contradiction** (FRAGMENT section 6): a defined term and its use disagree.
- **Discriminating case (test in `g3-tests-art9-restricted-section`).** A charity in the general section that meets the funding condition: A, it may request entry in the restricted section; B, it may not.

### F3.13  Article 8(3)(a): does it reach sub-paragraph (ba) of Article 2(1)?

- **Provision:** 8(3)(a)(i) `src:224`, (ii) `src:225`; Article 2(1)(ba) `src:51-54`; R&O.56/2025 inserted (ba) from 16 October 2025 and amended nothing else; trap T5.
- **Record field and enumeration:** `reach of Article 8(3)(a) to sub-paragraph (ba)` : `Whether Article 8(3)(a) reaches sub-paragraph (ba) of Article 2(1)`.
- **Readings.** A (taken) `Article 8(3)(a) reaches only the sub-paragraphs it names`: (f) to (j) for the "also within (a)" statement, (e), (g), (h) and (j) for the details; (ba) is in neither list. B `Article 8(3)(a) treats sub-paragraph (ba) like sub-paragraphs (f) to (j) for the note of sub-paragraph (a) and like (e), (g), (h) and (j) for the details`: (ba) is a body corporate established under the law of Jersey, like (e) and (g), and was inserted without amending the Article that lists the others.
- **Why A is taken.** It is the text. The gap is reported under contradictions.
- **Discriminating case (test in `g3-tests-art8-register`).** A Jersey NPO body corporate within (ba) only: A, no "also within (a)" statement and no details; B, a statement (FALSE) and details. The same entity that is also a trustee: A, no statement; B, the statement TRUE.

### Periods registered (the brief asks for a fork on every kind of period)

| id | provision | the words | kind | forks that settle its counting |
| --- | --- | --- | --- | --- |
| P3 | 8(3)(j) | "whether the registered charity has or has not sent its annual return for the most recent year" | look-back (the year just ended) | F3.2 (what a year is), F3.7 (which year is the most recent on the day asked), F3.5 (a year added at 29 February, for the anniversary-year meaning) |
| P4 | 8(6) | "retain for 10 years, in respect of each registered charity, a copy of" | retention period running forward from an event | F3.1 (the event), F3.4 (is the day of the event counted), F3.5 (the tenth anniversary of 29 February) |

No other period is stated in Articles 8 to 10: Article 9(7)(a) and Article 10(1) state no time, and none is invented.


## 3. Answer table

Each row is asserted in the tests named; the expected value was decided from the Article cited, on the favoured readings unless the row says otherwise.
"Entered" means: the Article requires the item to be entered in the register.

| # | scenario | answer | Article | test module |
| --- | --- | --- | --- | --- |
| 1 | A company in the general section, with no further facts | seven items are required: (a) status note, (b) governors' names, (c) principal address, (e) purposes, (f) public benefit statement, (g) date registered, (j) annual-return flag | 8(3) | `g3-tests-art8-register` |
| 2 | The same charity in the restricted section | the same seven | 8(3) lead-in "whether entered in the general or restricted section" | `g3-tests-art8-register` |
| 3 | The same charity with every conditional fact present | all fourteen | 8(3)(a) to (n) | `g3-tests-art8-register` |
| 4 | A formerly registered charity, or an applicant | no item under 8(3); a formerly registered charity has the items of 8(5) | 8(3), 8(5) | `g3-tests-art8-register`, `g3-tests-art8-historic` |
| 5 | A company that is also the sole trustee of a trust | the note says it also falls within sub-paragraph (a) | 8(3)(a)(i) | `g3-tests-art8-register` |
| 6 | A body incorporated under, but not by, an enactment | the note says it does not also fall within (a), and requires details of the enactment | 8(3)(a)(i), (ii) | `g3-tests-art8-register` |
| 7 | A Jersey NPO body corporate within sub-paragraph (ba) only | no statement about (a) and no details are required (the Article was not amended): fork F3.13 | 8(3)(a) | `g3-tests-art8-register` |
| 8 | A charity run from a private dwelling house, governors with addresses in Jersey | any governor's address may be the principal address (F3.10) | 8(4)(b), (c) | `g3-tests-art8-address` |
| 9 | A company whose constitutional Law requires an office in Jersey | the office is the principal address, whatever the premises | 8(4)(a) | `g3-tests-art8-address` |
| 10 | A charity registered 1 March 2019, calendar years, asked 30 June 2026, its 2025 return sent 15 February 2026 | it has sent its return for the most recent year; asked on 14 February 2026 it has not | 8(3)(j) | `g3-tests-art8-time` |
| 11 | A charity registered 1 January 2026, asked 2 January 2026 | refused: no year of the charity has ended since it was registered, and the Law does not say what is entered | 8(3)(j) | `g3-tests-art8-time` |
| 12 | A constitution copy received 1 March 2019, the charity still registered | may be discarded from 2 March 2029 (F3.1 A, F3.4 A); discarding it on 1 March 2029 is a breach | 8(6) | `g3-tests-art8-retention` |
| 13 | A copy received 29 February 2016 | may be discarded from 1 March 2026 (F3.5 A) | 8(6) | `g3-tests-art8-retention` |
| 14 | A required steps notice served on a governor | noted in the register under 8(3)(k); no copy need be retained under 8(6)(c) | 8(3)(k), 8(6)(c) | `g3-tests-art8-register`, `g3-tests-art8-retention` |
| 15 | A charity in the restricted section, a summary produced, no notice | public elements: the number, the status note, the purposes, the public benefit statement, the annual-return note, the summary; not the name | 9(1) | `g3-tests-art9-restricted-section` |
| 16 | A general-section charity meeting the funding condition | may request the restricted section (F3.12 A) | 9(2) | `g3-tests-art9-restricted-section` |
| 17 | An applicant who states, with its request, that the charity should remain so registered | the statement does not fit an applicant: 9(5)(a) allows (i) or (ii) only | 9(5) | `g3-tests-art9-restricted-section` |
| 18 | The Commissioner satisfied of (a) and (c) but not (b) | may not enter the charity; entering it is a breach | 9(6) | `g3-tests-art9-restricted-section` |
| 19 | The Commissioner refuses a request | must give written notice (no time stated, so no breach by delay); may proceed on the stated intention | 9(7) | `g3-tests-art9-restricted-section` |
| 20 | An Order for another manner of access with no payment | not within Article 10(2) | 10(2) | `g3-tests-art10-public-access` |
| 21 | A matter in the general section | public, the name included; subject to a designation | 10(3)(a) | `g3-tests-art10-public-access` |
| 22 | The registered name of a restricted-section charity | not public; its registration number is | 9(1)(a), 10(3)(b) | `g3-tests-art10-public-access` |
| 23 | A matter in the historic section | public, the name included | 10(3)(c) | `g3-tests-art10-public-access` |
| 24 | A deregistered entity whose historic-section summary would endanger a person | the Commissioner has no power to designate it (F3.3 A), so it stays public | 10(4), 10(5) | `g3-tests-art10-public-access` |


## 4. Nouns requests for the INTEGRATOR

None blocks the group: each noun below is defined locally (in `g3-nouns`) and the integrator may keep it there.
They are listed because another group's rule meets the same fact.

1. **`Section of the register` and `Placement of an entity in a section of the register`** (general, restricted, historic; a dated entry of an entity in a section). G5 (13(5), 13(6)(b)) and G6 (deregistration into the historic section) speak of sections; domain.l4's `Standing on the register` is the stored form. Proposed for domain.l4 if two groups use them.
2. **`Previous registered names`** are not a field of `Registered charity` (domain.l4 has `registered name` and `alternative registered names`). G3 takes them as an input of `Facts for the items of Article 8(3)` and `Facts for the items of Article 8(5)`. G4's Article 12(5) enters "the new or alternative registered name"; whether an alternative registered name is also a name "under which the entity was registered" (8(5)(b)) is an open question below.
3. **A governor's address in Jersey.** `Governor` (domain.l4) has no address; Article 8(4)(c) needs "the address in Jersey of one of the governors". G3 takes the list of those addresses as an input (`addresses in Jersey of the governors`); a field `address in Jersey` of `Governor` would make it derivable.
4. **`Entry in the register for a registered charity (Article 8(3))`** wraps `Registered charity` and adds the items the register holds beyond it. It is the producer the integrator can wire as `the registered charity` (IP7) together with G4's Article 12(2) and G6's `date deregistered`.
5. **`Act in relation to the register`** (the acts of the Commissioner, the Minister and the court that G3 rules are typed by) and **`Matter that an Order of the Minister prescribes (Articles 8 to 10)`** (the seven matters of Articles 8 to 10 on which the Minister may make an Order: 8(3)(n), 8(5)(e), 8(6)(d), 9(1)(d), 9(2)(a), 9(2)(b), 10(2)). If G4 to G8 declare their own act types, the integrator may merge them into one `make an Order prescribing` act whose payload is the matter; G3 uses one shape for all seven powers (`the Minister may by Order prescribe`).
6. **`Annual return sent by a charity (Article 8(3)(j))`** (the last day of the year a return relates to, and the date sent). G5's Article 13(7) duty will want the same record; the integrator should share one.
7. **`Premises of a charity (Articles 8(3)(d) and 8(4))`** (address, in Jersey, a private dwelling house, an activity undertaken there).
8. **`Interpretation of Articles 8 to 10`.** The integrator sets its field `meaning of the year of an annual return` from the same value as G5's (IP33).


## 5. Standard inputs consumed and functions exported

How the integrator wires G3.

- **Facts G3 consumes and does not decide** arrive under the standard names of section 5.1. G3 never calls another group.
- **Facts G3 decides and others consume**: IP17 `Art 8(4) the entity has a principal address in Jersey` (to G4, Article 11(4)(d)); IP25 `Art 10(3) the matter is in a public part of the register` (to G8, Article 29(2)(a)); IP27 `Art 9(6) the decision of the Commissioner on the request for the restricted section` (to G8, Article 33; G9, Schedule 1 paragraph 4(3)); IP7 `Entry in the register for a registered charity (Article 8(3))`, whose field `the registered charity` is the `Registered charity` the other groups read.
- **The section of the register is a function, not a stored flag.** `Art 8(2) the section in which the entity is entered on` computes it from the entity's dated entries and the day (F3.6). The stored `standing on the register` of `Entity` is what the Article 8(3), 8(5), 9 and 10 rules read; the integrator should assert that, on every test day, `the section named by the standing` of `the entity` equals the computed section.
- **IP6** (`the entity is a registered charity`): G3 reads the stored standing (`the standing is that of a registered charity`). It must equal G1's `Art 1 the entity is a registered charity` on the same entity; the integrator should assert it.
- **IP33**: the field `meaning of the year of an annual return` of `Interpretation of Articles 8 to 10` is set from the same value as G5's field (F5.2).
- **Orders** are inputs. The booleans and lists that carry them: `information prescribed by an Order under Article 8(3)(n)`, `matters prescribed by an Order under Article 8(5)(e)`, `an Order under Article 9(1)(d) prescribes another element`, `the funding condition prescribed under Article 9(2)(a) is met`, `another condition prescribed under Article 9(2)(b) is met`, `Content of an Order under Article 9`, `Content of an Order under Article 10(2)`.
- **Commencement** is the integrator's wrapper: Part 4 (Articles 8 to 17) is stage 2, in force 1 May 2018 (R&O.17/2018). No rule here reads the vintage.
- **Traces.** A DEONTIC value cannot be compared; every `#TRACE` of G3 carries an `-- EXPECT:` comment (FULFILLED, BREACH with the text, or STANDING) that `check-traces.py` reads. The time unit is one day when a trace is stamped with `DATE_SERIAL`, and one unit otherwise.


### 5.1 Standard inputs consumed (PLAN section (c)), by the exact `GIVEN` name

| standard `GIVEN` name | integration point | consumed by (exports of G3) |
| --- | --- | --- |
| `the entity` | IP5 | `Art 8(3)(a) the note of the status of the entity`; `Art 8(4) the addresses that may be entered as the principal address`; `Art 8(4) the entity has a principal address in Jersey`; `Art 8(4) the address is a principal address of the registered charity`; `Art 9(2) the request for entry in the restricted section may be made`; `Art 9(5) the request is accompanied by a statement of intention that Article 9(5) allows`; `Art 9(4) and (5) the request complied`; `Art 10(4) paragraph (5) applies`; `Art 10(5) the Commissioner may designate the matter as not a public part of the register`; `Art 10(3) the matter is in a public part of the register` |
| `the registered charity` | IP7 | `Art 8(3) the entries required for the registered charity`; `Art 8(3) the Commissioner must enter in the register the entries required for the registered charity`; `Art 8(3)(j) the registered charity has sent its annual return for the most recent year`; `Art 8(5)(b) the names to be entered in the historic section`; `Art 8(5) the entries required in the historic section`; `Art 8(5) the Commissioner must enter in the historic section the entries required for the formerly registered charity`; `Art 8(6) the Commissioner may discard the copy on`; `Art 8(6) the Commissioner must retain the copy for 10 years`; `Art 9(1) the public elements of the restricted section` |
| `the day` | IP1 | `Art 8(2) the section in which the entity is entered on`; `Art 8(3)(j) the registered charity has sent its annual return for the most recent year` |
| `the entity meets the charity test only by virtue of an Order under Article 5(3)` | IP10 | `Art 8(3) the entries required for the registered charity`; `Art 8(3) the Commissioner must enter in the register the entries required for the registered charity`; `Art 8(3) the items missing from the register entry` |
| `the required steps notices served` | IP19 | `Art 8(3) the entries required for the registered charity`; `Art 8(3) the Commissioner must enter in the register the entries required for the registered charity`; `Art 8(3) the items missing from the register entry`; `Art 9(1) the public elements of the restricted section` |
| `an Order under Article 13(9) applies to the registered charity` | IP29 | `Art 8(3) the entries required for the registered charity`; `Art 8(3) the Commissioner must enter in the register the entries required for the registered charity`; `Art 8(3) the items missing from the register entry` |
| `the basis of deregistration` | IP32 | `Art 8(5)(c) the summary must include the reason for the service of the notice` |

Read as fields, not as separate `GIVEN`s: `is an organized religious charity` of `the registered charity` (IP20, Article 8(3)(h)); `date served` of `Required steps notice` (IP34, Article 8(3)(k)); `standing on the register`, `kinds of entity` and `governors` of `the entity` (IP5, IP6).

### 5.2 Every `@export` of G3 (generated from the deposited modules)

42 exports. `interp` is `Interpretation of Articles 8 to 10`: a caller may give it partly (any field left out takes the favoured reading) but not as `{}`, which the boundary refuses as "not known".

| module | function | `GIVEN`s | gives | what it answers |
| --- | --- | --- | --- | --- |
| `g3-art8-register` | `Art 8(1) the Commissioner must establish and maintain a register of charities` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner must establish and maintain a register of charities (Article 8(1)); stands until the Commissioner does so |
| `g3-art8-register` | `Art 8(2) the register must be kept so as to distinguish between the general, restricted and historic sections` | none | DEONTIC `Legal actor` `Act in relation to the register` | The register must be kept so as to distinguish between the general, restricted and historic sections (Article 8(2)); the actor is the Commissioner by Article 8(1) |
| `g3-art8-register` | `Art 8(2) the section in which the entity is entered on` | `interp` : Interpretation of Articles 8 to 10; `placements` : LIST OF `Placement of an entity in a section of the register`; `the day` : DATE | MAYBE `Section of the register` | The section of the register (general, restricted or historic) in which an entity is entered on a day, from its dated entries; NOTHING if it is in no section on that day |
| `g3-art8-register` | `Art 8(3)(a) the note of the status of the entity` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity | `Requirement of the note of status (Article 8(3)(a))` | What the note of the status of an entity must say (Article 8(3)(a)): the sub-paragraphs of Article 2(1) it falls within, whether an entity within (f) to (j) also falls within (a), and the sub-paragraphs (e), (g), (h), (j) for which details of the enactment or foreign law are required |
| `g3-art8-register` | `Art 8(3) the entries required for the registered charity` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `the entity meets the charity test only by virtue of an Order under Article 5(3)` : BOOLEAN; `the required steps notices served` : LIST OF `Required steps notice`; `an Order under Article 13(9) applies to the registered charity` : BOOLEAN; `facts` : Facts for the items of Article 8(3) | LIST OF `Entry required by Article 8(3)` | The items the Commissioner must enter in the register for a registered charity (Article 8(3), (a) to (n)); empty if the charity is not entered in the general or restricted section |
| `g3-art8-register` | `Art 8(3) the Commissioner must enter in the register the entries required for the registered charity` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `the entity meets the charity test only by virtue of an Order under Article 5(3)` : BOOLEAN; `the required steps notices served` : LIST OF `Required steps notice`; `an Order under Article 13(9) applies to the registered charity` : BOOLEAN; `facts` : Facts for the items of Article 8(3) | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner must enter each item required by Article 8(3) in the register for a registered charity; a conjunction of one duty per item, and FULFILLED if no item is required |
| `g3-art8-register` | `Art 8(3) the items missing from the register entry` | `interp` : Interpretation of Articles 8 to 10; `entry` : Entry in the register for a registered charity (Article 8(3)); `the entity meets the charity test only by virtue of an Order under Article 5(3)` : BOOLEAN; `the required steps notices served` : LIST OF `Required steps notice`; `an Order under Article 13(9) applies to the registered charity` : BOOLEAN; `facts` : Facts for the items of Article 8(3) | LIST OF `Entry required by Article 8(3)` | Which items required by Article 8(3) are missing from the register entry of a registered charity; empty if the entry is complete |
| `g3-art8-register` | `Art 8(4) the addresses that may be entered as the principal address` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `facts` : Facts for the principal address (Article 8(4)) | LIST OF STRING | The addresses in Jersey that may be entered as the principal address of a registered charity (Article 8(4)): the registered office or business address, else the main premises unless a private dwelling house, else the address in Jersey of one of the governors (so, any of those addresses) |
| `g3-art8-register` | `Art 8(4) the entity has a principal address in Jersey` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `facts` : Facts for the principal address (Article 8(4)) | BOOLEAN | Whether the entity has a principal address in Jersey within the meaning of Article 8(4) (the fact Article 11(4)(d) asks of an applicant) |
| `g3-art8-register` | `Art 8(4) the address is a principal address of the registered charity` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `facts` : Facts for the principal address (Article 8(4)); `address` : STRING | BOOLEAN | Whether an address is one that Article 8(4) allows as the principal address of a registered charity |
| `g3-art8-register` | `Art 8(3)(j) the registered charity has sent its annual return for the most recent year` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `the day` : DATE; `facts` : Facts for the annual return entry (Article 8(3)(j)) | BOOLEAN | Whether the registered charity has sent its annual return for the most recent year, as at a day (Article 8(3)(j)); refuses if no year of the charity has ended since it was registered, or if the financial-year reading is asked and the year-end is not given |
| `g3-art8-register` | `Art 8(3)(n) the Minister may by Order prescribe other information to be entered in the register` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order prescribe other information to be entered in the register for a registered charity (Article 8(3)(n)) |
| `g3-art8-register` | `Art 8(5)(e) the Minister may by Order prescribe other matters to be entered in the historic section` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order prescribe other matters to be entered in the historic section (Article 8(5)(e)) |
| `g3-art8-register` | `Art 8(6)(d) the Minister may by Order prescribe other documents to be retained` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order prescribe other documents of which the Commissioner must retain a copy (Article 8(6)(d)) |
| `g3-art8-register` | `Art 8(5)(b) the names to be entered in the historic section` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `facts` : Facts for the items of Article 8(5) | LIST OF STRING | The names to be entered in the historic section for a formerly registered charity (Article 8(5)(b)): its name immediately before deregistration and its previous names, if it was registered in the general section; none if it was in the restricted section; refuses if no earlier entry of the entity in a section is recorded |
| `g3-art8-register` | `Art 8(5)(c) the summary must include the reason for the service of the notice` | `the basis of deregistration` : Basis of deregistration | BOOLEAN | Whether the summary of the reason for deregistration must also give the reason for the service of the required steps notice (Article 8(5)(c)) |
| `g3-art8-register` | `Art 8(5) the entries required in the historic section` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `facts` : Facts for the items of Article 8(5) | LIST OF `Entry required by Article 8(5)` | The items the Commissioner must enter in the historic section for a formerly registered charity that has been deregistered (Article 8(5), (a) to (e)); empty if the entity is not entered in the historic section; refuses if it is, but no earlier entry of it in a section is recorded (item (b) cannot then be decided) |
| `g3-art8-register` | `Art 8(5) the Commissioner must enter in the historic section the entries required for the formerly registered charity` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `facts` : Facts for the items of Article 8(5) | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner must enter each item required by Article 8(5) in the historic section for a formerly registered charity; FULFILLED if no item is required; refuses if the entity is entered in the historic section but no earlier entry of it in a section is recorded |
| `g3-art8-register` | `Art 8(6) the Commissioner may discard the copy on` | `interp` : Interpretation of Articles 8 to 10; `copy` : Copy held by the Commissioner (Article 8(6)); `the registered charity` : Registered charity | `Earliest day on which a copy may be discarded (Article 8(6))` | The first day on which the Commissioner may discard a copy of a document held in respect of a registered charity (Article 8(6)), or that it may not be discarded while the charity is registered, or that Article 8(6) does not require it to be retained |
| `g3-art8-register` | `Art 8(6) the Commissioner must retain the copy for 10 years` | `interp` : Interpretation of Articles 8 to 10; `copy` : Copy held by the Commissioner (Article 8(6)); `the registered charity` : Registered charity | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner must retain a copy of a document held in respect of a registered charity for 10 years (Article 8(6)): a prohibition on discarding it until the ten years are over |
| `g3-art9-restricted-section` | `Art 9(1) the public elements of the restricted section` | `interp` : Interpretation of Articles 8 to 10; `the registered charity` : Registered charity; `the required steps notices served` : LIST OF `Required steps notice`; `facts` : Facts for the public elements (Article 9(1)) | LIST OF `Element of the restricted section (Article 9(1))` | The public elements of the restricted section for a charity registered in it (Article 9(1)): the registration number but not the name, the matters of Article 8(3)(a), (e), (f), (j) and (k), a summary of the reasons, and any element an Order prescribes; empty for a charity not in the restricted section |
| `g3-art9-restricted-section` | `Art 9(1) the matter is a public element of the restricted section` | `matter` : Matter entered on the register | BOOLEAN | Whether a matter entered on the register is a public element of the restricted section (Article 9(1)): the registration number is, the registered name is not |
| `g3-art9-restricted-section` | `Art 9(1)(d) the Minister may by Order prescribe other elements of the restricted section that are public` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order prescribe other elements of the restricted section that are public (Article 9(1)(d)) |
| `g3-art9-restricted-section` | `Art 9(2) the request for entry in the restricted section may be made` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `the funding condition prescribed under Article 9(2)(a) is met` : BOOLEAN; `another condition prescribed under Article 9(2)(b) is met` : BOOLEAN | BOOLEAN | Whether an entity may request entry in the restricted section (Article 9(2)): it is an applicant for registration or a charity in the general section, and meets the funding condition or another condition prescribed by Order |
| `g3-art9-restricted-section` | `Art 9(2)(a) the Minister may by Order prescribe the funding condition for entry in the restricted section` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order prescribe the funding condition for entry in the restricted section (Article 9(2)(a)) |
| `g3-art9-restricted-section` | `Art 9(2)(b) the Minister may by Order prescribe other conditions for entry in the restricted section` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order prescribe other conditions for entry in the restricted section (Article 9(2)(b)) |
| `g3-art9-restricted-section` | `Art 9(3) the Order contains what Article 9(3) requires` | `content` : Content of an Order under Article 9 | BOOLEAN | Whether the Order under Article 9 contains what Article 9(3) requires: grounds for accepting or refusing a request, and what soliciting, a donation and (where no description of persons is prescribed) the general public are |
| `g3-art9-restricted-section` | `Art 9(4) the request is in the published form and supported to the Commissioner's satisfaction` | `request` : Request for entry in the restricted section (Article 9) | BOOLEAN | Whether a request for entry in the restricted section is in the form the Commissioner published and is supported by information and evidence to the Commissioner's satisfaction (Article 9(4)) |
| `g3-art9-restricted-section` | `Art 9(5) the request is accompanied by a statement of intention that Article 9(5) allows` | `the entity` : Entity; `request` : Request for entry in the restricted section (Article 9) | BOOLEAN | Whether a request is accompanied by a statement of the applicant's intention on refusal that fits the one who requests (Article 9(5)): an applicant for registration states (a)(i) or (a)(ii); a charity registered in the general section states (b)(i) or (b)(ii) |
| `g3-art9-restricted-section` | `Art 9(4) and (5) the request complied` | `the entity` : Entity; `request` : Request for entry in the restricted section (Article 9) | BOOLEAN | Whether the request complied with Article 9(4) and (5), as a matter of fact (the fact the Commissioner is to be satisfied of under Article 9(6)(a)) |
| `g3-art9-restricted-section` | `Art 9(6) the Commissioner may enter the charity in the restricted section` | `satisfaction` : Satisfaction of the Commissioner under Article 9(6) | BOOLEAN | Whether the Commissioner is satisfied of all three things Article 9(6) requires before entering a charity in the restricted section; each satisfaction is the Commissioner's own state of mind and is supplied |
| `g3-art9-restricted-section` | `Art 9(6) the Commissioner must not enter the charity in the restricted section unless satisfied` | `satisfaction` : Satisfaction of the Commissioner under Article 9(6) | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner must not enter a charity in the restricted section unless satisfied of the three things in Article 9(6); a prohibition that bites only where the Commissioner is not so satisfied |
| `g3-art9-restricted-section` | `Art 9(6) the decision of the Commissioner on the request for the restricted section` | `the Commissioner enters the charity in the restricted section` : BOOLEAN | `Decision of the Commissioner` | The decision of the Commissioner on a request for entry in the restricted section: the subject (Article 9(6) and (7)) and whether the Commissioner did what was asked or refused |
| `g3-art9-restricted-section` | `Art 9(7)(a) the Commissioner must give written notice of the refusal` | `the Commissioner refuses the request` : BOOLEAN | DEONTIC `Legal actor` `Act in relation to the register` | If the Commissioner refuses a request, the Commissioner must give written notice of the refusal to the applicant or charity (Article 9(7)(a)); no time is stated |
| `g3-art9-restricted-section` | `Art 9(7)(b) the consequence of proceeding on the intention` | `intention` : Intention stated with a request (Article 9(5)) | `Consequence of proceeding on the intention stated with a request (Article 9(7)(b))` | What follows if the Commissioner proceeds on the intention stated with a refused request (Article 9(7)(b) with 9(5)): withdrawn, treated as an application for the general section, remains registered, or treated as applying to be deregistered (Article 15) |
| `g3-art9-restricted-section` | `Art 9(7)(b) the Commissioner may proceed on the intention stated with the request` | `the Commissioner refuses the request` : BOOLEAN; `intention` : Intention stated with a request (Article 9(5)) | DEONTIC `Legal actor` `Act in relation to the register` | If the Commissioner refuses a request, the Commissioner may proceed on the basis of the intention stated with it (Article 9(7)(b)); a permission, so not proceeding is no breach |
| `g3-art10-public-access` | `Art 10(1) the Commissioner must make the public parts of the register available on a website` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner must make the public parts of the register available to the public on a website for inspection without charge (Article 10(1)); stands until the Commissioner does so |
| `g3-art10-public-access` | `Art 10(2) the Minister may by Order provide for other access to the public parts of the register` | none | DEONTIC `Legal actor` `Act in relation to the register` | The Minister may by Order provide for the Commissioner to make the public parts of the register available in any other specified manner, on payment of a charge (Article 10(2)) |
| `g3-art10-public-access` | `Art 10(2) the Order provides for another specified manner of access on payment of a charge within (a) or (b)` | `content` : Content of an Order under Article 10(2) | BOOLEAN | Whether an Order provides for access to the public parts of the register in another specified manner on payment of a charge within Article 10(2)(a) or (b) |
| `g3-art10-public-access` | `Art 10(4) paragraph (5) applies` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `the Commissioner considers that public access to the matter would significantly put safety or security at risk` : BOOLEAN | BOOLEAN | Whether Article 10(5) applies: the Commissioner considers that the safety or security of any person, property or premises would be significantly put at risk by public access to a matter entered on a section of the register in respect of a particular registered charity |
| `g3-art10-public-access` | `Art 10(5) the Commissioner may designate the matter as not a public part of the register` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `the Commissioner considers that public access to the matter would significantly put safety or security at risk` : BOOLEAN; `matter` : Matter entered on the register | DEONTIC `Legal actor` `Act in relation to the register` | The Commissioner may designate a matter entered in respect of a registered charity as not being a public part of the register (Article 10(5)); available only where Article 10(4) applies; a permission, so not designating is no breach |
| `g3-art10-public-access` | `Art 10(3) the matter is in a public part of the register` | `interp` : Interpretation of Articles 8 to 10; `the entity` : Entity; `matter` : Matter entered on the register; `the Commissioner has designated the matter as not a public part of the register` : BOOLEAN | BOOLEAN | Whether a matter entered on the register for an entity is in a public part of the register (Article 10(3)): the general section, the public elements of the restricted section, the historic section, less what the Commissioner has validly designated as not public (Article 10(5)) |

### 5.3 Names that differ from PLAN section (b), and why

PLAN section (b) proposes names; the text and the types forced these changes, and no other.

| PLAN name | name used | why |
| --- | --- | --- |
| `Art 8(1) the Commissioner must establish and maintain the register` | `Art 8(1) the Commissioner must establish and maintain a register of charities` | the Article's own words |
| `Art 8(3)(a) the status note of the entity` | `Art 8(3)(a) the note of the status of the entity` | the Article's own words; it gives a requirement record, not a list |
| `Art 8(4) the principal address of the registered charity` (gives `MAYBE STRING`) | `Art 8(4) the addresses that may be entered as the principal address` (gives `LIST OF STRING`) | limb (c) is "the address in Jersey of one of the governors": the Law makes no choice between them, so the rule returns every permitted address; `Art 8(4) the address is a principal address of the registered charity` tests one |
| `Art 8(5) the entries required in the historic section` taking `the basis of deregistration` | the same name; the basis is taken by `Art 8(5)(c) the summary must include the reason for the service of the notice` only | the basis changes the content of entry (c), never whether it is required |
| `Art 8(6) the Commissioner may discard the copy on` (gives `DATE`) | gives `Earliest day on which a copy may be discarded (Article 8(6))` | a copy may be one that must not be discarded while the charity is registered (F3.1 B and C), or one Article 8(6) does not list; a date cannot say so |
| `Art 9(7) the Commissioner must give written notice of the refusal` | `Art 9(7)(a) ...` taking `the Commissioner refuses the request` | the duty arises only on a refusal |
| `Art 9(7) the Commissioner may proceed on the stated intention` | `Art 9(7)(b) the Commissioner may proceed on the intention stated with the request` | the same |
| `Art 10(2) the Minister may by Order provide for other access` | `Art 10(2) the Minister may by Order provide for other access to the public parts of the register` | the Article's own words |
| `Art 10(3) the matter is in a public part of the register` taking the section and the designation | taking `the entity`, the matter and the designation | the section of a matter is the section its entity's standing names, and a designation counts only where Article 10(4) reaches the entity (F3.3) |
| `Art 10(5) the Commissioner may designate the matter as not a public part` | `... of the register` | the Article's own words |

New modules: `g3-nouns` (the group-local nouns and the fork record), `g3-fixtures` and the test modules.


## 6. Contradictions in the source

Found by a separate pass over Articles 8 to 10 and the provisions they cite, after the encoding, reading the source (`src:217-297`) against the PDF text layer (identical in these Articles) and the cross-references against the Law.
Each entry names both provisions, the case that discriminates, and what the encoding does.
"Fork" means the other reading is a callable function with a test.

1. **"The applicant" in Article 9(2)(a) and (b) against the lead-in of Article 9(2) and the definition in Article 11(1).** (`src:260-262`, `src:299`.)
   The lead-in lets "an applicant for registration, or a charity registered in the general section" request entry in the restricted section; (a) and (b) say "the applicant meets the ... condition".
   Article 11(1) defines "the applicant" as an entity that applies to be registered.
   Case: a charity already in the general section that meets the funding condition.
   Taken: whoever requests (the lead-in would otherwise confer a right no one can use).
   **Fork F3.12**; test in `g3-tests-art9-restricted-section`.
2. **Article 8(3)(a) against Article 2(1)(ba).** (`src:224-225`, `src:51-54`.)
   Sub-paragraph (ba) was inserted into Article 2(1) from 16 October 2025 by R&O.56/2025, which amended nothing else.
   Article 8(3)(a)(i) asks, for an entity within one of "(f) to (j)", whether it also falls within (a); (ii) asks for details for "(e), (g), (h) or (j)".
   A (ba) body is a body corporate established under the law of Jersey that is not within (c) to (h), exactly as (e) and (g) are, yet neither limb names it.
   Case: a Jersey NPO body corporate that is also the trustee of a trust.
   Taken: the Article is read as written (no note, no details). **Fork F3.13**; tests in `g3-tests-art8-register`, and the purposive expectation in `g3-tests-red` (RED 2, RED 3).
3. **Article 8(4)(a) against Article 2(5).** (`src:240`, `src:80-85`; trap T6.)
   Article 8(4)(a) asks whether an entity is "required by its constitutional Law" to have a registered office or business address in Jersey.
   Article 2(5) defines "constitutional Law" for trusts, fidéicommis and 1862 associations, foundations, companies, and (e) bodies "incorporated by (but not under)" another Law.
   It gives none for (ba), (g) and (h) (incorporated "under, but not by"), (i) or (j).
   Case: a body incorporated under, but not by, an enactment that itself requires a registered office.
   The encoding does not decide it: whether a Law requires an office is an input (`its constitutional Law requires a registered office or business address in Jersey`), and the caller gives FALSE where Article 2(5) names no Law.
   The test that gives TRUE for kind (g) assumes G1's reading (F1.3) that the enactment of incorporation is its constitutional Law.
   The related reading of the proviso in (b) is **fork F3.10**; the reading of the qualifier in (a) is **fork F3.9**.
4. **Article 10(4) against Article 1 "registered charity" and Article 10(3)(c).** (`src:296`, `src:34`, `src:295`; trap T16.)
   The historic section is public, and a matter "entered on any section of the register" may be protected, but only "in relation to a particular registered charity", which the Law defines as an entity in the general or restricted section.
   Case: a historic-section summary of the reasons for deregistration that would endanger a person.
   Taken: no power. **Fork F3.3**; test in `g3-tests-art10-public-access`.
5. **Article 8(3)(k) against Article 8(6)(c).** (`src:235`, `src:252`.)
   Item (k) notes a required steps notice served "on the registered charity, or on a governor of the registered charity", and allows "a copy of the notice" to be entered; 8(6)(c) retains a copy of "any notice served on the charity" only.
   Case: a notice served on a governor.
   Taken: the narrow wording (the Law distinguishes the two recipients in (k), and in 27(3)).
   Not a fork: the narrow reading is the only one the wording supports.
   A copy of such a notice is nevertheless held in the register under (k), and Article 17(1)(a) keeps "the information registered" for ten years after deregistration, which is the only thing that retains it.
6. **Article 8(6) against Article 17(1)(a): two ten-year retention duties over overlapping objects, neither with a start.** (`src:249`, `src:444`; trap T14.)
   A copy of a required steps notice entered under 8(3)(k) is both "a copy of any notice served on the charity" (8(6)(c)) and "information registered" (17(1)(a)).
   Case: a notice served in 2015 on a charity that is deregistered in 2030: on the reading taken for 8(6) (F3.1 A) the copy may be discarded from 2025; on 17(1)(a) the information is kept until 2040.
   Not resolved here: G6's F6.5 settles 17(1)(a); the integrator should state the pair (BRIEF, NOTES item 4 of the survey).
   Also, "each registered charity" in 8(6) excludes a deregistered entity (Article 1), so on readings B and C of F3.1 the duty would run past the point at which its subject stops being a "registered charity".
7. **Article 9(1)(a) against Article 8(3)(k) and 9(1)(b): the name that the restricted section withholds.** (`src:256`, `src:235`, `src:257`.)
   The registered name of a restricted-section charity is withheld, but 9(1)(b) makes public the matters of 8(3)(a), (e), (f), (j) and (k), and (k) may be "a copy of the notice", which names the charity; (e) and (f) are statements the charity drafts.
   Case: a required steps notice served on a restricted-section charity, entered as a copy.
   The encoding makes the note of the notice a public element and cannot see what the copy says: a limit, reported here.
8. **Article 8(3), the list of items, against Article 12(5).** (`src:222-238`; `src:364`.)
   Article 12(5) has the Commissioner enter "the new or alternative registered name", but Article 8(3)(l) lists only "the previous registered name or names" of a name "changed".
   An alternative registered name is therefore an entry the list of 8(3) does not mention.
   Not a fork (no case the encoding decides differently); see the open questions.
9. **Article 8(2)(c) against Article 1.** (`src:221`, `src:20`, `src:43`.)
   "General section" and "restricted section" are defined in Article 1; "historic section" is not (trap T7).
   The encoding defines it by Article 8(5) (the section for a formerly registered charity that has been deregistered).
10. **Cross-references in Articles 8 to 10, checked.**
    8(3) to Article 12(2) (the registered name and number): present (`src:359-361`).
    8(3)(h) to Article 28 (organized religious charity): present (`src:653`).
    8(3)(i) to Article 5(3) and to paragraph (2) of Article 5: present (`src:150`, `src:155`).
    8(3)(m) to Article 13(9)(c): present (`src:397`).
    9(1)(b) to Article 8(3)(a), (e), (f), (j) and (k): present.
    9(6) to paragraphs (2), (3), (4) and (5) of Article 9: present.
    10(3)(b) to Article 9(1): present.
    No cross-reference points at the renumbered provisions (the Table of Renumbered Provisions concerns the original Articles 41 to 44 only).


## 7. Open questions for a domain expert

For a domain expert (Jersey charity law and the practice of the Jersey Charity Commissioner).

1. **What is "the most recent year" for the annual-return entry (8(3)(j))?** The calendar year, the charity's financial year, or the year from registration (F3.2)? Has the Commissioner published guidance? Which year is current on a given day (F3.7)?
2. **What is entered under 8(3)(j) before a charity's first year has ended?** The encoding refuses; the practice may be "not yet due".
3. **When do the ten years of 8(6) start (F3.1)?** And does the Commissioner in practice keep a registered charity's constitution for as long as it is registered?
4. **Which Law requires a registered office or business address in Jersey, and of whom (8(4)(a))?** Does every Jersey company and foundation have one? Are bodies incorporated under, but not by, an enactment covered (T6)?
5. **Who chooses which governor's address is entered as the principal address under 8(4)(c)?** The encoding allows any of them.
6. **Does an alternative registered name (Article 12(5)) count as a name "under which the entity was registered" for 8(5)(b)?** The encoding enters the registered name and the previous names only.
7. **What does "approved by the Commissioner" in 8(3)(e) and (f) require?** The encoding takes the approval as an input.
8. **Is a charity ever moved from the restricted section back to the general section, and by what act?** Article 9 describes only the move into the restricted section; Article 13(6)(b) speaks of "entering it in a different section". The encoding takes the sequence of entries as an input.
9. **What do the Orders say?** The Charities (Additional Information) (Jersey) Order 2018 R&O.59/2018, the Charities (Restricted Section of Register) (Jersey) Order 2018 R&O.60/2018 and any Order under 8(5)(e), 8(6)(d), 9(1)(d) and 10(2) are not among the sources. The funding condition, the grounds, what soliciting and a donation are, and the general public (9(2), 9(3)) are inputs.
10. **Does a copy of a required steps notice entered under 8(3)(k) disclose the name of a restricted-section charity (9(1)(a))?**
11. **Can the Commissioner protect a matter of a deregistered entity (10(4), F3.3)?** If a person is endangered by the summary of reasons in the historic section, what is the remedy?
12. **Is a charity run from a private dwelling house able to register (F3.10)?** And is "main premises" the premises the charity says, or the premises the Commissioner finds?
13. **Under the Restricted Section Order, what is the funding condition, and does a prescribed description of persons replace "the general public" in it (9(2)(a), 9(3)(b)(iii))?** What do the Order's definitions of soliciting and of a donation say?


## 8. What the sources do not answer

Each is a place where the encoding takes an input, answers a named refusal, or states no time, and never a plausible default.

1. **No Order is among the sources.** The Orders and Regulations the Articles name (8(3)(n), 8(5)(e), 8(6)(d), 9(1)(d), 9(2)(a), 9(2)(b), 9(3), 10(2)) and their content are inputs; so are "solicit" and "donation" (Article 1; 9(3)(b)(i), (ii)).
2. **No time is stated for**: establishing the register (8(1)); entering the items (8(3), 8(5)); the Commissioner's written notice of a refusal (9(7)(a)); making the public parts available on a website (10(1)). The rules carry no `WITHIN`. A MUST with no deadline stands until done and cannot be breached by delay; the encoding says so and invents nothing.
3. **The start of the ten years (8(6))** and **which year is "the most recent"** (8(3)(j)) are forks, not facts. The Interpretation (Jersey) Law 1954, which would settle how a period is counted, is not among the sources.
4. **What is entered under 8(3)(j)** when no year of the charity has ended since registration: a named refusal (`Art 8(3)(j) no year of the charity has ended since it was registered`).
5. **Whether the entity "was registered in the general section"** (8(5)(b)) when no earlier entry of the entity in a section is recorded: a named refusal.
6. **The date of the financial year-end**, when the financial-year reading is asked and it is not given: a named refusal.
7. **Which governor's address** is the principal address under 8(4)(c): the Law does not say; the encoding returns every address that is permitted.
8. **Everything in the Commissioner's judgement**: "approved by the Commissioner" (8(3)(e), (f)), "to the satisfaction of the Commissioner" (9(1)(c), 9(4)(b)), "satisfied" (9(6)), "considers" (9(6)(c), 10(4)), "specified" (10(2)); the Commissioner's own state of mind is an input in each case.
9. **Another enactment's requirement** that a company, foundation or other entity have a registered office or business address in Jersey (8(4)(a)): an input.
10. **Whether a premises is a "private dwelling house"**, and which are the "main premises": inputs.
11. **How a section change is made** (restricted to general, general to historic): Articles 9, 15 and 16 and Part 5; the encoding takes the dated entries of the entity as an input and computes the section from them.
12. **Vintages and commencement.** So far as the sources show, the text of Articles 8 to 10 is the same in all nine point-in-time versions from 1 January 2019: the Table of Endnote References lists amendments only to Article 1, Article 2(1), Article 19(1) (editorial), Article 31 (editorial) and Schedule 1, and none of the amending instruments in `inputs/amending/` touches Articles 8 to 10 (their other mentions of "Article 8", "9" or "10" are of other Laws).
    Who "the Minister" is in 8(3)(n), 8(5)(e), 8(6)(d), 9 and 10(2) does depend on the vintage: the rules are typed by the role `the Minister`, and the office is G1's `Art 1 the Minister under the text of` the vintage.
    Part 4 (Articles 8 to 17) came into force on 1 May 2018 (R&O.17/2018, Table of Legislation History); no rule here gates itself on commencement, the integrator's wrapper does.
    The enacted text of 2014 and anything after 2 October 2026 are not in the sources.
13. **What the funding condition of 9(2)(a) asks.** The Article says the condition is "as to refraining from soliciting donations from the general public or from any prescribed description of persons", and 9(3)(b)(iii) requires the Order to say what "the general public" is only "if the Order does not prescribe a description of persons".
    Whether the condition is met by refraining from soliciting the general public, the described persons, or both, and what "soliciting" and "a donation" are ("solicit" and "donation" are construed by the Order, Article 1), the Law does not say.
    The encoding takes "the funding condition is met" as one input and checks only what the Order must contain (`Art 9(3) the Order contains what Article 9(3) requires`).


## 9. Tests, checks and what they print

### 9.1 What the group's `check.sh` prints (verbatim, run on 2026-10-26 after the last edit)

`check.sh` is the skill's `assets/check.sh` extended with the template's warnings column, restricted to `deposit/g3-*.l4`, plus the import-graph check, `srcrefs.py check --refs` over every module, and `check-traces.py --require-all` over every module with a `#TRACE` (a DEONTIC value has no equality, so each trace carries an `-- EXPECT:` comment).
A module is RED if it has an error other than its expected failed assertions, a failed count other than `expected_failed` (12 for `g3-tests-red.l4`, 0 elsewhere), a refused assertion, or any warning.
Its copy is `work/g3/check.sh`; it is not a deliverable (the integrator writes the real one).

```text
l4 binary: FLEET_DIR/bin/l4 (sha256 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475)
(fleet pin: 18bd5a72fb8dc3180540afeece05da982f87d03aa098de562de2140e4e89d475)

module                                    errors satisfied  failed  refused  warnings  exp.fail
g3-art10-public-access.l4                      0         0       0        0         0         0
g3-art8-register.l4                            0         0       0        0         0         0
g3-art9-restricted-section.l4                  0         0       0        0         0         0
g3-fixtures.l4                                 0         0       0        0         0         0
g3-nouns.l4                                    0         0       0        0         0         0
g3-tests-art10-public-access.l4                0        50       0        0         0         0
g3-tests-art8-address.l4                       0        28       0        0         0         0
g3-tests-art8-historic.l4                      0        26       0        0         0         0
g3-tests-art8-register.l4                      0       129       0        0         0         0
g3-tests-art8-retention.l4                     0        26       0        0         0         0
g3-tests-art8-time.l4                          0        44       0        0         0         0
g3-tests-art9-restricted-section.l4            0       103       0        0         0         0
g3-tests-readings.l4                           0        43       0        0         0         0
g3-tests-red.l4                               12         0      12        0         0        12
TOTAL (14 modules)                            12       449      12        0         0        12
(a failed assertion is also an error; a refused assertion is also a warning; any other error or warning makes the run red)

shape: every g3 module has a plain name and imports only prelude, daydate, domain and g3- modules
srcrefs check: 168 src: lines, 69 runs, 77 locators, 0 problems
module                                        traces in-module   sidecar     ok   bad  unguarded
g3-tests-art10-public-access.l4                    9         9         0      9     0          0
g3-tests-art8-historic.l4                          4         4         0      4     0          0
g3-tests-art8-register.l4                          7         7         0      7     0          0
g3-tests-art8-retention.l4                        17        17         0     17     0          0
g3-tests-art9-restricted-section.l4               15        15         0     15     0          0
TOTAL                                             52        52         0     52     0          0
check-traces: all 52 guarded trace(s) behaved as expected

check.sh (G3): GREEN
(a green run says nothing about whether a domain expert agrees with any reading in FRAGMENT-G3.md)
```

### 9.2 The counts

- 14 modules: 5 rule or noun modules (`g3-nouns`, `g3-art8-register`, `g3-art9-restricted-section`, `g3-art10-public-access`, `g3-fixtures`) and 9 test modules.
- 449 assertions satisfied; 12 failed, all in `g3-tests-red.l4`, which lists exactly 12 on purpose (section 2 and the file's own comments say what each expectation was and why it fails); 0 refused; 0 warnings; 0 errors other than those 12.
- 52 `#TRACE`s, each guarded by an `EXPECT` comment; a STANDING expectation also names the modal (`MUST`, `MAY`, `MUST NOT`) and the act, because without a deadline a `MUST` and a `MAY` stand identically and only the printed residual tells them apart.
- `srcrefs.py check --refs`: 168 quote lines, 69 runs, 77 locators, 0 problems. Every public rule of the three rule modules quotes the source mechanically (the quote lines come from `srcrefs.py quote`, never retyped) and carries a locator.
- All 42 `@export`s have a sentence saying what they answer and a `@desc` on every `GIVEN` (checked by a script, 0 missing). Three were run through `l4 batch` against JSON (a record, a DEONTIC, an entity with a list): they evaluate.
  `l4 batch` refuses `interp` given as `{}` ("not known"); a partial record works, and the fields left out take the favoured reading.
- The binary is the fleet's (sha256 `18bd5a72...`).

### 9.3 Mutation testing (a measure of the tests; not a gate)

97 one-line mutations of the three rule modules (a comparison flipped, a bound moved by one day, a `MAY` made a `MUST`, an `AND` made an `OR`, a reading dispatched to the other reading, a list item dropped, and so on), each run against all the test modules and traces: **SUMMARY 97 killed, 0 survived, 0 skipped** (the final pass, on the final code and tests).
Earlier passes left 9 mutants alive: 7 pointed to real gaps in the tests, closed by adding tests (the tie between two entries on one day; the match of a note of a notice on its date; and five changes of a modal, which only the printed residual of a STANDING trace shows, because without a deadline a `MUST` and a `MAY` stand alike), and 2 were in fact killed by a refused assertion, which is a warning and which the first version of the harness did not count. The list is `work/g3/mutants.json` and the passes are `work/g3/mut-run*.txt`.

### 9.4 Method notes

- **Expected values come from the source.** Each was written from the Article (or from the convention a fork names) before the code ran. One expectation was corrected during the work, for a reason in the file: the first draft said that an entry with nothing recorded would be missing item (g), the date of registration; but the date is a field the register record always has, so it cannot be missing (a mistake in my premise, not an edit to fit the output; the comment in `g3-tests-art8-register` says so).
- **A re-read of every number in the tests against the source** was done: ten years (`src:249`, the only number in Articles 8 to 10 besides cross-references); the fourteen lettered items of 8(3) (`src:223-238`, counted by indentation: (a) to (n)); the five of 8(5) (`src:244-248`); the four of 8(6) (`src:250-253`); the three limbs of 8(4) (`src:240-242`); the four elements of 9(1) and the five matters of 9(1)(b) "(a), (e), (f), (j) and (k)" (`src:256-259`); the three paragraphs and the (i), (ii), (iii) of 9(3) (`src:264-269`); the four intentions of 9(5) (`src:274-279`); the three parts of 10(3) (`src:293-295`); the letter sets "(f) to (j)" and "(e), (g), (h) or (j)" (`src:224-225`) against the constructors of `Kind of entity` they select; and the constructor counts of the enumerations in `g3-nouns` (3, 14, 5, 4 plus one for 8(6), 8, 4, 2, 7). Every date of the tests was recomputed by hand (anniversaries, the day after, 29 February, the 1 January and 31 December edges).
- **No offence and no penalty** occurs in Articles 8 to 10, so no `Penalty provided` is used.
- **Nothing outside the permitted set was read** (see the final report's `peeked`).

