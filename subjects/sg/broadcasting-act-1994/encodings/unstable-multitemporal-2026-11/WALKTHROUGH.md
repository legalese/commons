# A retrospective regulation in L4: a walkthrough

Built on 4 November 2026 by `build-walkthrough.py`, with the unstable build `unstable-20261101-8e19faa (unstable, 8e19faa, 2026-11-01)` and, for the last step, the stable build `1.6.98 (main, 7689b0d, 2026-10-19)`.

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

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.
- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").
- `EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.
  It moves valid time ("When did, or does, the fact hold in the world?").
  Here d is the day of the conduct.
- `TODAY` is the day on which the question is being asked.
  It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.

The case has three dates, and the reader's day makes a fourth.

| the date | what it is | which clock L4 carries it on |
|---|---|---|
| the day of the conduct, for example 1 June 2011 | when the person had the television | valid time: "When did, or does, the fact hold in the world?" |
| 1 January 2011 | the day the notification is deemed to have started | rule-effective time: "Which version of the law applies?" Compared with `RULES EFFECTIVE DATE` |
| 30 October 2012 (made) and 31 October 2012, 5.00 pm (first published) | the day a reader could first have known of it | no clock of its own: kept as an ordinary date in the rule and compared with the day you ask |
| the day you ask, for example 1 August 2012 | when the question is being put | system time: "When is this evaluation actually running?" Read with `TODAY` |

The three dates of the notification, in the module that holds them (the quoted words are the Gazette's):

`sgbau-sched-s549.l4:25-29`

```
25  -- src:20 | 1. This Notification may be cited as the Broadcasting Act
26  -- src:21 | (Amendment of First Schedule) Notification 2012 and shall be deemed
27  -- src:22 | to have come into operation on 1st January 2011.
28  @ref S 549/2012, cl 1 (src:20-22)
29  `S 549/2012 is deemed to have come into operation on` MEANS Date 1 1 2011
```

`sgbau-sched-s549.l4:33-35`

```
33  -- src:3 | First published in the Government Gazette, Electronic Edition, on 31st October 2012 at 5.00 pm.
34  @ref S 549/2012, front matter (src:3)
35  `S 549/2012 was first published in the Gazette on` MEANS Date 31 10 2012
```

`sgbau-sched-s549.l4:37-39`

```
37  -- src:37 | Made this 30th day of October 2012.
38  @ref S 549/2012, signature line (src:37)
39  `S 549/2012 was made on` MEANS Date 30 10 2012
```

The two clocks that the rule reads, each named once so that nothing else in the module touches a clock:

`sgbau-first-schedule.l4:50`

```
50  `the day whose text governs` MEANS `RULES EFFECTIVE DATE`
```

`sgbau-first-schedule.l4:53`

```
53  `the day the law is read` MEANS TODAY
```

## Step 1. Conduct in 2011, read before 31 October 2012

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.
- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").
- `EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.
  It moves valid time ("When did, or does, the fact hold in the world?").
  Here d is the day of the conduct.
- `TODAY` is the day on which the question is being asked.
  It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.

A person had a television, a radio or a satellite dish at home on 1 June 2011.
Someone asks on 1 August 2012, before the notification was published.

How to read the rule that picks the text of the Schedule:

- Names in backticks are ordinary words that L4 treats as one name.
- `BRANCH` lists conditions in order, and L4 takes the first one that holds.
- `BELOW` means before, and `AT LEAST` means on or after.
- `REFUSE` means "this encoding does not answer for that day".
- The text it picks is `the First Schedule of three items` (television, radio and satellite dish are listed) or `the First Schedule of the TVRO system only` (only the satellite dish is listed).

The rule, in the module `sgbau-first-schedule.l4`:

`sgbau-first-schedule.l4:63-71`

