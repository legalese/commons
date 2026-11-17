# NEEDS-CORE.md -- ccc3

What this part wanted from the core (`ccc-core.l4`) and did not find.
No layer-1 rule of this part is blocked by it: each item is handled locally, under this part's prefix, and the lead may hoist it.

1. **`Party` constructors for the officials of Part II.1.**
   The core's `Party` (the constructors from `the accused` to `the Correctional Service of Canada` and the like) has no constructor for the Minister of Public Safety and Emergency Preparedness, the Minister of Foreign Affairs, the Minister of Citizenship and Immigration, the Commissioner of the Royal Canadian Mounted Police, the Director of the Canadian Security Intelligence Service, or a judge of the Federal Court (it has `the Minister of Justice`, `the Governor in Council`, `a judge` and `the court`).
   This part does not need a `Party` for them: `s 83.031(1) Public Safety Minister` takes "the person is the Minister of Public Safety and Emergency Preparedness" as a plain fact, and every other function that turns on one of these officials takes the fact it needs as a plain input.
   Wanted, if a later part compares a `Party` with these offices: constructors named for them.
2. **Nothing else.**
   `Punishment`, `Imprisonment`, `Fine`, `Length of time`, `Class of offence`, `Provision of the Code` and `Party` were enough for every offence, penalty and period of this range.
