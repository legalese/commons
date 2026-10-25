# Graffiti Vandalism Act 2016 (WA): baseline encoding for three seats

BASELINE, 25 October 2026. Not for public use as advice.

## Method

Written straight from the deposited text with the `writing-l4-rules` skill. It follows the design the main session set for Michael (the D1 to D7 decisions below) and the defaults ruled on 2026-10-18.

There are three modules:

- `gva-core.l4`, a seat-neutral core of the Act's operative provisions, in its own actors and terms, with ten regulative rules;
- `gva-dates.l4`, a small date module (no `daydate` import);
- `gva-seat.l4`, one seat layer for all three seats. It IMPORTs the core, restates no rule, and projects each regulative rule a seat meets into plain questions.

There are two case files: `gva-cases-core.l4` and `gva-cases-seat.l4`.

Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. There was no pipeline, no coverage table, no independent test pass and no human gate.

There was no earlier encoding of this Act, so nothing is replaced.

## Edition

The compilation of the Graffiti Vandalism Act 2016 (No. 16 of 2016) at legislation.wa.gov.au (law_a147110, mrdoc 29645), retrieved 7 September 2026. It is deposited at `../../registers/source-bundle/mrdoc_29645.txt`.

- **Commencement:** Part 1 on 11 July 2016; the rest on 12 October 2016.
- **Amendments included:** the Local Government Legislation Amendment Act 2016 (No. 26 of 2016) Pt 3 Div 14, in force 21 January 2017. It amended s 4.

These deposited Acts are read and cited, but not encoded:

- the Sentencing Act 1995 s 9 (`subjects/au/wa/sentencing-act-1995/`);
- the Interpretation Act 1984 ss 61, 64 and 71 (`subjects/au/wa/interpretation-act-1984/`);
- the State Administrative Tribunal Act 2004 s 92 (`subjects/au/wa/state-administrative-tribunal-act-2004/`);
- The Criminal Code s 731 (`subjects/au/wa/criminal-code-act-compilation-act-1913/`).

## Checks

Each command was `l4 run <file>.l4`, run from this folder with the stable `l4` 1.6.98. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

| File | Assertions written | Satisfied | Errors | Warnings |
|---|---|---|---|---|
| `gva-dates.l4` | 0 | 0 | 0 | 0 |
| `gva-core.l4` | 0 | 0 | 0 | 0 |
| `gva-seat.l4` | 0 | 0 | 0 | 0 |
| `gva-cases-core.l4` | 132 | 132 | 0 | 0 |
| `gva-cases-seat.l4` | 224 | 224 | 0 | 0 |

- **`gva-cases-core.l4`** has 22 `#TRACE`s, each with an `-- expect:` line, and each was read and came out as expected:
  - 12 breaches: s 5 twice, s 6 once, s 7 twice, s 18 twice, s 24 once and ss 27-28 four times;
  - 6 rules still waiting: s 5, s 18, the s 19 debt, the s 19 permission after a reasonable excuse, s 25, and the entry permission;
  - 2 permissions lapsed without a breach: ss 22 and 23;
  - 2 fulfilled after the lapse: further time allowed to object, and an extension sought.
- **`l4 check gva-seat.l4`** reports `Check succeeded`.
- **A script read every `@export` block in `gva-seat.l4`.** It found 38 exported questions. Each takes `my role` IS A Role as its first input. None takes a DEONTIC or EVENT input: their inputs are BOOLEAN, NUMBER, DATE, Role and four plain enumerations.
- **`l4 batch`** was run on two questions as a spot check. The entry question returns `no` at 23.99 hours and `yes` at 24. `l4 batch` requires every input in each row, even inputs the function never reads (finding 28). So "never asked" is shown by the ASSUMEd inputs in `gva-cases-seat.l4`, not by batch rows.

## Seats

The seat is a parameter. Every exported question takes `my role` first ("Which of these describes you"), as one of:

