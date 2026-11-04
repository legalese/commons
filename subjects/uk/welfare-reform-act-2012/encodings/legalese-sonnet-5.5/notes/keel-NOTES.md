# NOTES: Welfare Reform Act 2012 (United Kingdom), 2012 c. 5. The keel (shared vocabulary)

Status: draft. No domain expert has read this against the source.
Written by the keel agent of row `iaw-wra-k` (model Sonnet 5.5, stable `l4` 1.6.98).
Target dialect: `main` (the stable build is the compiler that has to read it); every module also runs on the main build 1.6.108 with the same four counts.

## The source is not the official text

The only source is `inputs/ukpga-2012-5.txt`, a plain-text rendering made by a converter script from legislation.gov.uk (`ukpga/2012/5`, point-in-time version 2026-07-01).
It is not the official text, and nothing here is "verified against the official text".
`inputs/ukpga-2012-5.meta.json` records that the revised text "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish".
A provision that appears to say two things may therefore be two extent versions, which is not a fork.
Licence: Crown copyright, Open Government Licence v3.0 (`inputs/STUB-SOURCE-LICENSE.md`): "Contains public sector information licensed under the Open Government Licence v3.0."

## What the keel covers

My range is line 1 of the raw file (`inputs/PARTS.md`: `keel (you) | 1-1 | 38 words`), the enacting formula.
So the keel encodes no operative provision and no definition of the Act.
`wra-definitions.l4` exists but defines nothing (imports and a header), so that the file name the brief and the merge checklist use resolves; it has no tests file because it has nothing to test.
What it adds is `wra-core.l4`, the nouns the four part agents (wra1 to wra4) share, and `PLAN.md`, which says who holds what and what the parts must take from each other.
`wra-core-tests.l4` proves every type in the core can be built and read back, and shows the construction shapes.
The definitions that exist in the Act are all in the parts' ranges; `PLAN.md` section 9 lists them by part and raw line.

## Seat

The seat the parts serve is the individual: a person who claims, receives or is moved to Universal Credit, or who claims Personal Independence Payment, or whose benefits are capped (brief, "The subject and the sources").
No seat for an official: the Secretary of State, the tribunals and the rest appear in the core only as the other party to what the individual is owed or owes.

## Coverage table (my range only)

| line | provision | disposition | why |
| --- | --- | --- | --- |
| 1 | enacting formula ("Be it enacted by the Queen's most Excellent Majesty ... as follows:") | inert | reason 1: not operative (enacting words); it creates no rule |

The rows for lines 2-3959 belong to the part agents (`PLAN.md` section 3 copies their ranges unchanged).

## Fork register

None in my range.
I looked at line 1, and at the whole text for the nouns and cross-part questions that `PLAN.md` lists; a fork needs a rule, and the keel has none.
I saw no fork in the text the parts will meet.
Three places need care, none a fork: the benefit cap's two figures per pair, which regulations choose (s 96(5A)-(5B)(a); `NOTHING`-kind, `PLAN.md` section 11 item 5); the two halves of the SSFA benefit lists, one in wra1's Schedule 2 and one in wra4's s 117 (seam 7); and the shared reading of s 102 and Schedule 11 (seam 8).

### Reading a result: FALSE and NOTHING

The core defines no decision function, so it returns no `FALSE`, no `NOTHING` and no constructor meaning "the text says no".
In this Act a "no" is the text saying no in its own words: "means" in an interpretation section, a condition introduced with "if", "only if", "unless", "while", "until", "except", a list closed with "only", or a flat negative ("is not entitled", "may not", "does not").
"Not covered" is everything else: a power to make regulations ("Regulations may ...", "such as may be prescribed", "is to be determined in accordance with regulations"), a rate, amount, period or description the Act leaves to regulations, an unclosed list, "includes", and any question the Act hands to the Secretary of State, a tribunal or a court.
That is most of this Act, so a part's answer will often be `NOTHING` where a reader expects a number.
`PLAN.md` section 7 gives the part agents one convention for the values regulations supply, and section 12 gives one verified shape for a function that answers `JUST FALSE`, `JUST TRUE` or `NOTHING`.

## Marginal readings for a lawyer

