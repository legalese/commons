# NEEDS-CORE.md -- ccc19

Written by part agent `ccc19` (2026-11-13). Two constructors that `Party` in `ccc-core.l4` lacks and that s 492.3 (line 11019) names:

- `counsel representing the Attorney General of Canada` ("by counsel representing the Attorney General of Canada")
- `a person acting on behalf of the prosecutor or the Attorney General of Canada` ("by any person acting on behalf of the prosecutor or the Attorney General of Canada")

`Party` has `the prosecutor` and `the Attorney General of Canada` but not these two. They are not needed as actors of any regulative rule here (the only party of s 492.3's duty is `the court`); they appear as the answers of `s 492.3 who took the action`, a small enumeration declared in `ccc19-s492-27-to-3.l4` under this part's prefix (`s 492.3 the prosecutor`, `s 492.3 counsel representing the Attorney General of Canada`, `s 492.3 a person acting on behalf of the prosecutor or the Attorney General of Canada`, `s 492.3 someone else`). If the lead hoists the two constructors into `Party`, that enumeration can be replaced by `Party`; nothing else in this part needs a core change.