- `I put graffiti on property, or am accused of it`: the individual to whom the law is applied (ss 5, 6, 8, 10, 13). This seat comes first.
- `I sell spray paint or wide markers`: the seller on whom s 7 puts a duty. A shop or small business is fine.
- `I own or occupy property with graffiti on it`: the owner or occupier on whom Part 3 puts duties and costs, with the rights to object, seek review and refuse entry.

The local government is an actor in the core, with duties and powers. It is never a seat. Nor are the court, the State Administrative Tribunal or the police.

**Questions by role.** These are the exported names, in the layer's order.

- **Accused** (9):
  - `Is it an offence for me to put this mark on this property`
  - `What is the most I can be fined for damaging property by graffiti`
  - `What is the longest I can be imprisoned for damaging property by graffiti`
  - `What is the least penalty I can be given for damaging property by graffiti`
  - `How many hours of unpaid community work must my community order require`
  - `Can the court order me to restore the property or pay for its restoration`
  - `Can the court order this thing of mine forfeited`
  - `Is it an offence for me to have this thing with me`
  - `What is the most I can be fined for having a thing to use for graffiti`
- **Seller** (4):
  - `Is this item a graffiti implement`
  - `Is my sale of this item to this buyer an offence`
  - `Do I have the defence that I believed the buyer was an adult`
  - `What is the most I can be fined for selling a graffiti implement to a child`
- **Owner or occupier** (25):
  - s 18: `Can the local government require me to have the graffiti obliterated`, `Must I have the graffiti obliterated`, `By what date must the graffiti be obliterated`, `Has the notice been complied with in time`, `What is the most I can be fined for not complying with the notice`, `How much is the further fine for each day the notice is not complied with`, `Must the owner be told in writing that the notice was given`
  - s 19: `What may the local government do if the notice is not complied with`, `Can I get some of what the notice cost me back from the owner or occupier`
  - ss 20-22: `Must I be given written reasons for the notice and told of my rights`, `May I object to the notice`, `By what date must I lodge my objection`, `Did I lodge my objection in time`, `Can the local government still allow me further time to object`
  - s 23: `May I apply to the State Administrative Tribunal for a review now`, `By what date must I apply to the State Administrative Tribunal`, `Did I apply to the State Administrative Tribunal in time`, `Can I ask the Tribunal to extend my time to apply`
  - s 24: `Is the notice suspended while my objection or review is decided`
  - ss 27-30: `May the local government enter my land`, `How much notice of entry must I be given`, `Must the person entering tell me the power under which they enter`
  - ss 25 and 5: `May the local government remove graffiti put on my property without consent`, `Was it an offence to put this mark on my property`
  - s 12: `Can I be sued if someone is hurt removing graffiti on my property`

**Mirror cases.** The accused's s 5 question and the owner's "was it an offence" question are asked on the same facts in `gva-cases-seat.l4`, and agree. The facts are a fence sprayed without consent, the same with consent, and a sticker.

## Design decisions

Michael decided these, through the main session, and they were followed exactly.

- **D1. The core is seat-neutral** (`gva-core.l4`) and uses the Act's own actors: `the person`, `the seller`, `the notice recipient`, `the affected person` and `the local government`.
  - Duties, prohibitions and permissions with deadlines are regulative rules: s 5, s 6, s 7 (with the s 7(2) defence), s 18 (with the time the notice gives, the s 18(2) manner and the s 18(5) excuse), s 22, s 23 (from the day the right arose), s 24, and ss 27-28.
  - Computations are functions: the penalties, the minimum penalty for an adult or a child, the s 18(5) daily further fine, s 19 cost recovery and the court's power to apportion (s 19(5)-(7)).
  - The local government is an actor, never a seat.
