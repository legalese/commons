# Victoria Theatre Act 1903 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/VTA1903.txt`. It "incorporates all amendments up to
and including 1 December 2021" and came into operation on 31 December 2021. It
annotates no later amendment.

**Checks:** one case file, 32 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This is requirement **REQ-0253** in `subjects/sg/requirements.jsonl`: tier 4 of the
remaining Singapore Acts, ordered by everyday-life relevance. The requirement asks
what the Act decides for a person or business it applies to; no scenario has asked a
sharper question yet.

The Act has three sections, so nothing is scoped out of the operative text: ss 2 and 3
are encoded in full. Not encoded: s 1 (short title) and the preamble's history,
except to tell the Victoria Memorial Hall apart from the Theatre.

## What the Act turns out to say

### 1. No one has a right to use the Theatre, and a refusal needs no reasons

s 2(2): "The Government may refuse any application made for the use of the Theatre
without assigning any reason for its refusal." A person or company uses the Theatre
only by the Government's permission, given "at its discretion" and on "such terms and
conditions as it thinks fit" (s 2(1)). The encoding makes a refusal open whether or not
reasons are given, and makes no applicant entitled to a grant. Whether general public
law would still review a refusal is outside the text and not encoded. Asserted.

### 2. The Theatre is outside the Public Entertainments Act 1958; the Memorial Hall is not exempted by this Act

s 3 exempts "The Victoria Theatre" from the 1958 Act. The preamble distinguishes the
Old Town Hall, to be converted into the Theatre, from "The Victoria Memorial Hall"
built on another portion of the same land. The exemption names only the Theatre, so
this Act does nothing for the Memorial Hall. Whether the 1958 Act applies to the
Memorial Hall is for that Act. Asserted.

### 3. The permitted uses are a closed list of kinds

s 2(1) lets the Government permit "the public or private representation of stage
plays or the holding of public or private entertainments, theatrical or otherwise,
concerts or public meetings". Private stage plays and private entertainments are
allowed; meetings must be "public". The encoding treats a private business meeting, a
trade exhibition and a shop as outside the list. That is this row's reading (an
"entertainment ... or otherwise" might be read more widely), not the text's words.
Asserted.

### 4. The Government's own use is limited to public purposes

The Government holds the Theatre "upon trust to use it for such public purposes as it
thinks fit". Asserted, as a single condition: the purpose is public.

### 5. The preamble and the section name different holders

The preamble recites that the land is vested in "the Municipal Commissioners of
Singapore" and that they are to decide terms; s 2(1) as deposited says "The Government
shall hold the Victoria Theatre". The text does not say how the holding passed; that it
changed through later amendment or revision is an inference. Not asserted.

## What would need doing before this is worth anything

- The Public Entertainments Act 1958 (or its successor) was not read, so what the s 3
  exemption takes away (licences, conditions, offences) is not known to this row.
- The terms and conditions the Government sets for use, and what follows a breach,
  are not in the Act and were not searched for.
- No case law on s 2(2) or on review of a refusal was searched.