```
63  `the version of the First Schedule that governs` MEANS
64      BRANCH IF `the day whose text governs` BELOW `the first deposited edition operated from`
65             THEN REFUSE "not covered: the conduct day is before the first deposited edition (31 July 2003)"
66             IF `the day the law is read` BELOW `the first deposited edition operated from`
67             THEN REFUSE "not covered: the reading day is before the first deposited edition (31 July 2003)"
68             IF     `the day whose text governs` AT LEAST `S 549/2012 is deemed to have come into operation on`
69                AND `the day the law is read` AT LEAST `S 549/2012 was first published in the Gazette on`
70             THEN `the First Schedule of the TVRO system only`
71             OTHERWISE `the First Schedule of three items`
```

The question as a person asks it: it pins the day of the conduct and the day you ask.

`sgbau-seat.l4:152-155`

```
152  `Which text of the First Schedule applied` MEANS
153      `EVAL AS OF SYSTEM TIME` `the day the law is to be read`
154          (`EVAL UNDER VALID TIME` `the day you are asking about`
155              `the version of the First Schedule that governs`)
```

The helper that asks whether the licensing rule, as encoded, catches a television, with everything else about the person fixed:

`sgbau-walkthrough.l4:28-29`

```
28  `the licensing rule catches a television` MEANS
29      `Did I need a licence for my apparatus` conduct reading
```

What `l4 run` printed:

| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |
|---|---|---|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:68-71` |

## Step 2. The same conduct, read on and after 31 October 2012

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.
- `TODAY` is the day on which the question is being asked.
  It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.

The conduct is the same: 1 June 2011.
The question is put on 31 October 2012, on 1 November 2012, and in 2020.
The rule is the same rule; only the day you ask has moved.
The gate that reads the day you ask is the second condition of this arm:

`sgbau-first-schedule.l4:69-71`

```
69                AND `the day the law is read` AT LEAST `S 549/2012 was first published in the Gazette on`
70             THEN `the First Schedule of the TVRO system only`
71             OTHERWISE `the First Schedule of three items`
```

What `l4 run` printed:

| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |
|---|---|---|---|---|---|---|---|
| P02 | 1 Jun 2011 | 31 Oct 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:73-76` |
| P03 | 1 Jun 2011 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:78-81` |
| P04 | 1 Jun 2011 | 1 Jan 2020 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:83-86` |

## Step 3. Conduct before 1 January 2011, read before and after

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.

The conduct is on 31 December 2010, the day before the notification is deemed to have started.
The question is put on 1 August 2012 and on 1 November 2012.
The rule has a second gate, on the day of the conduct, and the conduct fails it:

`sgbau-first-schedule.l4:68-71`

```
68             IF     `the day whose text governs` AT LEAST `S 549/2012 is deemed to have come into operation on`
69                AND `the day the law is read` AT LEAST `S 549/2012 was first published in the Gazette on`
70             THEN `the First Schedule of the TVRO system only`
71             OTHERWISE `the First Schedule of three items`
```

What `l4 run` printed:

| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |
|---|---|---|---|---|---|---|---|
| P05 | 31 Dec 2010 | 1 Aug 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:88-91` |
| P06 | 31 Dec 2010 | 1 Nov 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:93-96` |

## Step 4. The edge days: 30 and 31 October 2012, 1 November 2012, 1 January 2011


The Gazette says the notification was first published at 5.00 pm on 31 October 2012, and made on 30 October.
A clock in L4 is a whole day, so the hour cannot be held.
The encoding counts a reader on 31 October 2012 as reading after publication; that is a convention, not something the text says.
The date it uses, from the Gazette's own front matter:

`sgbau-sched-s549.l4:35`

```
35  `S 549/2012 was first published in the Gazette on` MEANS Date 31 10 2012
```

What `l4 run` printed for readers on each side of the edge, and for conduct on each side of 1 January 2011:

| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |
|---|---|---|---|---|---|---|---|
| P07 | 1 Jun 2011 | 30 Oct 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:98-101` |
| P02 | 1 Jun 2011 | 31 Oct 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:73-76` |
| P03 | 1 Jun 2011 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:78-81` |
| P12 | 1 Jan 2011 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:123-126` |
| P06 | 31 Dec 2010 | 1 Nov 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:93-96` |
| P08 | 30 Oct 2012 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:103-106` |
| P09 | 31 Oct 2012 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:108-111` |
| P10 | 1 Nov 2012 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:113-116` |
| P11 | 31 Oct 2012 | 30 Oct 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:118-121` |

## Step 5. Today

- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").
- `EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.
  It moves valid time ("When did, or does, the fact hold in the world?").
  Here d is the day of the conduct.
- `TODAY` is the day on which the question is being asked.
  It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.

Conduct today, asked today.
The day is written into the question so that this page can be rebuilt on any day; the line after it leaves the day you ask to the machine's own clock instead, and `TODAY` then reads that clock.

| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |
|---|---|---|---|---|---|---|---|
| P13 | 4 Nov 2026 | 4 Nov 2026 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:128-131` |

With the day you ask left to the clock:

`sgbau-walkthrough.l4:143`

```
  143  #EVAL `the text, with the reading day left to the clock` (Date 4 11 2026)   -- P13 clock
```

`l4 run` printed:

```
`the First Schedule of the TVRO system only`
```

## Step 6. The radio, at the same days as the television


The First Schedule listed three kinds of apparatus: a broadcast television receiver, a broadcast sound receiver (a radio) and a satellite dish system.
The notification deleted the Schedule and put back only the satellite dish system.
The Act's item says "sound receiver"; it does not separate AM from FM, and neither does the encoding.
The two texts, as the encoding holds them (the quoted words are the Gazette's):

`sgbau-sched-three-items.l4:29-39`

```
29  -- src:2168 | 2. Broadcast sound receiver.
30  -- src:2171 | “broadcast sound receiver” means any apparatus used for the aural reception
31  -- src:2172 | of any broadcasting service;
32  -- src:BA1994.20030731:2141 | 2. Broadcast sound receiver.
33  -- src:BA1994.20030731:2146 | ‘‘broadcast sound receiver’’ means any apparatus used for the aural
34  -- src:BA1994.20030731:2147 | reception of any broadcasting service;
35  @ref Broadcasting Act (Cap 28), First Schedule, item 2 and its definition (src:2168-2172; src:BA1994.20030731:2141-2147)
36  GIVEN apparatus IS AN Apparatus
37  GIVETH A BOOLEAN
38  `item 2 of the three-item Schedule, a broadcast sound receiver` MEANS
39      apparatus's `used for the aural reception of a broadcasting service`
```

`sgbau-sched-s549.l4:55-59`

```
55  @ref S 549/2012, cl 2 (src:25-35)
56  GIVEN apparatus IS AN Apparatus
57  GIVETH A BOOLEAN
58  `the TVRO-only Schedule specifies the apparatus` MEANS
59      apparatus's `capable of direct reception from a satellite in extra-terrestrial space`
```

The helper for the radio is the television's, with the kind of receiver changed:

`sgbau-walkthrough.l4:36-37`

```
36  `the licensing rule catches a radio` MEANS
37      `Did I need a licence for my apparatus` conduct reading
```

What `l4 run` printed, a television beside a radio and a dish, at the days of steps 1 to 5:

| pair | conduct day | reading day | text that governs | the licensing rule, as encoded, catches a television | a radio | a satellite dish | printed at |
|---|---|---|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:68-71` |
| P02 | 1 Jun 2011 | 31 Oct 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:73-76` |
| P05 | 31 Dec 2010 | 1 Aug 2012 | `the First Schedule of three items` | TRUE | TRUE | TRUE | `sgbau-walkthrough.l4:88-91` |
| P12 | 1 Jan 2011 | 1 Nov 2012 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:123-126` |
| P13 | 4 Nov 2026 | 4 Nov 2026 | `the First Schedule of the TVRO system only` | FALSE | FALSE | TRUE | `sgbau-walkthrough.l4:128-131` |

Satellite dish systems are also the subject of the Broadcasting (TVRO System) Regulations, which this row does not encode, so nothing here says who may hold a dish.
What this does not say: the encoding does not model the exemptions in the Act (section 20(3) and (4), and the Exemption Orders), so it cannot say that a plain radio is exempt from licensing in general.
It says only what the First Schedule's list says, at the days shown.

