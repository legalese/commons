# A retrospective regulation in L4: a walkthrough

Built on {{var TODAY}} by `build-walkthrough.py`, with the unstable build `{{var L4VERSION}}` and, for the last step, the stable build `{{var MAINVERSION}}`.

How to read this page:

- Every excerpt of L4 was copied by a script from the file named, with its line numbers (`file:line`).
- Every "printed" result was copied by the script from a real `l4 run`.
- Nothing on this page is retyped.
- The encoding takes the notification as the text states it.
- It does not decide whether a retrospective notification is valid.
- This page is about how L4 handles dates.
- It does not say whether anyone was or is liable for having a television or a radio.
- The Telecommunications Act is a separate question and is not covered here.
- Where a table says TRUE or FALSE for a television, a radio or a satellite dish, it means whether the apparatus is "broadcasting apparatus" within section 2(1) of the Broadcasting Act, and so within section 20(1)(c).
- That is on one reading of section 2(1), called Reading A, which the sources do not settle (the stable encoding records the same fork).
- It leaves aside sections 20(3) and 20(4) and the Exemption Orders, which the row does not encode (step 6).
- This row is forward-looking and unstable-only.
- The stable build cannot read it (step 8).

## In short

What a retroactive regulation does to "what was the law on day X?":

1. When a regulation says it applies from a past date, "what was the law on day X?" depends on a second day: the day you ask (steps 1 and 2).
2. The same television, kept on the same day in 2011, is caught by the Broadcasting Act's licensing rule, as encoded, for a reader in August 2012 and is not caught for a reader in November 2012 (steps 1 and 2).
3. Conduct before the regulation's start date is not touched: the two readers in step 3 get the same answer (step 3).
4. The answer flips between 30 and 31 October 2012 for the person asking, and between 31 December 2010 and 1 January 2011 for the conduct (step 4).
5. Today the First Schedule, as encoded, lists the satellite dish and does not list the television or the radio; the radio goes as the television does (steps 5 and 6).

Why that needs two clocks:

