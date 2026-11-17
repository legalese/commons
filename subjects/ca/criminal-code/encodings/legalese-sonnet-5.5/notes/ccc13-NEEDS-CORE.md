# NEEDS-CORE.md -- ccc13

Things the part needed from the core or the keel and did not have.
The lead hoists them at the merge; until then they are declared here and used under the `ccc13` prefix.

## 1. Three-valued helpers (hoist)

`ccc13 all of`, `ccc13 any of` and `ccc13 not`, in `ccc13-logic.l4`.
Every part that joins `MAYBE BOOLEAN` answers needs the same three.
Kleene's rules: `all of` answers JUST FALSE if any answer is JUST FALSE, otherwise NOTHING if any is NOTHING, otherwise JUST TRUE; `any of` is the dual; `not` swaps JUST TRUE and JUST FALSE and leaves NOTHING alone.
Tests: `ccc13-tests-logic.l4`.

## 2. A constructor that says no, for the terms the Code says "includes" (request)

The keel's `s 2 testamentary instrument` and the enum `s 2 testamentary instrument kind` have a last constructor for a document that is none of those; because the Code says a testamentary instrument "includes" a list, the keel's function answers NOTHING for it.
A caller that needs a no from it (`s 380(1)(a)`, `s 430(3)`, `s 430(4)`) cannot get one.
This part took a plain yes/no from the person at the seat (fork F13) and left layer 1 taking the answer as a `MAYBE BOOLEAN`.
Request: a constructor of the kind enum that the keel's function maps to JUST FALSE ("what the person judges not to be one"), for this term and any other "includes" term that a caller must be able to answer no.

## 3. Duplicate constructors (note)

The keel's enums repeat constructors such as `a thing that is none of those`; a module that uses one needs `GIVETH A <type>` on the constant, or the name is ambiguous.
Suggest the keel prefix them by type.