## Step 7. Other ways of writing the rule, on the same days

Eight ways of writing the retrospective rule were tried.
Each was run on the same fifteen pairs of days (the first one, W1, in steps 1 to 6).
The table at the end sets them side by side.
In every table, A means `the First Schedule of three items` and B means `the First Schedule of the TVRO system only`.

### 7a. W2: pin the rule-effective axis directly

- `EVAL UNDER RULES EFFECTIVE AT` d x works out x using the version of the law in force on day d, whatever day the facts belong to.
  It moves rule-effective time ("Which version of the law applies?").
- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").

The same rule, asked with the day of the conduct on the rule-effective clock instead of the valid-time clock.

`sgbau-walkthrough.l4:55-57`

```
55  `the text, with the rule-effective axis pinned` MEANS
56      `EVAL AS OF SYSTEM TIME` reading
57          (`EVAL UNDER RULES EFFECTIVE AT` conduct `the version of the First Schedule that governs`)
```

What `l4 run` printed:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | A | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | B | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | A | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | A | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | A | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | refused | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | A | A |

Printed by the directives at `sgbau-walkthrough.l4:72-142`, one for each pair, in the order of the table.

### 7b. W0: write it as an ordinary amendment, with no reader gate

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.
- `EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.
  It moves valid time ("When did, or does, the fact hold in the world?").
  Here d is the day of the conduct.
- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").

The notification is given its start date, 1 January 2011, and nothing else.
The rule cannot tell a reader before 31 October 2012 from a reader after it.

`findings/alt-w0-no-publication-gate.l4:16-21`

```
16  `the text, read at the rule-effective date` MEANS
17      BRANCH IF `RULES EFFECTIVE DATE` BELOW (Date 31 7 2003)
18             THEN REFUSE "not covered: the conduct day is before the first deposited edition (31 July 2003)"
19             IF `RULES EFFECTIVE DATE` AT LEAST (Date 1 1 2011)
20             THEN `the First Schedule of the TVRO system only`
21             OTHERWISE `the First Schedule of three items`
```

What `l4 run` printed:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | B **differs** | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | B | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | A | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | B **differs** | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | B **differs** | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | refused | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | A | A |

Printed by the directives at `findings/alt-w0-no-publication-gate.l4:30-44`, one for each pair, in the order of the table.

### 7c. W3: apply the reader's knowledge outside the rule, by moving the date the text is read at

- `EVAL UNDER RULES EFFECTIVE AT` d x works out x using the version of the law in force on day d, whatever day the facts belong to.
  It moves rule-effective time ("Which version of the law applies?").
- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.

A selector decides which date to read the text at: before 31 October 2012 a 2011 conduct is read "as at 31 December 2010".
The rule itself reads only the day whose law is used.

`findings/alt-w3-selector.l4:32-33`

```
32  `the date the text is read at` MEANS
33      IF reading BELOW (Date 31 10 2012) AND conduct AT LEAST (Date 1 1 2011) THEN Date 31 12 2010 ELSE conduct
```

`findings/alt-w3-selector.l4:38-39`

```
38  `the text under this way` MEANS
39      `EVAL UNDER RULES EFFECTIVE AT` (`the date the text is read at` conduct reading) `the text, read at the rule-effective date`
```

What `l4 run` printed, one day at a time:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | A | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | B | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | A | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | A | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | A | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | refused | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | A | A |

Printed by the directives at `findings/alt-w3-selector.l4:53-67`, one for each pair, in the order of the table.

Over a period it goes wrong.
A reader of 1 August 2012 should find the three-item text for every day of January 2011; `ALWAYS BETWEEN` asks exactly that, and prints:

`findings/alt-w3-selector.l4:48`

```
   48  #EVAL `EVAL UNDER RULES EFFECTIVE AT` (`the date the text is read at` (Date 1 1 2011) (Date 1 8 2012)) (`ALWAYS BETWEEN` (Date 1 1 2011) (Date 31 1 2011) `the three-item text governs that day`)
