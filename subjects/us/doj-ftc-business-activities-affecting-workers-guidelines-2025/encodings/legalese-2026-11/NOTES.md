# DOJ/FTC Antitrust Guidelines for Business Activities Affecting Workers (2025): notes for a reviewer

**AGENCY ENFORCEMENT POLICY, NOT LAW.**
These guidelines say how the Department of Justice's Antitrust Division and the Federal Trade Commission identify and assess business practices affecting workers.
They do not say what a court must hold, and nothing in this encoding does either.

## 1. Status and what was checked

Status: `draft`, version 0.2.0.
Version 0.1.0 was written 2026-11-26 by one encoder working alone from the brief (`BRIEF.md`).
Version 0.2.0, the same day, answers an independent test pass (section 15) and an adversarial review (section 16), both made by other agents and relayed by the parent session.
No domain expert has read it.

What was checked, and how:

- The source is `../../registers/source-bundle/2025-business-activities-affecting-workers-guidelines.txt`, a `pdftotext` extraction of the 13-page PDF (text sha256 `522b2e1e…`, PDF sha256 `d882d0e6…`, both in the `.meta.json` beside it).
  It was read in full, footnotes included, before the design.
- The deposited text has no paragraph breaks, so for every question of which sentences share a paragraph the PDF itself was read, as `pdftotext -layout` output (section 11 lists the facts taken from it).
- `check.sh` was run with both builds, and its output is in section 7.
- `check.sh` was shown able to fail, on scratch copies of this folder on 2026-11-26: for version 0.1.0 it exited 1 when one expected count was wrong (96 for `wk-tests-boundaries.l4`), and exited 2 with an unstable build given as `L4_MAIN`, with no main build at the path given, with no `l4` at the path given, and with a stub `l4` that prints nothing it recognises; for version 0.2.0 the first case was run again (125 for `wk-tests-boundaries.l4`) and it exited 1.
  `wk-tests-red.l4` holds nine wrong assertions, and both builds fail all nine; `wk-tests.l4` (49) and `wk-tests-boundaries.l4` (126) are satisfied on both; `tests-independent.l4` has 123 satisfied and 6 failed on both, the 6 being its genuine ambiguities (section 15).
- Every double-quoted span in the modules' comments and in this file was checked against the deposited text by a script (section 14).
- The text's contact details in section 8 (its telephone numbers, postal addresses and complaint portals) are not reproduced anywhere in this folder: a search for their digits and street names finds nothing (section 14).

**Whether the guideline is in force** (what was read at source, and what was only reported):

| fact | how it is known |
| --- | --- |
| The document is titled "Antitrust Guidelines for Business Activities Affecting Workers" and marked "Revised: January 2025". | Read at source: the title page [pdf page 1]. |
| It is listed among the DOJ's current guidelines and policy statements. | Reported: the parent session read the DOJ's index page on 2026-11-25 (the `in_force_check` field of the `.meta.json`, which records that the page says "Updated November 17, 2025"), and the brief says the index dates the document January 16, 2025. This encoder fetched nothing and read neither. |
| It replaces the Antitrust Guidance for Human Resource Professionals (2016). | Read at source: n.1 [pdf page 2], "This document replaces the Antitrust Guidance for Human Resource Professionals (2016)." |

**What the document says it is.**
n.1 [pdf page 2], read at source: it "should not be construed as legal advice, and it has no force or effect of law"; it "is not intended to create any substantive or procedural rights enforceable at law by any party"; nothing in it "should be construed as mandating a particular outcome in any specific case"; and nothing in it "limits the discretion of any U.S. government agency to take any action, or not to take action".
The common brief's phrase "creates no independent rights or obligations" is not in this text (a search finds neither "independent rights" nor "rights or obligations"); n.1's own words are the ones above.
So the results are named for what the text says, with its own modal ("may violate", "can be per se illegal", "may require a fuller analysis", "may investigate and take action"), and no result says that a business acted lawfully or unlawfully.
Where the text states a sentence flatly ("are illegal even if they did not result in actual harm"), the result says "the agencies state that ...".

## Seat

A business, or its counsel, asking what the guidelines say of an agreement with another business about workers, of an exchange of information about workers, of a term in its own employment contracts, or of a claim it makes about workers' earnings.
The agencies are never the seat.
There is no seat layer with `@export` and `@desc` questions (deferred; the brief did not ask for one).

## 2. Target and builds

Target compiler: **`main`** (the stable `l4`), build `1.6.112 (main, e4f4bf3, 2026-11-18)`.
Written and tested with `unstable-20261125-82a76fe (unstable, 82a76fe, 2026-11-25)`.
`main` has no `REFUSE`, so a case the text does not answer is `NOTHING` from a `MAYBE`, never `FALSE`.
Every `NOT` is bracketed.
One dialect difference was met while writing: a constructor spelled like a field of the record input it is compared with (`the businesses are potentially competing employers`) is read as the field by the unstable build, which then fails to type-check, and as the constructor by main, which checks cleanly; the constructor was renamed before any test was written (`..., not shown to compete in the same labor market`), and the field has since become the three-valued `the finding that the businesses are potentially competing employers` (section 13).
No module uses anything `main` lacks; the two builds give the same counts on every module (section 7).

## 3. Scope

In scope: every sentence of the Overview, the general principles and sections 1 to 7 that states what the agencies or the antitrust laws may, can or will do with a kind of conduct, and the text's own examples as fixtures.

- **The Overview's list** (items 1 to 5) and its "This list is not exhaustive", as a lookup from the item to its own sentences.
- **General principles**: the agreement as a finding; its form, which no rule reads; the kinds of evidence, reported; whether the businesses compete for workers, from the labor markets they hire in; and, for an identified agreement, every statement the text makes on whether its effects matter.
- **Section 1**: the substance of wage-fixing and no-poach agreements (n.11 included), the crime, civil and DOJ sentences, "illegal even if they did not result in actual harm" with n.15's qualification, the starting point, and the Criminal Antitrust Anti-Retaliation Act sentence.
- **Section 2**: franchisor and franchisee; the franchisor organizing or enforcing among franchisees; franchisees among themselves.
- **Section 3**: every sentence on exchanges with competitors, the effect sentence with three values for the finding.
- **Sections 4 and 5**: non-compete clauses, and non-disclosure, training repayment, non-solicitation and exit fee or liquidated damages provisions, and the unnamed rest.
- **Section 6**: the Overview's sentence on independent contractors' compensation, and the competing-platforms example.
- **Section 7**: the body's "false or misleading" and the Overview's "false claims".

Not computed, by design:

- **No weighing.** Where the text lists evidence ("For example, they may consider whether a business has ..."), the caller supplies it and a function reports which kinds are present; nothing infers an agreement from it.
- **Findings are inputs.** Whether there is an agreement, whether the businesses are potentially competing employers, the n.15 conjuncts, the exchange's effect, whether a term limits competition, impedes worker mobility, or functions to prevent the worker from taking other work or starting a business, whether a claim is false or misleading: all are the caller's, never derived.
- **The labor market is the caller's.** The text gives no test for delineating one; each business names the labor markets it hires or retains workers in, and two compete for workers when they name one the same way, ignoring case and the whitespace around a name (fork F1).
- **Three-valued findings.** A finding whose absence must not be read as its contrary has a value for each: made, contrary made, not made (`Finding`, for potential competition and n.15's two conditions; and the findings on an agreement and on an exchange's effect). Every other finding is a BOOLEAN, TRUE when made; its FALSE stands for both the contrary and a finding not made, which is safe only where the text says nothing of the contrary (section 12, the last row of the last table).
- **No numeric inputs.** The text states no figure, so no rule takes a number, and there is no range to guard; the guards are the `NOTHING` answers of section 12.

## 4. Modules

| module | what it holds |
| --- | --- |
| `wk-nouns.l4` | Types only: the inputs, one record per kind of conduct. |
| `wk-agreements.l4` | The Overview's list; the general principles (evidence, whether the businesses compete for workers, whether the agreement's effects matter); section 1 (substance, statements, the Act); section 2. |
| `wk-information.l4` | Section 3. |
| `wk-restrictive-terms.l4` | Sections 4 and 5. |
| `wk-contractors-and-claims.l4` | Sections 6 and 7. |
| `wk-test-fixtures.l4` | Businesses, pairs and builders shared by the test modules; no rule and no assertion. |
| `wk-tests.l4` | Tests from the text: a scenario for each of its examples and its definite sentences, cited by provision and pdf page. |
| `wk-tests-boundaries.l4` | Both sides of every distinction, the guards, the fields no rule reads, and a discriminating fixture per fork that can have one. |
| `wk-tests-red.l4` | Nine positive controls, each a misreading that must fail. |
| `tests-independent.l4` | The independent test author's file (section 15): 129 assertions, 6 of them left failing as genuine ambiguities. |

