# NEEDS-CORE -- ccc4 (Criminal Code of Canada, lines 1904-2381)

What this part defines in its own module because the core lacks it, so that the lead can hoist it at the merge (PLAN section 1: "A type or constructor the core lacks is defined in the part's own module under its own prefix and recorded in `NEEDS-CORE.md`").
Status 2026-11-16: read from `ccc4-s99-108-trafficking-and-others.l4` and the core `ccc-core.l4`; nothing here is planned work.

## Constants of type `Length of time`

The core has `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years` and `fourteen years` (`ccc-core.l4:208-214`) and has no three-year or one-year constant.
This part needs two, and defines them under its own prefix (`ccc4-s99-108-trafficking-and-others.l4:19` and `:23`):

| name in this part | definition | used by |
| --- | --- | --- |
| `s 99(2) three years` | `Length of time` OF 3, 0, 0, FALSE | the minimum punishment of a first offence in s 99(2), s 100(2) and s 103(2) |
| `s 102(2) one year` | `Length of time` OF 1, 0, 0, FALSE | the minimum punishment in s 102(2)(a) |

If the core gains `three years` and `one year`, the two names above can be deleted from this module and the callers renamed; until then they stay, and nothing else in the module depends on them.

## Types

This part declares 22 types of its own in layer 1 (7 in `ccc4-s84-definitions.l4`, 1 in `ccc4-s85-98-use-possession.l4`, 2 in `ccc4-s99-108-trafficking-and-others.l4`, 12 in `ccc4-s109-110-3-prohibition-orders.l4`), each named with its section label (for example `s 84(1) kind of thing`, `s 109 act of the court or of a justice`), and one in the seat layer (`ccc4 seat: the penalty of the offence`).
None is asked of the core.

## A function PLAN expects of this part and this part did not write

`s 110.1 an emergency prohibition order has been made` (PLAN section 6, ccc4 row: ss 110.4 to 113, ccc5, ask for it, `MAYBE BOOLEAN`).
It is not defined here; see "Seams (ccc4)" in `NOTES.md` for what is written instead and why the lead should join it at the merge.
