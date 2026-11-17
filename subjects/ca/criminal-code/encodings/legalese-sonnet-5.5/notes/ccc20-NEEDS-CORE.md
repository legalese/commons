# NEEDS-CORE.md -- part agent ccc20 (Criminal Code (Canada), Part XVI, ss 493 to 529.5)

Each item is a type or constructor the keel's `ccc-core.l4` lacks and that this part needed.
The part did not edit the core; where a constructor was missing it declared a small type of its own, with the section label first, and uses that.
Checked against `ccc-core.l4` as supplied to this run: `grep -n -i -E 'custody|any one|private'` returns only the outcome `detention in custody` (line 141) and a comment (line 154), and the `Party` list (lines 49 to 85) has no private arrester and no custodian.

1. **An hours unit for `Length of time`.**
   `Length of time` (ccc-core.l4, line 174) has `years`, `months`, `days` and `less a day`, and no hours.
   Section 503(1)(a) and (b) count a period of 24 hours (and s 503(2) says when it begins).
   The part takes the 24 hours as a plain `NUMBER` of hours in `s 503(1) the person was taken before a justice as paragraph (a) or (b) requires` and `s 503(2) the hours that run against the 24-hour period` (ccc20-part16-taking-before-justice.l4).
   Wanted: an `hours` field (or a `Length of time` constructor in hours) so that the 24 hours can be a `Length of time`.

2. **A `Party` for "any one other than a peace officer" who arrests.**
   Section 494(3): "Any one other than a peace officer who arrests a person without warrant shall forthwith deliver the person to a peace officer."
   `Party` has `a peace officer` and no constructor for a private arrester.
   The part declares `s 494(3) the actor` and `s 494(3) the act` (ccc20-part16-arrest.l4, lines 77 and 81) for the regulative rule, so the rule's actor is local to this part.
   Wanted: a `Party` constructor such as `a person who is not a peace officer`.

3. **A `Party` for "the person having the custody of an accused".**
   Section 525(1) puts a duty on "the person having the custody of an accused", and s 527(3) addresses an order to "the person who has custody of the prisoner".
   `Party` has `the keeper of a prison` and no constructor for whoever has custody.
   The part declares `s 525(1) the actor` and `s 525(1) the act` (ccc20-part16-failure-and-delay.l4, lines 514 and 517) for the regulative rule.
   Wanted: a `Party` constructor such as `the person having the custody of an accused`.
