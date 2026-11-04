# Broadcasting Act 1994: "broadcasting apparatus" on three time axes (forward-looking, unstable target)

**UNSTABLE-ONLY, FORWARD-LOOKING, DO NOT DEPLOY.**
This row is written for the `unstable` dialect of L4 and cannot be read by the stable build that Legalese Cloud runs (`encoding.json` says `"target": "unstable"` and `"deployable": false`).
It is not the answer of record: the stable encoding of the same facts is the row `encodings/legalese-sonnet-5.5/`, which is a different row and is not edited by this one.

## Purpose and status

The row asks what the Act's rule on "broadcasting apparatus" looks like when a rule moves on more than one time axis, using the language's own time built-ins, which `main` (build 1.6.98) rejects.
A main build cannot read it, and that is intended: the modules that use the built-ins fail on `main` with "could not find a definition" (section "The stable build", below).
It is also a test of the semantics.
The Act's First Schedule has a retrospective amendment (S 549/2012, published 31 October 2012, deemed in operation from 1 January 2011), which is the hardest real case of its kind the corpus has met.
Where the built-ins cannot say what the text says, that is recorded as a finding, with a reproducer, and the encoding is not bent to hide it.
Status: `draft`, not reviewed by a person who knows the law.
`WALKTHROUGH.md` in this folder is the raw material for a public explainer: it steps through every variant with the temporal syntax, and every excerpt and every printed result in it was copied by a script (`build-walkthrough.py`), not typed.

## What the Commons guide requires, and how this row departs from it

`docs/ENCODING-GUIDE.md` does not forbid an unstable-only row, and nine such rows are already in the tree (for example `subjects/uk/interpretation-act-1978/encodings/legalese-sonnet-5.5/`).
What it requires, and what this row does:

| the guide says | this row |
| --- | --- |
| section 1, item 2: check with the stable `l4`, "what Legalese Cloud runs, so an encoding that only a pre-release `l4` accepts cannot be deployed or used on the website" | not possible: the stable build rejects the time built-ins. The row is run on the unstable shelf build, the stable build is run on every module to record how each fails, and the row is marked `"deployable": false` for exactly this reason |
| section 5: no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`; return `NOTHING` or a constructor for a day outside the encoding | departs: the row uses `REFUSE` and `#ASSERT REFUSED` (target `unstable`, `skills/.../dialects.md`). Both are also rejected by the stable build, so `REFUSE` is a second unstable construct beyond the time built-ins |
| section 5: write `Date day month year`, never `YMD` | follows it: `YMD` is not used, so the modules without time built-ins read on the stable build |
| section 5: `@export` and `@desc` on every question | follows it: five seat questions, each with seat-worded `@desc` |
| section 5: `l4 run` on every file shows no error or warning, and assertions written equal assertions satisfied | follows it for everything but one module: 274 written, 274 satisfied, 0 errors. `sgbau-walkthrough.l4` prints 5 warnings, the five refusals of the pair "conduct 30 July 2003", which it shows on purpose |
| section 5: expected values hand-written from the text | follows it: `gen-tests-schedule.py` is the hand-written table, and `build-walkthrough.py` carries the same table extended with the edge days |
| section 10: the seat module is deployed to Legalese Cloud | does not apply until `main` has the built-ins (the section "When `main` gets the temporals") |

## The question

For conduct on day D, read as the law stands on reading day R: was the apparatus (a broadcast television receiver, a broadcast sound receiver, or a TVRO system) "broadcasting apparatus" under s 2(1), and so within s 20(1) and the s 47 penalty if the person held no licence?
"Holds a licence" and "broadcasting services are received" are plain inputs.
D and R are two plain DATE inputs on every seat question.

## The binary

- **Used for every number in this file, in `findings/` and in `WALKTHROUGH.md`:** the unstable prerelease `unstable-20261101-8e19faa`, whose `l4 --version` prints `unstable-20261101-8e19faa (unstable, 8e19faa, 2026-11-01)`.
- Its `BUILD-INFO.txt`: commit `8e19faa0dd550cd9f0f087ed083bcf7a33656f4e`, ref `unstable`, platform `darwin-arm64`, ghc 9.10.2, built 2026-11-01 02:15:05 UTC, from `legalese/l4-ide`, release `legalese/prereleases` tag `unstable-20261101-8e19faa`, run `https://github.com/legalese/prereleases/actions/runs/41264386483`.
- It was downloaded by team-lead with Meng's approval and its checksum was checked against the release's `SHA256SUMS` (the archive is 66,492,187 bytes). The `l4` in it is 162,331,360 bytes, sha256 `713a458c282c2e7768a65b444485c7665bde9b689e4fa40ba0ea4c1b63e92f9f`, and it sits in the session scratchpad, not in the repository.
- `JL4_LIBRARY_PATH` was unset for every run.
- The stable build, used for the failure evidence and for step 8 of the walkthrough: `$HOME/.cache/l4-main/98/l4`, `1.6.98 (main, 7689b0d, 2026-10-19)`.
- The tutorial's two examples were run first on the shelf build, and `gst-rate-change-example.l4` printed the values the tutorial states (9, 7, 9, 70, 90, 7, 9, 7, then today's serial number twice, 7, 7, 9, TRUE, TRUE, and two `JUST OF (DATE OF ...)`). `bna-adoption-two-axes.l4` ran and printed ten lists of booleans; I did not check them line by line against the tutorial.
- `@effective` and `@repealed` are **not** in this build (finding 1).

