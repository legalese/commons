# Skills and Workforce Development Agency Act 2026 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions as shown in the example rows, and nothing else. No pipeline, no coverage
table, no independent test pass, no human gate.

**Edition:** Act No. 17 of 2026, informal consolidation, "version in force from
1/7/2026" per the page footer of the deposit (`SWDAA2026.txt`, retrieved 1 October
2026). The deposit annotates no amendments and carries no legislative history. Section 1
leaves commencement to a Gazette notification whose date the deposit does not give.

**Checks:** one case file, 53 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This row answers **REQ-0218** in `subjects/sg/requirements.jsonl`. That is Tier 3 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks what
the Act decides for a person or business it applies to, and no scenario has yet asked a
sharper question.

Most of the Act sets up the Agency that takes over from SkillsFuture Singapore and
Workforce Singapore: ss 67-71 transfer their staff and records, and ss 73-74 repeal their
Acts. People and businesses meet it in Parts 7 and 8: training grants and their
abuse, course advertising, refunds when a funded course collapses, appeals, punishments,
officers' liability and service of documents. This row covers ss 49-56, 58-61 and 64,
plus the maximum punishments in ss 8(2) and 35(2) so that the composition cap can be
set across every offence in the Act.

Not encoded:
- the Agency's constitution, functions, staff and finance (Parts 2 to 6), apart from the
  punishments in ss 8(2) and 35(2);
- the verification and inspection powers of ss 46-48, beyond the obstruction offence;
- the partnership and association mirror of s 61 (s 62);
- codes of practice (s 66);
- the transfers, repeals and consequential amendments (Parts 9 to 11).

## What the Act turns out to say

### 1. A trainee who just attends the course can be the offender

Under s 50(5)(c), a person "facilitates" an abusive funding arrangement if, "by
attending a course or programme", the person "participates in, enables or aids" it. A
marketing agent who promotes it is caught by (d). Under s 50(1), facilitating is as much
an offence as entering into the arrangement. Section 50(6) excludes only carriers, network
and online-service providers, and messaging or publishing platforms, and only when they
act "in the ordinary course of business". Asserted.

### 2. Intent is presumed, and getting nothing is no defence

Section 50(7) presumes the dishonest intent "until the contrary is proved" whenever the
arrangement involves any step "capable of assisting" anyone to obtain the funding.
Section 50(8) says it is no defence that the accused obtained nothing. Knowledge or reason
to believe that the arrangement is abusive still has to be shown. Asserted.

### 3. The penalty for an abusive arrangement is the money itself, on top of the fine

On conviction under s 50(2)(a), the person "shall ... pay a penalty equal to the amount of
wrongly obtained funding" they obtained "or would have obtained". Under s 50(3) it does
not matter who benefited. On top of that comes a fine of up to $10,000, imprisonment of
up to 3 years, or both. Separately, s 51 lets the court order the funding repaid to the
Agency as a judgment debt. Read together, these suggest (an inference; the text does not
say so directly) that a facilitator could both pay a penalty equal to the funding and be
ordered to repay it. Section 49(3) nets off whatever would have been obtained without the
arrangement. Asserted, with the floor at zero marked as an inference.

### 4. The composition cap is $2,000 for every offence a business meets

Under s 60, composition cannot exceed the lower of half the maximum fine and $2,000. Every
offence in Part 7 (ss 50-59), and the misuse of the Agency's symbol under s 8(2), has a
maximum fine of $5,000 or $10,000. Half of that is never below $2,000, so for those
offences the cap is always $2,000. The one exception is the secrecy offence in s 35(2),
which binds the Agency's own people: its maximum fine is $2,000, so its cap is $1,000.
Which offences are compoundable is left to regulations, which were not retrieved.
Asserted (cap only).

### 5. A cancelled course must refund what was paid before the default day, whatever the contract says

Section 54 lets the Agency direct a funded provider to refund the trainee (and to refund
the Agency's grant) when a course does not start on schedule or stops before it is
completed. The trainee must not have withdrawn "before the default day". Under s 54(9)
that is the scheduled start or the day the course stopped, so withdrawing on the default
day itself does not bar the refund. Only money received before the default day is
refundable (s 54(2)(a)). Under s 54(7), a contrary term in the contract is overridden.
The provider must get at least 14 days to make representations (s 54(3)). Section 53
(advertisements) sets no minimum. Asserted, except for the 14-day period.

### 6. The appeal window is 14 days, and the direction bites meanwhile

Under s 55(2), an appeal to the Minister must be in writing with grounds and made within
14 days after the direction is given. The Minister "may" reject a late appeal, but does
not have to. Under s 56, the decision is final, and the direction must be complied with
pending the appeal unless the Minister directs otherwise. Asserted.

### 7. Recklessness is enough for a false course advertisement

Under s 52(1), it is enough that the person "ought reasonably to have known" the
advertisement was false or misleading, or was "reckless". The six heads in s 52(4) all
tie back to the Agency or to Agency funding. A misdescription of an unfunded course by an
unfunded provider falls under none of them. Whether the list is exhaustive is not stated.
Ignoring a direction to fix an advertisement carries a further $1,000 for each day it
continues after conviction (s 53(7)(b)). Asserted.

## What would need doing before this is worth anything

- The commencement notification and any regulations (compoundable offences, a substituted
  appeal or representation period) were not retrieved.
- The day-counting convention for "within 14 days after" is assumed (day 14 is in time).
  Whether "given" in s 55(2) means the day service takes effect under s 64(5) is not
  decided here.
- Section 62 (partnerships and associations) and the inspection powers are not encoded.
- No case law was searched. Section 50(5)(c)'s reach over ordinary trainees in particular
  needs one.