6. L4 keeps the day of the conduct and the day you ask on separate clocks, and keeps the regulation's own dates beside the text they date (step 0).
7. The clocks are whole days; the Gazette gives an hour, 5.00 pm, which a whole-day clock cannot hold (step 4, and the way that gates on the Gazette's hour in step 7e).

What each variant shows:

8. Eight ways of writing the rule were run on the same days (step 7, and the table at the end): some agree with the chosen way and some do not.
9. One way, the decorators, is not accepted by the unstable build at all, and the stable build rejects four of the five clock words (steps 7g and 8).

## Step 0. The three dates in the case, and the clocks they live on

{{uses RED EAS EUV TODAY}}

The case has three dates, and the reader's day makes a fourth.

| the date | what it is | which clock L4 carries it on |
|---|---|---|
| the day of the conduct, for example 1 June 2011 | when the person had the television | valid time: "When did, or does, the fact hold in the world?" |
| 1 January 2011 | the day the notification is deemed to have started | rule-effective time: "Which version of the law applies?" Compared with `RULES EFFECTIVE DATE` |
| 30 October 2012 (made) and 31 October 2012, 5.00 pm (first published) | the day a reader could first have known of it | no clock of its own: kept as an ordinary date in the rule and compared with the day you ask |
| the day you ask, for example 1 August 2012 | when the question is being put | system time: "When is this evaluation actually running?" Read with `TODAY` |

The three dates of the notification, in the module that holds them (the quoted words are the Gazette's):

{{code sgbau-sched-s549.l4 | -- src:20 | 5}}

{{code sgbau-sched-s549.l4 | -- src:3 | 3}}

{{code sgbau-sched-s549.l4 | -- src:37 | 3}}

The two clocks that the rule reads, each named once so that nothing else in the module touches a clock:

{{code sgbau-first-schedule.l4 | `the day whose text governs` MEANS | 1}}

{{code sgbau-first-schedule.l4 | `the day the law is read` MEANS | 1}}

## Step 1. Conduct in 2011, read before 31 October 2012

{{uses RED EAS EUV TODAY}}

A person had a television, a radio or a satellite dish at home on 1 June 2011.
Someone asks on 1 August 2012, before the notification was published.

How to read the rule that picks the text of the Schedule:

- Names in backticks are ordinary words that L4 treats as one name.
- `BRANCH` lists conditions in order, and L4 takes the first one that holds.
- `BELOW` means before, and `AT LEAST` means on or after.
- `REFUSE` means "this encoding does not answer for that day".
- The text it picks is `the First Schedule of three items` (television, radio and satellite dish are listed) or `the First Schedule of the TVRO system only` (only the satellite dish is listed).

The rule, in the module `sgbau-first-schedule.l4`:

{{code sgbau-first-schedule.l4 | `the version of the First Schedule that governs` MEANS | 10}}

The question as a person asks it: it pins the day of the conduct and the day you ask.

{{code sgbau-seat.l4 | `Which text of the First Schedule applied` MEANS | 4}}

The helper that asks whether the licensing rule, as encoded, catches a television, with everything else about the person fixed:

{{code sgbau-walkthrough.l4 | `the licensing rule catches a television` MEANS | 2}}

What `l4 run` printed:

{{pairs P01}}

## Step 2. The same conduct, read on and after 31 October 2012

{{uses RED TODAY}}

The conduct is the same: 1 June 2011.
The question is put on 31 October 2012, on 1 November 2012, and in 2020.
The rule is the same rule; only the day you ask has moved.
The gate that reads the day you ask is the second condition of this arm:

{{code sgbau-first-schedule.l4 | AND `the day the law is read` AT LEAST | 3}}

What `l4 run` printed:

{{pairs P02 P03 P04}}

## Step 3. Conduct before 1 January 2011, read before and after

{{uses RED}}

The conduct is on 31 December 2010, the day before the notification is deemed to have started.
The question is put on 1 August 2012 and on 1 November 2012.
The rule has a second gate, on the day of the conduct, and the conduct fails it:

{{code sgbau-first-schedule.l4 | IF     `the day whose text governs` AT LEAST | 4}}

What `l4 run` printed:

{{pairs P05 P06}}

## Step 4. The edge days: 30 and 31 October 2012, 1 November 2012, 1 January 2011


The Gazette says the notification was first published at 5.00 pm on 31 October 2012, and made on 30 October.
A clock in L4 is a whole day, so the hour cannot be held.
The encoding counts a reader on 31 October 2012 as reading after publication; that is a convention, not something the text says.
The date it uses, from the Gazette's own front matter:

{{code sgbau-sched-s549.l4 | `S 549/2012 was first published in the Gazette on` MEANS | 1}}

What `l4 run` printed for readers on each side of the edge, and for conduct on each side of 1 January 2011:

{{pairs P07 P02 P03 P12 P06 P08 P09 P10 P11}}

## Step 5. Today

{{uses EAS EUV TODAY}}

Conduct today, asked today.
The day is written into the question so that this page can be rebuilt on any day; the line after it leaves the day you ask to the machine's own clock instead, and `TODAY` then reads that clock.

{{pairs P13}}

With the day you ask left to the clock:

{{run sgbau-walkthrough.l4 | -- P13 clock}}

## Step 6. The radio, at the same days as the television


The First Schedule listed three kinds of apparatus: a broadcast television receiver, a broadcast sound receiver (a radio) and a satellite dish system.
The notification deleted the Schedule and put back only the satellite dish system.
The Act's item says "sound receiver"; it does not separate AM from FM, and neither does the encoding.
The two texts, as the encoding holds them (the quoted words are the Gazette's):

{{code sgbau-sched-three-items.l4 | -- src:2168 | 11}}

{{code sgbau-sched-s549.l4 | @ref S 549/2012, cl 2 | 6}}

The helper for the radio is the television's, with the kind of receiver changed:

{{code sgbau-walkthrough.l4 | `the licensing rule catches a radio` MEANS | 2}}

What `l4 run` printed, a television beside a radio and a dish, at the days of steps 1 to 5:

{{pairs P01 P02 P05 P12 P13}}

Satellite dish systems are also the subject of the Broadcasting (TVRO System) Regulations, which this row does not encode, so nothing here says who may hold a dish.
What this does not say: the encoding does not model the exemptions in the Act (section 20(3) and (4), and the Exemption Orders), so it cannot say that a plain radio is exempt from licensing in general.
It says only what the First Schedule's list says, at the days shown.

## Step 7. Other ways of writing the rule, on the same days

Eight ways of writing the retrospective rule were tried.
Each was run on the same fifteen pairs of days (the first one, W1, in steps 1 to 6).
The table at the end sets them side by side.
In every table, A means {{var LEGEND_A}} and B means {{var LEGEND_B}}.

### 7a. W2: pin the rule-effective axis directly

{{uses EUR EAS}}

The same rule, asked with the day of the conduct on the rule-effective clock instead of the valid-time clock.

{{code sgbau-walkthrough.l4 | `the text, with the rule-effective axis pinned` MEANS | 4}}

What `l4 run` printed:

{{w2}}

### 7b. W0: write it as an ordinary amendment, with no reader gate

{{uses RED EUV EAS}}

The notification is given its start date, 1 January 2011, and nothing else.
The rule cannot tell a reader before 31 October 2012 from a reader after it.

{{code findings/alt-w0-no-publication-gate.l4 | `the text, read at the rule-effective date` MEANS | 6}}

What `l4 run` printed:

{{ways W0}}

### 7c. W3: apply the reader's knowledge outside the rule, by moving the date the text is read at

{{uses EUR RED}}

A selector decides which date to read the text at: before 31 October 2012 a 2011 conduct is read "as at 31 December 2010".
The rule itself reads only the day whose law is used.

{{code findings/alt-w3-selector.l4 | `the date the text is read at` MEANS | 3}}

{{code findings/alt-w3-selector.l4 | `the text under this way` MEANS | 2}}

What `l4 run` printed, one day at a time:

{{ways W3}}

Over a period it goes wrong.
A reader of 1 August 2012 should find the three-item text for every day of January 2011; `ALWAYS BETWEEN` asks exactly that, and prints:

{{run findings/alt-w3-selector.l4 | #EVAL `EVAL UNDER RULES EFFECTIVE AT` (`the date the text is read at` (Date 1 1 2011) (Date 1 8 2012))}}

The reason is that `ALWAYS BETWEEN` moves the rule-effective clock itself, to each day in turn, and that overwrites the selector's choice.
A caller that goes round the selector also gets the wrong text, with no warning:

{{run findings/alt-w3-selector.l4 | #EVAL `EVAL AS OF SYSTEM TIME` (Date 1 8 2012) (`EVAL UNDER RULES EFFECTIVE AT` (Date 1 6 2011)}}

### 7d. W4: the versions as a table of data

{{uses RED TODAY EAS EUV}}

Each row of the table has the day the text operates from and the day it was published; one rule keeps the rows that already operate and are already published, and takes the one that operates latest.

{{code findings/alt-w4-version-table.l4 | `the versions table` MEANS | 3}}

{{code findings/alt-w4-version-table.l4 | `the text, from the table` MEANS | 4}}

What `l4 run` printed:

{{ways W4}}

### 7e. W1-NOW: the same gate, but on the Gazette's hour

{{uses TODAY EAS}}

`NOW` is the instant the question is being asked.
The Gazette's own instant is 5.00 pm on 31 October 2012, so the gate compares `NOW` with that instant instead of comparing `TODAY` with the date.
The day you ask can only be pinned as a whole day, which lands at 8.00 am in Singapore, before 5.00 pm.

{{code findings/alt-w1-now-gate.l4 | `the text, with the reader gate on NOW` MEANS | 8}}

What `l4 run` printed:

{{ways W1NOW}}

### 7f. The reverse mapping: the day you ask on the rule-effective clock

{{uses RED EUR EUV}}

It is natural to want "the law in force on the day I ask".
That puts the day you ask on the rule-effective clock and the day of the conduct on the valid-time clock.
But nothing in L4 reads the valid-time clock on its own, so the rule never sees the day of the conduct.

{{code findings/alt-reverse-mapping.l4 | `the text, read at the rule-effective date` MEANS | 6}}

What `l4 run` printed:

{{ways REV}}

### 7g. The decorators: one rule per text, each dated

{{uses RED}}

The legislative style would be two rules with the same name, each marked with the day it takes effect.
The unstable build does not know the marker.
It warns that it will ignore it, and then rejects the two rules for having the same name.

{{code findings/alt-decorators.l4 | @effective 2003-07-31 | 8}}

What `l4 run` printed for the markers:

{{diag findings/alt-decorators.l4 | @effective 2003-07-31 | unstable}}

and for the place where the two same-named rules are used:

{{diag findings/alt-decorators.l4 | conduct `the text, by decorator` | unstable}}

No pair is answered:

{{ways DEC}}

## Step 8. What the stable build says

The stable build (`{{var MAINVERSION}}`) is the one Legalese Cloud runs.
This is the file, one clock word to a line, and what the stable build printed for each line, verbatim.

The one it knows, `TODAY`:

{{diag findings/walkthrough-main-probe-today.l4 | #EVAL TODAY | main}}

`RULES EFFECTIVE DATE`:

{{diag findings/walkthrough-main-probe.l4 | #EVAL `RULES EFFECTIVE DATE` | main}}

`EVAL UNDER RULES EFFECTIVE AT`:

{{diag findings/walkthrough-main-probe.l4 | #EVAL `EVAL UNDER RULES EFFECTIVE AT` | main}}

`EVAL UNDER VALID TIME`:

{{diag findings/walkthrough-main-probe.l4 | #EVAL `EVAL UNDER VALID TIME` | main}}

`EVAL AS OF SYSTEM TIME`:

{{diag findings/walkthrough-main-probe.l4 | #EVAL `EVAL AS OF SYSTEM TIME` | main}}

`REFUSE`, which the encoding also uses to say "this day is not covered":

{{diag findings/walkthrough-main-probe.l4 | #EVAL REFUSE | main}}

The decorator, which the stable build does not even read as a word:

{{diag findings/walkthrough-main-probe-decorator.l4 | @effective 2011-01-01 | main}}

## Judgement calls

These are choices the text does not make, and the encoding makes them as stated here.

**The hour (step 4, and step 7e).**
The Gazette says 5.00 pm on 31 October 2012, and a whole-day clock cannot hold an hour.
The encoding counts a reader on 31 October 2012 as reading after publication; that is a convention, not something the text says.

**Published, not made (step 0).**
The gate is the day of first publication, 31 October 2012, not the day the notification was made, 30 October 2012.
The sources do not say whether it was effective before it was published, and the encoding does not decide that.

**Asking before the conduct (step 4, pair P11).**
A reader who asks on 30 October 2012 about conduct on 31 October 2012 is answered with the law as it then read; the encoding does not refuse.
That says nothing about whether the law would change before the conduct day.

## The table: every way, on every pair of days

Each row is a pair (the day of the conduct, the day you ask).
"The text says" is the hand-written expectation from the Gazette texts: the three-item text governs unless the conduct is on or after 1 January 2011 and the reader is on or after 31 October 2012.
A cell marked "(differs)" printed something else.
The first way is the chosen one.

{{table}}

The pairs, in words:

{{pairlist}}
