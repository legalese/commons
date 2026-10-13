# Israel's HVAC work-licensing Law 5785-2025 and its Fees Regulations, in L4 (draft)

This directory is one row, `legalese-full-sonnet-5.5`, of an encoding of Israel's Regulation of Engagement in Work on Refrigeration or Air-Conditioning Systems Law, 5785-2025, and the Fees Regulations made under it.
It was written by a fleet of eight encoders, each owning part of the Law, and an integrator who wired them together; three independent test authors then wrote tests of their own, from the sources and before opening the encoding, and those tests are in this directory too (the files with the prefixes `ind-a-`, `ind-b-` and `ind-c-`, and the `INDEPENDENT-*-expectations.md` documents).
It is a draft: no domain expert has read it against the Law, and every reading in it is the fleet's own, assumed and not ruled, except one: day X of s.63(a)(1) is 16 July 2025, a reading the owner has ruled.

**What you can ask it.**
The integration modules (`int-*.l4`) answer five questions: may this person be granted this licence on this day; may this person do this work on this day; what is the sanction for this violation; on which day does the Law commence, and when did the Fees Regulations come into force; what is the fee for this service in this version of the regulations.
Each answer is a value or a named refusal that says what is missing from the sources, never a default.

**Where to start.**
Read `NOTES.md`: what is and is not encoded, the answer table, the places where the groups' readings differ, the contradictions found in the Law's text, and the questions a domain expert should settle.
The one ruling the owner has made so far (day X of s.63(a)(1): 16 July 2025, with 16 October 2025 documented as the alternative) is in its section "Owner rulings".
The readings that could go either way are listed as forks (one index in `NOTES.md`; the detail in `FRAGMENT-G1.md` to `FRAGMENT-G8.md`), and each has a callable alternative.

**To run it.**
Put an `l4` on your path (the numbers in `NOTES.md` come from the build named in `encoding.json`), leave `JL4_LIBRARY_PATH` unset, and run `bash check.sh` in this directory.
It runs every module, checks the vendored time module's hash, checks every quotation of the Hebrew against the raw sources if you point `INPUTS` and `SRCREFS` at them, and checks every deontic trace.
The nine `*-tests-red.l4` files and the three `ind-*-tests-ambiguous.l4` files are meant to fail, and three `ind-` files are meant to refuse, each with a stated count: each such assertion states a reading the encoders did not take, or a refusal the encoding returns.

**Source terms.**
`SOURCE-LICENSE.md` records the terms the quoted source text carries.