- **D2. The seat is a parameter.** `DECLARE Role IS ONE OF` the three names above, unchanged. Every exported question takes `my role` IS A Role first, with `@desc Which of these describes you`.
- **D3. There is one seat layer**, `gva-seat.l4`, for all three seats. There is no per-seat layer and no per-seat deployment.
  - This departs from CLAUDE.md's `<prefix>-seat-<party>.l4` pattern for further seats.
  - One deployment serves all three seats, for example `au-wa-graffiti-vandalism-act-2016` (33 characters).
- **D4. Every answer type has an explicit `does not arise for you`.**
  - The types are `Yes or no`, `Amount`, `Years`, `Hours`, `Date answer`, `Done in time or not`, `Least penalty`, `What the local government may do` and `Who may be ordered to pay me back`.
  - A question about another role returns `does not arise for you` without reading any other input. `gva-cases-seat.l4` asks all 38 questions for the two roles they are not about, with ASSUMEd inputs that would stop evaluation if read.
  - Ten questions settle on the role alone, so the form can drop them: fines and prison terms, the least hours, the s 8 order, the daily fine, further time to object, the SAT extension, the hours of notice of entry, and s 30.
- **D5. Each regulative rule is projected into plain questions.**
  - (a) Does it apply to me?
  - (b) By when? The deadline is computed from the same named period the rule's WITHIN uses (`the days the notice allows`, `s 22(2) -- the days to object`, `s 23(3) -- the days to apply after the right arose`, `s 28(3) -- the hours of notice ...`), never from a restated number.
  - (c) Have I complied? The rule is run over what happened, inside the question, with CONSIDER EVALTRACE ... WHEN FULFILLED. On 1.6.98 this tells the cases apart correctly (finding 20), so no deadline arithmetic stands in for it.
  - (d) What follows if not?
  - No exported question takes a DEONTIC or EVENT input; the rules and events are built inside the seat layer.
- **D6. The questions per role follow the guide,** with the additions listed below.
- **D7. Scope out:** s 2, Part 3 Div 1 delegations (ss 15-17), Part 4, Parts 5-6, s 11 and s 31.
  - s 12 is kept as a one-line owner question, because it is natural there.
  - Judgments are inputs, answered conditionally: unsightly or offensive, a manner acceptable to the local government, reasonable excuse, reasonable suspicion, reasonable grounds, gross negligence, and what is fair and reasonable.

These are the points the design left open, and what was decided:

1. **The s 7(2) defence sits in the s 7 rule's LEST.** Where it is proved, the sale leads to FULFILLED (nothing more is owed); where it is not, it is a breach. So "Is my sale ... an offence" runs the rule with the defence facts, and the defence is also its own question.
2. **The s 18 rule takes only the days the notice allows and the reasonable excuse.** The s 18(1) conditions and "was the notice given to me" are in question (a), not in the rule: the rule is the duty a notice creates.
3. **The s 18(2) manner is the act's own field.** "In a manner acceptable to the local government" is `ensure the graffiti is obliterated` HAS `the manner`, and the rule matches only the acceptable manner. A cover-up the council rejects does not discharge the duty (asserted).
4. **The s 22 and s 23 permissions are written with DO, not MAY** (finding 21). Their LESTs are not breaches: the council may allow further time, and the person may ask the Tribunal for more time.
5. **There are ten regulative rules, not eight.** s 19(3)-(4) (the council may obliterate, then the recipient must pay) and s 25 (the council may obliterate graffiti applied without consent) are rules too.
6. **The rule-run helper (`the outcome of`) is in the seat layer, not the core.** It is projection machinery, not a provision.
7. **The s 23 route is worked out from facts, not chosen.** The facts are whether an objection was lodged, whether written notice of the decision was given, and the days since lodging. The core gives the first day, the day the right arose and the last day. The seat adds two outcomes the generic answer type needs for s 23(1)(b): `done too early, before the right to do it arose on` and `not open yet: it opens on`.
8. **`amount 0` is used where the role is right but the facts give no offence.** Examples are a notice given to the occupier rather than me, compliance in time, or a reasonable excuse. `does not arise for you` is kept for the role alone.
9. **The owner or occupier states one fact about the notice:** who it was given to, and how they stand to the property (`The notice and me`, six values). That one input serves ss 18(3), 18(5), 19, 20, 21, 22 and 23.
10. **The prohibitions without a deadline (ss 5, 6, 7) have no (b).** Question (c) is the same as "is it an offence", which runs the rule over the act.
11. **The entry rule counts whole minutes from the notice of entry.** The seat truncates the stated hours to whole minutes, so 23.99 hours is short of 24.
12. **Questions were added where the text gives the owner something:**
    - s 18(3), the owner told in writing;
    - s 21, written reasons and rights;
    - s 30, the particulars of the power of entry;
    - further time to object after the 28 days (Interpretation Act s 64(1));
    - an extension of time from the Tribunal (SAT Act s 92).

    The seller also gets `Is this item a graffiti implement`.
