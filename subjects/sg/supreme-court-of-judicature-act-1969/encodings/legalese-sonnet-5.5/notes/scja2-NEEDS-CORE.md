# NEEDS-CORE.md (scja2)

Written 2026-11-05. One item; nothing else in the keel (`scja-core.l4`) was missing for ss 30 to 72.

1. **`Hearing` cannot say how many Judges are unable to continue.**
   The keel's `Hearing` record has `a Judge is unable to continue IS A BOOLEAN`.
   Sections 36(3)(a) and 54(3)(a) turn on a count: the court "must continue to hear and decide the case if every party to the case consents and there are at least 2 Judges remaining", where the bench was 3 or more Judges and one or more are unable to continue, and a Boolean cannot give "at least 2 remain".
   This part does not use `Hearing` or `Bench` at all: the two functions take the number of Judges who constituted the court and the number unable to continue as plain `NUMBER` inputs, and `every party to the case consents` as a `BOOLEAN`.
   If the lead wants a `Hearing` that those functions can read, the field would be a number (the Judges unable to continue) in place of, or beside, the Boolean; the same record also names `oral evidence is given in this part of the hearing` and `all the parties consent`, which ss 37(2) and 55(2) take as plain `BOOLEAN` inputs here.
   Nothing in this part is blocked on it.
