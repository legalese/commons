# NEEDS-CORE.md -- ccc1: constructors wanted in the core's `Party`

The core's `Party` (`ccc-core.l4`, line 49) has no constructor for four persons that Part I, sections 25.1 to 25.4 and 29, put a duty on or give a power to.
A part cannot extend a type from another module, so `ccc1` declared small types of its own under its prefix and used those.
Each line below gives the constructor wanted, the text that names the person, and where `ccc1` declares its own stand-in.
These were checked against the files on 2026-11-16: the text lines are in `inputs/R.S.C.-1985-c.-C-46.txt`; the declarations are the lines named.

| constructor wanted in `Party` | text | `ccc1`'s stand-in |
| --- | --- | --- |
| `a senior official` | line 652: "senior official means a senior official who is responsible for law enforcement and who is designated under subsection (5)" | `s 25.2 a senior official`, `ccc1-s25-reports.l4:21` |
| `a competent authority` | line 647: "competent authority means, with respect to a public officer or a senior official, ..." | `s 25.2 a competent authority`, `ccc1-s25-reports.l4:22` |
| `a person who executes a process or warrant` | line 747: "It is the duty of every one who executes a process or warrant to have it with him ..." | `s 29 a person who executes a process or warrant`, `ccc1-s26-33-force.l4:121` |
| `a person who arrests a person` | line 749: "It is the duty of every one who arrests a person, whether with or without a warrant, to give notice ..." | `s 29 a person who arrests a person, whether with or without a warrant`, `ccc1-s26-33-force.l4:122` |

Two things the lead should know before hoisting:

- `ccc1-s25-reports.l4:20` also declares `s 25.2 a public officer`, although the core already has `a public officer`: the three persons of section 25.2 are one declared type there, so that the three are one `DECLARE`.
  If the core gains the first two constructors, that type can go, and the `PARTY` lines can name the core's constructors (the `PARTY` lines of `s 25.1(6)`, `s 25.2`, `s 25.3(1)` and `s 25.4(1)`).
- No other constructor, type or function is wanted from the core.
  Everything else `ccc1` needs from section 2 is read as an input typed `MAYBE BOOLEAN` and named `s 2 <term>: ...`, or is the core's own `s 2 peace officer` and `s 2 public officer`, which the seat layer calls.
