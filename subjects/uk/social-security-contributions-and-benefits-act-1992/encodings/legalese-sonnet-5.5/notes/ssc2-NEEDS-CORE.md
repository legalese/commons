# NEEDS-CORE -- ssc2

Written 2026-11-04 by part agent ssc2.
Nothing here blocks anything: each constructor below is already declared locally under the `ssc2` prefix and used, so the layer-1 files run without the core changing.
The lead can hoist them if another part needs the same constructors; if not, the local types can stay.

Checked against `ssc-core.l4` (the `DECLARE Benefit IS ONE OF` block, which starts at line 146) on 2026-11-04.

## Constructors of `Benefit` the core lacks

Section 22(2) lists the purposes for which an earnings factor is treated as derived, and four of them name a benefit or payment that is not a Part II contributory benefit.
The core's `Benefit` has no constructor for any of them.

| wanted in `Benefit` | text | used in | declared locally as |
| --- | --- | --- | --- |
| a contribution-based jobseeker's allowance | s 22(2)(a), s 22(5) (src:771, 792) | `ssc2-factors.l4` | `s 22(2)(a) establishing entitlement to a contribution-based jobseeker's allowance`, a constructor of `s 22(2) Purpose` |
| a contributory employment and support allowance | s 22(2)(a), s 22(5), s 22(8) (src:771, 792, 804) | `ssc2-factors.l4` | `s 22(2)(a) establishing entitlement to a contributory employment and support allowance`, a constructor of `s 22(2) Purpose` |
| a state pension under Part 1 of the Pensions Act 2014 | s 22(2)(c) (src:773) | `ssc2-factors.l4` | `s 22(2)(c) establishing entitlement to a state pension under Part 1 of the Pensions Act 2014, or calculating its rate`, a constructor of `s 22(2) Purpose` |
| bereavement support payment under section 30 of the Pensions Act 2014 | s 22(2)(d) (src:774) | `ssc2-factors.l4` | `s 22(2)(d) establishing entitlement to bereavement support payment under section 30 of the Pensions Act 2014`, a constructor of `s 22(2) Purpose` |

These are the only four purposes in s 22(2) that name something the core's `Benefit` cannot hold.

## A basis for the Category B retirement pension

Section 23A(1)(b) and (c) (src:819-820) apply to a Category B retirement pension only "payable by virtue of section 48A or 48AA" or "by virtue of section 48B".
The core's `Benefit` has one `Category B retirement pension` and no field for the section it is payable by virtue of.
ssc2 declares `s 23A(1) Basis of a Category B retirement pension` (`s 23A(1)(b) payable by virtue of section 48A or 48AA`, `s 23A(1)(c) payable by virtue of section 48B`, `s 23A(1) payable by virtue of another section`) and takes it as a second parameter beside the `Benefit`.
A part that encodes ss 48A to 48B is the likely second user of this distinction; the lead may prefer one hoisted type to two local ones.

## Not wanted in the core

The other types ssc2 declares (`s 21(1) Route of entitlement`, `s 21(5)(c) Paragraph that governs the year`, `s 21(5)(d) Meaning of year`, `s 22(1)(a) Pay period`, `s 22(3) Source of an earnings factor`, `s 30DD(5) Kind of payment`, `s 30E(2) Kind of allowance`, `s 39A Kind of survivor`, `s 39A Candidate`, and the `Party` and `Act` pairs of the regulative rules) belong to one provision each, and nothing outside it should need them.