Every rule carries an `@ref` with its section, footnote and `[pdf page N]`.
The function for section 6's platform example (`6: whether the text says the agreement is one between competing platforms to fix the compensation of independent contractors`, with the predicate `6: the agreement is one between competing platforms to fix the compensation of independent contractors` true only when it is) is defined in `wk-agreements.l4`, beside the general principles' function that reads it, and is cited to section 6; `wk-contractors-and-claims.l4` uses the same function.
So is section 2's per se function (`2: whether the text says that such an agreement between a franchisor and its franchisee can be per se illegal`), and n.15's (`n.15: whether the restraint is ...`).

Every report returns the text's sentences that apply, in the text's order.
`EMPTY` means that no sentence of that section applies to the facts given; it is never a finding that the conduct is lawful.
`NOTHING` means that the answer turns on a finding the caller has not made, that the case is one the section does not speak of, or that the text gives no answer (fork F23; section 12 lists every case).

## 5. Coverage

Every part of the text, every list item with its own rule, and every footnote, with its disposition.
The text numbers its sections 1 to 8 and the Overview's items 1 to 5; the unnumbered Overview and general principles are split here by paragraph or sentence.

| part | disposition | where, or why |
| --- | --- | --- |
| Title page [pdf page 1] | inert | Title and date ("Revised: January 2025"). |
| Overview, first paragraph [pdf page 2] | inert | Framing: the agencies, the laws they enforce, and why competition for workers matters; "Business practices may violate the antitrust laws when they harm the competitive process" states no test the agencies apply (each section states its own). |
| How to Use, the map of sections and "Certain agreements ... may give rise to criminal liability. Other types ... may be subject to civil liability rather than criminal prosecution" [pdf pages 2-3] | inert | Framing: which agreements may give rise to criminal liability is said in sections 1 and 6; the other types, subject to civil liability rather than criminal prosecution, are not named (section 6 of these notes). |
| How to Use, the independent contractors sentence [pdf page 3] | encoded | `6: what section 6 says of the agreement`, its first statement. |
| How to Use, the false claims sentence [pdf page 3] | encoded | `7: what section 7 says of the claim`, its first statement (fork F19). |
| How to Use, section 8 | inert | A pointer. |
| "the Agencies may investigate certain types of agreements or business practices" [pdf page 3] | encoded | `Overview: what the list says of the practice`. |
| Overview item 1 | encoded | The same, with its "may expose companies and executives to criminal liability" and DOJ's felony charges; section 1 holds the facts. |
| Overview item 2 | encoded | The same; its "subject to antitrust scrutiny even if ... among the franchisees" is also given, as the Overview's, by `2: what section 2 says of the agreement` for franchisees among themselves (fork F24). |
| Overview item 3 | encoded | The same; "may be illegal even if companies use a third party or intermediary". Its middle sentence, "This includes exchanges of information about compensation or other terms or conditions of employment, and other exchanges of information that harm competition for workers", is not in the item's answer (items 4 and 5 carry their "These include" sentences); section 3 holds the facts. |
| Overview item 4 | encoded | The same, with its three kinds of non-compete provision (fork F15). |
| Overview item 5 | encoded | The same, with its four kinds. |
| "This list is not exhaustive. Listed activities may or may not be an antitrust violation." | encoded | In every item's answer; an unnamed practice answers NOTHING (fork F3). The invitation to report is inert (section 8). |
| General principles: the focus on "an agreement between businesses that harms competition for workers" [pdf page 3] | encoded | The agreement is the caller's finding, three-valued (fork F2), and the gate of sections 1, 2 and 6 and of the effects question. |
| General principles: "need not be explicit or written down", formal or informal, express or implicit [pdf pages 3-4] | encoded | `Form of the agreement`, read by no rule; a fixture changes every field and gets the same answer. |
| General principles: "illegal even if they are never carried out" [pdf page 4] | encoded | The same field set (`it was ever carried out`). |
| General principles: direct and circumstantial evidence, the four examples [pdf page 4] | encoded | `General principles: the kinds of evidence of an agreement that are present`, a report (fork F3). |
| General principles: "If the Agencies identify an agreement ... Some types of agreements are illegal regardless of their effects. In other cases, the Agencies perform a deeper analysis" [pdf page 4], n.8 | encoded | `General principles: what the text says of whether the agreement's effects matter` (forks F5, F20). |
| General principles: "compete for workers", "compete in the same labor markets even if they do not compete as sellers" [pdf page 4] | encoded | `General principles: whether the businesses compete for workers` (fork F1). |
| General principles: a joint venture or other collaboration; not competitors downstream; the airplane manufacturers and part suppliers [pdf page 4] | encoded | Not read by the test; the airplane example is a fixture. |
| 1, heading [pdf page 5] | inert | "Some types of agreements, including ..." is read for fork F3. |
| 1, "may be committing an antitrust crime" [pdf page 5] | encoded | `1: what section 1 says of the agreement` (fork F4). |
| 1, "Even if criminal charges are not pursued ... civil liability" [pdf page 5], n.9 | encoded | The same. |
| 1, "whether they are informal or formal, written or unwritten, or spoken or unspoken" [pdf page 5], n.10 | encoded | Not read. |
| 1, the wage-fixing bullet [pdf page 5] | encoded | `1: what the agreement is, in substance`. Whether it is "between individuals at different businesses" is not read. |
| 1, the no-poach bullet [pdf page 5], n.11 | encoded | The same; n.11's permission agreement is a no-poach agreement, and its employer-worker non-solicitation agreement is section 5's. |
| 1, "substance ... regardless of its precise form"; a range, ceiling, or benchmark [pdf page 5], n.12 | encoded | The same. |
| 1, a restriction short of a complete prohibition; no cold calls [pdf pages 5-6], n.13 | encoded | The same; whether applicants may still be hired is not read. |
| 1, "When formed between competing or potentially competing employers ... illegal even if they did not result in actual harm" [pdf page 6], n.14 | encoded | Section 1's third statement (fork F4); "directly or through an intermediary" not read. |
| 1, "Nor does it matter if the agreement does not include specific pay rates"; the starting point [pdf page 6], n.16 | encoded | Section 1's starting-point statement (fork F6). |
| 1, "The DOJ may criminally investigate and, where appropriate, bring felony charges" [pdf page 6] | encoded | Section 1's last statement (fork F4). |
| 1, the Criminal Antitrust Anti-Retaliation Act [pdf page 6] | encoded | `1: what section 1 says of a report of an antitrust crime` (fork F21). |
| 2, heading and "No-poach clauses in franchise agreements are also subject to antitrust scrutiny" [pdf page 6] | encoded | `2: what section 2 says of the agreement`. |
| 2, "Often, franchisors compete with franchisees for workers" [pdf page 6], n.18 | encoded | Read as the condition of the per se sentence; whether they compete is an input, never presumed (fork F7). |
| 2, franchisor and franchisee, "can be per se illegal" [pdf pages 6-7], n.19 | encoded | `2: whether the text says that such an agreement between a franchisor and its franchisee can be per se illegal`, and `2: what section 2 says of the agreement` (fork F7). |
| 2, the franchisor "organizing or enforcing" among franchisees that compete [pdf page 7], n.20 | encoded | The same (fork F9). |
| 2, franchisees among themselves, "other federal and state laws" [pdf page 7], n.21 | encoded | The same (fork F28); the state statutes of n.21 are out-of-scope. |
| 3, heading, and "Sharing ... may violate the antitrust laws" [pdf page 7], n.22 | encoded | `3: what section 3 says of the exchange` (fork F13). |
| 3, "may be unlawful when the information exchange has, or is likely to have, an anticompetitive effect, whether or not that effect was intended" [pdf page 7], n.23 | encoded | The same (fork F12). |
| 3, "may be explicit or it may be implied" [pdf page 7] | encoded | Not read. |
| 3, "may indicate the existence of a wage-fixing conspiracy" [pdf page 7] | encoded | The same (fork F13). |
| 3, through an algorithm or a third party's tool or product [pdf page 7] | encoded | The same (fork F25). |
| 3, the poultry processors' settlement [pdf page 7], n.24 | encoded | Two fixtures, direct with the effect not assessed and through a third-party firm with the effect found. |
| 3, recommendations generated through a third party [pdf page 7], n.25 | encoded | The same; adherence not read. |
| 3, an agreement to use shared recommendations, despite discretion or cheating [pdf page 8] | encoded | The same; discretion not read. |
| 3, "Companies can sometimes work together ... in ways that are not illegal" [pdf page 8] | inert | States no test. |
| 3, a joint venture's agreement to share wage information [pdf page 8] | encoded | The same; the transaction not read. |
| 4, heading and "Non-compete clauses that restrict workers from switching jobs or starting a competing business can violate the antitrust laws" [pdf page 8], n.26 | encoded | `4: what section 4 says of the term` (fork F26). |
| 4, how non-competes harm competition [pdf page 8] | inert | Explanation. |
| 4, "may investigate and take action against non-competes and other restraints on worker mobility that limit competition" [pdf page 8] | encoded | The same (forks F14, F18). |
| 4, the 2020 deferred prosecution agreement [pdf page 8], n.27 | inert | A past resolution; its remedy states no test. |
| 4, the FTC's enforcement actions "In 2021" and its merger orders [pdf pages 8-9], n.28, n.29 | inert | Past actions; section 11 notes the date. |
| 4, the FTC's final rule of April 2024, its setting aside, its appeal, and "the FTC retains the legal authority" [pdf page 9], n.30-n.32 | out-of-scope | Dated: the text reports the rule's status as of its January 2025 writing ("The order is currently on appeal") and sends the reader to ftc.gov for the latest; encoding that status as current would state a fact this encoding cannot keep true, and the sentence on the FTC's authority states no test on any conduct. |
| 4, "may also violate other federal laws", "can also violate state laws" [pdf page 9], n.33-n.35 | encoded | The same; the laws themselves are out-of-scope. |
| 5, heading, and "may also investigate and take action against other restrictive agreements that impede worker mobility or otherwise undermine competition" [pdf page 10] | encoded | `5: what section 5 says of the term` (fork F14). |
| 5, "The following examples illustrate" [pdf page 10] | inert | Framing, read for fork F17. |
| 5, the non-disclosure agreement bullet [pdf page 10], n.36, n.37 | encoded | Its three sentences (forks F16, F27). |
| 5, the training repayment bullet [pdf page 10], n.38 | encoded | The definition is the caller's kind; the hedged sentence and the example (fork F16). |
| 5, the non-solicitation bullet [pdf page 10] | encoded | The same. |
| 5, the exit fee and liquidated damages bullet [pdf page 10], n.39 | encoded | The same. |
| 5, how these restrictions harm competition, and monopsony power [pdf page 11], n.40 | inert | Explanation. |
| 5, "Such provisions raise many of the same antitrust concerns as non-competes, and the Agencies may investigate if there are indications" [pdf page 11] | encoded | The same, as two statements (forks F17, F27). |
| 5, other federal agencies' authorities [pdf page 11], n.41, n.42 | out-of-scope | Other agencies' statutes, not these guidelines' statements about the antitrust laws. |
| 5, "State law also sets limits on training repayment requirements and NDA restrictions" [pdf page 11], n.43 | encoded | The same (fork F28); the Colorado statute of n.43 is out-of-scope. |
| 6, heading and "workers, which includes both employees and independent contractors" [pdf page 11] | encoded | Sections 1 and 2 read no kind of workers (fork F10); section 6's function. |
| 6, what independent contractors "typically" are, and platform apps [pdf page 11], n.44 | inert | A description, not a test: whether the workers are independent contractors is the caller's; n.44's FLSA rule is out-of-scope. |
| 6, "The antitrust laws also apply to these kinds of platform businesses" [pdf page 11] | inert | States no test: no rule excludes a platform, and only section 6's example reads the platform field. |
| 6, the competing platforms fixing contractors' compensation [pdf page 11] | encoded | `6: what section 6 says of the agreement` (fork F11). |
| 7, heading and "may investigate and take action against businesses that make false or misleading claims about potential earnings" [pdf page 12] | encoded | `7: what section 7 says of the claim` (fork F19). |
| 7, the FTC's actions [pdf page 12], n.45-n.48 | encoded | A fixture: claims that workers "would earn substantially more", false. |
| 7, "honest businesses are less able to fairly compete" [pdf page 12] | inert | Explanation. |
| 8, reporting violations [pdf page 13] | inert | An invitation, contact details (not reproduced here) and six questions a complaint may answer; it states no rule. |