13. **Forfeiture (s 13) is asked of the accused only.** s 13 also follows a seller's s 7 conviction, but that is not asked.
14. **The compliance questions pass FALSE for the excuse.** The reasonable excuse changes what follows a failure, not whether the act was in time, so the fine question asks it instead. A comment marks the placeholder.

## Defaults (ruled 2026-10-18)

Followed:

- **The Act alone.** The instruments that bear on its numbers and dates are deposited and cited, but not encoded. These are Sentencing Act s 9(2), (3), (6) and (7), Interpretation Act ss 61(1)(b), 64(1) and 71, SAT Act s 92, and Criminal Code s 731.
- **The actors the text names.**
- **Judgments answered conditionally** (D7).
- **The Act's own definitions worked out from facts:** graffiti (s 3), adult and child, graffiti implement and offender (s 4), and affected person (s 20). The borrowed terms "owner" (LG Act s 1.4, through s 3) and "occupier" (s 14) are asked as facts.
- **One case is the text's natural unit:** one mark, one thing possessed, one sale, one notice, one entry.
- **The Act's own terms**, glossed in comments and `@desc`.
- **Machinery out.**

Departed from:

- **Three seats in one layer, not one module per seat** (D3, Michael's decision).
- **Days are counted under the Interpretation Act s 61(1)(b)**, the first day left out. This is a general instrument, not one that sets the Act's numbers; it is used because the Act's periods ("within 28 days after") need a counting rule.

## Scope

**In:**

- s 3 (graffiti);
- s 4 (adult, child, graffiti implement, offender, possession);
- ss 5 and 6, and s 7 with the s 7(2) defence;
- ss 8, 10 and 13 (the court's orders);
- s 12 (the owner's immunity);
- s 14 (public place, as a gloss);
- s 18(1)-(5) and s 19(3)-(7);
- ss 20, 21, 22, 23 and 24(1), (3);
- s 25;
- ss 27, 28 and 29 (the warrant as an input) and s 30.

**Out:**

- s 1;
- s 2, commencement;
- s 9, which applies the Sentencing Act to s 8 orders: not encoded;
- s 11, the immunity of the person removing graffiti, who is not a seat;
- ss 15-17, delegations;
- s 22(3), the procedure under LG Act Part 9 and s 9.6;
- s 26, the application of Division 4 (noted in comments);
- s 31, protection from liability;
- s 32, review of the Act;
- ss 33-44, amendments to other Acts.

## What the Act turns out to say

1. **s 23(3) sets a 42-day period in its chapeau, and its paragraph (c) can differ from it.** The chapeau gives 42 days "after the right to make it arose". Under s 23(2) that right arises once written notice of the decision has been given. Paragraph (c) says "within 42 days after the objection was decided". Where the written notice comes later than the decision, the chapeau gives a later last day. The encoding takes (c), the earlier and safer date. Asserted: decided 10 April 2027, apply by 22 May 2027.
2. **s 23(3)(b), "more than 35 days, but within 77 days" after lodging, agrees with the chapeau** (35 + 42 = 77). An application on or before day 35 comes before the right exists. The first day is the 36th. Asserted: lodged 20 March 2027; 20 April is too early; 25 April and 5 June are in time; 6 June is late.
3. **s 23(1)(b) and (2) overlap when the written decision arrives after day 35.** The person had the (1)(b) right and then gains the (2) right. The Act does not say whether (1)(b) survives. The encoding takes (2) once written notice has been given.
4. **s 24 suspends "the effect of the notice", but does not say how the notice's time runs afterwards.** It may restart, or the days of suspension may be added. The deadline questions give the notice's own date and say it may be suspended.
5. **s 18(5)(b) imposes "a further fine of $500 in respect of each day or part of a day during which the offence continues".**
   - It is read as counting from the day after the last day to comply up to the day the graffiti is obliterated (or the day asked about), with that day a part day.
   - Sentencing Act s 9(7) supports a daily penalty "for each day or part of a day during which the offence continues, in addition to any other penalty".
   - Interpretation Act s 71(1)(e)-(f) makes a failure that continues after conviction a further offence for each day after conviction, at $50 "unless otherwise provided". s 18(5)(b) provides otherwise as to the amount.
   - Whether the $500 runs from the failure or only after conviction is not settled by the text. The encoding counts from the failure, the larger maximum. Asserted: 5 days late, $7 500.
6. **s 7(1)(b) gives "a subsequent offence" a higher fine but does not define it.** It is read as an offence after an earlier conviction under s 7(1).
7. **The minimum penalty in s 5(1)(a), (b) depends on whether the offender is an adult or a child, but not as at when.** It is read as at the time of the offence, and asked as "your age when it happened".
8. **s 5(1)'s fine and imprisonment are maximums, and the minimum penalty binds the court.** The Sentencing Act makes the figures maximums (s 9(2)), lets them be imposed together or alone (s 9(6)), and makes the court impose at least the minimum (s 9(3)). s 5(3) and s 44 put the minimum beyond Young Offenders Act s 46(5a).
9. **s 8 (cleaning orders) and s 10 (at least 10 hours of community work) apply only to a s 5 offender** ("offender", s 4), not to s 6 or s 7. s 13 forfeiture follows any offence under the Act, but only on the prosecutor's application (s 13(4)). Criminal Code s 731(1) then says the court "may" order it, after the owner has had the chance to show cause (s 731(2)).
10. **s 20 adds only the owner as an affected person.** An occupier whose landlord was given the notice is not an affected person: they get no reasons and cannot object or seek review. Only the notice recipient can seek costs under s 19(5). Asserted.
11. **Interpretation Act s 61(1)(e) is not encoded.** A last day that falls on a Saturday, Sunday or public holiday moves to the next day that is not an excluded day. The deadline answers are the dates before that adjustment.
12. **s 18(1) and s 25 divide graffiti by consent.** Graffiti applied with the consent of the owner or occupier is a notice case (s 18). Graffiti applied "without the consent of the owner or occupier" may be removed by the council (s 25), read as neither having consented. Graffiti not visible from a public place falls under neither section. Asserted.
13. **s 22(2)'s "such further time as the local government may allow" can be allowed after the 28 days have passed.** Interpretation Act s 64(1) says a power to extend time may be used though the application comes after the time expired. Asserted as the s 22 rule's LEST: further time allowed on day 31, FULFILLED.
14. **s 28(3)'s "not less than 24 hours" counts hours, not days,** so s 61(1)(f) (clear days) does not apply. Entry exactly 24 hours after the notice is lawful; 23 hours 59 minutes is not. Asserted.
15. **s 27(2) lets the owner, occupier or a person they authorise stop a notified entry by objecting.** The council then needs a warrant (s 29(2)(a)). Asserted.
16. **s 18(2) requires obliteration "in a manner acceptable to the local government".** A cover-up the council does not accept does not discharge the notice. Asserted.
17. **s 18(4): the terms on which land is occupied do not prevent compliance,** so a tenant cannot rely on the lease. Noted in comments.
18. **The s 7(2) defence covers "a person acting on behalf of the accused",** such as a shop assistant. The accused must prove it.
19. **s 12 protects the owner only against death or injury suffered in graffiti removal under the Act or a community order,** and only short of gross negligence. The action lies against the State instead (s 12(3)), and the State may recover from a grossly negligent owner (s 12(4)).

## What the stable l4 (1.6.98) turned out to do

20. **CONSIDER EVALTRACE can match FULFILLED, but not BREACH.**
    - `WHEN BREACH` is a parse error, bare or as `WHEN BREACH BY p BECAUSE r`.
    - OTHERWISE takes a breached trace without error, but cannot tell a breach from a rule still waiting.
    - `EVALTRACE ... EQUALS` on a breached trace errors both ways ("Trying to check equality on types that do not support it").

    So `the outcome of` runs the rule once. Where the act was done, a FULFILLED trace means in time. Where it was not, the helper asks whether doing it now would keep the rule: if so the rule is still open, and if not the time has run out. It gives `done in time`, `not done in time` and `still open until` correctly, including at the edges (the last day, the day after, a lapse with a reasonable excuse that leads to s 19 rather than a breach), so no deadline arithmetic stands in for it. Asserted in the helper cases.
21. **A MAY with a WITHIN takes its HENCE whether it is used in time or lets the time run out,** so its trace cannot tell lodging in time from lodging late. The s 22 and s 23 permissions are written with DO, whose LEST is not a breach.
22. **BREACH ends a trace.** The s 19 power, which arises "for any reason" the notice is not complied with, cannot follow the s 18 breach in the same trace. It follows only the reasonable-excuse branch. The breach's BECAUSE names s 19, and the seat's s 19 question uses the compliance outcome.
23. **An event before a rule's start counts as in time.** The s 23(1)(b) "too early" check is made from the first day, outside the rule.
24. **The event that passes a deadline is not matched against the rule that follows.** The helper puts a WAITUNTIL before each event. A #TRACE shows the entry permission left waiting without it.
25. **`LIST OF EVENT ...` is not accepted as a GIVEN type** ("could not find a definition for the identifier EVENT"). The helper therefore takes the rule, party, act and times, and builds the event list itself. This also keeps EVENT values out of every signature.
26. **`IF NOT a AND (b)` on one line parses as `NOT (a AND b)`.** A case caught it in the s 23 in-time question, and it is now bracketed. Every NOT in the modules is bracketed.
27. **A WHERE-local name spelled like a field of a declared type** (`the first day`, `the last day`) gives "multiple definitions". The locals were renamed.
28. **`l4 batch` requires every input in each row,** even inputs the function never reads for that role.
29. **A constructor in a rule's action pattern matches only that constructor.** This is the s 18(2) manner. PROVIDED works too.

## Before relying on it

- An independent test pass and the human gates (HG1, HG2).
- **Excluded days** (Interpretation Act s 61(1)(e), finding 11). Weekend days could be computed from the date; public holidays need a deposited list.
- **How the notice's time runs after a s 24 suspension** (finding 4), and how the s 18(5)(b) days are counted (finding 5). Both need case law or departmental guidance.
- **The State Administrative Tribunal Rules 2004,** which carry the s 92 extension power, are not deposited. The SAT extension answer is "you may ask", not "it will be granted".
- **The procedure for an objection** under LG Act Part 9 and s 9.6 (s 22(3)), the Sentencing Act orders behind ss 8-10, and Criminal Code s 731 are cited, not encoded.
- **Deployment** as one deployment for the three seats (D3) is done by a person with Legalese Cloud access.
