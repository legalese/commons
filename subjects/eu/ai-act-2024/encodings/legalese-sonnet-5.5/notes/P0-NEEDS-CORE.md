# NEEDS-CORE (P0 seat layer)

Two things in the keel could not be called as a seat question needs them.
Neither stops the seat layer: each has a workaround in place, named below, and no keel function was copied or edited.

## 1. A version-dispatching `Art 111(2) the system is saved`

**What is missing.**
The keel offers the saving of Article 111(2), first sentence, as two functions, `Art 111(2) as enacted the system is saved` and `Art 111(2) as amended the system is saved` (aia-timeline.l4, lines 165 and 182).
Both return `BOOLEAN` and take the provision group, the route, the placement date and the significant-change flag.
No function takes `the date asked` and chooses between them.
The date functions of the same paragraph do dispatch (`Art 111(2) the date by which providers and deployers ... must comply` takes `the date asked`), which is why the gap is easy to miss.

**What the seat layer does instead.**
The seat question `Under Article 111(2), as <role>, is my high-risk AI system saved from the application of the Regulation?` (six operator seats) chooses the function itself, with `CONSIDER` on the keel's `Omnibus Art 4 the version in force` of the date asked.
It restates no rule and adds no condition: it only picks which of the two keel functions to call, and passes the group `Chapter III Sections 1 to 3`, the route, the placement date and the flag through.
That dispatch is the one piece of keel-shaped logic in layer 2.

**Request.**
A function `Art 111(2) the system is saved` whose first argument is `the date asked` and whose body is that dispatch, so that a seat only calls it.

**Who is affected.**
Every part agent that asks whether a legacy high-risk AI system is saved from its provisions has the same choice to make.

## 2. The Annex X act as a `STRING`

**What is missing.**
`Annex X the large-scale IT system is established by a listed legal act` takes the act as a `STRING`.
A seat can therefore ask the act only as free text.
An enumeration of the twelve acts would let a form offer a choice.

**What the seat layer does instead.**
The input `the act that establishes that large-scale IT system` is a `STRING` whose `@desc` lists the twelve spellings Annex X uses, and says to write `none` if the system is not a large-scale IT system component.

**The failure is silent.**
A misspelt act, an extra space or a different dash reads as "an act Annex X does not list", and the answer is `NOTHING` ("not covered") with no error.
The case files assert that an unlisted act gives `NOTHING`; they cannot tell a typo from a true "not listed".

**Request.**
A `DECLARE` of the twelve acts as constructors in aia-annex-x.l4, and a variant of the function that takes it.