```

`l4 run` printed:

```
FALSE
```

The reason is that `ALWAYS BETWEEN` moves the rule-effective clock itself, to each day in turn, and that overwrites the selector's choice.
A caller that goes round the selector also gets the wrong text, with no warning:

`findings/alt-w3-selector.l4:50`

```
   50  #EVAL `EVAL AS OF SYSTEM TIME` (Date 1 8 2012) (`EVAL UNDER RULES EFFECTIVE AT` (Date 1 6 2011) `the text, read at the rule-effective date`)
```

`l4 run` printed:

```
`the First Schedule of the TVRO system only`
```

### 7d. W4: the versions as a table of data

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.
- `TODAY` is the day on which the question is being asked.
  It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.
- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").
- `EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.
  It moves valid time ("When did, or does, the fact hold in the world?").
  Here d is the day of the conduct.

Each row of the table has the day the text operates from and the day it was published; one rule keeps the rows that already operate and are already published, and takes the one that operates latest.

`findings/alt-w4-version-table.l4:22-24`

```
22  `the versions table` MEANS LIST
23      Row WITH `the text` IS `the First Schedule of three items`,         `operates from` IS Date 31 7 2003, `published on` IS Date 31 7 2003
24      Row WITH `the text` IS `the First Schedule of the TVRO system only`, `operates from` IS Date 1 1 2011,  `published on` IS Date 31 10 2012
```

`findings/alt-w4-version-table.l4:38-41`

```
38  `the text, from the table` MEANS
39      CONSIDER filter `the row governs` `the versions table`
40      WHEN EMPTY                THEN REFUSE "not covered: no version operates and is published"
41      WHEN row FOLLOWED BY rows THEN (foldl `the later-operating of` row rows)'s `the text`
```

What `l4 run` printed:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | A | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | B | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | A | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | A | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | A | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | refused | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | A | A |

Printed by the directives at `findings/alt-w4-version-table.l4:50-64`, one for each pair, in the order of the table.

### 7e. W1-NOW: the same gate, but on the Gazette's hour

- `TODAY` is the day on which the question is being asked.
  It reads system time, which `EVAL AS OF SYSTEM TIME` moves and nothing else moves.
- `EVAL AS OF SYSTEM TIME` d x works out x as if the question were being asked on day d.
  It moves system time ("When is this evaluation actually running?").

`NOW` is the instant the question is being asked.
The Gazette's own instant is 5.00 pm on 31 October 2012, so the gate compares `NOW` with that instant instead of comparing `TODAY` with the date.
The day you ask can only be pinned as a whole day, which lands at 8.00 am in Singapore, before 5.00 pm.

`findings/alt-w1-now-gate.l4:18-24`

```
18  `the text, with the reader gate on NOW` MEANS
19      BRANCH IF `RULES EFFECTIVE DATE` BELOW (Date 31 7 2003)
20             THEN REFUSE "not covered: the conduct day is before the first deposited edition (31 July 2003)"
21             IF     `RULES EFFECTIVE DATE` AT LEAST (Date 1 1 2011)
22                AND NOW AT LEAST `the Gazette instant`
23             THEN `the First Schedule of the TVRO system only`
24             OTHERWISE `the First Schedule of three items`
```

What `l4 run` printed:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | A | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | A **differs** | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | A | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | A | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | A | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | refused | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | A | A |

Printed by the directives at `findings/alt-w1-now-gate.l4:33-47`, one for each pair, in the order of the table.

### 7f. The reverse mapping: the day you ask on the rule-effective clock

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.
- `EVAL UNDER RULES EFFECTIVE AT` d x works out x using the version of the law in force on day d, whatever day the facts belong to.
  It moves rule-effective time ("Which version of the law applies?").
- `EVAL UNDER VALID TIME` d x works out x about the facts as they stood on day d.
  It moves valid time ("When did, or does, the fact hold in the world?").
  Here d is the day of the conduct.