**Footnote: the dev build the row was first written on.**
The first runs were on `/Users/mengwong/.local/bin/l4`, which is a symlink (dated 28 Sep 2026) to `~/.cabal/bin/l4`, which is a symlink (dated 1 Nov 2026 10:24) to the store binary `/Volumes/transcend/caches/cabal/store/ghc-9.10.3-fe9c/jl4-0.1-ebe709e8/bin/l4`.
That file is 246,639,728 bytes, dated 1 Nov 2026 10:24, sha256 `25a091f450fd99d12a4ee9e4731721c0c03c13d75c14eb11dbe04392931aa051`, and `l4 --version` prints only `dev`.
The brief said it was "installed on 28 Sep 2026"; 28 Sep is the date of the first symlink, and the file it resolves to is dated 1 Nov.
**Dev against shelf: no difference.** All 34 files of the row (the 11 modules, the 14 findings reproducers, the 6 alternative ways and the 3 probes), and also the tutorial's two examples and six early probes kept outside the repository, were run on both builds, and the normalised diagnostics (range, severity, the first lines of each message) are identical on every one.
So no finding in this file depends on which of the two builds was used (`findings/shelf-vs-dev.out`, section "Findings on the semantics").

## What is encoded, and what is not

The row encodes one chain: **s 2(1) "broadcasting service" and "broadcasting apparatus" -> s 20(1)(a)-(c) -> s 47**, with the First Schedule in each of its two texts, and S 549/2012 cl 1-2, which moves from the first to the second.
Everything else in the Broadcasting Act is out of this row's scope.

| provision | status | where |
| --- | --- | --- |
| s 2(1) "broadcasting service" | encoded | `sgbau-act.l4` |
| s 2(1) "broadcasting apparatus" (both limbs: capable of reception; specified in the First Schedule) | encoded | `sgbau-act.l4` |
| s 2(1) "broadcasting apparatus licence" and "licensee" | out of scope (a licence is a plain input) | |
| s 20(1)(a), (b), (c) and the closing words "except under and in accordance with a licence" | encoded | `sgbau-act.l4` |
| s 20(2) (form, period and terms of a licence) | out of scope | |
| s 20(3) (armed forces and the like) and s 20(4) (exemptions by the Authority, which the Exemption Orders use) | out of scope; the stable row has them | |
| s 47 (fine up to $40,000, imprisonment up to 3 years, forfeiture) | encoded | `sgbau-act.l4` |
| First Schedule, three-item text (items 1 to 3 and their three definitions), 2003 and 2012 Revised Editions | encoded | `sgbau-sched-three-items.l4` |
| First Schedule, one-item text (TVRO system), as substituted by S 549/2012 cl 2 and as in the Act today | encoded | `sgbau-sched-s549.l4` |
| S 549/2012 cl 1 (deemed operation from 1 January 2011); first publication 31 October 2012, 5.00 pm; made 30 October 2012 | encoded as three DATEs | `sgbau-sched-s549.l4` |
| Which text governs conduct on D read on R | encoded | `sgbau-first-schedule.l4` |
| Legislative History entries 15 and 20 (the 2003 edition's operation date; S 549/2012's commencement) | quoted and used | `sgbau-first-schedule.l4` |
| S 549/2012 preamble: the power it is made under, s 65 of the Act | out of scope; whether s 65 can authorise a retrospective commencement is not asked | |
| Second, Third and Fourth Schedules; every other section; the TVRO System Regulations 1991 (deposited as a subject beside this one) | out of scope | |

## Sources

All quotations are in `-- src:N | text` lines with `@ref` locators, and are checked by `srcrefs.py`.
There are four raw files, in three directories, and `srcrefs.py` resolves `src:ID:N` only to a file beside the raw file it is given, so each module is checked against one raw file:

| module | raw file passed to `srcrefs.py check --strict` |
| --- | --- |
| `sgbau-first-schedule.l4`, `sgbau-act.l4` | `../../registers/source-bundle/BA1994.txt` (SSO consolidation, version in force from 25/9/2024) |
| `sgbau-sched-three-items.l4` | `../../registers/source-bundle/BA1994.20120831.txt` (Revised Edition 2012, 31 August 2012), with the Revised Edition 2003 (31 July 2003, `BA1994.20030731.txt`) quoted as `src:BA1994.20030731:N` |
| `sgbau-sched-s549.l4` | `../../../broadcasting-amendment-of-first-schedule-notification-2012/registers/source-bundle/BA1994-S549-2012.txt` |

The Gazette texts are `pdftotext -layout` renderings, which their `.meta.json` files say are an aid and not prima facie evidence; the PDF is the source.
The three editions of s 2(1), s 20(1) and s 47 were read side by side on 2026-11-03 and differ only in drafting ("no person shall" and "a person must not", "his" and "the person's"); the line numbers are in the header of `sgbau-act.l4`.
That comparison is by eye and is not a gate.

## Seat

The seat is the individual to whom the law is applied: someone who owns a television, a radio or a satellite dish and asks what the Act required of them.
`sgbau-seat.l4` is the seat layer: five `@export` questions, grouped under four `§` headings in the order a person would ask them (licence needed; offence and fine; which text applied; over a period).
**Every question that is about a receiver takes the kind of receiver as a plain input**, `television`, `radio` or `satellite dish`, so the answer shows for each.
The kind maps to the facts the First Schedule's words turn on: `television` to "broadcast television receiver" (used for the visual and aural reception of a broadcasting service), `radio` to "broadcast sound receiver", item 2 of the Revised Edition 2012 and deleted by S 549/2012 (used for the aural reception), and `satellite dish` to "TVRO system" (capable of direct reception from a satellite).
The Act's item does not separate AM from FM, and the encoding does not either.
A wrong kind is refused at the boundary: through `l4 batch`, `toaster` came back as an error naming the three allowed values.
A person with a television connected to a dish asks twice, once for each kind.
Each kind sets the first limb of s 2(1) (capable of reception) to TRUE, so the seat can no longer express an apparatus that cannot receive a broadcasting service, which the earlier version of the seat could (it took four yes/no facts); that control now lives only in `sgbau-tests-act.l4`.
The questions are:

1. "Did I need a broadcasting apparatus licence for my television, radio or satellite dish on a given day, as the law is read on a given day?"
2. "Would having it without a licence on a given day have been an offence under section 47, as the law is read on a given day?" (shown only if the person did not hold a licence)
3. "What is the most I could have been fined under section 47 ...?"
4. "Which text of the First Schedule governed conduct on a given day, as the law is read on a given day?"
5. "Was there any day in a period on which I needed a licence ..., as the law is read on a given day?" (shown only if the person had the apparatus for more than one day or is unsure of the day)

Each takes the two dates (or, for question 5, the first and last day of the period and the reading day) as plain `DATE` inputs with seat-worded `@desc`, and pins both axes with the built-ins inside the question.
The Act's own figures ($40,000, 3 years) are not asked of the person.
The only placeholder is the `acts under and in accordance with a licence` field in questions 1 and 5, which is set to `FALSE` and which those two questions do not read (`s 20(1) requires a licence` does not look at it); each is commented in the seat module.
It was run through `l4 batch` with ISO date strings and the kind as a string (`batch/`), which is how a form would call it.

## Design: how the axes carry (D, R)

**Chosen (W1).**
The conduct day D is pinned on the **valid-time** axis (`EVAL UNDER VALID TIME`), and `RULES EFFECTIVE DATE` follows it by the documented fallback (the presumption against retroactivity).
The reading day R is pinned on the **system-time** axis (`EVAL AS OF SYSTEM TIME`), and `TODAY` reads it.
Each **version of the text carries both of its own dates**: the day it is deemed to operate from, compared with `RULES EFFECTIVE DATE`, and the day it was first published, compared with `TODAY`.
S 549/2012 applies only if both hold: conduct on or after 1 January 2011, and a reader on or after 31 October 2012.
Reasons for choosing it:

- **It is isomorphic to the instrument.** The Notification says in cl 1 that it is deemed to operate from 1 January 2011, and its front matter says when it was first published; each date is beside the text it dates, and each is checked against one quotation.
- **The gate cannot be bypassed.** It is inside the version, so any caller that reaches the rule gets it (W3 below does not have this property).
- **It composes** with `EVER BETWEEN`, `ALWAYS BETWEEN`, `WHEN LAST`, `WHEN NEXT` and `VALUE AT` (tests in `sgbau-tests-axes.l4`) and across `IMPORT`.
- **It fails loudly outside the sources:** `REFUSE`, never `FALSE`.

What it costs: the dispatcher reads two axes, the publication date is a second constant per version that the language does not know is special, and the caller must pin both axes (findings 2 and 6).

**Alternatives tried, and kept in `findings/`.**

| design | what it is | result |
| --- | --- | --- |
| W2 | pin the rule-effective axis to D directly (`EVAL UNDER RULES EFFECTIVE AT`), or both, instead of valid time | identical answers on every cell tried (`sgbau-tests-axes.l4`, first block, (a) to (d)); the difference is only whether "the text at D" is the default or is asserted, and an explicit rule-effective pin beats a valid-time pin in either nesting |
| W3 (`findings/alt-w3-selector.l4`) | the version reads `RULES EFFECTIVE DATE` only; a selector outside moves the date the text is read at (a reader before publication reads 2011 conduct "as at 31 December 2010") | same as W1 for one day; **wrong over a period**, because `ALWAYS BETWEEN` and its siblings re-stamp the rule-effective axis for each day and overwrite the selector's clamp (finding 9); and a caller who reaches the version rule directly bypasses the selector, silently |
| W4 (`findings/alt-w4-version-table.l4`) | the versions as data: rows with `operates from` and `published on`; one rule reads both axes once and takes the latest-operating published row | same answers as W1; shorter to extend; less isomorphic; and "latest operating date wins" is a tie-break the Act does not state |
| reverse mapping | rule-effective axis = R, valid time = D | cannot be written: valid time has no reader, so D is unreachable inside a rule (finding 3) |
| same-named versioned rules with `@effective` / `@repealed` | the legislative authoring style | not in this build (finding 1) |

### What each axis does and does not give you

- **Valid time** (`EVAL UNDER VALID TIME`): carries the conduct day. It has no reader of its own; it is observable only through the fallback of `RULES EFFECTIVE DATE` (and through the ledger, which this row does not use).
- **Rule-effective time** (`RULES EFFECTIVE DATE`, `EVAL UNDER RULES EFFECTIVE AT`): carries "which version of the text". Its fallback chain is explicit pin, else valid-time pin, else system-day. A retrospective version can be given a rule-effective date earlier than the day it became known; nothing prevents it and nothing marks the gap (finding 5).
- **System time** (`TODAY`, `NOW`, `EVAL AS OF SYSTEM TIME`): carries the reading day. Inside a version `TODAY` is the pin, whatever the other axes say (`sgbau-tests-axes.l4`, "Which axis each of the two helper rules reads"). It takes a `DATE` only. It also feeds the rule-effective axis when neither of the others is pinned (finding 2).
- **What the case needs that no built-in offers:** a **publication-time** (or knowledge-time) axis, so that a version can say "I operate from D1 and I am known from D2" once, and the language can do the lookup. Today that second date is a hand-written constant compared with `TODAY` (finding 5).

## Tests, from the text