| footnote | disposition | note |
| --- | --- | --- |
| n.1 | inert | The document's own disclaimers and the 2016 guidance it replaces (section 1; section 10). |
| n.7 | out-of-scope | Points to the 2023 Merger Guidelines for "how agencies consider the effects of business transactions such as mergers and acquisitions on workers"; another subject of this repository. |
| n.11, n.15 | encoded | No-poach agreements and their difference from non-solicitation agreements; the subordinate-and-collateral qualification, its two conditions three-valued findings. |
| n.17 | out-of-scope | The Criminal Antitrust Anti-Retaliation Act itself (15 U.S.C. § 7a-3), a statute; only the text's sentence about it is encoded. |
| n.21, n.35, n.43 | out-of-scope | State statutes (Washington, Minnesota; California, North Dakota; Colorado). |
| n.30, n.31, n.32 | out-of-scope | The FTC's non-compete rule and its litigation, dated (the coverage row above). |
| n.41, n.42 | out-of-scope | Other federal agencies' authorities and actions. |
| n.44 | out-of-scope | The Fair Labor Standards Act classification rule. |
| all others: n.2-6, n.8-10, n.12-14, n.16, n.18-20, n.22-29, n.33, n.34, n.36-40, n.45-48 | inert | Citations of cases, orders, statements of interest and complaints that support a body sentence and state no test of their own (the full text of every footnote was read on 2026-11-26). |

Footnotes named in a part's row are named to locate it; each footnote's disposition is the one in the footnote table.

Counts.
Parts (72 rows): 55 encoded, 15 inert, 2 out-of-scope, 0 deferred (counted from the table by a script, 2026-11-26, after the "Often, franchisors compete" row became encoded on review, fork F7).
Footnotes (48): 2 encoded, 11 out-of-scope, 35 inert, each listed once; n.28 spans pdf pages 8 and 9, and the numerals of n.10 and n.33 sit one line out of place in the extraction.

## 6. Criminal and civil: where the text says which

The brief asked for "where it says civil liability only".
**The text names no conduct as civil-only.**
How to Use says only that "Other types of agreements may be subject to civil liability rather than criminal prosecution" [pdf page 3], without naming them, and the Criminal Antitrust Anti-Retaliation Act sentence is about whistleblower protection for reporting crimes, not about civil liability.
What the text says of criminal exposure, all encoded:

| sentence | where | result |
| --- | --- | --- |
| "may expose companies and executives to criminal liability"; DOJ "exercises its authority to bring felony criminal charges" | Overview item 1 [pdf page 3] | `Overview: what the list says of the practice` |
| "may be committing an antitrust crime" (businesses that compete with each other for workers) | 1 [pdf page 5] | section 1's first statement |
| "Even if criminal charges are not pursued, these agreements may also be subject to civil liability" | 1 [pdf page 5] | section 1's second statement |
| "The DOJ may criminally investigate and, where appropriate, bring felony charges" | 1 [pdf page 6] | section 1's last statement |
| "may constitute the type of per se violation of the antitrust laws", which "exposes the platforms to criminal liability" (the text has "that the exposes", section 11) | 6 [pdf page 11] | section 6's second statement |

Three more mentions are not statements of their own about the conduct, and are not encoded as such: section 1's heading says such agreements "can lead to criminal charges" [pdf page 5], which its first sentence states in full; How to Use says "Certain agreements and other activities may give rise to criminal liability" [pdf page 3], naming none; and section 4 reports a 2020 deferred prosecution agreement for a conspiracy "to allocate chemotherapy and radiation treatments for cancer patients", whose "criminal resolution required the defendant to waive and not enforce non-compete provisions" [pdf page 8]; it does not say that a non-compete carries criminal liability.
Sections 2, 3, 5 and 7 say nothing of criminal or civil liability.
The footnotes' descriptions of the matters they cite (a holding "in a civil case", n.12; private civil damages cases and consent decrees, n.13; the deferred prosecution agreement, n.27) describe those matters, not the conduct the guidelines address, and are inert (a search of the text for `crim`, `civil`, `felony` and `prosecut` on 2026-11-26 found no other mention).

