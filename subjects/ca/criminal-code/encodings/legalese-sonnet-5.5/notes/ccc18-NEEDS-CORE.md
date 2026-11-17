# NEEDS-CORE.md -- part ccc18 of the Criminal Code (Canada): types and constructors the core lacks

Written 2026-11-16 by `work/mknotes.py` from the declarations in the modules (nothing typed twice).

`ccc-core.l4` declares one actor type, `Party`.
Eight bearers of duties and powers that the text of lines 10275-10956 names in its own words are not among its constructors (checked by searching `ccc-core.l4` for each phrase: no hit).
Each is declared in the part's own module as a one-constructor type under its section label, so that no name collides at the merge, and is used only in the regulative rule of that provision (fork F1).
No bearer is invented: the nearest core constructor (`a public officer`, `a peace officer`, `the keeper of a prison`) would name an actor the text does not.

| local type | constructor wanted in `Party` (the text's words) | module:line |
| --- | --- | --- |
| `s 490.021(6) party` | `s 490.021(6) the person who served the notice` | ccc18-soira-notice:223 |
| `s 490.02903(3) party` | `s 490.02903(3) the person who served the notice` | ccc18-soira-foreign:110 |
| `s 490.02911(3) party` | `s 490.02911(3) a police service` | ccc18-soira-foreign:910 |
| `s 490.02915(1) party` | `s 490.02915(1) the person in charge of the place` | ccc18-soira-itoa:624 |
| `s 490.03(1) party` | `s 490.03(1) the Commissioner of the Royal Canadian Mounted Police or a person authorized by the Commissioner` | ccc18-soira-offences:51 |
| `s 490.5(3) party` | `s 490.5(3) the applicant` | ccc18-forfeiture:452 |
| `s 490.81(4) party` | `s 490.81(4) a person appointed to manage property` | ccc18-forfeiture:781 |
| `s 492(1) party` | `s 492(1) the person who executes the warrant` | ccc18-weapons-evidence:404 |

If the lead hoists a constructor into `Party`, the local type and its constructor in the named module are deleted and the regulative rule names the core's constructor; no other change is needed.

No other type, constructor or constant was needed: every other name this part uses is declared in `ccc-core.l4` (`Party`, `Process document`, `Provision of the Code`, `Punishment`, `Length of time`, `Province or territory` and the `no imprisonment is stated` / `no fine is stated` constructors) or under this part's own labels.
