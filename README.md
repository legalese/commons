# L4 Commons

**Making the world's laws and contracts understandable by AI.**

Every entry here is a body of law (a statute, a regulation, a contract form) encoded in
[L4](https://github.com/legalese/l4-ide), the language for law, together with the evidence
that the encoding is faithful: section-by-section citations back to the source, scenario
tests, a fork register recording every place the text can reasonably be read two ways, and,
once someone qualified has checked it, a signed human review.

From the _canons of construction_ to the construction of canon: where the interpretive
tradition leaves construction implicit in a reader's judgement, an entry here carries its
construction on its face — which reading was taken at each ambiguous site, on what argument
or authority, and what turns on the difference.

**Status (16 October 2026):** 598 subjects with L4 encodings across ten jurisdictions.
Every one is `draft`: no subject is yet marked reviewed.
Most are scoped first passes, covering the provisions behind the most common questions about an Act rather than the whole Act; each row's `NOTES.md` says what it covers and what it leaves out.
This repository was called `canon` until October 2026; old links redirect here.

## Contributor's guide: add your country's law

1. In [Claude Code](https://claude.com/claude-code), install the L4 plugin:
   `/plugin marketplace add legalese/l4-plugin`, then `/plugin install l4-computational-law@legalese`.
2. Point it at a law and ask for the whole job, for example:
   *"Encode the Interpretation Act of Malaysia for the L4 Commons, solo, with the `encoding-a-subject` skill, and finish with a pull request to legalese/commons."*
3. That is one session doing the whole job: it installs `l4` (the plugin's `scripts/install-l4.sh`), gathers the official text, writes a brief, encodes the law section by section with citations, tests it, has an independent pass write tests from the source alone, writes `NOTES.md`, and opens a pull request from your fork.

What we care about most in a contribution is **the forks**.
Wherever the text can reasonably be read two ways (an "and" that might be an "or", an exception that might attach at either level, a deadline that might count calendar or working days), do not quietly pick one:

- record the fork in `NOTES.md`: the readings, the one you took, and the text that licenses each;
- write a **discriminating example** for it: a concrete scenario whose answer differs under each reading, kept as a test, so that anyone can see exactly what turns on the choice.

A fork with a discriminating example is a question a lawyer can often answer in minutes, and those answers are what turn a `draft` into a `reviewed` encoding.
Your contribution is welcome as a draft; say in `NOTES.md` what you did not cover.

## Layout: one class, many instances

```
subjects/
  <subject-id>/          one body of law
    subject.json         the descriptor: sources, corpus modules, projections, version
    NOTES.md             this subject's idiosyncrasies, in prose
    SOURCE-LICENSE.md    the terms the quoted legal text carries (see Licensing)
    *.l4                 the encoding
    cases/               dated scenario cases with expected values, machine-evaluated
    projections/         emitted DMN / BPMN / other artifacts, with fidelity reports
    registers/           fork register · external-modification register · source bundle
    report/              the conversion report
    gates/               HG1/HG2 grant artifacts — signatures and waivers (see Gates)
```

The layout is a **class/instance** design: the generic "⟨body of law⟩: go" template (the
subject-sidecar shape) is the class; each encoding job is an instance expected to veer, and
its divergences are recorded in its own `NOTES.md` — never by forking the template.

How the tree **above** these leaves is organised — jurisdictions and their subdivisions,
commercial-contract genres, and leaves that index an encoding hosted in someone else's
repository instead of vendoring it here — is proposed, not yet adopted, in
[docs/directory-conventions.md](docs/directory-conventions.md).

## Status vocabulary

Every subject declares exactly one of:

| status                   | meaning                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ |
| `draft`                  | the encoding exists; no claim of fidelity is made                              |
| `adversarially-reviewed` | machine gates passed; independent adversarial review completed                 |
| `reviewed`               | a named domain expert has signed HG1: the encoding is isomorphic to its source |

## Versioning: two axes, deliberately separate

The **encoding version** (semver, in `subject.json`) numbers the encoding itself — it
increments when the L4 changes. The **law-time axis** is inside the encoding: L4's
`EVAL UNDER RULES EFFECTIVE AT` evaluates any entry under the rules effective at a chosen
date, so amended regimes are dated arms in one artifact, not forked files. An encoding at
version 2.1.0 can still answer questions about the law as it stood in 2016.

## Gates: human sign-off you can verify yourself

Review here is not a badge; it is a **detached SSH signature over a content digest** of the
reviewed files. Each subject's `gates/` directory carries the signed payload, the signature,
and the `allowed_signers` entry. To verify one:

```
ssh-keygen -Y verify -f gates/allowed_signers -I <signer> -n l4-go-gate \
  -s gates/HG1.payload.sig < gates/HG1.payload.txt
```

A signature binds to content — edit the encoding and the grant visibly no longer verifies.
Waivers, where used, are equally on the record: a waiver is a verdict with a reason attached,
never an absence. Agents can verify signatures; they cannot make them.

## Licensing

- **Everything authored here** — encodings, cases, schemas, harnesses, reports — is licensed
  under [Apache-2.0](LICENSE).
- **Quoted legal text carries its own terms**, recorded per subject in `SOURCE-LICENSE.md`
  and attributed in [NOTICE](NOTICE). United States federal material is in the public domain
  (17 U.S.C. § 105 and the edicts-of-government doctrine); United Kingdom legislation is
  quoted under the [Open Government Licence v3](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
  with attribution.
- **Prose artifacts** (conversion reports, commentary, comparison notes) may additionally be
  offered under CC-BY-4.0 where a subject's `SOURCE-LICENSE.md` says so, so they can flow
  into attribution-share-alike wikis without ShareAlike reaching the encodings.

## Tooling

Encodings here are produced and checked by the pipeline in
[legalese/l4-ide](https://github.com/legalese/l4-ide) — the `etc/go/` orchestrator, whose
subject sidecars mirror this repository's layout. This repository holds law; that one holds
tools.