The expected values for the conduct-day by reading-day table were written **by hand, as data, in `gen-tests-schedule.py`, from the text of the sources, at 23:31 on 2026-11-03, before the stable row's schedule modules were read** (read at 23:46).
The file `sgbau-tests-schedule.l4` is generated from that table and is not edited.
The table, with 1 = the three-item text, 2 = the TVRO-only text:

| conduct on | read 1 Aug 2012 | read 31 Oct 2012 | read 1 Nov 2012 | read 3 Nov 2026 |
| --- | --- | --- | --- | --- |
| 31 Dec 2010 | 1 | 1 | 1 | 1 |
| 1 Jan 2011 | 1 | 2 | 2 | 2 |
| 1 Jun 2011 | 1 | 2 | 2 | 2 |
| 30 Oct 2012 | 1 | 2 | 2 | 2 |
| 31 Oct 2012 | 1 | 2 | 2 | 2 |
| 1 Nov 2012 | 1 | 2 | 2 | 2 |
| 3 Nov 2026 ("today", pinned) | 1 | 2 | 2 | 2 |

Under text 1 a television set, a radio set, a satellite dish system and a television set with a dish are all specified; under text 2 only the dish system and the television set with a dish are.
The dish system is the control: it is TRUE in every covered cell.
Conduct before 31 July 2003, or a reader before it, is not covered: the answer is `REFUSE`.

| module | assertions | what |
| --- | --- | --- |
| `sgbau-tests-schedule.l4` | 149 | the table above, 28 cells x (the version + 4 apparatus) = 140, and 9 more at the edges of coverage (the day before the first deposited edition, the first covered day, a reader before it) |
| `sgbau-tests-act.l4` | 42 | s 2(1) limbs, s 20(1)(a), (b), (c), the licence exception, s 47's fine, imprisonment and forfeiture, under each text, and the two witnesses for the Notification's commencement |
| `sgbau-tests-axes.l4` | 29 | the pins, their order, explicit rule-effective pin beating valid-time pin, what each helper rule reads, the deep pin through `JUST` and `LIST`, the interval built-ins |
| `sgbau-tests-seat.l4` | 54 | the five seat questions, for a television, a radio and a dish owner and for a set that receives nothing, including the radio at the same days as the television |
| `sgbau-walkthrough.l4` | 0 | no assertions: the directives that `WALKTHROUGH.md` shows (section "The walkthrough") |

`check.sh`, run on the shelf build with `L4=<shelf l4> L4_TARGET=unstable` (so the main comparison is skipped), printed:

```
module                                    errors satisfied  failed  refused  expected
sgbau-act.l4                                   0         0       0        0         0
sgbau-first-schedule.l4                        0         0       0        0         0
sgbau-nouns.l4                                 0         0       0        0         0
sgbau-sched-s549.l4                            0         0       0        0         0
sgbau-sched-three-items.l4                     0         0       0        0         0
sgbau-seat.l4                                  0         0       0        0         0
sgbau-tests-act.l4                             0        42       0        0         0
sgbau-tests-axes.l4                            0        29       0        0         0
sgbau-tests-schedule.l4                        0       149       0        0         0
sgbau-tests-seat.l4                            0        54       0        0         0
sgbau-walkthrough.l4                           0         0       0        0         0
TOTAL (11 modules)                             0       274       0        0
```

No assertion is expected to fail, and none does.
A failing test would have been a finding; the harness can fail, which was shown by changing the code and reading `check.sh`'s failed column (assertions failed, act / axes / schedule / seat):
dropping the reading-day gate, 12 / 10 / 18 / 11;
moving the commencement from 1 January 2011 to 31 October 2012, 9 / 9 / 27 / 12;
moving the publication day from 31 October to 1 November 2012 (the day-granularity edge), 0 / 0 / 18 / 3;
leaving the licence test un-negated, 8 / 0 / 0 / 10;
taking the aural fact away from the radio kind in the seat, 0 / 0 / 0 / 7.
`srcrefs.py check --strict` printed `0 problems` for each module against its raw file (31, 15, 5 and 32 quote lines), and a deliberately altered quote failed it.
`l4 check` prints no "is at the end of the file" or "follows code on its line" warning on any module.
`l4 run` prints no warning on any module except `sgbau-walkthrough.l4`, which prints five: the refusals of its pair "conduct 30 July 2003", which are shown on purpose.
The whole row runs in about 30 seconds.

## Findings on the semantics

Each has a reproducer in `findings/` and its printed output beside it (`run-findings.sh` regenerates them; the clock is pinned with `--fixed-now`).
Sorted into loud (an error or a warning) and silent (exit 0, a wrong answer):

