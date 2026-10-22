# Births, Deaths and Marriages Registration Act 1998 (WA) — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill. No pipeline, no coverage table, no independent test pass, no human gate.
Not for public use. The first pass (October 2026) did not use the skill; it was
conformed to the `writing-l4-rules` skill on 14 October 2026, and brought into line
with section 5 of `docs/ENCODING-GUIDE.md` (what the stable `l4` accepts) on 22
October 2026 — see the last two sections.

**Edition:** the compilation deposited at
`../../registers/source-bundle/mrdoc_49099.txt` (retrieved 2026-09-07). Its
compilation table runs to the Births, Deaths and Marriages Registration Amendment
(Sex or Gender Changes) Act 2024 Pt 2, in force 30 May 2025, and it carries
"© State of Western Australia 2025". The deposit states no compilation number. The
Assisted Reproductive Technology and Surrogacy Act 2025 Pt 15 is listed as
uncommenced and is not shown.

**Checks:** two modules (`bdm-registration.l4`, on a clock of days;
`bdm-cause-of-death.l4`, s 44, on a clock of hours) and one case file
(`bdm-cases-registration.l4`), each run with `l4 run` on the stable `l4` (the one
bundled in the L4 VS Code extension 1.6.98), `JL4_LIBRARY_PATH` unset, on the files
as committed: 0 errors and 0 warnings on each of the three; in the case file 62
assertions written and 62 satisfied (7 of them assert a `not covered` answer), and
40 traces, each matching the `-- expect:` line above it. (First pass: 53 of 53, one
module.)

## Why this Act, and why scoped