It is natural to want "the law in force on the day I ask".
That puts the day you ask on the rule-effective clock and the day of the conduct on the valid-time clock.
But nothing in L4 reads the valid-time clock on its own, so the rule never sees the day of the conduct.

`findings/alt-reverse-mapping.l4:16-21`

```
16  `the text, read at the rule-effective date` MEANS
17      BRANCH IF `RULES EFFECTIVE DATE` BELOW (Date 31 7 2003)
18             THEN REFUSE "not covered: the reading day is before the first deposited edition (31 July 2003)"
19             IF `RULES EFFECTIVE DATE` AT LEAST (Date 31 10 2012)
20             THEN `the First Schedule of the TVRO system only`
21             OTHERWISE `the First Schedule of three items`
```

What `l4 run` printed:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | A | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | B | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | B **differs** | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | A | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | A | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | B **differs** | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | B **differs** | A |

Printed by the directives at `findings/alt-reverse-mapping.l4:30-44`, one for each pair, in the order of the table.

### 7g. The decorators: one rule per text, each dated

- `RULES EFFECTIVE DATE` asks which day's version of the law is being used.
  Its axis is rule-effective time, the tutorial's question "Which version of the law applies?".
  Unless told otherwise it follows the day of the conduct.

The legislative style would be two rules with the same name, each marked with the day it takes effect.
The unstable build does not know the marker.
It warns that it will ignore it, and then rejects the two rules for having the same name.

`findings/alt-decorators.l4:16-22`

```
16  @effective 2003-07-31
17  GIVETH A `Version of the First Schedule`
18  `the text, by decorator` MEANS `the First Schedule of three items`
19  
20  @effective 2011-01-01
21  GIVETH A `Version of the First Schedule`
22  `the text, by decorator` MEANS `the First Schedule of the TVRO system only`
```

What `l4 run` printed for the markers:

`findings/alt-decorators.l4:16`

```
   16  @effective 2003-07-31
```

printed:

```
Range:    16:1-16:22
Severity: Warning
Message:
    Unknown annotation `@effective`: this version of L4 does not know it, so it is ignored, along with the rest of its line. The annotations this version knows are @desc, @export, @infix, @infixl, @infixr, @lang, @nlg, @nonassertable, @nonexhaustive, @ref, @ref-map, @ref-src.
```

and for the place where the two same-named rules are used:

`findings/alt-decorators.l4:28`

```
   28      `EVAL AS OF SYSTEM TIME` reading (`EVAL UNDER VALID TIME` conduct `the text, by decorator`)
```

printed:

```
Range:    28:71-28:95
Severity: Error
Message:
    There are multiple definitions for the identifier

      `the text, by decorator`

    and I do not have sufficient information to make a choice between them.
    The options are:

      `the text, by decorator` (defined at alt-decorators.l4:22:1-25) of type `Version of the First Schedule`
      `the text, by decorator` (defined at alt-decorators.l4:18:1-25) of type `Version of the First Schedule`
```

No pair is answered:

| pair | conduct day | reading day | printed | the text says |
|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | no value **differs** | A |
| P02 | 1 Jun 2011 | 31 Oct 2012 | no value **differs** | B |
| P03 | 1 Jun 2011 | 1 Nov 2012 | no value **differs** | B |
| P04 | 1 Jun 2011 | 1 Jan 2020 | no value **differs** | B |
| P05 | 31 Dec 2010 | 1 Aug 2012 | no value **differs** | A |
| P06 | 31 Dec 2010 | 1 Nov 2012 | no value **differs** | A |
| P07 | 1 Jun 2011 | 30 Oct 2012 | no value **differs** | A |
| P08 | 30 Oct 2012 | 1 Nov 2012 | no value **differs** | B |
| P09 | 31 Oct 2012 | 1 Nov 2012 | no value **differs** | B |
| P10 | 1 Nov 2012 | 1 Nov 2012 | no value **differs** | B |
| P11 | 31 Oct 2012 | 30 Oct 2012 | no value **differs** | A |
| P12 | 1 Jan 2011 | 1 Nov 2012 | no value **differs** | B |
| P13 | 4 Nov 2026 | 4 Nov 2026 | no value **differs** | B |
| P14 | 30 Jul 2003 | 4 Nov 2026 | no value **differs** | refused |
| P15 | 31 Jul 2003 | 4 Nov 2026 | no value **differs** | A |