## 7. Checks

`L4=<unstable l4> L4_MAIN=<main l4> ./check.sh`, run 2026-11-26 on version 0.2.0, exit status 0:

```
your l4:    unstable-20261125-82a76fe (unstable, 82a76fe, 2026-11-25)
main build: 1.6.112 (main, e4f4bf3, 2026-11-18)
module                          err  sat fail  ref  expected |  err  sat fail  ref  main
tests-independent.l4              6  123    6    0     123/6 |    6  123    6    0  same
wk-agreements.l4                  0    0    0    0       0/0 |    0    0    0    0  same
wk-contractors-and-claims.l4      0    0    0    0       0/0 |    0    0    0    0  same
wk-information.l4                 0    0    0    0       0/0 |    0    0    0    0  same
wk-nouns.l4                       0    0    0    0       0/0 |    0    0    0    0  same
wk-restrictive-terms.l4           0    0    0    0       0/0 |    0    0    0    0  same
wk-test-fixtures.l4               0    0    0    0       0/0 |    0    0    0    0  same
wk-tests-boundaries.l4            0  126    0    0     126/0 |    0  126    0    0  same
wk-tests-red.l4                   9    0    9    0       0/9 |    9    0    9    0  same
wk-tests.l4                       0   49    0    0      49/0 |    0   49    0    0  same
TOTAL (10 modules): satisfied unstable 298, main 298; failed (positive controls and expected failures) unstable 15, main 15
(a failed assertion is also an error; the expected column is satisfied/failed)
check.sh: all passed
```

The nine errors in `wk-tests-red.l4` are its nine failed assertions, and the six in `tests-independent.l4` are its six expected failures (lines 511, 552, 553, 669, 735 and 736 on both builds, section 15); no module has any other error.
The stable `l4 run` exits 0 on `wk-tests-red.l4` and the unstable one exits 1 (both measured 2026-11-26), which is why `check.sh` reads the diagnostics.
What it does not see: equal counts on the two builds can hide a different assertion failing on each side; for `tests-independent.l4` the failing lines were listed on each build after every commit of version 0.2.0, and were the same on both.

## 8. Fork register

Every reading below is **assumed, not ruled**; F7's was changed at the parent session's direction, which its relay calls a ruling; it is not recorded here as one.
Each has a fixture in `wk-tests-boundaries.l4` (or `wk-tests.l4` where named) on which the reading taken and its alternative give different answers, except those whose last column says there is no fixture, because their alternative is a different name, layout or rule rather than a different answer.