| # | finding | loud or silent | reproducer |
| --- | --- | --- | --- |
| 1 | `@effective` and `@repealed` do not exist in this build: two warnings "Unknown annotation ... ignored", then an error "multiple definitions for the identifier `rate`". The tutorial and the design spec say they are planned. On the stable build `@effective` is worse: a lexer error that stops the whole file. | loud | `f01-no-effective-decorator`, `alt-decorators` |
| 2 | Pin only the reading day and `RULES EFFECTIVE DATE` becomes the reading day: the law in force on R is applied to the conduct, with no diagnostic. | **silent** | `f02-system-pin-moves-the-rule-date` |
| 3 | Valid time has no reader of its own (`VALID TIME` is not an identifier). With the rule-effective axis pinned to R and valid time to D, D cannot be read anywhere. So D and R can both be read inside a rule only if D rides on the rule-effective axis and R on system time. | loud for the name; **silent** for the effect | `f03-valid-time-has-no-reader`, `f03b-no-valid-time-name` |
| 4 | `EVAL AS OF SYSTEM TIME` takes a `DATE`, not a `DATETIME`, so the Gazette's "5.00 pm" cannot be pinned. A date pin is 00:00 UTC: in Singapore `NOW` is then 08:00 that day, and with `TIMEZONE` west of UTC `TODAY` reads the day before (30 Oct for a pin of 31 Oct in Los Angeles). | loud (the type error); **silent** (the time zone) | `f04-system-pin-is-a-date`, `f04b-...`, `f04c-system-pin-los-angeles` |
| 5 | There is no publication-time axis. A retrospective version given its deemed commencement as its rule-effective date is applied to a reader who could not have known of it (the 1 Aug 2012 reader is told a television was not scheduled for June 2011). The fix is a second date in the rule, compared with `TODAY`. The encoded-time axis has a writer and no reader, and means something else (`RULES ENCODED DATE` is not an identifier); and the rule-version field `tcRuleVersionTime`, which one might hope carries publication, is written (`TemporalContext.hs:97`) and never read in the l4-ide tree at `8e19faa0d` (a grep of `jl4-core/src` at commit `8e19faa0d`, the commit the shelf build was built from). A gate on `NOW` against 5.00 pm gives the opposite answer to the date gate for the whole of 31 October 2012. | **silent** (a); loud (b) | `f05-no-publication-axis`, `f05b-...`, `f05c-gate-on-now-...` |
| 6 | A caller that pins the conduct day and forgets the reading day reads the machine's clock: the same file printed TRUE under a clock of 1 Aug 2012 and FALSE under 3 Nov 2026. | **silent** | `f06-unpinned-reading-day-is-the-wall-clock`, `f06-two-clocks.out` |
| 7 | A time built-in written **directly** as a constructor argument or record field (`Stamp WITH d IS TODAY`, `JUST TODAY`, `LIST TODAY`, `Stamp WITH d IS RULES EFFECTIVE DATE`) escapes the pin and reads the ambient clock, although the pin is documented as deep and a named rule in the same place is pinned. This is not one of the four documented boundaries of the deep pin (closures, obligations, the depth budget, the back-edge arm; `TEMPORAL-RULE-VERSION-DESIGN.md` section 1.4.1), so I read it as a defect in this build; that is for the language designers to confirm. The row always names each built-in in a rule first (`the day the law is read`, `the day whose text governs`). | **silent** | `f07-bare-builtin-escapes-the-pin` |
| 8 | `TODAY` needs a `TIMEZONE` in the module that evaluates, not in the module that defines the rule; an importing module without one gets an error at each directive. Every evaluating module of the row declares `Asia/Singapore`, which is east of UTC, so finding 4's day shift does not occur here. | loud | `f08a`, `f08b-timezone-of-the-evaluating-module` |
| 9 | Applying the reader's knowledge outside the version (W3) is right for one day and wrong over a period, because the interval built-ins re-stamp the rule-effective axis per day; it can also be bypassed. | **silent** | `alt-w3-selector` |

**Each of the nine findings reproduces on the shelf build exactly as on the dev build.**
`findings/compare-builds.sh` runs every reproducer on both and compares what each diagnostic says (range, severity, the first lines of its message); its output, `findings/shelf-vs-dev.out`, is 25 comparisons (the 14 reproducers, the six alternative ways, the three probes, and finding 6 under two clocks), 25 identical and none different.
So there is no finding of its own about a difference between the builds.

What worked, so the list is not only complaints:

- the pins compose across `IMPORT`, and `TODAY` inside an imported module reads the importer's pin;
- the deep pin holds through `JUST`, `LIST` and a record whose field is a named rule (finding 7 is the exception);
- `EVER BETWEEN`, `ALWAYS BETWEEN`, `WHEN LAST`, `WHEN NEXT` and `VALUE AT` step the conduct day and leave the reading day alone, which is what a period question needs;
- `REFUSE` propagates through all of them, so a period that reaches back before the first deposited edition refuses;
- the seat runs through `l4 batch` with ISO date strings, and a refusal comes back as `refused` with its reason.

## Forks, choices and assumptions

Nothing here is ruled by Meng or a domain expert; each is a choice taken, with the reading not taken.