Printed by the directives at `findings/alt-decorators.l4:31-45`, one for each pair, in the order of the table.

## Step 8. What the stable build says

The stable build (`1.6.98 (main, 7689b0d, 2026-10-19)`) is the one Legalese Cloud runs.
This is the file, one clock word to a line, and what the stable build printed for each line, verbatim.

The one it knows, `TODAY`:

`findings/walkthrough-main-probe-today.l4:6`

```
    6  #EVAL TODAY
```

printed:

```
Range:    6:1-6:12
Severity: Information
Message:
    DATE OF 4, 11, 2026
```

`RULES EFFECTIVE DATE`:

`findings/walkthrough-main-probe.l4:10`

```
   10  #EVAL `RULES EFFECTIVE DATE`
```

printed:

```
Range:    10:7-10:29
Severity: Error
Message:
    I could not find a definition for the identifier

      `RULES EFFECTIVE DATE`

    which I have inferred to be of type: 

      `RULES EFFECTIVE DATE`2
```

`EVAL UNDER RULES EFFECTIVE AT`:

`findings/walkthrough-main-probe.l4:11`

```
   11  #EVAL `EVAL UNDER RULES EFFECTIVE AT` (Date 1 6 2011) TODAY
```

printed:

```
Range:    11:7-11:38
Severity: Error
Message:
    I could not find a definition for the identifier

      `EVAL UNDER RULES EFFECTIVE AT`

    which I have inferred to be of type: 

      FUNCTION FROM DATE AND DATE TO res8
```

`EVAL UNDER VALID TIME`:

`findings/walkthrough-main-probe.l4:12`

```
   12  #EVAL `EVAL UNDER VALID TIME` (Date 1 6 2011) TODAY
```

printed:

```
Range:    12:7-12:30
Severity: Error
Message:
    I could not find a definition for the identifier

      `EVAL UNDER VALID TIME`

    which I have inferred to be of type: 

      FUNCTION FROM DATE AND DATE TO res13
```

`EVAL AS OF SYSTEM TIME`:

`findings/walkthrough-main-probe.l4:13`

```
   13  #EVAL `EVAL AS OF SYSTEM TIME` (Date 1 6 2011) TODAY
```

printed:

```
Range:    13:7-13:31
Severity: Error
Message:
    I could not find a definition for the identifier

      `EVAL AS OF SYSTEM TIME`

    which I have inferred to be of type: 

      FUNCTION FROM DATE AND DATE TO res18
```

`REFUSE`, which the encoding also uses to say "this day is not covered":

`findings/walkthrough-main-probe.l4:14`

```
   14  #EVAL REFUSE "not covered"
```

printed:

```
Range:    14:7-14:13
Severity: Error
Message:
    I could not find a definition for the identifier

      REFUSE

    which I have inferred to be of type: 

      FUNCTION FROM STRING TO res22
```

The decorator, which the stable build does not even read as a word:

`findings/walkthrough-main-probe-decorator.l4:7`

```
    7  @effective 2011-01-01
```

printed:

```
Range:    7:1-7:1
Severity: Error
Message:
      |
    7 | @effective 2011-01-01
      | ^
    unexpected '@'
    expecting "'s", "--", "..", "...", "/*", "//", "<<", ">>", "@desc", "@export", "@ref-map", "@ref-src", "{-", '"', '#', '%', '(', ')', ',', '-', '.', ':', ';', '[', ']', '^', '`', '{', '}', '§', Natural Language Generation Annotation, Reference Annotation, end of input, float, integer, operator char, or whitespace