| fork | the question | reading taken | the alternative | the text |
| --- | --- | --- | --- | --- |
| F1 | What makes two businesses "compete for workers"? | Both hire or retain workers in a labor market the caller names the same way, compared ignoring case and the whitespace around a name (a run of spaces inside a name is not made one, and a blank name names no labor market); one shared market among several is enough; their products and any collaborative relationship are not read. Failing a shared market, the caller's three-valued finding that they are potentially competing employers: made, they are (whether or not both name labor markets); contrary, they do not compete if both name their labor markets, and NOTHING if either names none; not made, NOTHING. The same business named twice (names alike, compared the same way) is NOTHING. Changed on review (A1): names were compared exactly, and the finding was a BOOLEAN whose FALSE read as the contrary. | A test that reads the products or the relationship; a delineation of labor markets by the encoding; or an exact comparison of names. | General principles [pdf page 4] "compete in the same labor markets even if they do not compete as sellers"; "even if they have some other collaborative or cooperative relationship"; 1 [pdf page 6]. Fixtures: the airplane example; Acme and Cove (same products, different labor markets); the finding not made; names differing in case and spacing; blank names; one business named twice; a positive control. |
| F2 | How is the agreement supplied? | A finding with three values (identified, found none, not determined); never inferred from the evidence, which is only reported. | Inferring an agreement from the evidence present. | General principles [pdf pages 3-4]. No fixture for the alternative: it is a rule the text does not state. The three values each have a fixture. |
| F3 | How is a list that "is not exhaustive" represented? | The Overview's list: a practice it does not name answers NOTHING, not a finding that the list does not cover it. The evidence ("For example"): other evidence is reported as such. The types illegal regardless of effects ("Some types", "including"): an agreement of a type no section speaks of gets NOTHING from the effects question, not the "deeper analysis" of the "other cases". | Treating an unlisted practice as outside the agencies' interest, or an unlisted type as an "other case" given a deeper analysis. | Overview [pdf page 3]; General principles [pdf page 4]; 1 heading [pdf page 5]. Fixtures: the unnamed practice; other evidence; `something else relating to workers`. |
| F4 | Which competitors does each sentence of section 1 reach? | Word for word, with the PDF's paragraphs (section 11): the first paragraph's "Businesses that compete with each other for workers may be committing an antitrust crime" and its civil sentence ("these agreements") for actual competitors only; the "When formed between competing or potentially competing employers ... illegal even if" sentence for both; and the DOJ sentence, a paragraph of its own, for both, its "these agreements" read with their nearest antecedent, the preceding paragraph's "these types of agreements". Re-decided on review: version 0.1.0 gave the same answers, but said the DOJ sentence was in that paragraph, which the PDF shows it is not. | Every sentence for both; every sentence for actual competitors only (the DOJ sentence then pairs with the crime sentence of the first paragraph); or the DOJ sentence for any wage-fixing or no-poach agreement, competitors or not (the heading's "can lead to criminal charges"). | 1 [pdf pages 5-6]. Fixtures: potentially competing employers get two statements, not four, and a positive control; `tests-independent.l4` line 470 (potential competitors get the DOJ sentence; red under the actual-only reading) and line 478 (non-competitors do not; red under the any-agreement reading). |
| F5 | Where does n.15 reach? | It is attached to "illegal even if they did not result in actual harm" and replaces that sentence when both its findings are made; a contrary finding on either leaves the sentence; otherwise (one made and one not made, or neither made) the answer is NOTHING, each finding being three-valued since review (B(i)). It does not withdraw the crime, civil or DOJ sentences, and it does not reach section 2 or section 6. The general principles' "collaborative or cooperative relationship" [pdf page 4] is not one of its conditions. | n.15 also withdraws the crime, civil or DOJ sentences (the independent author's reading: `tests-independent.l4` lines 552 and 553, left failing as a genuine ambiguity); or it qualifies section 2's per se sentence too; or it needs the collaborative relationship field as well. | n.15 [pdf page 6] "Such agreements may require a fuller analysis of their effects, however, when the restraint is subordinate and collateral to a broader business collaboration". Fixtures: each condition alone; both; one made and one not made; a franchisor's no-poach with n.15 (section 2's statement remains); the collaboration field with no n.15 finding. |
| F6 | The starting point. | "may be a form of wage fixing under the law" is given, for competing or potentially competing employers, and section 1's other sentences are not; the effects question gives NOTHING; section 6 gives NOTHING, since whether a starting point is "fix the compensation" [pdf page 11] the text does not say (changed on review, A2: it was EMPTY). A caller with the agencies' conclusion that it is wage fixing supplies it as a coordination of wages. | Treating the starting point as a wage-fixing agreement outright, so that "illegal even if" follows, as "Nor does it matter if the agreement does not include specific pay rates", in the same paragraph, suggests (the independent author's reading: `tests-independent.l4` line 511, left failing as a genuine ambiguity). | 1 [pdf page 6] "an agreement to set a starting point for compensation may be a form of wage fixing under the law". Fixtures in all three places. |
| F7 | Does section 2's per se sentence for a franchisor and its franchisee need them to compete for workers? | Yes, changed on review at the parent session's direction (A5): "Often, franchisors compete with franchisees for workers" introduces the agreements "in which the franchisor and franchisee agree not to compete for workers", and "Such an agreement can be per se illegal". Not competing: the scrutiny sentence only; potentially competing, or not stated: NOTHING, since section 2 does not speak of potential competitors. When they compete, section 1's sentences apply as well (F20). | Version 0.1.0's reading, kept as the alternative: not conditioned, "Often" being background, so that a franchisor and franchisee that do not compete get the per se sentence too. | 2 [pdf pages 6-7]. Fixtures: not competing; potentially competing; not stated; a positive control. |
| F8 | An agreement with several terms. | One term per agreement record; a caller assesses each term. | A list of terms in one record. | 1 [pdf page 5]. No fixture: a layout. |
| F9 | Section 2's "franchisees that compete for workers". | Actual competitors only, and the franchisor's sentence needs its organizing or enforcing; for potentially competing franchisees with the franchisor organizing, NOTHING, since section 2 does not speak of potential competitors (changed on review, A2: the sentence was omitted). The other-law sentence is F28's, and the Overview's F24's. | Potential competitors too; or potential competitors omitted (version 0.1.0). | 2 [pdf page 7]. Fixtures: potentially competing franchisees, the franchisor organizing and not. |
| F10 | Do sections 1 and 2 reach independent contractors? | Yes: section 6 says the antitrust laws prohibit anticompetitive conduct directed at workers, "which includes both employees and independent contractors", so neither reads the kind of workers. | Sections 1 and 2 for employees only, independent contractors left to section 6. | 6 [pdf page 11]. Fixture: section 1 on independent contractors. |
| F11 | Section 6's "competing platforms" and "fix the compensation". | Platforms that compete for those workers in the same labor market (actual); potentially competing platforms NOTHING, since section 6 does not speak of potential competitors (changed on review, A2: the per se sentence was omitted); "fix the compensation" is section 1's wage-fixing substance, and a starting point is NOTHING (F6). The Overview's sentence on independent contractors has no condition on competing and none is read: unlike section 3 (F13), nothing in that sentence or its section states one for it, and "competing platforms" is a separate example. | Platforms competing as sellers; or potential competitors too. | 6 [pdf page 11]; How to Use [pdf page 3]. Fixtures: platforms not competing, potentially competing, and agreeing a starting point. |
| F12 | Section 3's effect finding. | Three values: the effect found gives the sentence; the contrary found gives no effect sentence; not assessed, for competitively sensitive information between competitors, makes the whole answer NOTHING. Changed on review: version 0.1.0 gave the sentence in a form marked as not assessed, which is not one of F23's two values; now F12 is F23 applied (the answer turns on a finding not made), and `tests-independent.l4` line 626 passes. That form's constructor stays declared, never returned, because the independent tests name it. Intent is not read. | One BOOLEAN, so that an effect not assessed and an effect found absent read alike; or version 0.1.0's form. | 3 [pdf page 7] "has, or is likely to have, an anticompetitive effect, whether or not that effect was intended". Fixtures: all three values; two positive controls. |
| F13 | Whom, and what, does section 3 reach? | Every sentence is about exchanges with competitors: the heading, the first two sentences ("with competitors", "with a competitor") and Overview item 3 [pdf page 3] ("companies that compete for workers") say so, which is why the condition is read here and not into F11's Overview sentence, where nothing states one (and F7 now reads its own condition from its own text). So the section reads only businesses that compete for workers in the same labor market: EMPTY for non-competitors; NOTHING for potentially competing employers, of whom the section does not speak (changed on review, A2: it was EMPTY), and when not stated. The sentences that say "competitively sensitive" (and "may indicate the existence of a wage-fixing conspiracy", in the same paragraph of the PDF) need that field; the recommendations, shared-recommendations and joint-venture sentences, which do not use the words, do not. | Potential competitors too; or every sentence gated on competitively sensitive information; or the recommendations, shared-recommendations and joint-venture sentences, which never say "competitors" (the gate comes from the heading), read for any businesses. | 3 [pdf pages 7-8]. Fixtures: potential competitors; non-sensitive recommendations through an algorithm; joint venture partners that do not compete for workers agreeing to share wage data (EMPTY here; the third alternative gives the joint-venture sentence). |
| F14 | Are "that limit competition" (4) and "that impede worker mobility or otherwise undermine competition" (5) conditions? | Yes, restrictive clauses: each "may investigate and take action" sentence needs its finding. | Descriptive: every non-compete, every restrictive agreement. | 4 [pdf page 8]; 5 [pdf page 10]. Fixtures: with and without each finding. |
| F15 | A provision requiring a penalty on leaving. | The kind of term is the caller's: Overview item 4 counts it among non-compete provisions, section 5 calls it an exit fee; both answers are "may" or "can". | One kind decided by the encoding. | Overview item 4 [pdf page 3]; 5 [pdf page 10]. No fixture: the caller's choice. |
| F16 | Section 5's "function to prevent", and "such as if". | One finding for the four bullets' differing words ("seeking or accepting other work", "working for another firm", "seeking or accepting another job", "starting a business"). For training repayment, non-solicitation and exit fees, "Depending on the facts and circumstances ... can be anticompetitive" is given without condition and "such as if" is the text's example, given beside it only when found. For a non-disclosure agreement "can violate the antitrust laws when they span such a large scope" is a condition. `tests-independent.l4` lines 674, 680 and 686 expected nothing for the three kinds without the finding: a test-author error, corrected (section 15). | Four findings; or "such as if" as a condition, so that a provision without the finding gets no statement. | 5 [pdf page 10]. Fixtures: each kind with and without the finding; a positive control. |
| F17 | Whom do "Such provisions raise many of the same antitrust concerns as non-competes" and "the Agencies may investigate if there are indications that such a restrictive condition on workers is harming competition" reach? | Split on review (`tests-independent.l4` line 690): the first clause, "Such provisions", the kinds the bullets name, a non-disclosure agreement only when broad (F27); the second, "such a restrictive condition", every kind, the unnamed one included, since the bullets are examples that "illustrate how restrictive conditions could potentially violate the antitrust laws", read as F3 reads every list of examples, as open; it needs the finding. | Both clauses for the four kinds only (version 0.1.0); or both for every kind. | 5 [pdf pages 10-11]. Fixtures: the unnamed kind with indications of harm, and with nothing found. |
| F18 | Section 4 against section 5. | Section 4's statements for a non-compete clause only; section 5's for every other kind; section 4's "other restraints on worker mobility" is not given to section 5's kinds, which have section 5's own sentence. | Section 4's investigate sentence for every restraint on worker mobility. | 4 [pdf page 8]; 5 [pdf page 10]. Fixtures: each function on the other's kinds and findings. |
| F19 | False against misleading. | The body's "false or misleading" for the investigate sentence; the Overview's "false claims ... may violate federal laws against unfair, deceptive, or abusive practices" for a false claim only. | Both sentences for a misleading claim. | 7 [pdf page 12]; How to Use [pdf page 3]. Fixture: misleading, not false; a positive control. |
| F20 | Several sections speak to one agreement's effects, or to its criminal exposure. | Every statement that applies is listed, each with its own section's modal, with no precedence (a franchisor and franchisee that compete get section 1's and section 2's; competing platforms get section 1's and section 6's); section 1's crime and DOJ sentences are given to a franchisor and franchisee that compete, since section 2 is silent on criminal exposure and its first sentence says "also". | The more specific section wins, so that section 2's silence takes section 1's criminal sentences away (the independent author's reading: `tests-independent.l4` lines 735 and 736, left failing as a genuine ambiguity). | General principles [pdf page 4]; 2 [pdf page 6]. Fixture: the franchisor and franchisee that compete. |
| F21 | The Act's sentence. | Given for the four roles it names reporting an antitrust crime; NOTHING for another role or for conduct that is not an antitrust crime. The Act itself is not encoded. | The Act's own coverage. | 1 [pdf page 6], n.17. Fixtures: both NOTHING cases. |
| F22 | The Overview's items. | The caller names the item, and the answer is the item's own sentences; the facts are read in sections 1 to 5. | Deriving the item from the facts. | Overview [pdf page 3]. No fixture: a layout. |
| F23 | What a report's EMPTY and NOTHING mean. | EMPTY: no sentence of the section applies on the facts given. NOTHING: the answer turns on a finding not made, the case is one the section does not speak of, or the text does not answer; since a list cannot mark one sentence as open, one open sentence makes the whole report NOTHING. Section 12 tables when each sentence is given, omitted, or makes the report NOTHING. Section 3's effect not assessed (F12) is the first kind of NOTHING. Neither is a finding of lawfulness. | One value for both; or a list that leaves an open sentence out without saying so. | The brief's rule that a case the text does not answer is NOTHING; the EMPTY reading is this row's. Fixtures: every guard (section 12). |
| F24 | "No-poach clauses in franchise agreements are also subject to antitrust scrutiny", and Overview item 2. | The body's sentence is read for a franchisor and its franchisee, the parties to a franchise agreement. Franchisees among themselves get the Overview's sentence, which names them ("or, for example, among the franchisees of the same franchisor"), attributed to the Overview and listed first, whether or not the franchisor organizes (fixed on review, A5: version 0.1.0 gave them no scrutiny sentence). A franchisor and its franchisee do not also get the Overview's, since the body's says the same of them. | The body's sentence for franchisees among themselves too; or the Overview's for both relationships. | 2 [pdf page 6]; Overview item 2 [pdf page 3]. Fixtures: franchisees among themselves, organized and not. |
| F25 | "Providing competitively sensitive information through an algorithm or through a third party's tool or product". | Read for any route through a third party, because the text's own example of it is an exchange "through a third-party firm that facilitated the exchange". | Only an algorithm or a tool, not a third-party firm. | 3 [pdf page 7]. Fixture: the poultry processors through a third-party firm; the two routes compared. |
| F26 | Section 4's "Non-compete clauses that restrict workers from switching jobs or starting a competing business can violate the antitrust laws". | A condition: given when the caller finds that the clause restricts switching jobs or starting a competing business (either), since the relative clause has no comma. Registered on review (A4) and not changed: the grammar favours the condition, the context the description, and the text does not settle it. | Descriptive (the refuter's reading): every non-compete does one or the other, so the sentence is said of every non-compete clause; the next sentence, "By preventing workers from leaving jobs to pursue better employment opportunities, non-competes decrease competition for workers", speaks of non-competes generally, and the "also" of "Non-competes may also violate other federal laws", given here without condition, presupposes it. | 4 [pdf pages 8-9]. Fixture: a non-compete clause with neither finding gets the two other-law sentences only. |
| F27 | Which non-disclosure agreements are section 5's "Such provisions"? | One that is broad in one of the bullet's two antitrust ways: it functions to prevent leaving ("span such a large scope"), or it reaches any information "usable in" or relating to an industry ("drafted so broadly"); Overview item 5 lists "overly broad non-disclosure agreements" among conditions that "may violate the antitrust laws". Added on review (`tests-independent.l4` line 669, where a narrow agreement got the sentence). | Every non-disclosure agreement (version 0.1.0); or also one broad only in the federal-law limb's way ("worded so broadly as to suggest"). | 5 [pdf pages 10-11]; Overview item 5 [pdf page 3]. Fixtures: a bare non-disclosure agreement; one broad in the federal-law way; one reaching an industry. |
| F28 | The other-law sentences: section 2's "Agreements among franchisees, either written or unwritten, not to poach, hire, or solicit each other's workers may violate other federal and state laws", and section 5's "State law also sets limits on training repayment requirements and NDA restrictions". | Said of the kinds they name, without condition, as section 4's "may also violate other federal laws" and "can also violate state laws" [pdf page 9] are: franchisees among themselves, whether or not they compete or the franchisor organizes; every non-disclosure agreement and training repayment provision, broad or not. Registered on review (B(iii)). | Conditioned on what the antitrust sentences beside them need: competing franchisees; only a non-disclosure agreement or training repayment provision that restrains (section 5's sentence follows "Many of these agencies have enforced against restraints on worker mobility"). The independent author takes this view of a narrow non-disclosure agreement: `tests-independent.l4` line 669, left failing as a genuine ambiguity. | 2 [pdf page 7]; 5 [pdf page 11]. Fixtures: franchisees that do not compete; a bare non-disclosure agreement. |