None in my range: the keel has no branch that answers "no" or "not covered".
The two readings the brief marks "for a lawyer" ((a) a failed "if" counts as the text's no, and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not) are the status quo for the parts, and each part lists the branches that rest on them in its own `NOTES.md`.
`PLAN.md` section 8 (the reading for seam 8) names one branch the lead should expect to see listed twice, by wra3 and wra4.

## Jural relations

| provision | right/privilege/power/immunity holder | correlative bearer | section | L4 rule |
| --- | --- | --- | --- | --- |
| enacting formula | none | none | line 1 | none |

The core names the parties so that the parts' tables use the same words (`PLAN.md` section 4): the individual is "the claimant", "the person" or "the employee" by role; the other party is an `Authority` constructor or the employer.

## Design of the core: what I chose, and what I assumed (not ruled by a lawyer)

The core has 23 types (82 enumeration constructors, 33 record fields); `PLAN.md` section 4 lists every one, generated from the file.
It is nouns only, and the membership test was: could a witness of ordinary competence testify to this fact, or does answering it require reading the Act?

- Kept out: every test the Act applies ("the person meets the basic conditions", "the two people are a couple", "a child"), every number the Act states, every regulation-made value.
- `Person` serves for every natural person, a child included: "child" is a rule (s 40, raw line 432), so it is wra1's, and `age in years` carries the fact.
- `Person` carries both `age in years` and `date of birth`.
  They can disagree if a caller makes them; a seat layer asks the age and gives the date of birth a fixed placeholder, with a comment (the pattern of `inputs/EXAMPLE-sg-employment-act-seat/ea-seat.l4`).
- `Two people` carries the three facts s 39(1) turns on, as facts; it does not say whether the two are a couple, and `Claimants` says how a claim is made (s 1(2), s 2(2)), not what the people are.
- `Benefit` has one constructor for each benefit the Act names as paid or abolished (ss 33, 96(10), Schedule 4), splitting jobseeker's allowance and employment and support allowance by the two bases s 33(2) separates.
- `Provision that reduces an award` lists exactly what Schedule 5 para 1(3) and Schedule 6 para 5(4) name, so the parts holding those Schedules and the parts holding the sections share one list.
- `Authority` is limited to the holders of a power or duty that touches the individual and are named in more than one place; the Welsh and Scottish Ministers, the Treasury and the Commissions appear only in regulation-making, commencement and machinery, which are inert, and a part that needs one adds it under `NEEDS-CORE.md`.
- No `Prescribed` type: "not among the sources" is `NOTHING` in a `MAYBE`, as the brief prescribes, and `PLAN.md` section 7 says how to name the input.

These are design choices, labelled "assumed, not ruled"; none is a ruling on the law.

## Findings

### What the stable binary does not accept

The keel hit nothing the stable binary rejects: `wra-core.l4` and `wra-core-tests.l4` use none of `REFUSE`, `BECAUSE`, `#ASSERT REFUSED`, a section `GIVEN`, `TYPICALLY`, an opaque `DECLARE`, `YMD`, `SET OF`.
Things I verified work on the stable binary and the main build 1.6.108 (probes, then the shipped files):

- two records may use the same field name (`age in years` in two records);
- a backtick name may contain parentheses, spaces and a slash (`s 105 SSAA 71ZB(1)(a) ...`, `s 105/71ZB(1)(a) ...`, `sch 6 para 5(4) ...`);
- a record field may be a `DATE`, a `LIST OF` a record, or a record; a constructor field may be a `MAYBE` of a record;
- a module that only `DECLARE`s prints `Checking succeeded`, so `check.sh` can run it (a worry before running it: the script exits 2 for a module that prints nothing it recognises);
- the first `l4 run` of a scratch file once printed `Info | updateFileDiagnostics published different from new diagnostics` before the diagnostics; it is not a diagnostic of the file and did not recur.

### Facts about the raw text that cost a reader time (details in PLAN.md section 5)

- Inserted text keeps its host Act's section numbers and loses its quote marks, so a line `19<tab>Higher-level sanctions` (raw line 582) is section 19 of the Jobseekers Act 1995, not section 19 of this Act.
- Schedule paragraph numbers are not printed; the count by cross-heading is consistent with the Act's own references (s 43(3)(l), (m); Schedule 5 para 4).
  A sanction definition I first cited as Schedule 6 para 6(4) is para 5(4); I corrected the core's `@ref` after counting.
- A regex of "section N" hits (357) was nearly all sections of other Acts; the seams in `PLAN.md` section 8 are by reading.

## Open questions for a domain expert

1. Is `Person.date of birth` worth keeping beside `age in years`, or should the age be derived in each part? (Derivation by each part risks different leap-day readings in different parts; a stated age cannot.)
2. Should the lead hoist a `Child` type for Part 6 (child support: person with care, non-resident parent, qualifying child)? The keel left it to wra3 under `NEEDS-CORE.md`, because those terms are defined in the Child Support Act 1991, not among the sources.
3. Should the SSFA lists of "disqualifying benefit" and "sanctionable benefit" (seam 7) be composed at the merge by the lead, or does a lawyer want the original paragraphs (a)-(e) supplied as an input?

## What check.sh prints

Run on 4 November 2026 from the deposit directory, after the scratch files were deleted, as
`L4=<l4-stable-98> L4_MAIN=<l4-main-108> ./check.sh`.
The stable binary is `1.6.98 (main, 7689b0d, 2026-10-19)`; the main build it was compared with is `1.6.108 (main, 2ae7c9b, 2026-11-02)`.
The target is `main`: every module has the same four counts on both builds.
No assertion is expected to fail (`expected_failed` is empty), and none does.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
wra-core-tests.l4                              0        38       0        0         0 |      0        38       0        0  same
wra-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
wra-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (3 modules)                              0        38       0        0           |      0        38       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`wra-core-tests.l4` has 38 `#ASSERT` lines and 38 assertions satisfied.
`wra-core.l4` and `wra-definitions.l4` hold no directive, so their rows are zeros by construction; they print `Checking succeeded.` on both builds.
`l4 run` printed no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning` for any of the three modules, and `l4 check` printed no "follows code on its line" or "end of the file" notice.

The source quotations and `@ref` locators, `python3 -I srcrefs.py check --strict ../../../inputs/ukpga-2012-5.txt wra-core.l4 wra-core-tests.l4 wra-definitions.l4`:

```
srcrefs check: 58 src: lines, 15 runs, 29 locators, 0 problems
```

What these numbers do not show: that the core's nouns are the right ones for the four parts (only the parts' work tests that), and that the cross-part seams in `PLAN.md` section 8 are complete.