```

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

| pair | conduct day | reading day | the text says | W1, the chosen way | W2, rule-effective axis pinned | W0, no reader gate | W3, selector outside | W4, table of versions | W1-NOW, gate on NOW at 5.00 pm | reverse mapping | decorators |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | A | A | A | B (differs) | A | A | A | A | no value (differs) |
| P02 | 1 Jun 2011 | 31 Oct 2012 | B | B | B | B | B | B | A (differs) | B | no value (differs) |
| P03 | 1 Jun 2011 | 1 Nov 2012 | B | B | B | B | B | B | B | B | no value (differs) |
| P04 | 1 Jun 2011 | 1 Jan 2020 | B | B | B | B | B | B | B | B | no value (differs) |
| P05 | 31 Dec 2010 | 1 Aug 2012 | A | A | A | A | A | A | A | A | no value (differs) |
| P06 | 31 Dec 2010 | 1 Nov 2012 | A | A | A | A | A | A | A | B (differs) | no value (differs) |
| P07 | 1 Jun 2011 | 30 Oct 2012 | A | A | A | B (differs) | A | A | A | A | no value (differs) |
| P08 | 30 Oct 2012 | 1 Nov 2012 | B | B | B | B | B | B | B | B | no value (differs) |
| P09 | 31 Oct 2012 | 1 Nov 2012 | B | B | B | B | B | B | B | B | no value (differs) |
| P10 | 1 Nov 2012 | 1 Nov 2012 | B | B | B | B | B | B | B | B | no value (differs) |
| P11 | 31 Oct 2012 | 30 Oct 2012 | A | A | A | B (differs) | A | A | A | A | no value (differs) |
| P12 | 1 Jan 2011 | 1 Nov 2012 | B | B | B | B | B | B | B | B | no value (differs) |
| P13 | 4 Nov 2026 | 4 Nov 2026 | B | B | B | B | B | B | B | B | no value (differs) |
| P14 | 30 Jul 2003 | 4 Nov 2026 | refused | refused | refused | refused | refused | refused | refused | B (differs) | no value (differs) |
| P15 | 31 Jul 2003 | 4 Nov 2026 | A | A | A | A | A | A | A | B (differs) | no value (differs) |

A = `the First Schedule of three items`; B = `the First Schedule of the TVRO system only`; refused = the model refuses to answer; no value = the build printed an error instead of a value.

The pairs, in words:

| pair | conduct day | reading day | what the pair is |
|---|---|---|---|
| P01 | 1 Jun 2011 | 1 Aug 2012 | conduct in 2011, read before 31 October 2012 |
| P02 | 1 Jun 2011 | 31 Oct 2012 | conduct in 2011, read on 31 October 2012 |
| P03 | 1 Jun 2011 | 1 Nov 2012 | conduct in 2011, read on 1 November 2012 |
| P04 | 1 Jun 2011 | 1 Jan 2020 | conduct in 2011, read in 2020 |
| P05 | 31 Dec 2010 | 1 Aug 2012 | conduct in 2010, read before 31 October 2012 |
| P06 | 31 Dec 2010 | 1 Nov 2012 | conduct in 2010, read after 31 October 2012 |
| P07 | 1 Jun 2011 | 30 Oct 2012 | read the day before it was published |
| P08 | 30 Oct 2012 | 1 Nov 2012 | conduct the day it was made |
| P09 | 31 Oct 2012 | 1 Nov 2012 | conduct the day it was published |
| P10 | 1 Nov 2012 | 1 Nov 2012 | conduct the day after it was published |
| P11 | 31 Oct 2012 | 30 Oct 2012 | conduct the day it was published, read the day before |
| P12 | 1 Jan 2011 | 1 Nov 2012 | conduct on the first day it is deemed to operate |
| P13 | 4 Nov 2026 | 4 Nov 2026 | conduct today, read today |
| P14 | 30 Jul 2003 | 4 Nov 2026 | conduct the day before the first deposited edition |
| P15 | 31 Jul 2003 | 4 Nov 2026 | conduct on the first day of the first deposited edition |