## 9. Open questions for a domain expert

1. What delineates a labor market for "compete in the same labor markets"? The text gives no test (F1). n.7 points to the 2023 Merger Guidelines for mergers' effects on workers; whether their analysis of labor markets applies here, the text does not say.
2. Does n.15's fuller analysis bear on the crime, civil and DOJ sentences of section 1? n.15 is attached only to the "illegal even if" sentence, and the text does not say (F5; the independent author reads it as doing so).
3. Does n.15 reach section 2's franchise no-poach agreements, or section 6's platforms? The text does not say (F5, F7).
4. Is an agreement to set a starting point for compensation treated as wage fixing, for "illegal even if" and for the criminal sentences? The text says it "may be" (F6; the independent author reads it as wage fixing).
5. Are "potentially competing employers" reached by sections 2, 3 and 6? Those sections do not use the phrase, and this encoding answers NOTHING for them (F7, F9, F11, F13).
6. Section 4 says "In 2021, the FTC pursed several enforcement actions", and the orders n.28 cites are dated 2023. Which year is meant (section 11)?
7. What is the current status of the FTC's non-compete rule? The text's account is dated, and this encoding does not record it (coverage, section 4).
8. Does section 2's per se sentence need the franchisor and franchisee to compete for workers (F7, changed on review)?
9. Does section 2 take section 1's criminal sentences away from a franchisor and franchisee that compete for workers (F20; the independent author reads it so)?
10. Is section 4's first sentence a condition or a description of non-compete clauses (F26)?
11. Are the other-law sentences of sections 2 and 5 said of the kinds they name, or only of those the antitrust sentences reach (F28)?

## 10. Withdrawn and superseded guidelines

- **Antitrust Guidance for Human Resource Professionals (2016)**: replaced by these guidelines. Source: n.1 [pdf page 2], read at source. Its date is the year in its title; nothing else about it was read.
- **The FTC's Non-Compete Clause Rule** (89 Fed. Reg. 38342, May 7, 2024, n.30): the text says it "was scheduled to take effect on September 4, 2024", that on August 20, 2024 the Northern District of Texas "issued an order setting aside the rule", and that "The order is currently on appeal" [pdf page 9]. Reported by the text, as of its January 2025 writing; not checked since, and not encoded.
- **The 2023 Merger Guidelines** are cited in n.7 [pdf page 2] as current guidance on mergers' effects on workers; they are a subject of this repository.

## 11. Text slips and source notes

- 6 [pdf page 11]: "the type of per se violation of the antitrust laws that the exposes the platforms to criminal liability". The words "that the exposes" are a slip; the result's name drops the stray word, and the one comment that quotes the sentence in full marks it [sic] (`wk-contractors-and-claims.l4`).
- 4 [pdf page 8]: "In 2021, the FTC pursed several enforcement actions": "pursed" is a slip for pursued; and the four orders n.28 cites are dated February and May 2023 (open question 6).
- The extraction puts the numerals of n.10 and n.33 one line below the start of their text [pdf pages 5 and 9].
- **The deposited text has no paragraph breaks**: no blank line and no indent marks a paragraph, so a paragraph's first line looks like any wrapped line.
  Every question of which sentences share a paragraph was answered from the PDF (`workers-2025.pdf` in the parent session's corpus folder, whose sha256, `d882d0e6…`, is the `.meta.json`'s `pdf_sha256`, checked 2026-11-26), read as `pdftotext -layout` output.
  The facts taken from it:
  - section 1 [pdf pages 5-6]: the crime and civil sentences open the section's first paragraph; "When formed between competing or potentially competing employers", "Nor does it matter" and the starting point are one paragraph; "The DOJ may criminally investigate" is a paragraph of its own (F4); the Act's sentence is another;
  - section 2 [pdf pages 6-7]: two paragraphs, the franchisor and franchisee's sentences in the first, the franchisees' in the second;
  - section 3 [pdf pages 7-8]: four paragraphs, the first holding the sentences on competitively sensitive information and "may indicate the existence of a wage-fixing conspiracy" (F13);
  - section 5 [pdf pages 10-11]: the paragraph that begins "These types of restrictions" follows the four bullets and holds "Such provisions" (F17).
- **Outside this row, not changed**: the subject's `SOURCE-LICENSE.md` names "the **Merger Guidelines (2023)**" as its text in its first line, not these guidelines; the rest of it (17 U.S.C. 105(a), justice.gov's robots.txt) names no document, and its search for a copyright notice, repeated here on this row's text on 2026-11-26 (for `©`, `all rights reserved` and `copyright`, ignoring case), finds none. The brief allows this row to touch only the subject's `subject.json` note, so it is reported here and to the parent session.

## 12. Guards: which functions answer NOTHING, and when

