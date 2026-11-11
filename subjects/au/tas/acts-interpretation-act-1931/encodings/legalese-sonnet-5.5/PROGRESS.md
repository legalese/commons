# Progress: Acts Interpretation Act 1931 (Tasmania)

This file is the working state of the encoding.
It is rewritten as the work moves; it states where things stand now.

## The rulings that bind every rule

These paragraphs are copied from the brief and from `inputs/ENCODING-GUIDE.md` section 5, word for word.

A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless", a list the text closes with "only", a flat negative.
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
A period the text fixes in its own words: outside it, `JUST FALSE`.
A "where ..." condition that fails: `JUST FALSE`.
A scope limit with no "only": `NOTHING`.
Questions the rulings do not settle are decided at each site on the text's own words, with one fork line in the fork register (the provision, the function, the answer taken, the other reading).

From the guide, ruled 2026-11-05: "(a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`."
Also ruled 2026-11-05: "when", "upon" and "whenever" count as "where"; and for "the property does not pass until X" the bar is `JUST TRUE` before X and `JUST FALSE` after X.
Decided at each site, with one fork line each: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)".

## How these rulings are applied here

A rule of reading that answers `MAYBE BOOLEAN` is `JUST TRUE` when its text applies, `JUST FALSE` when the text itself says no (a failed "where", "if", "when", "upon", "until", "within", a period the text fixes, an "unless" or "only" once met), and `NOTHING` when the text is silent, the list is open, or the case is outside a scope limit that has no "only".
A rule that returns a day, a name or a value has no second not-covered value, so it returns `NOTHING` when its text does not apply.
A rule whose effect is itself negative ("is not liable", "may not be challenged") is named for that negative effect, so `JUST TRUE` means the text's no and a failed gate is `JUST FALSE`.

## State

- Layer 1: every module written, with tests, passing on both builds.
  The rulings above are applied in every module; failed "where" and "if" gates and fixed periods answer `JUST FALSE` for a yes-or-no rule, and `NOTHING` for a rule that returns a day, a name or a value.
- Layer 2: `tas-seat.l4` (22 questions, each with `@export` and `@desc`) and `tas-cases-seat.l4` (every question has at least one case, and an explicit not-covered case where it can answer `NOTHING`).
  Each question was also run through `l4 batch` with JSON inputs on both builds against the hand-derived values.
- Written: `NOTES.md` (seat, scope, jural relations, coverage table, fork register, worked-cases answer table, what the Act turns out to say, what the stable binary does not accept, what `check.sh` prints, cross-references, what is needed before reliance), `encoding.json`, `SOURCE-LICENSE.md`.
- Still to do: nothing in the brief.
  What a reviewer should do is in `NOTES.md`.

## Files

Layer 1: `tas-nouns.l4`, `tas-interpretation-time.l4` with `tas-tests-time.l4`, `tas-provisions.l4`, `tas-xrefs.l4`, `tas-terms.l4`,
`tas-ss01-04-application.l4`, `tas-ss05-07a-enactments.l4`, `tas-ss08-10a-reading-and-commencement.l4`, `tas-ss11-13-anticipatory-powers-and-citation.l4`,
`tas-ss14-18a-repeal-and-expiry.l4`, `tas-ss19-23-powers-and-appointments.l4`, `tas-ss23aa-23e-delegation-and-bodies.l4`, `tas-ss24-28-construction.l4`,
`tas-ss29a-31-units-service-and-notices.l4`, `tas-ss32-38-offences.l4`, `tas-ss38a-40a-instruments-and-notice.l4`, `tas-ss41-45-definitions.l4`,
`tas-ss46-46c-common-phrases.l4`, `tas-ss47-regulations.l4`, `tas-ss48-sch1-rules-of-court-and-transitional.l4`.

Layer 2: `tas-seat.l4`, `tas-cases-seat.l4`.

## Decisions taken so far

The decisions that read the text two ways are kept in `NOTES.md` under the fork register.