It is requirement **au/wa:REQ-0001**, priority 1, raised 12 times by the three
Western Australian cradle-to-grave lives: chloe c001 (her birth registered, day
nineteen), c054 (her marriage in Kings Park), c062 and c071 (Oliver's and Ella's
births), c086 (Graham's death at home), c096 and c098 (Liam's and Chloe's deaths);
jake k001 (his birth registered, day fifteen), k051 (Ruby born to unmarried
parents, both signing) and k097 (his death); daniel d001 (his birth registered,
day nine, in 1996) and d092 (his death).

The lives ask who must register a birth and by when, whether both unmarried
parents may be registered, what of the child's name, what registers a marriage,
and who registers a death and by when. This encoding takes those questions and the
definitions and exceptions they need: s 2 with the compilation table's
commencement date; ss 12, 13, 15, 16, 18, 19(3)-(4) and 22; Part 6 (ss 37-39); and
Part 7 ss 40, 42, 44, 45, 47 and 48. Not encoded: administration (Part 2), court
orders beyond their effect as an input (ss 20-21, 41), given-name changes (s 23),
parentage changes (Part 4), change of name (Part 5), change of registration of sex
or gender (Part 5A), suspected deaths (s 43), removal of remains from the State
(s 46), the Register and certificates (Part 8), and Part 9. Fees and approved forms
are set outside the Act and none was retrieved.

## What the Act turns out to say

### 1. Daniel's birth in 1996 is not governed by this Act

The compilation table: "Act other than s. 1 and 2: 14 Apr 1999". Daniel was born on
9 April 1996 and registered on 18 April 1996 (d001), three years before the Act
came into operation. The ledger asks this Act about that event, but it cannot
answer it; the law then in force is not deposited. Chloe's registration on
2 April 2003 (c001) is within it. Asserted.

### 2. The funeral director notifies a death; the Registrar registers it

s 42: the funeral director or other person who arranges for the disposal of the
remains must, "within 14 days of the date of death", lodge a death registration
statement and give the Registrar the doctor's certificate. s 48(1): "The Registrar
is to register a death". c086's title ("the funeral director registers the death")
blurs the two. The doctor's part is not 14 days either: s 44 gives the doctor
**48 hours** to certify the cause, and the certificate goes to the funeral director,
not the Registrar. No certificate is required where the doctor must report the death
to a coroner under s 17(3) of the Coroners Act 1996 (s 44(5)). For Graham, who died
on 19 August 2052, day 14 is 2 September 2052. Asserted.

### 3. The scenarios cite the wrong provisions

The lives' citations do not match the deposited numbering. "Part 5 (registration of
marriages)" is Part 6; Part 5 is change of name. "Part 6" for deaths is Part 7. The
parents' 60-day duty is in ss 15-16, not ss 12-13: s 12 is the hospital's (or
attendant's) notice within one month, and s 13 says when a birth must be registered.
"s 13 (both parents may register)" is s 15, and "s 19 (names)" is s 22; s 19 is about
adding details and a later change of surname. The encoding follows the deposit. Not
an assertion.

### 4. Both parents register jointly; marriage plays no part

s 15(1): "The parents of a child are jointly responsible for having the child's
birth registered ... (and must both sign the birth registration statement)". The
Registrar may take one parent's statement only where joining the other is
impracticable (death, disappearance, ill health, unavailability, or unwarranted
distress). s 18(1)(a): a joint application by both parents is enough for both
identities to be registered. Neither section mentions marriage, so Ruby's unmarried
parents (k051) stand as married parents would. Asserted.

### 5. Sixty days, but late is still accepted

s 16(1): the statement must be lodged "within 60 days after the date of the birth"
(penalty $1 000); s 16(2): "The Registrar must accept a birth registration statement
even though it is lodged after the end of the 60 day period." Chloe (day 19) and Jake
(day 15) are in time. Separately, s 12 requires the "responsible person" to notify the
Registrar within one month. For a public hospital that is the chief executive of the
health service provider; for a private hospital, its chief executive officer or
general manager. The encoding assumes, without reading it anywhere, that KEMH (c062) is
a public hospital, and reads "one month" as a calendar month (an inference). Asserted.

### 6. A marriage solemnised in WA must be registered, and Part 6 sets no deadline

s 37: "If a marriage is solemnized in the State, the marriage must be registered".
s 38: by lodging the certificate under the Marriage Act 1961 (Cth). Its note says the
celebrant's duty to lodge comes from s 50(4) of the Commonwealth Act, so the WA Act
places no duty or time limit on anyone for Chloe's marriage (c054). Registration is
asserted; the absence of a time limit is noted, not asserted.

### 7. The name is a matter of choice

s 22(3): nothing requires both a surname and a given name, or that "the surname be the
same as that of a parent". The statement need not name a stillborn child or one who
dies within 28 days (s 22(2), s 4 "neonatal death"). The Registrar may assign a name
if the name given is prohibited or the parents cannot agree (s 22(4)). Asserted.

## What would need doing before this is worth anything

- The law in force before 14 April 1999, for Daniel's 1996 registration, is not
  deposited.
- The regulations (fees, prescribed matters) and the Registrar's approved forms were
  not retrieved.
- "Within one month" (s 12) and "within 14 days of" (s 42) are counted by an
  inference about calendar months and day counts, not by any interpretation Act.
- The scenarios' citations (finding 3) should be corrected in the scenario files by
  whoever maintains them.
- No case law or Registry practice was consulted.

## Conformed to the writing-l4-rules skill (14 October 2026)

The first pass modelled every duty and deadline as a boolean about a number
("days after the birth <= 60") and had no regulative rule and no refusal. It was
rewritten in place to the skill, keeping the same provisions, the same quoted
text and findings 1-7 above. What changed:

- **Duties are regulative rules.** Thirteen `DEONTIC` rules, each with
  `PARTY … MUST/MAY/SHANT … WITHIN … HENCE … LEST BREACH BY … BECAUSE "…"`:
  s 12(2) (notice within one month), s 16(1) (lodgement within 60 days), s 42
  (statement and certificate within 14 days, as a `RAND` of (c) and (d)), s 44
  (certify and give within 48 hours, also a `RAND`), s 45 (notice within 7 days
  of disposal); the undated duties s 16(2), s 47 and s 48(1), with no `WITHIN`
  (phrasebook 5.9); the Registrar's prohibitions s 13(6) and s 18(1) as `SHANT`
  with no `WITHIN` (5.3); and the Registrar's permissions under s 15(1), s 18(2)(a),
  s 19(3) and s 22(4) as `MAY` (5.4). They are exercised by 40 `#TRACE`s, each
  with an `-- expect:` line above it. The first pass's seven "in time" booleans
  (s 16 ×4, s 42 ×2, s 45 ×1) became traces with the same days and the same
  answers.
- **What is not a duty stayed a boolean**, on the skill's three-question test
  (5.2): "the birth must be registered" (s 13(1), (2)), "the death must be
  registered" (s 40), "the marriage must be registered" (s 37) and "the statement
  must name the child" (s 22(1)) name no party; the passive "may be registered"
  (s 13(4), (5)) and the Registrar's "may accept / may enter / may assign" tests
  are eligibility tests (5.1), consulted by the permissions. Offences stay
  constitutive predicates, and the penalty a ceiling (5.7).
- **Domain types.** One party type (the offices and roles, 6.9) and one act type
  for the whole Act; records `Birth`, `Death`, `Marriage` and one per kind of
  application, replacing up to six positional booleans per rule. Dates are `DATE`s
  (`YMD`, `add months`, `Day`), not YYYYMMDD numbers. (Since 22 October 2026 `YMD`
  is a local shim; `add months` and `Day` are the stable `daydate`'s.) Commencement (s 2) is a
  value naming the pre-commencement case (4.1).
- **Refusals.** Five named `REFUSE`s, reached from eight places and tested by six
  `#ASSERT REFUSED`. (Since 22 October 2026 they are the five reasons of
  `Why not covered`, asserted; see the last section.) They were: a registrable event before 14 April 1999 (from ss 12, 16, 42
  and 44 — Daniel's 1996 birth, finding 1); the celebrant's duty under the
  Marriage Act 1961 (Cth) s 50(4) (asked as "who must lodge the marriage
  certificate, and by when", finding 6); a removal of remains from the State
  (s 46, from s 45); a suspected death established at an inquest (s 43, from
  s 42); and what s 42(d) requires for a death reportable to a coroner (below).
- **Two clocks, two modules.** Every period is in days except s 44's 48 hours.
  The skill keeps one unit per file (4.3), so s 44 moved to its own module,
  `bdm-cause-of-death.l4`. Each module's header says what its clock counts and
  what AT 0 is.
- **`@ref`** on every rule; limbs carry their statutory label (`"(a)" ... `),
  and `BRANCH` replaces the first pass's `ELSE IF` ladder in s 12(1).

**Expected values.** Every one of the first pass's 53 claims is still made: 46
as assertions, 7 as traces. None changed its answer. Three changed their form
only: the s 2 boolean is now the value `the Act was (not yet) in operation`; the
s 47 "31 days" is now 19 September 2052, 31 days after Graham's death; and
`registers the death` takes the party type, so "the funeral director" is now "the
funeral director or other person arranging disposal". Nine assertions are new:
31 January + one month is 28 February; the s 12 month after 5 September 2030 is
30 days; one parent's statement may be accepted where the other is missing; the
hand counts "day 19" (c001) and "day 15" (k001); Graham's last s 42 day is
2 September 2052 (finding 2, which said "asserted" and now is); two more s 47
cases; and s 48(4) on no inquest. On month-ends, `add months` (which clamps)
gives the same last day as the first pass's integer arithmetic did.

### What the regulative model surfaced

8. **s 12(3) and s 44(4)(a) take away the offence, not the duty.** "A person
   does not commit an offence under subsection (2) if notice of the birth is
   given by another person." Modelled as a duty, a notice by someone else does not
   discharge the responsible person's obligation: the trace reports a breach while
   the offence predicate reports no offence. The first pass's single "commits an
   offence" boolean could not show that the two come apart. Whether the duty
   should be read as discharged by anyone's notice is a fork; this encoding takes
   the literal reading. The same holds for another doctor's certificate under
   s 44(4)(a).
9. **s 16(2) is not a cure for s 16(1).** A statement lodged on day 61 breaches
   s 16(1) and must still be accepted. Hung on the `LEST` of s 16(1), the
   acceptance would turn the trace of a late lodgement into `FULFILLED` and hide
   the offence; so s 16(2) is a duty of its own on the Registrar, whose clock starts
   at the lodgement.
10. **s 42(d) presupposes a certificate that s 44(5) says need not exist.** The
    notifier must give the Registrar "the certificate of cause of death provided
    under section 44", but s 44 "does not require a doctor to give a certificate"
    where the death is reportable to a coroner. The Act does not say what the
    notifier gives then; the Coroners Act 1996 presumably does, and it is not
    deposited. s 42 answers `not covered` for such a death. The first pass, which
    counted days, could not see this.
11. **Nobody in this Act owes the marriage lodgement.** s 38 says "A person may
    have a marriage registered", and the duty is the celebrant's under the
    Commonwealth Act. Finding 6 said so in prose; the encoding now answers
    `not covered` when asked.
12. **Whose duty s 16 is, for a birth outside the State.** s 16(1) binds the
    person "responsible under section 15(1) or (2)", and s 15 is not confined to
    births in the State, but s 13 only permits registration of births outside it.
    The duty is taken to bite only where s 13(1) or (2) requires registration. A
    fork the first pass never met, because it did not gate s 16 at all.
13. **The order of s 12(1)(b)(ii) and (iii)** decides who notifies a stillbirth
    with no doctor or midwife present. The Act does not order them; this encoding
    tries (ii) first, as the first pass did without saying so.
14. **s 13(6) and s 18(1) bind the Registrar.** They are prohibitions with no
    period ("must not register", "is not to include ... unless"), not just
    conditions; s 18(1), once a limb is met, lifts to the permission in s 18(2)(a).
15. **The 48 hours are on another scale.** The first pass compared "hours after
    the death" with 48 beside rules that counted days, in one file; nothing went
    wrong because no rule combined them, but nothing said so either.

### Checks, and the binary

On 14 October 2026 no `l4` installed here ran these files as written (no `REFUSE`,
no `YMD`, and an older `daydate`), so they were checked on a mechanically altered
copy. That is no longer so: since 22 October 2026 the files as committed are what
is run, on the stable `l4` 1.6.98 (see the next section and **Checks** at the
top). The `l4` on `PATH` is older and was not used.

On 1.6.98, as on the binary of 14 October, a `RAND` whose two sides both fail
prints only the first side's reason: the s 44 trace in which another person
certifies and nothing more happens reports (c) alone, though (d) failed too. Read
that trace's reason as the first of two.

## Brought into line with the stable `l4` (22 October 2026)

The 14 October files failed on the stable `l4` with 76 errors in the case file
(`YMD` undefined 44 times, `REFUSE` 15, `WAIT UNTIL` 8, and ambiguity errors on
`Day`, `__GEQ__` and `__MINUS__` that followed from the untyped `YMD`), 7 in
`bdm-registration.l4` and 21 in `bdm-cause-of-death.l4`. Section 5 of
`docs/ENCODING-GUIDE.md` says how to write for that binary; this pass did that, and
changed nothing else of substance.

- **`YMD`** is a local shim in `bdm-registration.l4`, `YMD y m d MEANS Date d m y`
  (the stable `daydate`'s `Date` takes the day, the month and the year). The other
  two files have it by `IMPORT`. With `YMD` typed, the stable `daydate`'s own `Day`
  (also called `Date to days`) and `add months` resolve; nothing replaces them.
- **`WAIT UNTIL`** is spelled `WAITUNTIL` (8 traces).
- **Refusals.** `Why not covered` lists the five reasons, each worded as the named
  refusal it replaces, and `Answer` is either `answered` with an answer or
  `not covered` with a reason. Each duty that could refuse is now two rules:
  - the duty as its section states it, under its old name, which the traces run.
    It no longer looks at the gap: s 12(2), s 16(1), s 42 and s 44 ignore the date
    of the event, and s 45 is `FULFILLED` for a removal from the State, as its own
    words ("other than by way of removal of the remains from the State") give;
  - the question, "… or why it is not covered", which answers `not covered` with
    the reason for the cases the duty used to refuse, and `answered` with the duty
    otherwise. Ask the question, not the duty, about a case that may be outside
    the encoding.

  "Who must lodge the marriage certificate, and by when" always answers
  `not covered`.
- **The six `#ASSERT REFUSED`**, which the 14 October pass had left as `#CHECK`
  lines, are `#ASSERT`s that the question's answer EQUALS `not covered` with the
  reason:
  - s 12(2) and s 16(1) for Daniel's 1996 birth: before 14 April 1999;
  - who lodges Chloe's marriage certificate: the celebrant's Commonwealth duty;
  - s 42 for a death reportable to a coroner: s 42(d) with s 44(5);
  - s 42 for a suspected death established at an inquest: s 43;
  - s 45 for a removal of the remains from the State: s 46.

  One assertion is new, so that the s 44 module's question is run: s 44 for a
  death in the State on 1 January 1999 is `not covered` (before 14 April 1999). Its
  expected value comes from the compilation table's commencement date.
- **Every `NOT` is parenthesised**, in the rules and in the `#ASSERT NOT` lines;
  so is the comparison in s 19(4)(b) and in the s 44 offence.
- **Expected values.** None changed. The 40 `-- expect:` lines and the 55 earlier
  assertions are as they were.