Every NOTHING case below, and the EMPTY case beside it, is asserted in `wk-tests-boundaries.l4` (or `wk-tests.l4`), which `check.sh` runs on both builds; the three helpers (n.15's, section 2's per se and section 6's platforms) are asserted only through the reports that read them.

| function | NOTHING when | otherwise |
| --- | --- | --- |
| `Overview: what the list says of the practice` | the practice is one the list does not name | the item's sentences |
| `General principles: whether the businesses compete for workers` | the two are the same business; or, with no shared labor market, the finding of potential competition has not been made, or the contrary finding is made and either business names no labor market (a blank name names none) | one of three values |
| `General principles: what the text says of whether the agreement's effects matter` | no agreement is identified (found none or not determined); whether the businesses compete is not stated, or they are the same business; n.15's function is NOTHING for a wage-fixing or no-poach agreement between competing or potentially competing employers; section 2's or section 6's function is NOTHING; or no statement applies | a non-empty list |
| `1: what the agreement is, in substance` | what the businesses agree is `something else relating to workers` | one of three values |
| `n.15: whether the restraint is subordinate and collateral to a broader business collaboration and reasonably necessary to achieve its procompetitive potential` | neither contrary finding is made, and the two findings are not both made | TRUE or FALSE |
| `1: what section 1 says of the agreement` | whether there is an agreement has not been determined; or an agreement is identified and: the two are the same business; it is a wage-fixing or no-poach agreement or one to set a starting point, and whether the businesses compete is not stated; or it is a wage-fixing or no-poach agreement between competing or potentially competing employers, and n.15's function is NOTHING | a list; EMPTY when the agencies find no agreement, and for an agreement none of its sentences is about |
| `1: what section 1 says of a report of an antitrust crime` | another role, or conduct that is not an antitrust crime | the Act's sentence |
| `2: whether the text says that such an agreement between a franchisor and its franchisee can be per se illegal` | a no-poach agreement between a franchisor and its franchisee, and whether they compete is not stated, they are the same business, or they are only potentially competing | TRUE or FALSE |
| `2: what section 2 says of the agreement` | not determined; or, identified: the same business; a franchisor and its franchisee, when the function above is NOTHING; or a no-poach agreement among franchisees that the franchisor organizes or enforces, when whether they compete is not stated or they are only potentially competing | a list |
| `3: what section 3 says of the exchange` | whether the businesses compete is not stated, they are the same business, or they are only potentially competing; or competitively sensitive information shared between competitors whose effect has not been assessed | a list; EMPTY for businesses that do not compete |
| `6: whether the text says the agreement is one between competing platforms to fix the compensation of independent contractors` | the businesses are platforms, the workers concerned include independent contractors, and the agreement is to fix wages or to set a starting point; and neither do the platforms not compete, nor is it wage fixing between platforms that compete for workers | TRUE or FALSE |
| `6: what section 6 says of the agreement` | not determined; or, identified: the same business; a starting point, for independent contractors; or platforms fixing independent contractors' compensation, when the function above is NOTHING | a list |

`General principles: the kinds of evidence of an agreement that are present`, `4: what section 4 says of the term`, `5: what section 5 says of the term` and `7: what section 7 says of the claim` return a plain list and never NOTHING: every input they read is a BOOLEAN finding or a kind, and the text attaches no statement to a finding's absence.
No function takes a number, so there is no impossible numeric input to guard.

**When a sentence is given, omitted, or makes the report NOTHING** (fork F23).
A list cannot mark one sentence as open, so where one sentence turns on what the text or the caller has not said, the whole report is NOTHING.
Where a section itself draws a line between two classes (section 1 says "compete with each other" in one paragraph and "competing or potentially competing" in the next), a sentence that names one class is omitted for the other; where a section never speaks of a class (sections 2, 3 and 6 never mention potential competitors), its answer for that class is NOTHING.

| case | answer | why |
| --- | --- | --- |
| Section 1, potentially competing employers: the crime and civil sentences | omitted | The section draws the line itself (F4). |
| Section 1, potentially competing employers: "illegal even if" and the DOJ sentence | given | F4. |
| Section 1, both n.15 findings made: the crime, civil and DOJ sentences | given | n.15 is attached to "illegal even if" only (F5); `tests-independent.l4` lines 552 and 553 take the other view. |
| Section 1, n.15 open (no contrary finding, not both made) | NOTHING | n.15 switches between two of the section's sentences. |
| Section 1, the starting point: "illegal even if" and the DOJ sentence | omitted; the starting point's own sentence given | The text answers the starting point itself, with "may be" (F6); line 511 takes the other view. |
| Section 2, a franchisor and franchisee that do not compete: the per se sentence | omitted | F7. |
| Section 2, a franchisor and franchisee potentially competing, or not stated | NOTHING | Section 2 does not speak of potential competitors (F7). |
| Section 2, franchisees potentially competing, the franchisor organizing | NOTHING | The same (F9). |
| Section 2, a franchisor and franchisee that compete: section 1's crime and DOJ sentences | given, by section 1 | Section 2 is silent on criminal exposure (F20); lines 735 and 736 take the other view. |
| Section 3, potentially competing employers | NOTHING | Section 3 does not speak of them (F13). |
| Section 3, competitively sensitive information between competitors, effect not assessed | NOTHING | F12. |
| Section 5, a non-disclosure agreement broad in neither antitrust way: "Such provisions" | omitted | The bullet's "when" and Overview item 5's "overly broad" (F27). |
| Section 6, potentially competing platforms; a starting point | NOTHING | F11; F6. |
| Any report on an identified agreement or on an exchange, and the effects question, the same business named twice | NOTHING | F1, F23 (when the agencies find no agreement, sections 1, 2 and 6 answer EMPTY first). |
| Sections 4, 5 and 7, a BOOLEAN finding not made | its sentence omitted | The text attaches no statement to a finding's absence or to its contrary. |

## 13. Renames

Version 0.1.0 had none after its tests were written (one constructor was renamed before any test existed, section 2).
Version 0.2.0 renamed three names on review, and the independent tests were patched for exactly these, in a commit of their own (section 15):

- the field `the businesses are potentially competing employers` (a BOOLEAN) is `the finding that the businesses are potentially competing employers` (a `Finding`), A1;
- n.15's two fields are `the finding that the restraint is subordinate and collateral to a broader business collaboration, such as a joint venture` and `the finding that the restraint is reasonably necessary to achieve the procompetitive potential of that collaboration` (each a `Finding`), B(i);
- Overview item 2's second constructor restores the text's "or, for example, among the franchisees", A10.

It added the type `Finding` and its three constructors; section 2's constructor for the Overview's sentence; the functions `n.15: whether the restraint is ...`, `2: whether the text says that such an agreement between a franchisor and its franchisee can be per se illegal` and `6: whether the text says the agreement is one between competing platforms ...`; the two name-comparing functions and `General principles: the two businesses are the same business`; and three fixtures in `wk-test-fixtures.l4`.
It put `What section 7 says of the claim`'s two constructors in the text's order.
No other name changed (checked by comparing every backticked name in the six rule and fixture modules with version 0.1.0's).

## 14. Quotations and contact details: how they were checked

A script (kept outside the repository, in the builder's scratch folder) took every double-quoted span of 3 or more characters in this file and in the comments of every module, and looked for it in the deposited text, after: curly quotes and apostrophes made straight, a quotation inside a quotation written with single quotes, dashes and runs of whitespace normalised, case ignored, footnote numerals glued to or standing after a word removed, and a quotation broken by "..." checked piece by piece.
A sentence broken across a page and the footnotes between (the extraction has several) is found by joining the pages' bodies without their footnotes.
For each quotation of four or more words whose line or comment block cites a `[pdf page N]`, it checked that one of the cited pages holds the quotation.
Run 2026-11-26 on version 0.2.0, after the last edit to any quoted text: 464 quotations checked, 2 not found, 0 with no cited page matching.
The two not found are the independent author's, in `tests-independent.l4`, left as written: `even if [it is] never carried out` (line 443, with an editor's bracket) and `something else` (line 534, a constructor's words).
Version 0.1.0's run had checked 321 quotations, with none not found.
Eight spans are exempt, each a quotation of something other than the source: the common brief's "creates no independent rights or obligations" and its two halves, the task's "where it says civil liability only", the house label "assumed, not ruled", the house form "the agencies state that ...", the `.meta.json`'s "Updated November 17, 2025" and `SOURCE-LICENSE.md`'s first line.
The script was shown able to fail on a copy of this folder: a planted sentence the text does not contain was reported not found, and a true quotation of pdf page 8 cited to pdf page 9 was reported.
The single-quoted spans of `encoding.json` (30 in version 0.2.0) were checked the same way: none is missing from the text.

What the sweep does not see.
It removes every one- or two-digit number on both sides, so a day of the month or a small number inside a quotation is not checked by it; the two dates quoted in section 10 were read by hand against the text [pdf page 9].
The result names in backticks are not quotations but the text's sentences recast in the result's grammar ("such an agreement" for "these agreements"), and no script checks them; they were written from the text, and a reviewer should read them against it, their modals first.

Section 8's contact details (its telephone numbers, room number, street addresses, postal codes and complaint portal addresses) were searched for in every file of this folder, by their digits and words: no hit.

## 15. Independent test pass

**Who, and in what order.**
A fresh agent, by its test file's header, read the source text first and wrote its answers down in `answers.md` (in the parent session's scratch folder, not in this repository), frozen at 2026-11-25T17:31:46Z (sha256 `ba5f270c…`, which the header records and which matched again on 2026-11-26), before it opened this folder.
The header says it then read the nouns and the rule modules' output vocabularies to learn the names, and not this encoding's own tests.
It wrote `tests-independent.l4`, 129 assertions.
Two of them (lines 735 and 736) were added after its first run, from rows of `answers.md` written before it, as the block's own comment says.

**Counts**, on both builds, the failing lines the same on each after every commit:

| commit | what it changed | satisfied | failed | failing lines |
| --- | --- | --- | --- | --- |
| the independent test file, as its author left it | nothing | 118 | 11 | 511, 552, 553, 626, 669, 674, 680, 686, 690, 735, 736 |
| three-valued findings; signature-only patch to the independent tests | three renames | 118 | 11 | the same |
| review fixes to the encoding's readings | the encoding only | 120 | 9 | 511, 552, 553, 669, 674, 680, 686, 735, 736 |
| correct three test-author errors in the independent tests | three expectations | 123 | 6 | 511, 552, 553, 669, 735, 736 |

**The eleven failures, classified.**

| line | the case, and what the author expected | the source | class | what was done |
| --- | --- | --- | --- | --- |
| 511 | a starting point between competitors: "illegal even if" | 1 [pdf page 6]: "may be a form of wage fixing under the law", after "Nor does it matter if the agreement does not include specific pay rates" | genuine ambiguity | left failing (F6) |
| 552, 553 | both n.15 findings made: no crime and no DOJ sentence | n.15 [pdf page 6] is attached to "illegal even if" and says nothing of criminal exposure | genuine ambiguity | left failing (F5) |
| 626 | competitively sensitive information, effect not assessed: NOTHING | 3 [pdf page 7]: "may be unlawful when the information exchange has, or is likely to have, an anticompetitive effect" | encoding error | fixed (F12) |
| 669 | a narrow non-disclosure agreement: nothing | 5 [pdf pages 10-11]: "can violate the antitrust laws when they span such a large scope"; "State law also sets limits on training repayment requirements and NDA restrictions"; Overview item 5 [pdf page 3]: "overly broad non-disclosure agreements" | encoding error in part, genuine ambiguity in part | "Such provisions" is no longer given (F27); the state-law sentence still is, so the line still fails (F28) |
| 674, 680, 686 | a training repayment provision, a client non-solicitation agreement and an exit fee, each with no finding that it prevents leaving: nothing | 5 [pdf page 10]: "Depending on the facts and circumstances, these provisions can be anticompetitive, such as if" | test-author error | corrected (below) |
| 690 | the unnamed kind, with indications of harm: "may investigate if there are indications" | 5 [pdf pages 10-11]: "The following examples illustrate how restrictive conditions could potentially violate the antitrust laws"; "such a restrictive condition" | encoding error | fixed (F17) |
| 735, 736 | a franchisor and franchisee that compete for workers: no crime and no DOJ sentence | 2 [pdf pages 6-7] says nothing of criminal exposure and begins "No-poach clauses in franchise agreements are also subject to antitrust scrutiny"; 1 [pdf page 5]: "Businesses that compete with each other for workers may be committing an antitrust crime" | genuine ambiguity | left failing (F20) |

**The test-author corrections** are in a commit of their own, which does not call itself signature-only.
Lines 674, 680 and 686 each asserted `ind is empty`, and now assert that the kind's hedged sentence is present (`ind s5 TRAP`, `ind s5 non-solicit`, `ind s5 exit fee`).
The text compels the hedged sentence: it is stated with no condition, and the author's own row S5e of `answers.md` calls "such as if" an example, so an empty answer leaves out a sentence the text states without condition.
The next assertion on each, that the example sentence is not given, is untouched and passes.
Each corrected line carries its reason in a trailing comment, so no line number moved.

**The signature-only patch** is a commit of its own, made before any behaviour changed; its word diff is kept in the builder's scratch folder (`wk-fix/indep-word-diff.txt`).
It changed lines 140, 196, 197 and 603, and the file's line count is unchanged (736):

- 140: the field renamed (section 13); the author's BOOLEAN `potential` is mapped by an IF, TRUE to the finding made and FALSE to the contrary finding, because the author's comments and `answers.md` call the FALSE pairs not potential competitors (rows G8, S1n), which is a contrary finding; nothing in the file means the third value, not made.
- 196 and 197: n.15's two fields renamed; `subordinate` and `necessary` mapped the same way, because rows F15b and F15c say a condition is NOT met, and F15d that the restraint is unrelated to the joint venture, each a contrary finding (row F15e, where necessity is unknown, has no assertion).
- 603: the constructor on the expected side of the assertion, renamed with the encoding (A10); the sentence asserted is the same one.

No input value and no other expected value changed, and the failing lines before and after it were the same on both builds.

**Left failing, and why they are expected.**
Lines 511, 552, 553, 669, 735 and 736 each turn on a reading the text does not settle, and each has both readings in the fork register (F6, F5, F28, F20).
`check.sh` expects 123 satisfied and 6 failed in `tests-independent.l4`, and `encoding.json` records the 6, by line, in `expected_failed_independent` (its `expected_red` holds only the nine positive controls).

## 16. Adversarial review

A fresh agent read the encoding to refute it.
The parent session checked the findings it could against the text and relayed them as A1, A2 and A4 to A10 (A5 in two parts; the relay has no A3), with its own finding on paragraph breaks.

| finding | what it said | what was done |
| --- | --- | --- |
| A1 (high) | labor market names were compared exactly, and potential competition was a BOOLEAN, so a finding not made read as its contrary where section 1 reaches "competing or potentially competing employers" | names compared ignoring case and surrounding whitespace; the finding three-valued; not made, with no shared market, is NOTHING (F1) |
| A2 (medium) | section 3 for potentially competing employers; potentially competing franchisees with the franchisor organizing; platforms agreeing a starting point | all three NOTHING, and potentially competing platforms too (F6, F9, F11, F13) |
| A4 (medium) | section 4's first sentence may be descriptive, and its "also" sentences presuppose that | registered as F26, with both readings; not changed |
| A5 | section 2's per se sentence should need the franchisor and franchisee to compete for workers | changed at the parent session's direction (its relay calls it a ruling), with the three-valued handling; version 0.1.0's reading is the alternative (F7) |
| A5, F24 | franchisees among themselves lost "subject to antitrust scrutiny", which Overview item 2 gives them | they get the Overview's sentence, attributed and listed first (F24) |
| A6 | F13's third alternative had no fixture; and why does F13 read the heading's condition when F7 and F11 do not | a fixture added (joint venture partners that do not compete for workers, sharing wage data); F13 and F11 now say why |
| A7 | section 7 listed the Overview's sentence after the body's, while section 6 lists it first | section 7 lists it first, the text's order |
| A8 | section 2's `@ref` rested on n.18 | it cites n.18 to n.21 and Overview item 2 |
| A9 | the same business named twice got all four section 1 sentences | NOTHING in every report on an identified agreement or an exchange, and in the effects question (F1, F23) |
| A10 | Overview item 2's result dropped "for example" | restored, a rename (section 13) |
| the parent's: paragraph breaks | the DOJ sentence is a paragraph of its own, and a comment said it shared one | F4 re-decided from the PDF: the answers stand, the reason is corrected, and the tests' comments say what they assert (section 11) |
