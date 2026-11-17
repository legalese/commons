# NEEDS-CORE.md -- part ccc2 (Criminal Code, lines 850-1248: Part II, ss 46 to 83)

Written 2026-11-13. Each item is a type or constructor the core (`ccc-core.l4`) lacks, defined by this part under its own prefix so that nothing waits on the keel.

## 1. `Party` has no constructor for the officials named in s 67

Section 67 applies to "(a) a justice, mayor or sheriff, or the lawful deputy of a mayor or sheriff, (b) a warden or deputy warden of a prison, or (c) the institutional head of a penitentiary ... or that person's deputy" who receives notice of a riotous assembly of twelve or more persons.
The core's `Party` has `a justice` (read from `ccc-core.l4`) and no constructor for a mayor, a sheriff, the lawful deputy of a mayor or sheriff, a warden, a deputy warden, the institutional head of a penitentiary, or that head's deputy.

What this part did: `ccc2-riots.l4` declares `s 67 office`, nine constructors (`s 67(a) a justice`, `s 67(a) a mayor`, `s 67(a) a sheriff`, `s 67(a) the lawful deputy of a mayor or sheriff`, `s 67(b) a warden of a prison`, `s 67(b) a deputy warden of a prison`, `s 67(c) the institutional head of a penitentiary`, `s 67(c) the deputy of the institutional head of a penitentiary`, `s 67 another office`).
The decision functions `s 67 the person must go to that place` and `s 67 the person must command silence and make the proclamation` take an `s 67 office`.
The regulative rule `s 67 the duty of the person who receives notice` is typed ``DEONTIC `s 67 office` `s 67 act` ``, so its party type is this part's `s 67 office` and not the core's `Party`; the office is a `GIVEN` of the rule, and a `#TRACE` prints the input's name (`office`) in the residual instead of the value.

If the lead hoists these into the core: add the seven constructors to `Party`, retype the rule as `DEONTIC Party ...` with the office as a `Party` value, and delete `s 67 office`.
Nothing else in this part depends on it, and no seat question is about these officials (the section binds an official; the person meets it as the thirty minutes of s 68(b)).

## 2. Nothing else

No other core type or constructor is missing.
Every other name this part uses comes from the core as supplied: `Punishment`, `Imprisonment`, `Fine`, `Length of time` and its constants, `Mode of proceeding`, `Class of offence`, `Provision of the Code`, and the `Party` constructors `the accused` and `the Governor in Council`.