1. **"Specified in the First Schedule" qualifies the whole of "apparatus capable of or designed or constructed for the reception of any broadcasting service" (reading A).** The other reading attaches "specified in the First Schedule" only to "designed or constructed for", so that any apparatus capable of reception would be broadcasting apparatus whatever the Schedule says, and S 549/2012 would be inert for it. The stable row names the same fork (its F-BA-01) and takes reading A too; I did not examine it further, and I noticed it from its file after writing mine.
2. **Day granularity.** The Gazette says 5.00 pm on 31 October 2012; a `DATE` axis has no time of day. A reader on 31 October 2012 is counted as reading after publication ("on or after", as the brief says). This is a convention, not a reading of the text. A reader at 10.00 am that day, in fact, still had the old law (finding 4 and finding 5, `f05c`).
3. **Publication, not making.** The gate is the first publication (31 October 2012), not the day the Notification was made (30 October 2012). The sources do not say whether a Notification is effective before it is published; that is for the general law of subsidiary legislation, which is not in the sources.
4. **A reading day before the conduct day is answered, not refused.** "Conduct on 3 November 2026, read on 1 August 2012" answers with the law as it read on 1 August 2012 (the three-item text), applied to a day still to come. It does not say the law would not change before then. The seat's `@desc` and header say so.
5. **A day outside the sources refuses.** Conduct before 31 July 2003 (the 2003 Revised Edition's operation date, BA1994.txt:4602-4604), or a reader before it, gives `REFUSE`. The Act existed earlier (as the Singapore Broadcasting Authority Act 1994, Act 15 of 1994); its First Schedule then was not deposited. The 2003 edition is the first deposited edition.
6. **The first limb is asked last in the text and first in the code.** Each rule asks "is it specified in the First Schedule that governs" first, so that a day outside the sources refuses even for an apparatus that fails the other limb; AND is commutative, so the answers are unchanged where the sources cover the day.
7. **The three apparatus kinds are not exclusive.** A television set is "used for the visual and aural reception"; its sound is aural reception too, so on a literal reading it also fits "broadcast sound receiver". The test table sets the television set's aural-use fact to FALSE so that kinds stay apart; either setting gives the same answer under the three-item text.
8. **Facts the person can state.** The Schedule's definitions are worked out from four facts about the apparatus (capable of reception; used for aural reception; used for visual and aural reception; capable of direct satellite reception) and the s 2(1) service definition from four facts about what is received. "Equipment appropriate", "programme" and "for reception" are asked as one plain yes/no each.
9. **`Date day month year`, not `YMD year month day`.** The unstable build has `YMD`; `main` 1.6.98 does not, and the Commons guide says to write `Date`. Keeping `Date` means that the modules without time built-ins read on `main`, and in the others what `main` rejects is the time built-ins and `REFUSE`, not also `YMD`.
10. **s 20(3), s 20(4) and the Exemption Orders are out of scope**, so a person within s 20(3) or exempted under s 20(4) is not recognised; "holds a licence" is the only way out of s 20(1) here.
11. **A radio is a "broadcast sound receiver", and AM and FM are not told apart.** The seat's `radio` kind maps to item 2 of the three-item text; the Act's item does not separate AM from FM and neither does the encoding. Whether a plain FM or AM radio is exempt from licensing in general is not answered: the exemptions are out of scope (fork 10), so the encoding says only what the First Schedule's list says.
12. **The kind of receiver is one choice from three.** A person with a television connected to a satellite dish asks twice, as `television` and as `satellite dish`; the encoding does not have a kind for the two together, though its records could carry both facts (`gen-tests-schedule.py` and `sgbau-tests-schedule.l4` test a television set with a dish).
13. **"Today" in the walkthrough is the day it was built** (the Singapore date at build time), written into the questions so that every printed result is reproducible; the one directive that leaves the reading day to the clock is marked as such.

## The walkthrough

`WALKTHROUGH.md` is the raw material for a public explainer's sidebar, requested after the row was first written.
It is generated by `build-walkthrough.py` from `walkthrough-template.md`, with `L4=<shelf l4> L4_MAIN=<stable l4> python3 -I build-walkthrough.py`.
What the script does:

- It writes a block of `#EVAL` directives, one for each of 15 pairs of (conduct day, reading day), into `sgbau-walkthrough.l4` and into each alternative-way file in `findings/`.
- It runs `l4 run` on each file and keeps what was printed, by file and line, and runs the stable build on the probe files.
- It copies code excerpts from the modules with their line numbers, copies each directive's printed result, and copies the stable build's diagnostics verbatim. No result is retyped.
- It compares each printed value with the hand-written expectation for the pair, marks the rows that differ, and **stops if a claim of the top section is false** (the claims of the top section and the results of steps 7 and 8 are checked, for example that the way written without a reader gate tells a reader before 31 October 2012 the new text, and that the stable build does not know four of the five clock words).
- The claims are about what the build printed on this day; a different build may print something else and the script then stops, which is the point.

The eight ways, with the result of each on the 15 pairs (the table is in the walkthrough, and was last built with the shelf build):
W1 (chosen) and W2, W4 print the hand-written expectation on every pair;
W0 (no reader gate) is wrong for the three pairs where the reader is before 31 October 2012 and the conduct is on or after 1 January 2011;
W3 (selector) is right for one day and wrong over a period;
W1-NOW (the gate on the Gazette's hour) differs on the pair where the reader is on 31 October 2012;
the reverse mapping is wrong for conduct before 1 January 2011 read after publication, and at the edge of coverage (it cannot see the conduct day);
the decorators print no value, because the build rejects the file.
The walkthrough takes the notification as the text states it: it does not decide whether a retrospective notification is valid.

## The stable build

Every module was run once on `1.6.98 (main, 7689b0d, 2026-10-19)` with `JL4_LIBRARY_PATH` unset (`findings/run-on-main-build.sh`, output in `findings/main-build-per-module.out`).
The three modules without time built-ins or `REFUSE` (`sgbau-nouns`, `sgbau-sched-three-items`, `sgbau-sched-s549`) read on main (0 errors).
The rest fail, and the failure is "I could not find a definition for the identifier", for these names:

| module | errors | identifiers not found |
| --- | --- | --- |
| `sgbau-nouns`, `sgbau-sched-s549`, `sgbau-sched-three-items` | 0 | none |
| `sgbau-first-schedule` | 3 | `REFUSE` (x2), `RULES EFFECTIVE DATE` (x1) |
| `sgbau-act` | 9 | `REFUSE` (x6), `RULES EFFECTIVE DATE` (x3) |
| `sgbau-seat` | 19 | `REFUSE` (x6), `EVAL AS OF SYSTEM TIME` (x5), `EVAL UNDER VALID TIME` (x4), `RULES EFFECTIVE DATE` (x3), `EVER BETWEEN` (x1) |
| `sgbau-tests-act` | 22 | `REFUSE` (x6), `EVAL UNDER VALID TIME` (x5), `EVAL AS OF SYSTEM TIME` (x5), `REFUSED` (x3), `RULES EFFECTIVE DATE` (x3) |
| `sgbau-tests-axes` | 63 | `EVAL AS OF SYSTEM TIME` (x28), `EVAL UNDER VALID TIME` (x14), `EVAL UNDER RULES EFFECTIVE AT` (x8), `REFUSE` (x2), and one or two each of `WHEN NEXT`, `WHEN LAST`, `VALUE AT`, `EVER BETWEEN`, `ALWAYS BETWEEN`, `RULES EFFECTIVE DATE` |
| `sgbau-tests-schedule` | 13 | `REFUSED` (x6), `REFUSE` (x2), `EVAL UNDER VALID TIME` (x2), `EVAL AS OF SYSTEM TIME` (x2), `RULES EFFECTIVE DATE` (x1) |
| `sgbau-tests-seat` | 27 | `REFUSED` (x8), `REFUSE` (x6), `EVAL AS OF SYSTEM TIME` (x5), `EVAL UNDER VALID TIME` (x4), `RULES EFFECTIVE DATE` (x3), `EVER BETWEEN` (x1) |
| `sgbau-walkthrough` | 43 | `REFUSE` (x20), `RULES EFFECTIVE DATE` (x10), `EVAL AS OF SYSTEM TIME` (x6), `EVAL UNDER VALID TIME` (x5), `EVER BETWEEN` (x1), `EVAL UNDER RULES EFFECTIVE AT` (x1) |

`REFUSE` and `REFUSED` are a second unstable construct (`dialects.md`); the smallest file that uses the time built-ins and nothing else unstable is `findings/f09-stable-build-temporal-only.l4`, and on main it fails for `RULES EFFECTIVE DATE`, `EVAL UNDER RULES EFFECTIVE AT`, `EVAL UNDER VALID TIME` and `EVAL AS OF SYSTEM TIME` alone (`findings/f09-stable-build-main-build.out`), with one cascading "multiple definitions for the identifier `__GEQ__`".
`TODAY` and `TIMEZONE` exist on main (`findings/walkthrough-main-probe-today.l4` printed a date), and `Date` and the date comparisons read there; the time built-ins and `REFUSE` are what do not.
One more difference, which `WALKTHROUGH.md` step 8 shows verbatim: on the stable build the decorator `@effective` is a lexer error ("unexpected '@'") that stops the whole file, where on the unstable build it is a warning and the line is ignored.

## Comparison with the stable row

Read at 23:46 on 2026-11-03, after the table above was written, and only the non-quarantined layer-1 files: `sgba-sched.l4` (mtime 22:12), `sgba-vintage.l4` (22:11), `sgba-nouns.l4` (22:22), the `s 2(1)` "broadcasting apparatus" rule in `sgba-p1-defs.l4` (mtime 23:04), the first lines of `sgba-p5-apparatus.l4` (22:17), and `sgba-tests-sched.l4`.
That folder is untracked and was still being written; what follows describes those files at those times.
At 23:46 it had **no version table for the First Schedule**: it said its past texts "were not obtained", and it encoded the one-item text only.
At 23:47 its `sgba-nouns.l4` changed (re-read at 23:56): it now declares a `First Schedule version` with `takes effect on` and `published on`, and says the version read is "the latest published on or before the reading day among those that take effect on or before the day of the conduct".
Its `sgba-sched.l4` (mtime 22:12) and `sgba-vintage.l4` (22:11) had not changed at 23:56 or at 00:19 on 4 November, so no rule module reads that table yet, and what is compared in rows 11 to 14 is its nouns file and that file's header comment, not a rule.
Neither row was edited to agree with the other.

| # | disagreement | stable row (as read) | this row |
| --- | --- | --- | --- |
| 1 | inputs | one `DATE` input, `d`, standing for both the conduct day and the day the law is read | two `DATE` inputs, one per axis |
| 2 | coverage | the text in force on `d` only for 25 Sep 2024 to 1 Oct 2026 (`sgba-vintage.l4`) | conduct and reader from 31 Jul 2003 on, with no upper edge |
| 3 | outside coverage | `NOTHING` (a `MAYBE BOOLEAN`), and its tests assert `NOTHING` for 31 Dec 2010, 1 Jan 2011, 2 Jan 2011, 1 Jun 2015, 1 Jun 2019 | `REFUSE`; the same days (and the earlier ones) are covered here and answer |
| 4 | conduct on 31 Dec 2010 and 1 Jan 2011, any reader | `NOTHING` | 31 Dec 2010: three-item text for every reader; 1 Jan 2011: three-item text for a reader before 31 Oct 2012, TVRO-only text for a reader on or after it |
| 5 | conduct on 3 Nov 2026 ("today", this row's pinned day) | `NOTHING`: the window closes on 1 Oct 2026, the date of the consolidation | answers: the TVRO-only text, so a television needs no licence and a dish does |
| 6 | the items | one item, the TVRO system | items 1 to 3 and their definitions in the three-item text; one item in the other |
| 7 | the apparatus record | two facts (capable of reception; capable of direct satellite reception), which cannot tell a television from a radio | four facts, which can |
| 8 | the retrospective notification | S 549/2012 is named in the history note and "its text was not obtained"; it is not modelled | modelled: commencement 1 Jan 2011 deemed, first publication 31 Oct 2012 |
| 9 | cells where both answer | for conduct between 25 Sep 2024 and 1 Oct 2026, read today, the one-item text: a television is not specified, a dish is | the same, in those cells |
| 10 | the fork on "specified in the First Schedule" | named (F-BA-01), reading A | reading A (noticed from that file) |
| 11 | two dates per version | (nouns, 23:47) the same model: `takes effect on` and `published on`, as a table of versions | the same two dates, held inside each version's rule (W1); W4 in `findings/` is the table form |
| 12 | which version wins when more than one qualifies | (nouns, 23:47) the latest **published** on or before the reading day, among those taking effect on or before the conduct day | W1 has no tie-break: the BRANCH takes S 549/2012 when both of its gates hold. W4 takes the latest **operating**. All three give the same answer for these two versions; they would differ for a third version published later but operating earlier |
| 13 | what carries the publication date on an unstable build | (nouns, 23:47) its comment names the rule-version axis, `tcRuleVersionTime` | system time, `TODAY`, because in the l4-ide tree at `8e19faa0d` `tcRuleVersionTime` is written (`TemporalContext.hs:97`) and a grep of `jl4-core/src` finds no reader of it; finding 5 |
| 14 | "capable of" and "designed or constructed for" | (nouns, 23:47) two separate facts, so that both readings of fork 1 can be written | one fact, `capable of or designed or constructed for`, reading A only |

The stable row was re-read for changes before this file was finished: see PROGRESS.md.

## When `main` gets the temporals

Proposed, not landed: nothing below has happened, and the list says what in this row would be deleted or renamed if it did.

1. **Nothing changes in** `sgbau-nouns.l4`, `sgbau-sched-three-items.l4` and `sgbau-sched-s549.l4`; they read on `main` today.
2. **`REFUSE`.** If `main` takes `REFUSE` and `#ASSERT REFUSED`, nothing changes. If it does not, each `REFUSE` becomes a `NOTHING` from a `MAYBE`, and the `#ASSERT REFUSED` lines become `EQUALS NOTHING` (the stable row's way).
3. **`@effective` and `@repealed`.** The two Schedule texts become two same-named rules ``the Schedule specifies the apparatus``, one with `@effective` 31 July 2003 and one with `@effective` 1 January 2011, and `the version of the First Schedule that governs`, the `Version of the First Schedule` enum, and the `CONSIDER` in `apparatus is specified in the First Schedule that governs` are deleted, if the desugar supplies the dispatcher. **The publication gate does not go away:** a decorator carries one date, so `TODAY AT LEAST (S 549/2012 was first published in the Gazette on)` stays as a hand-written condition, or the decorator needs a second date (finding 5).
4. **`YMD`.** If `main` gets `YMD`, `Date d m y` may be replaced by `YMD y m d` throughout, which refuses an impossible date instead of rolling it.
5. **A `DATETIME` system pin.** The date gate on `TODAY` could become a gate on `NOW` against the 5.00 pm, and the convention in fork 2 and the second half of finding 4 would go.
6. **The deep-pin defect (finding 7).** Fixed, the habit of naming each built-in in a rule first is unnecessary, though harmless.
7. **A valid-time reader (finding 3).** If one is added, the rule could read the conduct day and the rule-effective day separately, and the fallback in finding 2 would matter less.
8. **Unchanged:** `TIMEZONE IS "Asia/Singapore"` in every evaluating module; the seat's two pins; the tests.

## What would need doing before this is worth relying on

- Done: every number was re-run on the named shelf build (`unstable-20261101-8e19faa`), and the dev build gave no different result on any of the 34 files.
- `WALKTHROUGH.md` is raw material: whoever cuts it down for a lay reader should keep each claim tied to its step.
- A person who knows Singapore law to read the rows of the test table against the Gazette texts, and to rule on fork 3 (whether a Notification is effective before its publication) and on whether a retrospective commencement under s 65 reaches conduct in the way finding 5's reader sees it; neither is in the sources.
- Whether S 549/2012's retrospective operation matters differently for a criminal provision than for a civil one is not examined here and not asserted.
- An independent test pass (step 8 of the skill): not done.
- The stable row's version table, when it exists, to be compared again.

## Files

| file | what |
| --- | --- |
| `sgbau-nouns.l4` | the domain: Apparatus, Transmission, Conduct, the two texts of the Schedule |
| `sgbau-sched-three-items.l4`, `sgbau-sched-s549.l4` | what each text of the First Schedule says; S 549/2012's dates |
| `sgbau-first-schedule.l4` | which text governs: the only module that reads an axis directly |
| `sgbau-act.l4` | s 2(1), s 20(1), s 47 |
| `sgbau-seat.l4` | the seat layer |
| `sgbau-tests-schedule.l4` (generated by `gen-tests-schedule.py`), `sgbau-tests-act.l4`, `sgbau-tests-axes.l4`, `sgbau-tests-seat.l4` | tests |
| `findings/` | reproducers and their output (`run-findings.sh`, `run-on-main-build.sh`) |
| `batch/` | `l4 batch` rows and output for two seat questions (question 1 for a television, a radio and a dish, and an invalid kind) |
| `WALKTHROUGH.md` | the explainer's raw material: the three dates, one step per variant, every way of writing the rule, what the stable build says, and a table; generated |
| `walkthrough-template.md`, `build-walkthrough.py` | its prose, and the script that copies excerpts, printed results and diagnostics into it, and checks the claims of its top section against what was printed |
| `sgbau-walkthrough.l4` | the directives the walkthrough shows (no assertions); its last block is generated |
| `findings/alt-*.l4` | the ways of writing the rule that were not chosen, each run on the same 15 pairs of days (a generated block at the end of each) |
| `findings/walkthrough-main-probe*.l4` | the one-built-in-per-line probes for the stable build |
| `findings/compare-builds.sh`, `findings/shelf-vs-dev.out` | every reproducer on the shelf build and on the dev build, and whether they print the same |
| `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` | copied from the `encoding-a-subject` skill |
| `encoding.json`, `SOURCE-LICENSE.md`, `PROGRESS.md` | descriptor, licence note, progress |
