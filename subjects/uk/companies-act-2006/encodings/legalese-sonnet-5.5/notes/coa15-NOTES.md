# NOTES (coa15): Companies Act 2006 (United Kingdom), Part 18, ss 658 to 737

**Range:** lines 8745-9668 of `ukpga-2006-46.txt` (Part 18, Acquisition by limited company of its own shares: Chapter 1 general provisions, Chapter 2 financial assistance, Chapter 3 redeemable shares, Chapter 4 purchase of own shares, Chapter 5 redemption or purchase out of capital, Chapter 6 treasury shares, Chapter 7 supplementary provisions).
**Run:** `dst-coa15`. **Binary:** the stable build `1.6.110 (main, e51181d, 2026-11-11)`; `check.sh` also runs every module on the main build `1.6.109` and compares the counts.

**The text is a converter rendering, not the official text.**
`ukpga-2006-46.txt` is a plain-text rendering of the Act made by a converter script.
Nothing in this folder is "verified against the official text"; every claim about what the Act says is a claim about this rendering, checked by `srcrefs.py` against the lines quoted in the `.l4` files.
Where the rendering shows damage (the two wordings of the daily default fine run together at lines 9300 and 9573; the words "a . . . resolution" with an omitted word; blank provisions shown as rows of dots) the encoding follows the rendering and says so under "What the text turns out to say".

## Status of the claims below, and how each was checked

| claim | how it was checked |
| --- | --- |
| Every `.l4` file compiles with no error and no warning on 1.6.110 | `check.sh` (its output is under "What check.sh printed"), and `l4 check` on each file: no warning and no layout note |
| Every assertion is satisfied, and the counts are the same on 1.6.109 | `check.sh`, the "main" columns |
| Every `-- src:` line is the text's line, and every `@ref` locator reaches exactly the lines its quote run quotes | `python3 -I srcrefs.py check --refs` and `--strict`, run on the raw text: 0 problems |
| Every `#TRACE` ends as the `-- expect:` comment above it says | `work/trace-expect.py` (a deontic cannot be compared with `EQUALS`, see "What the stable binary does not accept") |
| The expected values in the tests are written from the text | by hand, before the run; no golden was blessed from output. Where a first run disagreed (the trace expectations of duties with no `WITHIN`, where waiting leaves a residual and not a breach; and, in the seat cases, ss 661(2), 662(2) and 662(5)) the function and the text were re-read before the expectation was changed |
| Coverage rows come from the text by script, then are completed by hand | `work/units.py` (the units), `work/refmap.py` (the declarations whose `@ref` locators reach each unit); the script that builds this file lists the rows it could not map |
| Nothing was checked against a lawyer's reading | the readings under "Marginal readings for a lawyer" are put to a lawyer, not settled |

## What this folder holds

- `coa15-nouns.l4`: the types that more than one chapter shares (the person an offence charges, the statement of capital, the penalty for the two fines whose daily limit the core cannot say).
- `coa15-ch1.l4` to `coa15-ch7.l4`: layer 1, one module per chapter, the rule of each provision with `@ref` locators, in the text's order. Chapter 4 imports chapters 1 and 6, chapter 5 imports chapters 1 and 4, chapter 3 imports chapter 1, chapter 6 imports chapter 1.
- `coa15-tests-ch1.l4` to `coa15-tests-ch7.l4`: the tests of each module.
- `coa15-seat.l4` and `coa15-cases-seat.l4`: layer 2 and its cases. The seat is an individual who is, or is about to become, a director, a company secretary or a member of a company, or who deals with one (assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership). Every question is named "Under section N, ...", calls layer-1 rules only, and takes plain inputs.
- Naming: every top-level name in the layer-1 modules begins with the label of its provision (`s 4(2)(a) ...`); the seat questions begin "Under section N," as the brief asks. The test files also define test fixtures (named `fixture: ...`, which implement no provision); no file imports a test file, so a fixture name cannot collide with another part's.
- `PROGRESS.md`, `NEEDS-CORE.md`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`.
- `coa-core.l4` and `coa-definitions.l4` are the keel's and were not edited.

The `.l4` files are expanded from templates kept outside this folder (`work/src/*.l4.tpl`, by `work/build.py`); the expansion writes every `-- src:` quote line and its `@ref` locator from the raw text by script, so no quoted wording was typed.

## Coverage (coa15)

One row per heading, section, subsection, lettered paragraph and defined term of lines 8745-9668. Roman sub-paragraphs belong to the lettered paragraph above them. There is no table and no schedule in the range. Each row has exactly one disposition: `encoded` (a rule with `@ref` locators and a test), `fork` (the text reads two ways; see the fork register), `inert` with a reason number (1 not operative, 2 machinery, 3 shown repealed or blank), or `repealed or blank in this text`. There is no `deferred` and no `out-of-scope` row. The L4 column names the one or two declarations whose `@ref` locators reach the unit's lines (the first is the nearest in extent); the test column names the file that tests the first.

| unit | lines | disposition | L4 | tested in |
| --- | --- | --- | --- | --- |
| heading: Part 18 — Acquisition by limited company of its own shares | 8745-8745 | inert (reason 1) | a heading: not operative |  |
| heading: Chapter 1 — General provisions | 8746-8746 | inert (reason 1) | a heading: not operative |  |
| heading: Introductory | 8747-8747 | inert (reason 1) | a heading: not operative |  |
| s 658 General rule against limited company ... | 8748-8759 | fork F-not-in-default | `s 658(3) the penalty on conviction`; `s 658(2)(a) the person commits an offence` (+4 more) | coa15-tests-ch1.l4 |
| s 658(1) | 8749-8749 | encoded | `s 658(1) a limited company must not make the acquisition`; `s 658(1) the limited company shant acquire its own shares` | coa15-tests-ch1.l4 |
| s 658(2) | 8750-8754 | fork F-not-in-default | `s 658(2)(a) the person commits an offence`; `s 658(2)(b) the purported acquisition is void` (+1 more) | coa15-tests-ch1.l4 |
| s 658(2)(a) | 8751-8753 | fork F-not-in-default | `s 658(2)(a) the person commits an offence`; `s 658(2) person charged` | coa15-tests-ch1.l4 |
| s 658(2)(b) | 8754-8754 | encoded | `s 658(2)(b) the purported acquisition is void`; `s 658(2) person charged` | coa15-tests-ch1.l4 |
| s 658(3) | 8755-8759 | encoded | `s 658(3) the penalty on conviction` | coa15-tests-ch1.l4 |
| s 658(3)(a) | 8756-8756 | encoded | `s 658(3) the penalty on conviction` | coa15-tests-ch1.l4 |
| s 658(3)(b) | 8757-8759 | encoded | `s 658(3) the penalty on conviction` | coa15-tests-ch1.l4 |
| s 659 Exceptions to general rule | 8760-8769 | encoded | `s 659(2) section 658 does not prohibit the acquisition`; `s 659(1) a limited company may acquire its own shares` | coa15-tests-ch1.l4 |
| s 659(1) | 8761-8761 | encoded | `s 659(1) a limited company may acquire its own shares` | coa15-tests-ch1.l4 |
| s 659(2) | 8762-8769 | encoded | `s 659(2) section 658 does not prohibit the acquisition` | coa15-tests-ch1.l4 |
| s 659(2)(a) | 8763-8763 | encoded | `s 659(2) section 658 does not prohibit the acquisition` | coa15-tests-ch1.l4 |
| s 659(2)(b) | 8764-8768 | encoded | `s 659(2) section 658 does not prohibit the acquisition` | coa15-tests-ch1.l4 |
| s 659(2)(c) | 8769-8769 | encoded | `s 659(2) section 658 does not prohibit the acquisition` | coa15-tests-ch1.l4 |
| heading: Shares held by company's nominee | 8770-8770 | inert (reason 1) | a heading: not operative |  |
| s 660 Treatment of shares held by nominee | 8771-8783 | encoded | `s 660(1) this section applies to the shares`; `s 660(3)(a) section 660 does not apply to the shares` (+4 more) | coa15-tests-ch1.l4 |
| s 660(1) | 8772-8775 | encoded | `s 660(1) this section applies to the shares`; `s 660(1) how the shares come to the nominee` | coa15-tests-ch1.l4 |
| s 660(1)(a) | 8773-8773 | encoded | `s 660(1) this section applies to the shares`; `s 660(1) how the shares come to the nominee` | coa15-tests-ch1.l4 |
| s 660(1)(b) | 8774-8774 | encoded | `s 660(1) this section applies to the shares`; `s 660(1) how the shares come to the nominee` | coa15-tests-ch1.l4 |
| s 660(1)(c) | 8775-8775 | encoded | `s 660(1) this section applies to the shares`; `s 660(1) how the shares come to the nominee` | coa15-tests-ch1.l4 |
| s 660(2) | 8776-8778 | encoded | `s 660(2)(a) the shares are treated as held by the nominee on his own ac...`; `s 660(2)(b) the company is regarded as having no beneficial interest in...` | coa15-tests-ch1.l4 |
| s 660(2)(a) | 8777-8777 | encoded | `s 660(2)(a) the shares are treated as held by the nominee on his own ac...`; `s 660(2)(b) the company is regarded as having no beneficial interest in...` | coa15-tests-ch1.l4 |
| s 660(2)(b) | 8778-8778 | encoded | `s 660(2)(a) the shares are treated as held by the nominee on his own ac...`; `s 660(2)(b) the company is regarded as having no beneficial interest in...` | coa15-tests-ch1.l4 |
| s 660(3) | 8779-8783 | encoded | `s 660(3)(a) section 660 does not apply to the shares`; `s 660(3)(b) section 660 does not apply to the shares` | coa15-tests-ch1.l4 |
| s 660(3)(a) | 8780-8782 | encoded | `s 660(3)(a) section 660 does not apply to the shares` | coa15-tests-ch1.l4 |
| s 660(3)(b) | 8783-8783 | encoded | `s 660(3)(b) section 660 does not apply to the shares` | coa15-tests-ch1.l4 |
| s 661 Liability of others where nominee fai... | 8784-8800 | fork F-grant-661-3, F-grant-661-4a, F-grant-661-4b | `s 661(1) this section applies to the shares`; `s 661(2) the person is jointly and severally liable with the nominee to...` (+5 more) | coa15-tests-ch1.l4 |
| s 661(1) | 8785-8788 | encoded | `s 661(1) this section applies to the shares` | coa15-tests-ch1.l4 |
| s 661(1)(a) | 8786-8786 | encoded | `s 661(1) this section applies to the shares` | coa15-tests-ch1.l4 |
| s 661(1)(b) | 8787-8787 | encoded | `s 661(1) this section applies to the shares` | coa15-tests-ch1.l4 |
| s 661(1)(c) | 8788-8788 | encoded | `s 661(1) this section applies to the shares` | coa15-tests-ch1.l4 |
| s 661(2) | 8789-8792 | encoded | `s 661(2) the person is jointly and severally liable with the nominee to...` | coa15-tests-ch1.l4 |
| s 661(2)(a) | 8790-8790 | encoded | `s 661(2) the person is jointly and severally liable with the nominee to...` | coa15-tests-ch1.l4 |
| s 661(2)(b) | 8791-8792 | encoded | `s 661(2) the person is jointly and severally liable with the nominee to...` | coa15-tests-ch1.l4 |
| s 661(3) | 8793-8796 | fork F-grant-661-3 | `s 661(3) the court may relieve the subscriber or director from his liab...` | coa15-tests-ch1.l4 |
| s 661(3)(a) | 8794-8794 | fork F-grant-661-3 | `s 661(3) the court may relieve the subscriber or director from his liab...` | coa15-tests-ch1.l4 |
| s 661(3)(b) | 8795-8796 | fork F-grant-661-3 | `s 661(3) the court may relieve the subscriber or director from his liab...` | coa15-tests-ch1.l4 |
| s 661(4) | 8797-8799 | fork F-grant-661-4a, F-grant-661-4b | `s 661(4)(a) the subscriber or director may apply to the court`; `s 661(4)(a) the subscriber or director may apply to the court for relief` (+1 more) | coa15-tests-ch1.l4 |
| s 661(4)(a) | 8798-8798 | fork F-grant-661-4a | `s 661(4)(a) the subscriber or director may apply to the court`; `s 661(4)(a) the subscriber or director may apply to the court for relief` | coa15-tests-ch1.l4 |
| s 661(4)(b) | 8799-8799 | fork F-grant-661-4b | `s 661(4)(b) the court has the power to relieve him` | coa15-tests-ch1.l4 |
| s 661(5) | 8800-8800 | encoded | `s 661(5) section 661 does not apply to the shares` | coa15-tests-ch1.l4 |
| heading: Shares held by or for public company | 8801-8801 | inert (reason 1) | a heading: not operative |  |
| s 662 Duty to cancel shares in public compa... | 8802-8819 | encoded | `s 662(2)(a) the company must cancel the shares by the last day`; `s 662(1) this section applies to the shares` (+9 more) | coa15-tests-ch1.l4 |
| s 662(1) | 8803-8808 | encoded | `s 662(1) this section applies to the shares`; `s 662(1) how the shares come to be held` | coa15-tests-ch1.l4 |
| s 662(1)(a) | 8804-8804 | encoded | `s 662(1) this section applies to the shares`; `s 662(1) how the shares come to be held` | coa15-tests-ch1.l4 |
| s 662(1)(b) | 8805-8805 | encoded | `s 662(1) this section applies to the shares`; `s 662(1) how the shares come to be held` | coa15-tests-ch1.l4 |
| s 662(1)(c) | 8806-8806 | encoded | `s 662(1) this section applies to the shares`; `s 662(1) how the shares come to be held` | coa15-tests-ch1.l4 |
| s 662(1)(d) | 8807-8807 | encoded | `s 662(1) this section applies to the shares`; `s 662(1) how the shares come to be held` | coa15-tests-ch1.l4 |
| s 662(1)(e) | 8808-8808 | encoded | `s 662(1) this section applies to the shares`; `s 662(1) how the shares come to be held` | coa15-tests-ch1.l4 |
| s 662(2) | 8809-8811 | encoded | `s 662(2)(a) the company must cancel the shares`; `s 662(2)(b) the company must apply for re-registration as a private com...` (+2 more) | coa15-tests-ch1.l4 |
| s 662(2)(a) | 8810-8810 | encoded | `s 662(2)(a) the company must cancel the shares`; `s 662(2)(a) the company must cancel the shares by the last day` | coa15-tests-ch1.l4 |
| s 662(2)(b) | 8811-8811 | encoded | `s 662(2)(b) the company must apply for re-registration as a private com...`; `s 662(2)(b) the company must apply for re-registration as a private com...` (+1 more) | coa15-tests-ch1.l4 |
| s 662(3) | 8812-8815 | encoded | `s 662(3) the company cancelled the shares in time`; `s 662(3) the last day for cancelling the shares and for applying for re...` (+2 more) | coa15-tests-ch1.l4 |
| s 662(3)(a) | 8813-8813 | encoded | `s 662(3) the company cancelled the shares in time`; `s 662(3) the last day for cancelling the shares and for applying for re...` (+2 more) | coa15-tests-ch1.l4 |
| s 662(3)(b) | 8814-8814 | encoded | `s 662(3) the company cancelled the shares in time`; `s 662(3) the last day for cancelling the shares and for applying for re...` (+2 more) | coa15-tests-ch1.l4 |
| s 662(3)(c) | 8815-8815 | encoded | `s 662(3) the company cancelled the shares in time`; `s 662(3) the last day for cancelling the shares and for applying for re...` (+2 more) | coa15-tests-ch1.l4 |
| s 662(4) | 8816-8817 | encoded | `s 662(4) the directors may take the steps without complying with Chapte...` | coa15-tests-ch1.l4 |
| s 662(5) | 8818-8818 | encoded | `s 662(5) the person may exercise voting rights in respect of the shares` | coa15-tests-ch1.l4 |
| s 662(6) | 8819-8819 | encoded | `s 662(6) the purported exercise of the voting rights is void` | coa15-tests-ch1.l4 |
| s 663 Notice of cancellation of shares | 8820-8835 | fork F-empty-list, F-month, F-must, F-not-in-default | `s 663(3) the statement of capital states what the section requires`; `s 663(3)(c) every entry states what paragraph (c) requires` (+7 more) | coa15-tests-ch1.l4 |
| s 663(1) | 8821-8821 | fork F-month | `s 663(1) the company must give notice to the registrar`; `s 663(1) the last day for giving notice to the registrar` (+1 more) | coa15-tests-ch1.l4 |
| s 663(2) | 8822-8822 | fork F-must | `s 663(2) the notice is accompanied by a statement of capital` | coa15-tests-ch1.l4 |
| s 663(3) | 8823-8831 | fork F-empty-list, F-must | `s 663(3) the statement of capital states what the section requires`; `s 663(3)(c) every entry states what paragraph (c) requires` (+1 more) | coa15-tests-ch1.l4 |
| s 663(3)(a) | 8824-8824 | fork F-empty-list, F-must | `s 663(3) the statement of capital states what the section requires`; `s 663(3) class entry` | coa15-tests-ch1.l4 |
| s 663(3)(b) | 8825-8825 | fork F-empty-list, F-must | `s 663(3) the statement of capital states what the section requires`; `s 663(3) class entry` | coa15-tests-ch1.l4 |
| s 663(3)(ba) | 8826-8826 | fork F-empty-list, F-must | `s 663(3) the statement of capital states what the section requires`; `s 663(3) class entry` | coa15-tests-ch1.l4 |
| s 663(3)(c) | 8827-8830 | fork F-empty-list, F-must | `s 663(3)(c) every entry states what paragraph (c) requires`; `s 663(3) the statement of capital states what the section requires` (+1 more) | coa15-tests-ch1.l4 |
| s 663(3)(d) | 8831-8831 | repealed or blank in this text | the text shows a row of dots |  |
| s 663(4) | 8832-8834 | fork F-not-in-default | `s 663(4) the person commits an offence` | coa15-tests-ch1.l4 |
| s 663(4)(a) | 8833-8833 | fork F-not-in-default | `s 663(4) the person commits an offence` | coa15-tests-ch1.l4 |
| s 663(4)(b) | 8834-8834 | fork F-not-in-default | `s 663(4) the person commits an offence` | coa15-tests-ch1.l4 |
| s 663(5) | 8835-8835 | encoded | `s 663(5) the penalty on conviction` | coa15-tests-ch1.l4 |
| s 664 Re-registration as private company in... | 8836-8849 | fork F-must | `s 664(2) the resolution may make the change`; `s 664(4) the application is accompanied as the section requires` (+6 more) | coa15-tests-ch1.l4 |
| s 664(1) | 8837-8838 | encoded | `s 664(1) Chapter 3 of Part 3 applies to the resolution`; `s 664(1) the directors may resolve that the company should be re-regist...` (+1 more) | coa15-tests-ch1.l4 |
| s 664(2) | 8839-8842 | encoded | `s 664(2) the resolution may make the change` | coa15-tests-ch1.l4 |
| s 664(2)(a) | 8840-8840 | encoded | `s 664(2) the resolution may make the change` | coa15-tests-ch1.l4 |
| s 664(2)(b) | 8841-8842 | encoded | `s 664(2) the resolution may make the change` | coa15-tests-ch1.l4 |
| s 664(3) | 8843-8843 | fork F-must | `s 664(3) the application contains what the section requires` | coa15-tests-ch1.l4 |
| s 664(4) | 8844-8847 | fork F-must | `s 664(4) the application is accompanied as the section requires` | coa15-tests-ch1.l4 |
| s 664(4)(a) | 8845-8845 | fork F-must | `s 664(4) the application is accompanied as the section requires` | coa15-tests-ch1.l4 |
| s 664(4)(b) | 8846-8846 | fork F-must | `s 664(4) the application is accompanied as the section requires` | coa15-tests-ch1.l4 |
| s 664(4)(c) | 8847-8847 | fork F-must | `s 664(4) the application is accompanied as the section requires` | coa15-tests-ch1.l4 |
| s 664(5) | 8848-8848 | encoded | `s 664(5) the statement is the statement of compliance required` | coa15-tests-ch1.l4 |
| s 664(6) | 8849-8849 | encoded | `s 664(6) the registrar may accept the statement as sufficient evidence ...` | coa15-tests-ch1.l4 |
| s 665 Issue of certificate of incorporation... | 8850-8857 | fork F-must | `s 665(4)(a) the company becomes a private company by virtue of the issu...`; `s 665(1) the company shall be re-registered as a private company` (+4 more) | coa15-tests-ch1.l4 |
| s 665(1) | 8851-8851 | encoded | `s 665(1) the company shall be re-registered as a private company` | coa15-tests-ch1.l4 |
| s 665(2) | 8852-8852 | encoded | `s 665(2) the registrar must issue a certificate of incorporation` | coa15-tests-ch1.l4 |
| s 665(3) | 8853-8853 | fork F-must | `s 665(3) the certificate states what the section requires` | coa15-tests-ch1.l4 |
| s 665(4) | 8854-8856 | encoded | `s 665(4)(a) the company becomes a private company by virtue of the issu...`; `s 665(4)(b) the changes in the company's name and articles take effect` | coa15-tests-ch1.l4 |
| s 665(4)(a) | 8855-8855 | encoded | `s 665(4)(a) the company becomes a private company by virtue of the issu...` | coa15-tests-ch1.l4 |
| s 665(4)(b) | 8856-8856 | encoded | `s 665(4)(b) the changes in the company's name and articles take effect` | coa15-tests-ch1.l4 |
| s 665(5) | 8857-8857 | encoded | `s 665(5) the certificate is conclusive evidence that the requirements a...` | coa15-tests-ch1.l4 |
| s 666 Effect of failure to re-register | 8858-8860 | fork F-end | `s 666(1) Chapter 1 of Part 20 applies to the company as if it were a pr...`; `s 666(2) the company continues to be treated as a public company` | coa15-tests-ch1.l4 |
| s 666(1) | 8859-8859 | fork F-end | `s 666(1) Chapter 1 of Part 20 applies to the company as if it were a pr...` | coa15-tests-ch1.l4 |
| s 666(2) | 8860-8860 | encoded | `s 666(2) the company continues to be treated as a public company` | coa15-tests-ch1.l4 |
| s 667 Offence in case of failure to cancel ... | 8861-8869 | fork F-not-in-default | `s 667(2) the person commits an offence`; `s 667(3) the penalty on conviction` | coa15-tests-ch1.l4 |
| s 667(1) | 8862-8865 | fork F-not-in-default | `s 667(2) the person commits an offence` | coa15-tests-ch1.l4 |
| s 667(1)(a) | 8863-8863 | fork F-not-in-default | `s 667(2) the person commits an offence` | coa15-tests-ch1.l4 |
| s 667(1)(b) | 8864-8865 | fork F-not-in-default | `s 667(2) the person commits an offence` | coa15-tests-ch1.l4 |
| s 667(2) | 8866-8868 | fork F-not-in-default | `s 667(2) the person commits an offence` | coa15-tests-ch1.l4 |
| s 667(2)(a) | 8867-8867 | fork F-not-in-default | `s 667(2) the person commits an offence` | coa15-tests-ch1.l4 |
| s 667(2)(b) | 8868-8868 | fork F-not-in-default | `s 667(2) the person commits an offence` | coa15-tests-ch1.l4 |
| s 667(3) | 8869-8869 | encoded | `s 667(3) the penalty on conviction` | coa15-tests-ch1.l4 |
| s 668 Application of provisions to company ... | 8870-8878 | encoded | `s 668(1) this section applies to the shares`; `s 668(2) sections 662 to 667 apply to the company as if it had been a p...` (+2 more) | coa15-tests-ch1.l4 |
| s 668(1) | 8871-8876 | encoded | `s 668(1) this section applies to the shares`; `s 668(1) how the shares came to be held by or for the private company` | coa15-tests-ch1.l4 |
| s 668(1)(a) | 8872-8872 | encoded | `s 668(1) this section applies to the shares`; `s 668(1) how the shares came to be held by or for the private company` | coa15-tests-ch1.l4 |
| s 668(1)(b) | 8873-8873 | encoded | `s 668(1) this section applies to the shares`; `s 668(1) how the shares came to be held by or for the private company` | coa15-tests-ch1.l4 |
| s 668(1)(c) | 8874-8874 | encoded | `s 668(1) this section applies to the shares`; `s 668(1) how the shares came to be held by or for the private company` | coa15-tests-ch1.l4 |
| s 668(1)(d) | 8875-8876 | encoded | `s 668(1) this section applies to the shares`; `s 668(1) how the shares came to be held by or for the private company` | coa15-tests-ch1.l4 |
| s 668(2) | 8877-8877 | encoded | `s 668(2) sections 662 to 667 apply to the company as if it had been a p...` | coa15-tests-ch1.l4 |
| s 668(3) | 8878-8878 | encoded | `s 668(3) the date from which the period specified in section 662(3) runs` | coa15-tests-ch1.l4 |
| s 669 Transfer to reserve on acquisition of... | 8879-8885 | encoded | `s 669(1) the amount to be transferred to the reserve fund`; `s 669(1) an amount must be transferred out of profits available for div...` (+3 more) | coa15-tests-ch1.l4 |
| s 669(1) | 8880-8883 | encoded | `s 669(1) an amount must be transferred out of profits available for div...`; `s 669(1) the amount transferred is available for distribution` (+2 more) | coa15-tests-ch1.l4 |
| s 669(1)(a) | 8881-8881 | encoded | `s 669(1) an amount must be transferred out of profits available for div...`; `s 669(1) the amount transferred is available for distribution` (+2 more) | coa15-tests-ch1.l4 |
| s 669(1)(b) | 8882-8883 | encoded | `s 669(1) an amount must be transferred out of profits available for div...`; `s 669(1) the amount transferred is available for distribution` (+2 more) | coa15-tests-ch1.l4 |
| s 669(2) | 8884-8885 | encoded | `s 669(2) the value to read for the purposes of s 669(1)`; `s 669(1) the amount to be transferred to the reserve fund` | coa15-tests-ch1.l4 |
| heading: Charges of public company on own shares | 8886-8886 | inert (reason 1) | a heading: not operative |  |
| s 670 Public companies: general rule agains... | 8887-8894 | encoded | `s 670(3) the charge is permitted`; `s 670(1) the lien or charge is void` (+3 more) | coa15-tests-ch1.l4 |
| s 670(1) | 8888-8888 | encoded | `s 670(1) the lien or charge is void`; `s 670(1) lien or charge of a company on its own shares` | coa15-tests-ch1.l4 |
| s 670(2) | 8889-8889 | encoded | `s 670(1) lien or charge of a company on its own shares` | coa15-tests-ch1.l4 |
| s 670(3) | 8890-8893 | encoded | `s 670(3) the charge is permitted`; `s 670(2) the charge is permitted` (+1 more) | coa15-tests-ch1.l4 |
| s 670(3)(a) | 8891-8891 | encoded | `s 670(3) the charge is permitted`; `s 670(1) lien or charge of a company on its own shares` | coa15-tests-ch1.l4 |
| s 670(3)(b) | 8892-8893 | encoded | `s 670(3) the charge is permitted`; `s 670(1) lien or charge of a company on its own shares` | coa15-tests-ch1.l4 |
| s 670(4) | 8894-8894 | encoded | `s 670(4) the charge is permitted`; `s 670(1) lien or charge of a company on its own shares` | coa15-tests-ch1.l4 |
| heading: Supplementary provisions | 8895-8895 | inert (reason 1) | a heading: not operative |  |
| s 671 Interests to be disregarded in determ... | 8896-8900 | encoded | `s 671 the interest is to be disregarded in determining whether the comp...` | coa15-tests-ch1.l4 |
| s 672 Residual interest under pension schem... | 8901-8914 | encoded | `s 672(2) the right is a residual interest`; `s 672(4) the residual interest vests in possession` (+5 more) | coa15-tests-ch1.l4 |
| s 672(1) | 8902-8902 | encoded | `s 672(1) the residual interest is to be disregarded` | coa15-tests-ch1.l4 |
| s 672(2) | 8903-8906 | encoded | `s 672(2) the right is a residual interest` | coa15-tests-ch1.l4 |
| term: “residual interest” | 8903-8903 | encoded | `s 672(2) the right is a residual interest` | coa15-tests-ch1.l4 |
| s 672(2)(a) | 8904-8904 | encoded | `s 672(2) the right is a residual interest` | coa15-tests-ch1.l4 |
| s 672(2)(b) | 8905-8905 | encoded | `s 672(2) the right is a residual interest` | coa15-tests-ch1.l4 |
| s 672(2)(c) | 8906-8906 | encoded | `s 672(2) the right is a residual interest` | coa15-tests-ch1.l4 |
| s 672(3) | 8907-8909 | encoded | `s 672(3)(a) the right is a right within subsection (2)`; `s 672(3)(b) the liability is a liability arising under the scheme` | coa15-tests-ch1.l4 |
| s 672(3)(a) | 8908-8908 | encoded | `s 672(3)(a) the right is a right within subsection (2)` | coa15-tests-ch1.l4 |
| s 672(3)(b) | 8909-8909 | encoded | `s 672(3)(b) the liability is a liability arising under the scheme` | coa15-tests-ch1.l4 |
| s 672(4) | 8910-8912 | encoded | `s 672(4) the residual interest vests in possession` | coa15-tests-ch1.l4 |
| term: “vests in possession” (residual interest) | 8910-8912 | encoded | `s 672(4) the residual interest vests in possession` | coa15-tests-ch1.l4 |
| s 672(4)(a) | 8911-8911 | encoded | `s 672(4) the residual interest vests in possession` | coa15-tests-ch1.l4 |
| s 672(4)(b) | 8912-8912 | encoded | `s 672(4) the residual interest vests in possession` | coa15-tests-ch1.l4 |
| s 672(5) | 8913-8913 | encoded | `s 672(5) the date on which sections 660 and 661 are treated as applying...` | coa15-tests-ch1.l4 |
| s 672(6) | 8914-8914 | encoded | `s 672(6) the date on which sections 662 to 668 are treated as applying ...` | coa15-tests-ch1.l4 |
| s 673 Employer's charges and other rights o... | 8915-8921 | encoded | `s 673(1)(a) the charge, lien or set-off is to be disregarded`; `s 673(1)(b) the right is to be disregarded` (+1 more) | coa15-tests-ch1.l4 |
| s 673(1) | 8916-8920 | encoded | `s 673(1)(a) the charge, lien or set-off is to be disregarded`; `s 673(1)(b) the right is to be disregarded` | coa15-tests-ch1.l4 |
| s 673(1)(a) | 8917-8917 | encoded | `s 673(1)(a) the charge, lien or set-off is to be disregarded`; `s 673(1)(b) the right is to be disregarded` | coa15-tests-ch1.l4 |
| s 673(1)(b) | 8918-8920 | encoded | `s 673(1)(a) the charge, lien or set-off is to be disregarded`; `s 673(1)(b) the right is to be disregarded` | coa15-tests-ch1.l4 |
| s 673(2) | 8921-8921 | encoded | `s 673(2) the charge, lien or set-off is to be disregarded` | coa15-tests-ch1.l4 |
| s 674 Rights as personal representative or ... | 8922-8925 | encoded | `s 674 the right is to be disregarded` | coa15-tests-ch1.l4 |
| s 674(a) | 8924-8924 | encoded | `s 674 the right is to be disregarded` | coa15-tests-ch1.l4 |
| s 674(b) | 8925-8925 | encoded | `s 674 the right is to be disregarded` | coa15-tests-ch1.l4 |
| s 675 Meaning of “pension scheme” | 8926-8928 | encoded | `s 675(1) the scheme is a pension scheme`; `s 675(2) the benefit is a relevant benefit` | coa15-tests-ch1.l4 |
| s 675(1) | 8927-8927 | encoded | `s 675(1) the scheme is a pension scheme` | coa15-tests-ch1.l4 |
| term: “pension scheme” | 8927-8927 | encoded | `s 675(1) the scheme is a pension scheme` | coa15-tests-ch1.l4 |
| s 675(2) | 8928-8928 | encoded | `s 675(2) the benefit is a relevant benefit` | coa15-tests-ch1.l4 |
| term: “relevant benefits” | 8928-8928 | encoded | `s 675(2) the benefit is a relevant benefit` | coa15-tests-ch1.l4 |
| s 676 Application of provisions to directors | 8929-8930 | encoded | `s 676 the director is treated as employed by the company` | coa15-tests-ch1.l4 |
| term: “employer” | 8930-8930 | encoded | `s 676 the director is treated as employed by the company` | coa15-tests-ch1.l4 |
| term: “employee” | 8930-8930 | encoded | `s 676 the director is treated as employed by the company` | coa15-tests-ch1.l4 |
| heading: Chapter 2 — Financial assistance for purchase of own shares | 8931-8931 | inert (reason 1) | a heading: not operative |  |
| heading: Introductory | 8932-8932 | inert (reason 1) | a heading: not operative |  |
| s 677 Meaning of “financial assistance” | 8933-8948 | encoded | `s 677(1) the assistance given by the company is financial assistance`; `s 677(3) the aggregate amount of the company's liabilities` (+1 more) | coa15-tests-ch2.l4 |
| s 677(1) | 8934-8944 | encoded | `s 677(1) the assistance given by the company is financial assistance` | coa15-tests-ch2.l4 |
| term: “financial assistance” | 8934-8934 | encoded | `s 677(1) the assistance given by the company is financial assistance` | coa15-tests-ch2.l4 |
| s 677(1)(a) | 8935-8935 | encoded | `s 677(1) the assistance given by the company is financial assistance` | coa15-tests-ch2.l4 |
| s 677(1)(b) | 8936-8938 | encoded | `s 677(1) the assistance given by the company is financial assistance` | coa15-tests-ch2.l4 |
| s 677(1)(c) | 8939-8941 | encoded | `s 677(1) the assistance given by the company is financial assistance` | coa15-tests-ch2.l4 |
| s 677(1)(d) | 8942-8944 | encoded | `s 677(1) the assistance given by the company is financial assistance` | coa15-tests-ch2.l4 |
| s 677(2) | 8945-8945 | encoded | `s 677(2) the net assets of the company` | coa15-tests-ch2.l4 |
| term: “Net assets” | 8945-8945 | encoded | `s 677(2) the net assets of the company` | coa15-tests-ch2.l4 |
| s 677(3) | 8946-8948 | encoded | `s 677(3) the aggregate amount of the company's liabilities` | coa15-tests-ch2.l4 |
| s 677(3)(a) | 8947-8947 | encoded | `s 677(3) the aggregate amount of the company's liabilities` | coa15-tests-ch2.l4 |
| s 677(3)(b) | 8948-8948 | encoded | `s 677(3) the aggregate amount of the company's liabilities` | coa15-tests-ch2.l4 |
| heading: Circumstances in which financial assistance prohibited | 8949-8949 | inert (reason 1) | a heading: not operative |  |
| s 678 Assistance for acquisition of shares ... | 8950-8964 | encoded | `s 678(2) subsection (1) does not prohibit the assistance`; `s 678(3) it is not lawful for the company to give the financial assista...` (+5 more) | coa15-tests-ch2.l4 |
| s 678(1) | 8951-8951 | encoded | `s 678(1) it is not lawful for the company to give the financial assistance`; `s 678(1) the company shant give the financial assistance` | coa15-tests-ch2.l4 |
| s 678(2) | 8952-8955 | encoded | `s 678(2) subsection (1) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 678(2)(a) | 8953-8953 | encoded | `s 678(2) subsection (1) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 678(2)(b) | 8954-8955 | encoded | `s 678(2) subsection (1) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 678(3) | 8956-8959 | encoded | `s 678(3) it is not lawful for the company to give the financial assista...`; `s 678(3) the company shant give the financial assistance to reduce or d...` | coa15-tests-ch2.l4 |
| s 678(3)(a) | 8957-8957 | encoded | `s 678(3) it is not lawful for the company to give the financial assista...`; `s 678(3) the company shant give the financial assistance to reduce or d...` | coa15-tests-ch2.l4 |
| s 678(3)(b) | 8958-8959 | encoded | `s 678(3) it is not lawful for the company to give the financial assista...`; `s 678(3) the company shant give the financial assistance to reduce or d...` | coa15-tests-ch2.l4 |
| s 678(4) | 8960-8963 | encoded | `s 678(4) subsection (3) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 678(4)(a) | 8961-8961 | encoded | `s 678(4) subsection (3) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 678(4)(b) | 8962-8963 | encoded | `s 678(4) subsection (3) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 678(5) | 8964-8964 | encoded | `s 678(5) the assistance is prohibited by section 678 as it has effect s...` | coa15-tests-ch2.l4 |
| s 679 Assistance by public company for acqu... | 8965-8979 | encoded | `s 679(2) subsection (1) does not prohibit the assistance`; `s 679(3) it is not lawful for the public company to give the financial ...` (+5 more) | coa15-tests-ch2.l4 |
| s 679(1) | 8966-8966 | encoded | `s 679(1) it is not lawful for the public company to give the financial ...`; `s 679(1) the public company shant give the financial assistance` | coa15-tests-ch2.l4 |
| s 679(2) | 8967-8970 | encoded | `s 679(2) subsection (1) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 679(2)(a) | 8968-8968 | encoded | `s 679(2) subsection (1) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 679(2)(b) | 8969-8970 | encoded | `s 679(2) subsection (1) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 679(3) | 8971-8974 | encoded | `s 679(3) it is not lawful for the public company to give the financial ...`; `s 679(3) the public company shant give the financial assistance to redu...` | coa15-tests-ch2.l4 |
| s 679(3)(a) | 8972-8972 | encoded | `s 679(3) it is not lawful for the public company to give the financial ...`; `s 679(3) the public company shant give the financial assistance to redu...` | coa15-tests-ch2.l4 |
| s 679(3)(b) | 8973-8974 | encoded | `s 679(3) it is not lawful for the public company to give the financial ...`; `s 679(3) the public company shant give the financial assistance to redu...` | coa15-tests-ch2.l4 |
| s 679(4) | 8975-8978 | encoded | `s 679(4) subsection (3) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 679(4)(a) | 8976-8976 | encoded | `s 679(4) subsection (3) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 679(4)(b) | 8977-8978 | encoded | `s 679(4) subsection (3) does not prohibit the assistance` | coa15-tests-ch2.l4 |
| s 679(5) | 8979-8979 | encoded | `s 679(5) the assistance is prohibited by section 679 as it has effect s...` | coa15-tests-ch2.l4 |
| s 680 Prohibited financial assistance an of... | 8980-8988 | fork F-not-in-default | `s 680(2) the penalty on conviction`; `s 680(1) the person commits an offence` | coa15-tests-ch2.l4 |
| s 680(1) | 8981-8983 | fork F-not-in-default | `s 680(1) the person commits an offence` | coa15-tests-ch2.l4 |
| s 680(1)(a) | 8982-8982 | fork F-not-in-default | `s 680(1) the person commits an offence` | coa15-tests-ch2.l4 |
| s 680(1)(b) | 8983-8983 | fork F-not-in-default | `s 680(1) the person commits an offence` | coa15-tests-ch2.l4 |
| s 680(2) | 8984-8988 | encoded | `s 680(2) the penalty on conviction` | coa15-tests-ch2.l4 |
| s 680(2)(a) | 8985-8985 | encoded | `s 680(2) the penalty on conviction` | coa15-tests-ch2.l4 |
| s 680(2)(b) | 8986-8988 | encoded | `s 680(2) the penalty on conviction` | coa15-tests-ch2.l4 |
| heading: Exceptions from prohibition | 8989-8989 | inert (reason 1) | a heading: not operative |  |
| s 681 Unconditional exceptions | 8990-9001 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(1) | 8991-8991 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2) | 8992-9001 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(a) | 8993-8995 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(b) | 8996-8996 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(c) | 8997-8997 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(d) | 8998-8998 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(e) | 8999-8999 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(f) | 9000-9000 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 681(2)(g) | 9001-9001 | fork F-are | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 682 Conditional exceptions | 9002-9019 | fork F-are, F-other-than | `s 682(2) the transaction is one to which section 682 applies`; `s 682(1) neither section 678 nor section 679 prohibits the transaction` (+7 more) | coa15-tests-ch2.l4 |
| s 682(1) | 9003-9007 | encoded | `s 682(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 682(1)(a) | 9004-9004 | encoded | `s 682(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 682(1)(b) | 9005-9007 | encoded | `s 682(1) neither section 678 nor section 679 prohibits the transaction` | coa15-tests-ch2.l4 |
| s 682(2) | 9008-9014 | fork F-are, F-other-than | `s 682(2) the transaction is one to which section 682 applies`; `s 682(2)(c) the transaction is assistance in connection with transactio...` (+3 more) | coa15-tests-ch2.l4 |
| s 682(2)(a) | 9009-9009 | fork F-are | `s 682(2)(a) the transaction is a lending of money in the ordinary course`; `s 682(2) the transaction is one to which section 682 applies` | coa15-tests-ch2.l4 |
| s 682(2)(b) | 9010-9010 | fork F-are | `s 682(2)(b) the transaction is the provision of assistance for the purp...`; `s 682(2) the transaction is one to which section 682 applies` | coa15-tests-ch2.l4 |
| s 682(2)(c) | 9011-9013 | fork F-are | `s 682(2)(c) the transaction is assistance in connection with transactio...`; `s 682(2) the transaction is one to which section 682 applies` | coa15-tests-ch2.l4 |
| s 682(2)(d) | 9014-9014 | fork F-are, F-other-than | `s 682(2)(d) the transaction is a loan to a person other than a director...`; `s 682(2) the transaction is one to which section 682 applies` | coa15-tests-ch2.l4 |
| s 682(3) | 9015-9015 | encoded | `s 682(3) the net assets of the company` | coa15-tests-ch2.l4 |
| term: “net assets” | 9015-9015 | encoded | `s 682(3) the net assets of the company` | coa15-tests-ch2.l4 |
| s 682(4) | 9016-9018 | encoded | `s 682(4) the aggregate of the company's liabilities` | coa15-tests-ch2.l4 |
| s 682(4)(a) | 9017-9017 | encoded | `s 682(4) the aggregate of the company's liabilities` | coa15-tests-ch2.l4 |
| s 682(4)(b) | 9018-9018 | encoded | `s 682(4) the aggregate of the company's liabilities` | coa15-tests-ch2.l4 |
| term: “liabilities” | 9018-9018 | encoded | `s 682(4) the aggregate of the company's liabilities` | coa15-tests-ch2.l4 |
| s 682(5) | 9019-9019 | encoded | `s 682(5) the company is in the same group as the other company` | coa15-tests-ch2.l4 |
| term: “in the same group” (companies) | 9019-9019 | encoded | `s 682(5) the company is in the same group as the other company` | coa15-tests-ch2.l4 |
| heading: Supplementary | 9020-9020 | inert (reason 1) | a heading: not operative |  |
| s 683 Definitions for this Chapter | 9021-9029 | encoded | `s 683(1) the distributable profits in relation to the giving of the fin...`; `s 683(1)(a) the assistance is covered by the distributable profits` (+3 more) | coa15-tests-ch2.l4 |
| s 683(1) | 9022-9026 | encoded | `s 683(1) the distributable profits in relation to the giving of the fin...`; `s 683(1)(a) the assistance is covered by the distributable profits` (+1 more) | coa15-tests-ch2.l4 |
| term: “distributable profits” | 9023-9023 | encoded | `s 683(1) the distributable profits in relation to the giving of the fin...`; `s 683(1)(a) the assistance is covered by the distributable profits` | coa15-tests-ch2.l4 |
| s 683(1)(a) | 9024-9024 | encoded | `s 683(1) the distributable profits in relation to the giving of the fin...`; `s 683(1)(a) the assistance is covered by the distributable profits` | coa15-tests-ch2.l4 |
| s 683(1)(b) | 9025-9026 | encoded | `s 683(1) the payment is a distribution for the purposes of Chapter 2`; `s 683(1) the distributable profits in relation to the giving of the fin...` (+1 more) | coa15-tests-ch2.l4 |
| term: “distribution” | 9026-9026 | encoded | `s 683(1) the payment is a distribution for the purposes of Chapter 2` | coa15-tests-ch2.l4 |
| s 683(2) | 9027-9029 | encoded | `s 683(2)(a) the person incurs a liability`; `s 683(2)(b) the assistance is given for the purposes of reducing or dis...` | coa15-tests-ch2.l4 |
| s 683(2)(a) | 9028-9028 | encoded | `s 683(2)(a) the person incurs a liability` | coa15-tests-ch2.l4 |
| s 683(2)(b) | 9029-9029 | encoded | `s 683(2)(b) the assistance is given for the purposes of reducing or dis...` | coa15-tests-ch2.l4 |
| heading: Chapter 3 — Redeemable shares | 9030-9030 | inert (reason 1) | a heading: not operative |  |
| s 684 Power of limited company to issue red... | 9031-9035 | encoded | `s 684(1) the company may issue redeemable shares`; `s 684(1) the shares are redeemable shares` (+3 more) | coa15-tests-ch3.l4 |
| s 684(1) | 9032-9032 | encoded | `s 684(1) the company may issue redeemable shares`; `s 684(1) the shares are redeemable shares` | coa15-tests-ch3.l4 |
| term: “redeemable shares” | 9032-9032 | encoded | `s 684(1) the company may issue redeemable shares`; `s 684(1) the shares are redeemable shares` | coa15-tests-ch3.l4 |
| s 684(2) | 9033-9033 | encoded | `s 684(2) the articles may exclude or restrict the issue of redeemable s...` | coa15-tests-ch3.l4 |
| s 684(3) | 9034-9034 | encoded | `s 684(3) the public limited company may issue redeemable shares` | coa15-tests-ch3.l4 |
| s 684(4) | 9035-9035 | encoded | `s 684(4) the issue of redeemable shares is barred` | coa15-tests-ch3.l4 |
| s 685 Terms and manner of redemption | 9036-9044 | fork F-grant-685-1 | `s 685(1) the directors may determine the terms, conditions and manner o...`; `s 685(3)(b) the obligation to state the rights extends to the terms, co...` (+4 more) | coa15-tests-ch3.l4 |
| s 685(1) | 9037-9039 | fork F-grant-685-1 | `s 685(1) the directors may determine the terms, conditions and manner o...` | coa15-tests-ch3.l4 |
| s 685(1)(a) | 9038-9038 | fork F-grant-685-1 | `s 685(1) the directors may determine the terms, conditions and manner o...` | coa15-tests-ch3.l4 |
| s 685(1)(b) | 9039-9039 | fork F-grant-685-1 | `s 685(1) the directors may determine the terms, conditions and manner o...` | coa15-tests-ch3.l4 |
| s 685(2) | 9040-9040 | encoded | `s 685(2) the resolution is a good resolution under subsection (1)(b)` | coa15-tests-ch3.l4 |
| s 685(3) | 9041-9043 | encoded | `s 685(3)(b) the obligation to state the rights extends to the terms, co...`; `s 685(3)(a) the directors determined the terms before the shares were a...` (+1 more) | coa15-tests-ch3.l4 |
| s 685(3)(a) | 9042-9042 | encoded | `s 685(3)(a) the directors determined the terms before the shares were a...`; `s 685(3)(a) the directors must determine the terms before the shares ar...` (+1 more) | coa15-tests-ch3.l4 |
| s 685(3)(b) | 9043-9043 | encoded | `s 685(3)(b) the obligation to state the rights extends to the terms, co...` | coa15-tests-ch3.l4 |
| s 685(4) | 9044-9044 | encoded | `s 685(4) the terms, conditions and manner of redemption must be stated ...` | coa15-tests-ch3.l4 |
| s 686 Payment for redeemable shares | 9045-9048 | encoded | `s 686(1) the redemption is barred`; `s 686(2) the terms of redemption may provide for payment on a later date` (+2 more) | coa15-tests-ch3.l4 |
| s 686(1) | 9046-9046 | encoded | `s 686(1) the redemption is barred` | coa15-tests-ch3.l4 |
| s 686(2) | 9047-9047 | encoded | `s 686(2) the terms of redemption may provide for payment on a later date` | coa15-tests-ch3.l4 |
| s 686(3) | 9048-9048 | encoded | `s 686(3) the company must pay for the shares on redemption`; `s 686(3) the shares must be paid for on redemption` | coa15-tests-ch3.l4 |
| s 687 Financing of redemption | 9049-9060 | fork F-signpost | `s 687(4) the most of the premium that may be paid out of the proceeds o...`; `s 687(2) the redemption is out of a source the section permits` (+4 more) | coa15-tests-ch3.l4 |
| s 687(1) | 9050-9050 | encoded | `s 687(1) the private limited company may redeem the shares out of capital` | coa15-tests-ch3.l4 |
| s 687(2) | 9051-9053 | encoded | `s 687(2) the redemption is out of a source the section permits` | coa15-tests-ch3.l4 |
| s 687(2)(a) | 9052-9052 | encoded | `s 687(2) the redemption is out of a source the section permits` | coa15-tests-ch3.l4 |
| s 687(2)(b) | 9053-9053 | encoded | `s 687(2) the redemption is out of a source the section permits` | coa15-tests-ch3.l4 |
| s 687(3) | 9054-9054 | encoded | `s 687(3) the part of the premium that must be paid out of distributable...` | coa15-tests-ch3.l4 |
| s 687(4) | 9055-9058 | encoded | `s 687(4) the most of the premium that may be paid out of the proceeds o...` | coa15-tests-ch3.l4 |
| s 687(4)(a) | 9056-9056 | encoded | `s 687(4) the most of the premium that may be paid out of the proceeds o...` | coa15-tests-ch3.l4 |
| s 687(4)(b) | 9057-9058 | encoded | `s 687(4) the most of the premium that may be paid out of the proceeds o...` | coa15-tests-ch3.l4 |
| s 687(5) | 9059-9059 | encoded | `s 687(5) the amount of the company's share premium account after the pa...` | coa15-tests-ch3.l4 |
| s 687(6) | 9060-9060 | fork F-signpost | `s 687(6) the limits of section 687 on the source of payment are displac...` | coa15-tests-ch3.l4 |
| s 688 Redeemed shares treated as cancelled | 9061-9064 | encoded | `s 688(b) the amount of the company's issued share capital after the red...`; `s 688(a) the shares are treated as cancelled` | coa15-tests-ch3.l4 |
| s 688(a) | 9063-9063 | encoded | `s 688(a) the shares are treated as cancelled`; `s 688(b) the amount of the company's issued share capital after the red...` | coa15-tests-ch3.l4 |
| s 688(b) | 9064-9064 | encoded | `s 688(b) the amount of the company's issued share capital after the red...` | coa15-tests-ch3.l4 |
| s 689 Notice to registrar of redemption | 9065-9080 | fork F-month, F-must, F-not-in-default | `s 689(3) the statement of capital states what the section requires`; `s 689(4) the person commits an offence` (+5 more) | coa15-tests-ch3.l4 |
| s 689(1) | 9066-9066 | fork F-month | `s 689(1) the company must give notice to the registrar`; `s 689(1) the last day for giving notice to the registrar` (+1 more) | coa15-tests-ch3.l4 |
| s 689(2) | 9067-9067 | fork F-must | `s 689(2) the notice is accompanied by a statement of capital` | coa15-tests-ch3.l4 |
| s 689(3) | 9068-9076 | encoded | `s 689(3) the statement of capital states what the section requires` | coa15-tests-ch3.l4 |
| s 689(3)(a) | 9069-9069 | encoded | `s 689(3) the statement of capital states what the section requires` | coa15-tests-ch3.l4 |
| s 689(3)(b) | 9070-9070 | encoded | `s 689(3) the statement of capital states what the section requires` | coa15-tests-ch3.l4 |
| s 689(3)(ba) | 9071-9071 | encoded | `s 689(3) the statement of capital states what the section requires` | coa15-tests-ch3.l4 |
| s 689(3)(c) | 9072-9075 | encoded | `s 689(3) the statement of capital states what the section requires` | coa15-tests-ch3.l4 |
| s 689(3)(d) | 9076-9076 | repealed or blank in this text | the text shows a row of dots |  |
| s 689(4) | 9077-9079 | fork F-not-in-default | `s 689(4) the person commits an offence` | coa15-tests-ch3.l4 |
| s 689(4)(a) | 9078-9078 | fork F-not-in-default | `s 689(4) the person commits an offence` | coa15-tests-ch3.l4 |
| s 689(4)(b) | 9079-9079 | fork F-not-in-default | `s 689(4) the person commits an offence` | coa15-tests-ch3.l4 |
| s 689(5) | 9080-9080 | encoded | `s 689(5) the penalty on conviction` | coa15-tests-ch3.l4 |
| heading: Chapter 4 — Purchase of own shares | 9081-9081 | inert (reason 1) | a heading: not operative |  |
| heading: General provisions | 9082-9082 | inert (reason 1) | a heading: not operative |  |
| s 690 Power of limited company to purchase ... | 9083-9087 | fork F-grant-690-1 | `s 690(1) the limited company may purchase its own shares`; `s 690(2) the purchase is barred` | coa15-tests-ch4.l4 |
| s 690(1) | 9084-9086 | fork F-grant-690-1 | `s 690(1) the limited company may purchase its own shares` | coa15-tests-ch4.l4 |
| s 690(1)(a) | 9085-9085 | fork F-grant-690-1 | `s 690(1) the limited company may purchase its own shares` | coa15-tests-ch4.l4 |
| s 690(1)(b) | 9086-9086 | fork F-grant-690-1 | `s 690(1) the limited company may purchase its own shares` | coa15-tests-ch4.l4 |
| s 690(2) | 9087-9087 | encoded | `s 690(2) the purchase is barred` | coa15-tests-ch4.l4 |
| s 691 Payment for purchase of own shares | 9088-9091 | encoded | `s 691(1) the purchase is barred`; `s 691(2) the company must pay for the shares on purchase` (+2 more) | coa15-tests-ch4.l4 |
| s 691(1) | 9089-9089 | encoded | `s 691(1) the purchase is barred` | coa15-tests-ch4.l4 |
| s 691(2) | 9090-9090 | encoded | `s 691(2) the company must pay for the shares on purchase`; `s 691(2) the shares must be paid for on purchase` | coa15-tests-ch4.l4 |
| s 691(3) | 9091-9091 | encoded | `s 691(3) subsection (2) does not apply` | coa15-tests-ch4.l4 |
| s 692 Financing of purchase of own shares | 9092-9109 | fork F-must, F-signpost | `s 692(2)(a) the purchase is out of a source the section permits`; `s 692(2)(b) the part of the premium that must be paid out of distributa...` (+7 more) | coa15-tests-ch4.l4 |
| s 692(1) | 9093-9093 | encoded | `s 692(1) the private limited company may purchase its own shares out of...` | coa15-tests-ch4.l4 |
| s 692(1ZA) | 9094-9096 | encoded | `s 692(1ZA) the most the company may pay out of capital in the financial...` | coa15-tests-ch4.l4 |
| s 692(1ZA)(a) | 9095-9095 | encoded | `s 692(1ZA) the most the company may pay out of capital in the financial...` | coa15-tests-ch4.l4 |
| s 692(1ZA)(b) | 9096-9096 | encoded | `s 692(1ZA) the most the company may pay out of capital in the financial...` | coa15-tests-ch4.l4 |
| s 692(1A) | 9097-9097 | encoded | `s 692(1A) the value in sterling of the share capital` | coa15-tests-ch4.l4 |
| s 692(1B) | 9098-9098 | fork F-must | `s 692(1B) the rate is the rate the subsection requires` | coa15-tests-ch4.l4 |
| s 692(2) | 9099-9103 | encoded | `s 692(2)(a) the purchase is out of a source the section permits`; `s 692(2)(b) the part of the premium that must be paid out of distributa...` | coa15-tests-ch4.l4 |
| s 692(2)(a) | 9100-9102 | encoded | `s 692(2)(a) the purchase is out of a source the section permits`; `s 692(2)(b) the part of the premium that must be paid out of distributa...` | coa15-tests-ch4.l4 |
| s 692(2)(b) | 9103-9103 | encoded | `s 692(2)(a) the purchase is out of a source the section permits`; `s 692(2)(b) the part of the premium that must be paid out of distributa...` | coa15-tests-ch4.l4 |
| s 692(3) | 9104-9107 | encoded | `s 692(3) the most of the premium that may be paid out of the proceeds o...` | coa15-tests-ch4.l4 |
| s 692(3)(a) | 9105-9105 | encoded | `s 692(3) the most of the premium that may be paid out of the proceeds o...` | coa15-tests-ch4.l4 |
| s 692(3)(b) | 9106-9107 | encoded | `s 692(3) the most of the premium that may be paid out of the proceeds o...` | coa15-tests-ch4.l4 |
| s 692(4) | 9108-9108 | encoded | `s 692(4) the amount of the company's share premium account after the pa...` | coa15-tests-ch4.l4 |
| s 692(5) | 9109-9109 | fork F-signpost | `s 692(5) the limits of section 692 on the source of payment are displac...` | coa15-tests-ch4.l4 |
| heading: Authority for purchase of own shares | 9110-9110 | inert (reason 1) | a heading: not operative |  |
| s 693 Authority for purchase of own shares | 9111-9124 | encoded | `s 693(3) the shares are subject to a marketing arrangement on the exchange`; `s 693(1) the limited company may make the purchase` (+3 more) | coa15-tests-ch4.l4 |
| s 693(1) | 9112-9114 | encoded | `s 693(1) the limited company may make the purchase` | coa15-tests-ch4.l4 |
| s 693(1)(a) | 9113-9113 | encoded | `s 693(1) the limited company may make the purchase` | coa15-tests-ch4.l4 |
| s 693(1)(b) | 9114-9114 | encoded | `s 693(1) the limited company may make the purchase` | coa15-tests-ch4.l4 |
| s 693(2) | 9115-9117 | encoded | `s 693(2) the purchase is an off-market purchase` | coa15-tests-ch4.l4 |
| term: “off-market” | 9115-9117 | encoded | `s 693(2) the purchase is an off-market purchase` | coa15-tests-ch4.l4 |
| s 693(2)(a) | 9116-9116 | encoded | `s 693(2) the purchase is an off-market purchase` | coa15-tests-ch4.l4 |
| s 693(2)(b) | 9117-9117 | encoded | `s 693(2) the purchase is an off-market purchase` | coa15-tests-ch4.l4 |
| s 693(3) | 9118-9122 | encoded | `s 693(3) the shares are subject to a marketing arrangement on the exchange` | coa15-tests-ch4.l4 |
| term: “marketing arrangement” (subject to a marketing arrangement) | 9118-9122 | encoded | `s 693(3) the shares are subject to a marketing arrangement on the exchange` | coa15-tests-ch4.l4 |
| s 693(3)(a) | 9119-9119 | encoded | `s 693(3) the shares are subject to a marketing arrangement on the exchange` | coa15-tests-ch4.l4 |
| s 693(3)(b) | 9120-9122 | encoded | `s 693(3) the shares are subject to a marketing arrangement on the exchange` | coa15-tests-ch4.l4 |
| s 693(4) | 9123-9123 | encoded | `s 693(4) the purchase is a market purchase` | coa15-tests-ch4.l4 |
| term: “market purchase” | 9123-9123 | encoded | `s 693(4) the purchase is a market purchase` | coa15-tests-ch4.l4 |
| s 693(5) | 9124-9124 | encoded | `s 693(5) the exchange is a recognised investment exchange` | coa15-tests-ch4.l4 |
| term: “recognised investment exchange” | 9124-9124 | encoded | `s 693(5) the exchange is a recognised investment exchange` | coa15-tests-ch4.l4 |
| s 693A Authority for off-market purchase for... | 9125-9141 | fork F-grant-693A-1, F-grant-693A-6, F-must | `s 693A(2) the authority may take that form`; `s 693A(3) the authority contains what the subsection requires` (+7 more) | coa15-tests-ch4.l4 |
| s 693A(1) | 9126-9126 | fork F-grant-693A-1 | `s 693A(1) the company may make the off-market purchase` | coa15-tests-ch4.l4 |
| s 693A(2) | 9127-9129 | encoded | `s 693A(2) the authority may take that form` | coa15-tests-ch4.l4 |
| s 693A(2)(a) | 9128-9128 | encoded | `s 693A(2) the authority may take that form` | coa15-tests-ch4.l4 |
| s 693A(2)(b) | 9129-9129 | encoded | `s 693A(2) the authority may take that form` | coa15-tests-ch4.l4 |
| s 693A(3) | 9130-9132 | fork F-must | `s 693A(3) the authority contains what the subsection requires` | coa15-tests-ch4.l4 |
| s 693A(3)(a) | 9131-9131 | fork F-must | `s 693A(3) the authority contains what the subsection requires` | coa15-tests-ch4.l4 |
| s 693A(3)(b) | 9132-9132 | fork F-must | `s 693A(3) the authority contains what the subsection requires` | coa15-tests-ch4.l4 |
| s 693A(4) | 9133-9133 | encoded | `s 693A(4) the authority may be varied, revoked or renewed` | coa15-tests-ch4.l4 |
| s 693A(5) | 9134-9134 | fork F-must | `s 693A(5) the latest date on which the authority may be specified to ex...`; `s 693A(5) the resolution specifies a date of expiry that is not later t...` | coa15-tests-ch4.l4 |
| s 693A(6) | 9135-9137 | fork F-grant-693A-6 | `s 693A(6) the company may make a purchase of its own shares after the e...` | coa15-tests-ch4.l4 |
| s 693A(6)(a) | 9136-9136 | fork F-grant-693A-6 | `s 693A(6) the company may make a purchase of its own shares after the e...` | coa15-tests-ch4.l4 |
| s 693A(6)(b) | 9137-9137 | fork F-grant-693A-6 | `s 693A(6) the company may make a purchase of its own shares after the e...` | coa15-tests-ch4.l4 |
| s 693A(7) | 9138-9140 | encoded | `s 693A(7) the resolution may determine the price in that way` | coa15-tests-ch4.l4 |
| s 693A(7)(a) | 9139-9139 | encoded | `s 693A(7) the resolution may determine the price in that way` | coa15-tests-ch4.l4 |
| s 693A(7)(b) | 9140-9140 | encoded | `s 693A(7) the resolution may determine the price in that way` | coa15-tests-ch4.l4 |
| s 693A(8) | 9141-9141 | encoded | `s 693A(8) Chapter 3 of Part 3 applies to the resolution` | coa15-tests-ch4.l4 |
| heading: Authority for off-market purchase | 9142-9142 | inert (reason 1) | a heading: not operative |  |
| s 694 Authority for off-market purchase | 9143-9153 | fork F-must, F-omitted-word | `s 694(2) the contract is approved in the way the subsection requires`; `s 694(6) the resolution is barred by section 695 or section 696` (+4 more) | coa15-tests-ch4.l4 |
| s 694(1) | 9144-9144 | encoded | `s 694(1) the company may make the off-market purchase` | coa15-tests-ch4.l4 |
| s 694(2) | 9145-9147 | fork F-must, F-omitted-word | `s 694(2) the contract is approved in the way the subsection requires` | coa15-tests-ch4.l4 |
| s 694(2)(a) | 9146-9146 | fork F-must, F-omitted-word | `s 694(2) the contract is approved in the way the subsection requires` | coa15-tests-ch4.l4 |
| s 694(2)(b) | 9147-9147 | fork F-must, F-omitted-word | `s 694(2) the contract is approved in the way the subsection requires` | coa15-tests-ch4.l4 |
| s 694(3) | 9148-9148 | encoded | `s 694(3) the contract is a contract within section 694` | coa15-tests-ch4.l4 |
| s 694(4) | 9149-9149 | fork F-omitted-word | `s 694(4) the authority may be varied, revoked or renewed` | coa15-tests-ch4.l4 |
| s 694(5) | 9150-9150 | encoded | `s 694(5) the resolution specifies a date of expiry that is not later th...` | coa15-tests-ch4.l4 |
| s 694(6) | 9151-9153 | encoded | `s 694(6) the resolution is barred by section 695 or section 696` | coa15-tests-ch4.l4 |
| s 695 Resolution authorising off-market pur... | 9154-9163 | encoded | `s 695(3) the resolution is not effective`; `s 695(1) this section applies to the resolution` (+4 more) | coa15-tests-ch4.l4 |
| s 695(1) | 9155-9155 | encoded | `s 695(1) this section applies to the resolution` | coa15-tests-ch4.l4 |
| s 695(2) | 9156-9156 | encoded | `s 695(2) the member is not an eligible member` | coa15-tests-ch4.l4 |
| s 695(3) | 9157-9159 | encoded | `s 695(3) the resolution is not effective` | coa15-tests-ch4.l4 |
| s 695(3)(a) | 9158-9158 | encoded | `s 695(3) the resolution is not effective` | coa15-tests-ch4.l4 |
| s 695(3)(b) | 9159-9159 | encoded | `s 695(3) the resolution is not effective` | coa15-tests-ch4.l4 |
| s 695(4) | 9160-9163 | encoded | `s 695(4)(a) the member is regarded as exercising the voting rights`; `s 695(4)(b) the person may demand a poll on that question` (+1 more) | coa15-tests-ch4.l4 |
| s 695(4)(a) | 9161-9161 | encoded | `s 695(4)(a) the member is regarded as exercising the voting rights` | coa15-tests-ch4.l4 |
| s 695(4)(b) | 9162-9162 | encoded | `s 695(4)(b) the person may demand a poll on that question` | coa15-tests-ch4.l4 |
| s 695(4)(c) | 9163-9163 | encoded | `s 695(4)(c) the vote or demand is the same as a vote or demand by the m...` | coa15-tests-ch4.l4 |
| s 696 Resolution authorising off-market pur... | 9164-9173 | fork F-must | `s 696(2) the company must make the copy or memorandum available to members`; `s 696(2)(b) the copy or memorandum was made available to members for a ...` (+5 more) | coa15-tests-ch4.l4 |
| s 696(1) | 9165-9165 | encoded | `s 696(1) this section applies to the resolution` | coa15-tests-ch4.l4 |
| s 696(2) | 9166-9170 | fork F-must | `s 696(2) the company must make the copy or memorandum available to members`; `s 696(2)(b) the copy or memorandum was made available to members for a ...` (+1 more) | coa15-tests-ch4.l4 |
| s 696(2)(a) | 9167-9167 | fork F-must | `s 696(2)(a) the copy or memorandum was made available to members for a ...`; `s 696(2) the company must make the copy or memorandum available to members` (+1 more) | coa15-tests-ch4.l4 |
| s 696(2)(b) | 9168-9170 | fork F-must | `s 696(2) the company must make the copy or memorandum available to members`; `s 696(2)(b) the copy or memorandum was made available to members for a ...` | coa15-tests-ch4.l4 |
| s 696(3) | 9171-9171 | fork F-must | `s 696(3) the memorandum includes what the subsection requires` | coa15-tests-ch4.l4 |
| s 696(4) | 9172-9172 | fork F-must | `s 696(4) the copy has annexed to it what the subsection requires` | coa15-tests-ch4.l4 |
| s 696(5) | 9173-9173 | encoded | `s 696(5) the resolution is not validly passed` | coa15-tests-ch4.l4 |
| s 697 Variation of contract for off-market ... | 9174-9181 | fork F-must, F-omitted-word | `s 697(5) the resolution is barred by section 698 or section 699`; `s 697(1) the company may agree to the variation` (+3 more) | coa15-tests-ch4.l4 |
| s 697(1) | 9175-9175 | encoded | `s 697(1) the company may agree to the variation` | coa15-tests-ch4.l4 |
| s 697(2) | 9176-9176 | fork F-must, F-omitted-word | `s 697(2) the variation is authorised in the way the subsection requires` | coa15-tests-ch4.l4 |
| s 697(3) | 9177-9177 | fork F-omitted-word | `s 697(3) the authority may be varied, revoked or renewed` | coa15-tests-ch4.l4 |
| s 697(4) | 9178-9178 | encoded | `s 697(4) the resolution specifies a date of expiry that is not later th...` | coa15-tests-ch4.l4 |
| s 697(5) | 9179-9181 | encoded | `s 697(5) the resolution is barred by section 698 or section 699` | coa15-tests-ch4.l4 |
| s 698 Resolution authorising variation: exe... | 9182-9191 | encoded | `s 698(3) the resolution is not effective`; `s 698(1) this section applies to the resolution` (+4 more) | coa15-tests-ch4.l4 |
| s 698(1) | 9183-9183 | encoded | `s 698(1) this section applies to the resolution` | coa15-tests-ch4.l4 |
| s 698(2) | 9184-9184 | encoded | `s 698(2) the member is not an eligible member` | coa15-tests-ch4.l4 |
| s 698(3) | 9185-9187 | encoded | `s 698(3) the resolution is not effective` | coa15-tests-ch4.l4 |
| s 698(3)(a) | 9186-9186 | encoded | `s 698(3) the resolution is not effective` | coa15-tests-ch4.l4 |
| s 698(3)(b) | 9187-9187 | encoded | `s 698(3) the resolution is not effective` | coa15-tests-ch4.l4 |
| s 698(4) | 9188-9191 | encoded | `s 698(4)(a) the member is regarded as exercising the voting rights`; `s 698(4)(b) the person may demand a poll on that question` (+1 more) | coa15-tests-ch4.l4 |
| s 698(4)(a) | 9189-9189 | encoded | `s 698(4)(a) the member is regarded as exercising the voting rights` | coa15-tests-ch4.l4 |
| s 698(4)(b) | 9190-9190 | encoded | `s 698(4)(b) the person may demand a poll on that question` | coa15-tests-ch4.l4 |
| s 698(4)(c) | 9191-9191 | encoded | `s 698(4)(c) the vote or demand is the same as a vote or demand by the m...` | coa15-tests-ch4.l4 |
| s 699 Resolution authorising variation: dis... | 9192-9202 | fork F-must | `s 699(2)(b) the copy or memorandum was made available to members for a ...`; `s 699(2)(a) the copy or memorandum was made available to members for a ...` (+5 more) | coa15-tests-ch4.l4 |
| s 699(1) | 9193-9193 | encoded | `s 699(1) this section applies to the resolution` | coa15-tests-ch4.l4 |
| s 699(2) | 9194-9198 | encoded | `s 699(2)(b) the copy or memorandum was made available to members for a ...`; `s 699(2)(a) the copy or memorandum was made available to members for a ...` | coa15-tests-ch4.l4 |
| s 699(2)(a) | 9195-9195 | encoded | `s 699(2)(a) the copy or memorandum was made available to members for a ...`; `s 699(2)(b) the copy or memorandum was made available to members for a ...` | coa15-tests-ch4.l4 |
| s 699(2)(b) | 9196-9198 | encoded | `s 699(2)(b) the copy or memorandum was made available to members for a ...` | coa15-tests-ch4.l4 |
| s 699(3) | 9199-9199 | fork F-must | `s 699(3) the original contract is also made available` | coa15-tests-ch4.l4 |
| s 699(4) | 9200-9200 | encoded | `s 699(4) the memorandum includes what the subsection requires` | coa15-tests-ch4.l4 |
| s 699(5) | 9201-9201 | encoded | `s 699(5) the copy has annexed to it what the subsection requires` | coa15-tests-ch4.l4 |
| s 699(6) | 9202-9202 | encoded | `s 699(6) the resolution is not validly passed` | coa15-tests-ch4.l4 |
| s 700 Release of company's rights under con... | 9203-9211 | fork F-must, F-omitted-word | `s 700(5) sections 698 and 699 apply to the resolution`; `s 700(1) the release agreement is void` (+3 more) | coa15-tests-ch4.l4 |
| s 700(1) | 9204-9204 | encoded | `s 700(1) the release agreement is void` | coa15-tests-ch4.l4 |
| s 700(2) | 9205-9205 | fork F-must, F-omitted-word | `s 700(2) the release agreement is authorised in the way the subsection ...` | coa15-tests-ch4.l4 |
| s 700(3) | 9206-9206 | fork F-omitted-word | `s 700(3) the authority may be varied, revoked or renewed` | coa15-tests-ch4.l4 |
| s 700(4) | 9207-9207 | encoded | `s 700(4) the resolution specifies a date of expiry that is not later th...` | coa15-tests-ch4.l4 |
| s 700(5) | 9208-9211 | encoded | `s 700(5) sections 698 and 699 apply to the resolution` | coa15-tests-ch4.l4 |
| heading: Authority for market purchase | 9212-9212 | inert (reason 1) | a heading: not operative |  |
| s 701 Authority for market purchase | 9213-9229 | fork F-grant-701-6 | `s 701(2) the authority may take that form`; `s 701(3) the authority contains what the subsection requires` (+6 more) | coa15-tests-ch4.l4 |
| s 701(1) | 9214-9214 | encoded | `s 701(1) the company may make the market purchase` | coa15-tests-ch4.l4 |
| s 701(2) | 9215-9217 | encoded | `s 701(2) the authority may take that form` | coa15-tests-ch4.l4 |
| s 701(2)(a) | 9216-9216 | encoded | `s 701(2) the authority may take that form` | coa15-tests-ch4.l4 |
| s 701(2)(b) | 9217-9217 | encoded | `s 701(2) the authority may take that form` | coa15-tests-ch4.l4 |
| s 701(3) | 9218-9220 | encoded | `s 701(3) the authority contains what the subsection requires` | coa15-tests-ch4.l4 |
| s 701(3)(a) | 9219-9219 | encoded | `s 701(3) the authority contains what the subsection requires` | coa15-tests-ch4.l4 |
| s 701(3)(b) | 9220-9220 | encoded | `s 701(3) the authority contains what the subsection requires` | coa15-tests-ch4.l4 |
| s 701(4) | 9221-9221 | encoded | `s 701(4) the authority may be varied, revoked or renewed` | coa15-tests-ch4.l4 |
| s 701(5) | 9222-9222 | encoded | `s 701(5) the resolution specifies a date of expiry that is not later th...` | coa15-tests-ch4.l4 |
| s 701(6) | 9223-9225 | fork F-grant-701-6 | `s 701(6) the company may make a purchase of its own shares after the ex...` | coa15-tests-ch4.l4 |
| s 701(6)(a) | 9224-9224 | fork F-grant-701-6 | `s 701(6) the company may make a purchase of its own shares after the ex...` | coa15-tests-ch4.l4 |
| s 701(6)(b) | 9225-9225 | fork F-grant-701-6 | `s 701(6) the company may make a purchase of its own shares after the ex...` | coa15-tests-ch4.l4 |
| s 701(7) | 9226-9228 | encoded | `s 701(7) the resolution may determine the price in that way` | coa15-tests-ch4.l4 |
| s 701(7)(a) | 9227-9227 | encoded | `s 701(7) the resolution may determine the price in that way` | coa15-tests-ch4.l4 |
| s 701(7)(b) | 9228-9228 | encoded | `s 701(7) the resolution may determine the price in that way` | coa15-tests-ch4.l4 |
| s 701(8) | 9229-9229 | encoded | `s 701(8) Chapter 3 of Part 3 applies to the resolution` | coa15-tests-ch4.l4 |
| heading: Supplementary provisions | 9230-9230 | inert (reason 1) | a heading: not operative |  |
| s 702 Copy of contract or memorandum to be ... | 9231-9251 | fork F-must, F-ten-years | `s 702(5) the company must give notice to the registrar of the place`; `s 702(5) the company's duty to give notice to the registrar of the place` (+10 more) | coa15-tests-ch4.l4 |
| s 702(1) | 9232-9234 | encoded | `s 702(1) this section applies` | coa15-tests-ch4.l4 |
| s 702(1)(a) | 9233-9233 | encoded | `s 702(1) this section applies` | coa15-tests-ch4.l4 |
| s 702(1)(b) | 9234-9234 | encoded | `s 702(1) this section applies` | coa15-tests-ch4.l4 |
| s 702(2) | 9235-9237 | fork F-must | `s 702(2) the company has kept the copy or memorandum available for insp...`; `s 702(2) the company must keep the copy or memorandum available for ins...` | coa15-tests-ch4.l4 |
| s 702(2)(a) | 9236-9236 | fork F-must | `s 702(2) the company has kept the copy or memorandum available for insp...`; `s 702(2) the company must keep the copy or memorandum available for ins...` | coa15-tests-ch4.l4 |
| s 702(2)(b) | 9237-9237 | fork F-must | `s 702(2) the company has kept the copy or memorandum available for insp...`; `s 702(2) the company must keep the copy or memorandum available for ins...` | coa15-tests-ch4.l4 |
| s 702(3) | 9238-9240 | fork F-must, F-ten-years | `s 702(3) the copy or memorandum was kept available for the period`; `s 702(3) the first day of the period of ten years` (+2 more) | coa15-tests-ch4.l4 |
| s 702(3)(a) | 9239-9239 | fork F-must, F-ten-years | `s 702(3) the copy or memorandum was kept available for the period`; `s 702(3) the first day of the period of ten years` (+2 more) | coa15-tests-ch4.l4 |
| s 702(3)(b) | 9240-9240 | fork F-must, F-ten-years | `s 702(3) the copy or memorandum was kept available for the period`; `s 702(3) the first day of the period of ten years` (+2 more) | coa15-tests-ch4.l4 |
| s 702(4) | 9241-9243 | fork F-must | `s 702(4) the copy or memorandum is kept at a place the subsection allows` | coa15-tests-ch4.l4 |
| s 702(4)(a) | 9242-9242 | fork F-must | `s 702(4) the copy or memorandum is kept at a place the subsection allows` | coa15-tests-ch4.l4 |
| s 702(4)(b) | 9243-9243 | fork F-must | `s 702(4) the copy or memorandum is kept at a place the subsection allows` | coa15-tests-ch4.l4 |
| s 702(5) | 9244-9247 | encoded | `s 702(5) the company must give notice to the registrar of the place`; `s 702(5) the company's duty to give notice to the registrar of the place` | coa15-tests-ch4.l4 |
| s 702(5)(a) | 9245-9245 | encoded | `s 702(5) the company must give notice to the registrar of the place`; `s 702(5) the company's duty to give notice to the registrar of the place` | coa15-tests-ch4.l4 |
| s 702(5)(b) | 9246-9247 | encoded | `s 702(5) the company must give notice to the registrar of the place`; `s 702(5) the company's duty to give notice to the registrar of the place` | coa15-tests-ch4.l4 |
| s 702(6) | 9248-9250 | encoded | `s 702(6) the person may inspect the copy or memorandum without charge` | coa15-tests-ch4.l4 |
| s 702(6)(a) | 9249-9249 | encoded | `s 702(6) the person may inspect the copy or memorandum without charge` | coa15-tests-ch4.l4 |
| s 702(6)(b) | 9250-9250 | encoded | `s 702(6) the person may inspect the copy or memorandum without charge` | coa15-tests-ch4.l4 |
| s 702(7) | 9251-9251 | encoded | `s 702(7) section 702 applies to the document as it applies to the origi...` | coa15-tests-ch4.l4 |
| s 703 Enforcement of right to inspect copy ... | 9252-9257 | fork F-not-in-default | `s 703(1) the company is in default as the subsection describes`; `s 703(1) the person commits an offence` (+2 more) | coa15-tests-ch4.l4 |
| s 703(1) | 9253-9255 | fork F-not-in-default | `s 703(1) the company is in default as the subsection describes`; `s 703(1) the person commits an offence` | coa15-tests-ch4.l4 |
| s 703(1)(a) | 9254-9254 | fork F-not-in-default | `s 703(1) the company is in default as the subsection describes`; `s 703(1) the person commits an offence` | coa15-tests-ch4.l4 |
| s 703(1)(b) | 9255-9255 | fork F-not-in-default | `s 703(1) the company is in default as the subsection describes`; `s 703(1) the person commits an offence` | coa15-tests-ch4.l4 |
| s 703(2) | 9256-9256 | encoded | `s 703(2) the penalty on conviction` | coa15-tests-ch4.l4 |
| s 703(3) | 9257-9257 | encoded | `s 703(3) the court may order an immediate inspection` | coa15-tests-ch4.l4 |
| s 704 No assignment of company's right to p... | 9258-9263 | encoded | `s 704 the company's right under the contract is capable of being assigned` | coa15-tests-ch4.l4 |
| s 704(za) | 9260-9260 | encoded | `s 704 the company's right under the contract is capable of being assigned` | coa15-tests-ch4.l4 |
| s 704(a) | 9261-9261 | encoded | `s 704 the company's right under the contract is capable of being assigned` | coa15-tests-ch4.l4 |
| s 704(b) | 9262-9263 | encoded | `s 704 the company's right under the contract is capable of being assigned` | coa15-tests-ch4.l4 |
| s 705 Payments apart from purchase price to... | 9264-9275 | encoded | `s 705(1) the payment must be made out of the company's distributable pr...`; `s 705(2) the consequence of the requirement not being met` | coa15-tests-ch4.l4 |
| s 705(1) | 9265-9271 | encoded | `s 705(1) the payment must be made out of the company's distributable pr...` | coa15-tests-ch4.l4 |
| s 705(1)(a) | 9266-9266 | encoded | `s 705(1) the payment must be made out of the company's distributable pr...` | coa15-tests-ch4.l4 |
| s 705(1)(b) | 9267-9267 | encoded | `s 705(1) the payment must be made out of the company's distributable pr...` | coa15-tests-ch4.l4 |
| s 705(1)(c) | 9268-9271 | encoded | `s 705(1) the payment must be made out of the company's distributable pr...` | coa15-tests-ch4.l4 |
| s 705(2) | 9272-9275 | encoded | `s 705(2) the consequence of the requirement not being met` | coa15-tests-ch4.l4 |
| s 705(2)(a) | 9273-9273 | encoded | `s 705(2) the consequence of the requirement not being met` | coa15-tests-ch4.l4 |
| s 705(2)(b) | 9274-9274 | encoded | `s 705(2) the consequence of the requirement not being met` | coa15-tests-ch4.l4 |
| s 705(2)(c) | 9275-9275 | encoded | `s 705(2) the consequence of the requirement not being met` | coa15-tests-ch4.l4 |
| s 706 Treatment of shares purchased | 9276-9281 | encoded | `s 706(b)(ii) the amount of the company's issued share capital after the...`; `s 706(b)(i) the shares are treated as cancelled` (+1 more) | coa15-tests-ch4.l4 |
| s 706(a) | 9278-9278 | encoded | `s 706(a) the shares may be held and dealt with in accordance with Chapt...`; `s 706(b)(i) the shares are treated as cancelled` (+1 more) | coa15-tests-ch4.l4 |
| s 706(b) | 9279-9281 | encoded | `s 706(b)(i) the shares are treated as cancelled`; `s 706(b)(ii) the amount of the company's issued share capital after the...` | coa15-tests-ch4.l4 |
| s 707 Return to registrar of purchase of ow... | 9282-9300 | fork F-must, F-not-in-default, F-penalty | `s 707(2) the return distinguishes what the subsection requires`; `s 707(3) the return states what the subsection requires` (+9 more) | coa15-tests-ch4.l4 |
| s 707(1) | 9283-9283 | encoded | `s 707(1) the company must deliver a return to the registrar`; `s 707(1) the last day for delivering the return to the registrar` (+1 more) | coa15-tests-ch4.l4 |
| s 707(2) | 9284-9288 | fork F-must | `s 707(2) the return distinguishes what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(2)(a) | 9285-9285 | fork F-must | `s 707(2) the return distinguishes what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(2)(b) | 9286-9288 | fork F-must | `s 707(2) the return distinguishes what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(3) | 9289-9291 | fork F-must | `s 707(3) the return states what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(3)(a) | 9290-9290 | fork F-must | `s 707(3) the return states what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(3)(b) | 9291-9291 | fork F-must | `s 707(3) the return states what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(4) | 9292-9294 | fork F-must | `s 707(4) the return also states what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(4)(a) | 9293-9293 | fork F-must | `s 707(4) the return also states what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(4)(b) | 9294-9294 | fork F-must | `s 707(4) the return also states what the subsection requires` | coa15-tests-ch4.l4 |
| s 707(5) | 9295-9296 | encoded | `s 707(5) the amount to state under subsection (4)(a) in a single return` | coa15-tests-ch4.l4 |
| s 707(6) | 9297-9297 | fork F-not-in-default | `s 707(6) the person commits an offence` | coa15-tests-ch4.l4 |
| s 707(7) | 9298-9300 | fork F-penalty | `s 707(7) the penalty on conviction`; `s 707(7) penalty` (+1 more) | coa15-tests-ch4.l4 |
| s 707(7)(a) | 9299-9299 | encoded | `s 707(7) the penalty on conviction`; `s 707(7) penalty` | coa15-tests-ch4.l4 |
| s 707(7)(b) | 9300-9300 | fork F-penalty | `s 707(7) the penalty on conviction`; `s 707(7) daily default fine limit` (+1 more) | coa15-tests-ch4.l4 |
| s 708 Notice to registrar of cancellation o... | 9301-9319 | fork F-must, F-not-in-default | `s 708(3) the statement of capital states what the subsection requires`; `s 708(1) the company must give notice of cancellation to the registrar` (+7 more) | coa15-tests-ch4.l4 |
| s 708(1) | 9302-9305 | encoded | `s 708(1) the company must give notice of cancellation to the registrar`; `s 708(1) the company's duty to give notice of cancellation to the regis...` (+2 more) | coa15-tests-ch4.l4 |
| s 708(1)(a) | 9303-9303 | encoded | `s 708(1) the company must give notice of cancellation to the registrar`; `s 708(1) the company's duty to give notice of cancellation to the regis...` (+2 more) | coa15-tests-ch4.l4 |
| s 708(1)(b) | 9304-9305 | encoded | `s 708(1) the company must give notice of cancellation to the registrar`; `s 708(1) the company's duty to give notice of cancellation to the regis...` (+2 more) | coa15-tests-ch4.l4 |
| s 708(2) | 9306-9306 | fork F-must | `s 708(2) a statement of capital must accompany the notice`; `s 708(2) the notice is accompanied as the subsection requires` | coa15-tests-ch4.l4 |
| s 708(3) | 9307-9315 | encoded | `s 708(3) the statement of capital states what the subsection requires` | coa15-tests-ch4.l4 |
| s 708(3)(a) | 9308-9308 | encoded | `s 708(3) the statement of capital states what the subsection requires` | coa15-tests-ch4.l4 |
| s 708(3)(b) | 9309-9309 | encoded | `s 708(3) the statement of capital states what the subsection requires` | coa15-tests-ch4.l4 |
| s 708(3)(ba) | 9310-9310 | encoded | `s 708(3) the statement of capital states what the subsection requires` | coa15-tests-ch4.l4 |
| s 708(3)(c) | 9311-9314 | encoded | `s 708(3) the statement of capital states what the subsection requires` | coa15-tests-ch4.l4 |
| s 708(3)(d) | 9315-9315 | repealed or blank in this text | the text shows a row of dots |  |
| s 708(4) | 9316-9318 | fork F-not-in-default | `s 708(4) the person commits an offence` | coa15-tests-ch4.l4 |
| s 708(4)(a) | 9317-9317 | fork F-not-in-default | `s 708(4) the person commits an offence` | coa15-tests-ch4.l4 |
| s 708(4)(b) | 9318-9318 | fork F-not-in-default | `s 708(4) the person commits an offence` | coa15-tests-ch4.l4 |
| s 708(5) | 9319-9319 | encoded | `s 708(5) the penalty on conviction` | coa15-tests-ch4.l4 |
| heading: Chapter 5 — Redemption or purchase by private company out... | 9320-9320 | inert (reason 1) | a heading: not operative |  |
| heading: Introductory | 9321-9321 | inert (reason 1) | a heading: not operative |  |
| s 709 Power of private limited company to r... | 9322-9325 | fork F-grant-709-1, F-signpost | `s 709(1) the private limited company may make the payment out of capital`; `s 709(2) the payment is a payment out of capital for the purposes of th...` (+1 more) | coa15-tests-ch5.l4 |
| s 709(1) | 9323-9323 | fork F-grant-709-1 | `s 709(1) the private limited company may make the payment out of capital` | coa15-tests-ch5.l4 |
| s 709(2) | 9324-9324 | encoded | `s 709(2) the payment is a payment out of capital for the purposes of th...` | coa15-tests-ch5.l4 |
| s 709(3) | 9325-9325 | fork F-signpost | `s 709(3) the requirements of Chapter 5 are displaced by section 692(1ZA)` | coa15-tests-ch5.l4 |
| heading: The permissible capital payment | 9326-9326 | inert (reason 1) | a heading: not operative |  |
| s 710 The permissible capital payment | 9327-9332 | fork F-permissible | `s 710(1) the permissible capital payment` | coa15-tests-ch5.l4 |
| s 710(1) | 9328-9331 | fork F-permissible | `s 710(1) the permissible capital payment` | coa15-tests-ch5.l4 |
| s 710(1)(a) | 9329-9329 | fork F-permissible | `s 710(1) the permissible capital payment` | coa15-tests-ch5.l4 |
| s 710(1)(b) | 9330-9331 | fork F-permissible | `s 710(1) the permissible capital payment` | coa15-tests-ch5.l4 |
| s 710(2) | 9332-9332 | fork F-permissible | `s 710(1) the permissible capital payment` | coa15-tests-ch5.l4 |
| term: “the permissible capital payment” | 9332-9332 | fork F-permissible | `s 710(1) the permissible capital payment` | coa15-tests-ch5.l4 |
| s 711 Available profits | 9333-9335 | encoded | `s 711(2) the available profits of the company for the purposes of Chapt...` | coa15-tests-ch5.l4 |
| s 711(1) | 9334-9334 | encoded | `s 711(2) the available profits of the company for the purposes of Chapt...` | coa15-tests-ch5.l4 |
| s 711(2) | 9335-9335 | encoded | `s 711(2) the available profits of the company for the purposes of Chapt...` | coa15-tests-ch5.l4 |
| s 712 Determination of available profits | 9336-9356 | fork F-period-start | `s 712(2) the profits of the company before the reductions`; `s 712(3) the amount after the reduction` (+4 more) | coa15-tests-ch5.l4 |
| s 712(1) | 9337-9337 | encoded | `s 712(2) the profits of the company before the reductions` | coa15-tests-ch5.l4 |
| s 712(2) | 9338-9343 | encoded | `s 712(2) the profits of the company before the reductions` | coa15-tests-ch5.l4 |
| s 712(2)(a) | 9339-9339 | encoded | `s 712(2) the profits of the company before the reductions` | coa15-tests-ch5.l4 |
| s 712(2)(b) | 9340-9342 | encoded | `s 712(2) the profits of the company before the reductions` | coa15-tests-ch5.l4 |
| s 712(2)(c) | 9343-9343 | encoded | `s 712(2) the profits of the company before the reductions` | coa15-tests-ch5.l4 |
| s 712(3) | 9344-9347 | encoded | `s 712(3) the amount after the reduction` | coa15-tests-ch5.l4 |
| s 712(3)(a) | 9345-9345 | encoded | `s 712(3) the amount after the reduction` | coa15-tests-ch5.l4 |
| s 712(3)(b) | 9346-9347 | encoded | `s 712(3) the amount after the reduction` | coa15-tests-ch5.l4 |
| s 712(4) | 9348-9351 | encoded | `s 712(4) the payment is an other relevant payment lawfully made` | coa15-tests-ch5.l4 |
| term: “other relevant payment lawfully made” | 9348-9348 | encoded | `s 712(4) the payment is an other relevant payment lawfully made` | coa15-tests-ch5.l4 |
| s 712(4)(a) | 9349-9349 | encoded | `s 712(4) the payment is an other relevant payment lawfully made` | coa15-tests-ch5.l4 |
| s 712(4)(b) | 9350-9350 | encoded | `s 712(4) the payment is an other relevant payment lawfully made` | coa15-tests-ch5.l4 |
| s 712(4)(c) | 9351-9351 | encoded | `s 712(4) the payment is an other relevant payment lawfully made` | coa15-tests-ch5.l4 |
| s 712(5) | 9352-9352 | encoded | `s 712(5) the amount of the available profits` | coa15-tests-ch5.l4 |
| s 712(6) | 9353-9355 | encoded | `s 712(6) the accounts are the relevant accounts` | coa15-tests-ch5.l4 |
| term: “the relevant accounts” | 9353-9353 | encoded | `s 712(6) the accounts are the relevant accounts` | coa15-tests-ch5.l4 |
| s 712(6)(a) | 9354-9354 | encoded | `s 712(6) the accounts are the relevant accounts` | coa15-tests-ch5.l4 |
| s 712(6)(b) | 9355-9355 | encoded | `s 712(6) the accounts are the relevant accounts` | coa15-tests-ch5.l4 |
| s 712(7) | 9356-9356 | fork F-period-start | `s 712(7) the first day of the relevant period` | coa15-tests-ch5.l4 |
| term: “the relevant period” | 9356-9356 | fork F-period-start | `s 712(7) the first day of the relevant period` | coa15-tests-ch5.l4 |
| heading: Requirements for payment out of capital | 9357-9357 | inert (reason 1) | a heading: not operative |  |
| s 713 Requirements for payment out of capital | 9358-9364 | encoded | `s 713(1) the payment out of capital is not lawful`; `s 713(2) subsection (1) does not apply to the payment` | coa15-tests-ch5.l4 |
| s 713(1) | 9359-9363 | encoded | `s 713(1) the payment out of capital is not lawful` | coa15-tests-ch5.l4 |
| s 713(2) | 9364-9364 | encoded | `s 713(2) subsection (1) does not apply to the payment` | coa15-tests-ch5.l4 |
| s 714 Directors' statement and auditor's re... | 9365-9379 | fork F-must | `s 714 the statement and report contain everything section 714 requires`; `s 714(3) the statement states what the subsection requires` (+5 more) | coa15-tests-ch5.l4 |
| s 714(1) | 9366-9366 | fork F-must | `s 714(1) the directors must make a statement`; `s 714(2) the statement specifies the amount of the permissible capital ...` (+1 more) | coa15-tests-ch5.l4 |
| s 714(2) | 9367-9367 | fork F-must | `s 714(2) the statement specifies the amount of the permissible capital ...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(3) | 9368-9373 | fork F-must | `s 714(3) the statement states what the subsection requires`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(3)(a) | 9369-9369 | fork F-must | `s 714(3) the statement states what the subsection requires`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(3)(b) | 9370-9373 | fork F-must | `s 714(3) the statement states what the subsection requires`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(4) | 9374-9374 | fork F-must | `s 714(4) the directors took into account the liabilities the subsection...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(5) | 9375-9375 | fork F-must | `s 714(5) the statement is in the form and contains the information the ...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(6) | 9376-9379 | fork F-must | `s 714(6) the statement has annexed to it the report the subsection requ...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(6)(a) | 9377-9377 | fork F-must | `s 714(6) the statement has annexed to it the report the subsection requ...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(6)(b) | 9378-9378 | fork F-must | `s 714(6) the statement has annexed to it the report the subsection requ...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 714(6)(c) | 9379-9379 | fork F-must | `s 714(6) the statement has annexed to it the report the subsection requ...`; `s 714 the statement and report contain everything section 714 requires` | coa15-tests-ch5.l4 |
| s 715 Directors' statement: offence if no r... | 9380-9386 | fork F-not-in-default | `s 715(2) the penalty on conviction`; `s 715(1) the person commits an offence` | coa15-tests-ch5.l4 |
| s 715(1) | 9381-9381 | fork F-not-in-default | `s 715(1) the person commits an offence` | coa15-tests-ch5.l4 |
| s 715(2) | 9382-9386 | encoded | `s 715(2) the penalty on conviction` | coa15-tests-ch5.l4 |
| s 715(2)(a) | 9383-9383 | encoded | `s 715(2) the penalty on conviction` | coa15-tests-ch5.l4 |
| s 715(2)(b) | 9384-9386 | encoded | `s 715(2) the penalty on conviction` | coa15-tests-ch5.l4 |
| s 716 Payment to be approved by special res... | 9387-9392 | fork F-must | `s 716(3) the resolution is barred by section 717 or section 718`; `s 716(1) the payment is approved as the subsection requires` (+2 more) | coa15-tests-ch5.l4 |
| s 716(1) | 9388-9388 | fork F-must | `s 716(1) the payment is approved as the subsection requires` | coa15-tests-ch5.l4 |
| s 716(2) | 9389-9389 | encoded | `s 716(2) the last day for passing the resolution`; `s 716(2) the resolution was passed in time` | coa15-tests-ch5.l4 |
| s 716(3) | 9390-9392 | encoded | `s 716(3) the resolution is barred by section 717 or section 718` | coa15-tests-ch5.l4 |
| s 717 Resolution authorising payment: exerc... | 9393-9402 | encoded | `s 717(3) the resolution is not effective`; `s 717(1) this section applies to the resolution` (+4 more) | coa15-tests-ch5.l4 |
| s 717(1) | 9394-9394 | encoded | `s 717(1) this section applies to the resolution` | coa15-tests-ch5.l4 |
| s 717(2) | 9395-9395 | encoded | `s 717(2) the member is not an eligible member` | coa15-tests-ch5.l4 |
| s 717(3) | 9396-9398 | encoded | `s 717(3) the resolution is not effective` | coa15-tests-ch5.l4 |
| s 717(3)(a) | 9397-9397 | encoded | `s 717(3) the resolution is not effective` | coa15-tests-ch5.l4 |
| s 717(3)(b) | 9398-9398 | encoded | `s 717(3) the resolution is not effective` | coa15-tests-ch5.l4 |
| s 717(4) | 9399-9402 | encoded | `s 717(4)(a) the member is regarded as exercising the voting rights`; `s 717(4)(b) the person may demand a poll on that question` (+1 more) | coa15-tests-ch5.l4 |
| s 717(4)(a) | 9400-9400 | encoded | `s 717(4)(a) the member is regarded as exercising the voting rights` | coa15-tests-ch5.l4 |
| s 717(4)(b) | 9401-9401 | encoded | `s 717(4)(b) the person may demand a poll on that question` | coa15-tests-ch5.l4 |
| s 717(4)(c) | 9402-9402 | encoded | `s 717(4)(c) the vote or demand is the same as a vote or demand by the m...` | coa15-tests-ch5.l4 |
| s 718 Resolution authorising payment: discl... | 9403-9408 | fork F-must | `s 718(2)(b) the copy was made available to members for a resolution at ...`; `s 718(2)(a) the copy was made available to members for a written resolu...` (+2 more) | coa15-tests-ch5.l4 |
| s 718(1) | 9404-9404 | encoded | `s 718(1) this section applies to the resolution` | coa15-tests-ch5.l4 |
| s 718(2) | 9405-9407 | fork F-must | `s 718(2)(b) the copy was made available to members for a resolution at ...`; `s 718(2)(a) the copy was made available to members for a written resolu...` | coa15-tests-ch5.l4 |
| s 718(2)(a) | 9406-9406 | fork F-must | `s 718(2)(a) the copy was made available to members for a written resolu...`; `s 718(2)(b) the copy was made available to members for a resolution at ...` | coa15-tests-ch5.l4 |
| s 718(2)(b) | 9407-9407 | fork F-must | `s 718(2)(b) the copy was made available to members for a resolution at ...` | coa15-tests-ch5.l4 |
| s 718(3) | 9408-9408 | encoded | `s 718(3) the resolution is ineffective` | coa15-tests-ch5.l4 |
| s 719 Public notice of proposed payment | 9409-9424 | fork F-must | `s 719(1) the last day for publishing the notice in the Gazette`; `s 719(1) the notice states what the subsection requires` (+8 more) | coa15-tests-ch5.l4 |
| s 719(1) | 9410-9416 | fork F-must | `s 719(1) the last day for publishing the notice in the Gazette`; `s 719(1) the notice states what the subsection requires` (+2 more) | coa15-tests-ch5.l4 |
| s 719(1)(a) | 9411-9411 | fork F-must | `s 719(1) the last day for publishing the notice in the Gazette`; `s 719(1) the notice states what the subsection requires` | coa15-tests-ch5.l4 |
| s 719(1)(b) | 9412-9414 | fork F-must | `s 719(1) the last day for publishing the notice in the Gazette`; `s 719(1) the notice states what the subsection requires` | coa15-tests-ch5.l4 |
| s 719(1)(c) | 9415-9415 | fork F-must | `s 719(1) the last day for publishing the notice in the Gazette`; `s 719(1) the notice states what the subsection requires` | coa15-tests-ch5.l4 |
| s 719(1)(d) | 9416-9416 | fork F-must | `s 719(1) the last day for publishing the notice in the Gazette`; `s 719(1) the notice states what the subsection requires` | coa15-tests-ch5.l4 |
| s 719(2) | 9417-9419 | fork F-must | `s 719(2) the company must publish or give the notice`; `s 719(2) the company published or gave the notice in time` | coa15-tests-ch5.l4 |
| s 719(2)(a) | 9418-9418 | fork F-must | `s 719(2) the company must publish or give the notice`; `s 719(2) the company published or gave the notice in time` | coa15-tests-ch5.l4 |
| s 719(2)(b) | 9419-9419 | fork F-must | `s 719(2) the company must publish or give the notice`; `s 719(2) the company published or gave the notice in time` | coa15-tests-ch5.l4 |
| s 719(3) | 9420-9420 | encoded | `s 719(3) the newspaper is an appropriate national newspaper` | coa15-tests-ch5.l4 |
| term: “An appropriate national newspaper” | 9420-9420 | encoded | `s 719(3) the newspaper is an appropriate national newspaper` | coa15-tests-ch5.l4 |
| s 719(4) | 9421-9424 | encoded | `s 719(4) the company must deliver a copy of the statement and report to...`; `s 719(4) the copy was delivered to the registrar in time` (+1 more) | coa15-tests-ch5.l4 |
| s 719(4)(a) | 9422-9422 | encoded | `s 719(4) the company must deliver a copy of the statement and report to...`; `s 719(4) the copy was delivered to the registrar in time` (+1 more) | coa15-tests-ch5.l4 |
| s 719(4)(b) | 9423-9424 | encoded | `s 719(4) the company must deliver a copy of the statement and report to...`; `s 719(4) the copy was delivered to the registrar in time` (+1 more) | coa15-tests-ch5.l4 |
| s 720 Directors' statement and auditor's re... | 9425-9443 | fork F-must, F-not-in-default | `s 720(1) the first day of the period`; `s 720(1) the last day of the period` (+9 more) | coa15-tests-ch5.l4 |
| s 720(1) | 9426-9430 | fork F-must | `s 720(1) the first day of the period`; `s 720(1) the last day of the period` (+1 more) | coa15-tests-ch5.l4 |
| s 720(1)(a) | 9427-9429 | fork F-must | `s 720(1) the first day of the period`; `s 720(1) the last day of the period` (+1 more) | coa15-tests-ch5.l4 |
| s 720(1)(b) | 9430-9430 | fork F-must | `s 720(1) the first day of the period`; `s 720(1) the last day of the period` (+1 more) | coa15-tests-ch5.l4 |
| s 720(2) | 9431-9433 | fork F-must | `s 720(2) the statement and report are kept at a place the subsection al...` | coa15-tests-ch5.l4 |
| s 720(2)(a) | 9432-9432 | fork F-must | `s 720(2) the statement and report are kept at a place the subsection al...` | coa15-tests-ch5.l4 |
| s 720(2)(b) | 9433-9433 | fork F-must | `s 720(2) the statement and report are kept at a place the subsection al...` | coa15-tests-ch5.l4 |
| s 720(3) | 9434-9437 | encoded | `s 720(3) the company must give notice to the registrar of the place`; `s 720(3) the company's duty to give notice to the registrar of the place` | coa15-tests-ch5.l4 |
| s 720(3)(a) | 9435-9435 | encoded | `s 720(3) the company must give notice to the registrar of the place`; `s 720(3) the company's duty to give notice to the registrar of the place` | coa15-tests-ch5.l4 |
| s 720(3)(b) | 9436-9437 | encoded | `s 720(3) the company must give notice to the registrar of the place`; `s 720(3) the company's duty to give notice to the registrar of the place` | coa15-tests-ch5.l4 |
| s 720(4) | 9438-9438 | encoded | `s 720(4) the person may inspect the statement and report without charge` | coa15-tests-ch5.l4 |
| s 720(5) | 9439-9441 | fork F-not-in-default | `s 720(5) the company is in default as the subsection describes`; `s 720(5) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720(5)(a) | 9440-9440 | fork F-not-in-default | `s 720(5) the company is in default as the subsection describes`; `s 720(5) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720(5)(b) | 9441-9441 | fork F-not-in-default | `s 720(5) the company is in default as the subsection describes`; `s 720(5) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720(6) | 9442-9442 | encoded | `s 720(6) the penalty on conviction` | coa15-tests-ch5.l4 |
| s 720(7) | 9443-9443 | encoded | `s 720(7) the court may order an immediate inspection` | coa15-tests-ch5.l4 |
| heading: Requirements for payment out of capital: employees' share... | 9444-9444 | inert (reason 1) | a heading: not operative |  |
| s 720A Reduced requirements for payment out ... | 9445-9453 | fork F-must | `s 720A(2) the resolution is supported by a solvency statement`; `s 720A(1) section 713(1) does not apply` (+4 more) | coa15-tests-ch5.l4 |
| s 720A(1) | 9446-9446 | encoded | `s 720A(1) section 713(1) does not apply` | coa15-tests-ch5.l4 |
| s 720A(2) | 9447-9449 | encoded | `s 720A(2) the resolution is supported by a solvency statement` | coa15-tests-ch5.l4 |
| s 720A(2)(a) | 9448-9448 | encoded | `s 720A(2) the resolution is supported by a solvency statement` | coa15-tests-ch5.l4 |
| s 720A(2)(b) | 9449-9449 | encoded | `s 720A(2) the resolution is supported by a solvency statement` | coa15-tests-ch5.l4 |
| s 720A(3) | 9450-9450 | encoded | `s 720A(3) the copy of the solvency statement was sent or submitted in time` | coa15-tests-ch5.l4 |
| s 720A(4) | 9451-9451 | fork F-must | `s 720A(4) the copy of the solvency statement was made available at the ...` | coa15-tests-ch5.l4 |
| s 720A(5) | 9452-9452 | encoded | `s 720A(5) the validity of the resolution is affected by the failure` | coa15-tests-ch5.l4 |
| s 720A(6) | 9453-9453 | encoded | `s 720A(6) section 717 applies to the resolution` | coa15-tests-ch5.l4 |
| s 720B Registration of resolution and suppor... | 9454-9482 | fork F-must, F-not-in-default | `s 720B(2) the statement of capital states what the subsection requires`; `s 720B(1) the company must deliver the documents to the registrar` (+12 more) | coa15-tests-ch5.l4 |
| s 720B(1) | 9455-9458 | encoded | `s 720B(1) the company must deliver the documents to the registrar`; `s 720B(1) the documents were delivered within 15 days after the resolut...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(1)(a) | 9456-9456 | encoded | `s 720B(1) the company must deliver the documents to the registrar`; `s 720B(1) the documents were delivered within 15 days after the resolut...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(1)(b) | 9457-9457 | encoded | `s 720B(1) the company must deliver the documents to the registrar`; `s 720B(1) the documents were delivered within 15 days after the resolut...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(1)(c) | 9458-9458 | encoded | `s 720B(1) the company must deliver the documents to the registrar`; `s 720B(1) the documents were delivered within 15 days after the resolut...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(2) | 9459-9467 | encoded | `s 720B(2) the statement of capital states what the subsection requires` | coa15-tests-ch5.l4 |
| s 720B(2)(a) | 9460-9460 | encoded | `s 720B(2) the statement of capital states what the subsection requires` | coa15-tests-ch5.l4 |
| s 720B(2)(b) | 9461-9461 | encoded | `s 720B(2) the statement of capital states what the subsection requires` | coa15-tests-ch5.l4 |
| s 720B(2)(ba) | 9462-9462 | encoded | `s 720B(2) the statement of capital states what the subsection requires` | coa15-tests-ch5.l4 |
| s 720B(2)(c) | 9463-9466 | encoded | `s 720B(2) the statement of capital states what the subsection requires` | coa15-tests-ch5.l4 |
| s 720B(2)(d) | 9467-9467 | repealed or blank in this text | the text shows a row of dots |  |
| s 720B(3) | 9468-9468 | encoded | `s 720B(3) the registrar must register the documents`; `s 720B(3) the registrar must register the documents on receipt` | coa15-tests-ch5.l4 |
| s 720B(4) | 9469-9469 | encoded | `s 720B(4) the resolution cannot yet take effect` | coa15-tests-ch5.l4 |
| s 720B(5) | 9470-9472 | fork F-must | `s 720B(5) the company must deliver the directors' statement to the regi...`; `s 720B(5) the directors' statement was delivered within 15 days after t...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(5)(a) | 9471-9471 | fork F-must | `s 720B(5) the company must deliver the directors' statement to the regi...`; `s 720B(5) the directors' statement was delivered within 15 days after t...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(5)(b) | 9472-9472 | fork F-must | `s 720B(5) the company must deliver the directors' statement to the regi...`; `s 720B(5) the directors' statement was delivered within 15 days after t...` (+1 more) | coa15-tests-ch5.l4 |
| s 720B(6) | 9473-9475 | encoded | `s 720B(6) the validity of the resolution is affected by the failure` | coa15-tests-ch5.l4 |
| s 720B(6)(a) | 9474-9474 | encoded | `s 720B(6) the validity of the resolution is affected by the failure` | coa15-tests-ch5.l4 |
| s 720B(6)(b) | 9475-9475 | encoded | `s 720B(6) the validity of the resolution is affected by the failure` | coa15-tests-ch5.l4 |
| s 720B(7) | 9476-9476 | fork F-not-in-default | `s 720B(7) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720B(8) | 9477-9479 | fork F-not-in-default | `s 720B(8) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720B(8)(a) | 9478-9478 | fork F-not-in-default | `s 720B(8) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720B(8)(b) | 9479-9479 | fork F-not-in-default | `s 720B(8) the person commits an offence` | coa15-tests-ch5.l4 |
| s 720B(9) | 9480-9482 | encoded | `s 720B(9) the penalty on conviction` | coa15-tests-ch5.l4 |
| s 720B(9)(a) | 9481-9481 | encoded | `s 720B(9) the penalty on conviction` | coa15-tests-ch5.l4 |
| s 720B(9)(b) | 9482-9482 | encoded | `s 720B(9) the penalty on conviction` | coa15-tests-ch5.l4 |
| heading: Objection to payment by members or creditors | 9483-9483 | inert (reason 1) | a heading: not operative |  |
| s 721 Application to court to cancel resolu... | 9484-9504 | fork F-grant-721-5, F-grant-721-6, F-grant-721-7, F-must | `s 721(3) the court may adjourn the proceedings and give directions and ...`; `s 721(1) the member or creditor may apply to the court` (+9 more) | coa15-tests-ch5.l4 |
| s 721(1) | 9485-9488 | encoded | `s 721(1) the member or creditor may apply to the court`; `s 721(1) the person may apply to the court for the cancellation of the ...` | coa15-tests-ch5.l4 |
| s 721(1)(a) | 9486-9486 | encoded | `s 721(1) the member or creditor may apply to the court`; `s 721(1) the person may apply to the court for the cancellation of the ...` | coa15-tests-ch5.l4 |
| s 721(1)(b) | 9487-9488 | encoded | `s 721(1) the member or creditor may apply to the court`; `s 721(1) the person may apply to the court for the cancellation of the ...` | coa15-tests-ch5.l4 |
| s 721(2) | 9489-9491 | encoded | `s 721(2)(a) the application was made within five weeks after the passin...`; `s 721(2)(a) the last day for applying to the court` (+1 more) | coa15-tests-ch5.l4 |
| s 721(2)(a) | 9490-9490 | encoded | `s 721(2)(a) the application was made within five weeks after the passin...`; `s 721(2)(a) the last day for applying to the court` | coa15-tests-ch5.l4 |
| s 721(2)(b) | 9491-9491 | encoded | `s 721(2)(b) the application may be made on behalf of the persons entitl...` | coa15-tests-ch5.l4 |
| s 721(3) | 9492-9496 | encoded | `s 721(3) the court may adjourn the proceedings and give directions and ...` | coa15-tests-ch5.l4 |
| s 721(3)(a) | 9493-9495 | encoded | `s 721(3) the court may adjourn the proceedings and give directions and ...` | coa15-tests-ch5.l4 |
| s 721(3)(b) | 9496-9496 | encoded | `s 721(3) the court may adjourn the proceedings and give directions and ...` | coa15-tests-ch5.l4 |
| s 721(4) | 9497-9497 | fork F-must | `s 721(4) the court has made the order the subsection requires`; `s 721(4) the court must make an order cancelling or confirming the reso...` | coa15-tests-ch5.l4 |
| s 721(5) | 9498-9500 | fork F-grant-721-5 | `s 721(5) the court may by order alter or extend the date or period` | coa15-tests-ch5.l4 |
| s 721(5)(a) | 9499-9499 | fork F-grant-721-5 | `s 721(5) the court may by order alter or extend the date or period` | coa15-tests-ch5.l4 |
| s 721(5)(b) | 9500-9500 | fork F-grant-721-5 | `s 721(5) the court may by order alter or extend the date or period` | coa15-tests-ch5.l4 |
| s 721(6) | 9501-9503 | fork F-grant-721-6 | `s 721(6) the court's order may provide for the purchase of a member's s...` | coa15-tests-ch5.l4 |
| s 721(6)(a) | 9502-9502 | fork F-grant-721-6 | `s 721(6) the court's order may provide for the purchase of a member's s...` | coa15-tests-ch5.l4 |
| s 721(6)(b) | 9503-9503 | fork F-grant-721-6 | `s 721(6) the court's order may provide for the purchase of a member's s...` | coa15-tests-ch5.l4 |
| s 721(7) | 9504-9504 | fork F-grant-721-7 | `s 721(7) the court's order may restrict amendments of the articles` | coa15-tests-ch5.l4 |
| s 722 Notice to registrar of court applicat... | 9505-9513 | fork F-immediately, F-not-in-default | `s 722(4) the person commits an offence`; `s 722(1) the applicants must give notice to the registrar` (+5 more) | coa15-tests-ch5.l4 |
| s 722(1) | 9506-9507 | fork F-immediately | `s 722(1) the applicants must give notice to the registrar` | coa15-tests-ch5.l4 |
| s 722(2) | 9508-9508 | fork F-immediately | `s 722(2) the company must give notice to the registrar` | coa15-tests-ch5.l4 |
| s 722(3) | 9509-9509 | encoded | `s 722(3) the company must deliver a copy of the order to the registrar`; `s 722(3) the copy of the order was delivered in time` (+1 more) | coa15-tests-ch5.l4 |
| s 722(4) | 9510-9512 | fork F-not-in-default | `s 722(4) the person commits an offence` | coa15-tests-ch5.l4 |
| s 722(4)(a) | 9511-9511 | fork F-not-in-default | `s 722(4) the person commits an offence` | coa15-tests-ch5.l4 |
| s 722(4)(b) | 9512-9512 | fork F-not-in-default | `s 722(4) the person commits an offence` | coa15-tests-ch5.l4 |
| s 722(5) | 9513-9513 | encoded | `s 722(5) the penalty on conviction` | coa15-tests-ch5.l4 |
| heading: Supplementary provisions | 9514-9514 | inert (reason 1) | a heading: not operative |  |
| s 723 Time when payment out of capital to b... | 9515-9522 | encoded | `s 723(1) the company must make the payment out of capital by the closin...`; `s 723(1) the payment out of capital was made in the window` (+4 more) | coa15-tests-ch5.l4 |
| s 723(1) | 9516-9518 | encoded | `s 723(1) the company must make the payment out of capital by the closin...`; `s 723(1) the payment out of capital was made in the window` (+2 more) | coa15-tests-ch5.l4 |
| s 723(1)(a) | 9517-9517 | encoded | `s 723(1) the company must make the payment out of capital by the closin...`; `s 723(1) the payment out of capital was made in the window` (+2 more) | coa15-tests-ch5.l4 |
| s 723(1)(b) | 9518-9518 | encoded | `s 723(1) the company must make the payment out of capital by the closin...`; `s 723(1) the payment out of capital was made in the window` (+2 more) | coa15-tests-ch5.l4 |
| s 723(1A) | 9519-9521 | encoded | `s 723(1A) the shares were surrendered in the window` | coa15-tests-ch5.l4 |
| s 723(1A)(a) | 9520-9520 | encoded | `s 723(1A) the shares were surrendered in the window` | coa15-tests-ch5.l4 |
| s 723(1A)(b) | 9521-9521 | encoded | `s 723(1A) the shares were surrendered in the window` | coa15-tests-ch5.l4 |
| s 723(2) | 9522-9522 | encoded | `s 723(2) the dates and periods of subsection (1) are displaced by the c...` | coa15-tests-ch5.l4 |
| heading: Chapter 6 — Treasury shares | 9523-9523 | inert (reason 1) | a heading: not operative |  |
| s 724 Treasury shares | 9524-9535 | encoded | `s 724(1) this section applies`; `s 724(3) the company may do it with the shares` (+3 more) | coa15-tests-ch6.l4 |
| s 724(1) | 9525-9527 | encoded | `s 724(1) this section applies` | coa15-tests-ch6.l4 |
| s 724(1)(a) | 9526-9526 | encoded | `s 724(1) this section applies` | coa15-tests-ch6.l4 |
| s 724(1)(b) | 9527-9527 | encoded | `s 724(1) this section applies` | coa15-tests-ch6.l4 |
| s 724(2) | 9528-9528 | repealed or blank in this text | the text shows a row of dots |  |
| s 724(3) | 9529-9531 | encoded | `s 724(3) the company may do it with the shares` | coa15-tests-ch6.l4 |
| s 724(3)(a) | 9530-9530 | encoded | `s 724(3) the company may do it with the shares` | coa15-tests-ch6.l4 |
| s 724(3)(b) | 9531-9531 | encoded | `s 724(3) the company may do it with the shares` | coa15-tests-ch6.l4 |
| s 724(4) | 9532-9532 | encoded | `s 724(4) the company must be entered in its register of members`; `s 724(4) the company must be entered in its register of members as the ...` | coa15-tests-ch6.l4 |
| s 724(5) | 9533-9535 | encoded | `s 724(5) the company holds the shares as treasury shares` | coa15-tests-ch6.l4 |
| term: “holding shares as treasury shares” | 9533-9535 | encoded | `s 724(5) the company holds the shares as treasury shares` | coa15-tests-ch6.l4 |
| s 724(5)(a) | 9534-9534 | encoded | `s 724(5) the company holds the shares as treasury shares` | coa15-tests-ch6.l4 |
| s 724(5)(b) | 9535-9535 | encoded | `s 724(5) the company holds the shares as treasury shares` | coa15-tests-ch6.l4 |
| s 725 Treasury shares: maximum holdings | 9536-9537 | repealed or blank in this text | the text shows a row of dots |  |
| s 726 Treasury shares: exercise of rights | 9538-9546 | encoded | `s 726(4) section 726 prevents the transaction`; `s 726(2) the company may exercise a right in respect of the treasury sh...` (+5 more) | coa15-tests-ch6.l4 |
| s 726(1) | 9539-9539 | encoded | `s 726(1) this section applies` | coa15-tests-ch6.l4 |
| s 726(2) | 9540-9541 | encoded | `s 726(2) the company may exercise a right in respect of the treasury sh...`; `s 726(2) the company shant exercise a right in respect of the treasury ...` (+1 more) | coa15-tests-ch6.l4 |
| s 726(3) | 9542-9542 | encoded | `s 726(3) a dividend or other distribution may be paid or made to the co...` | coa15-tests-ch6.l4 |
| s 726(4) | 9543-9545 | encoded | `s 726(4) section 726 prevents the transaction` | coa15-tests-ch6.l4 |
| s 726(4)(a) | 9544-9544 | encoded | `s 726(4) section 726 prevents the transaction` | coa15-tests-ch6.l4 |
| s 726(4)(b) | 9545-9545 | encoded | `s 726(4) section 726 prevents the transaction` | coa15-tests-ch6.l4 |
| s 726(5) | 9546-9546 | encoded | `s 726(5) the shares are treated as purchased by the company, at the tim...` | coa15-tests-ch6.l4 |
| s 727 Treasury shares: disposal | 9547-9560 | encoded | `s 727(2) the consideration is a cash consideration`; `s 727(1) the company may dispose of the shares in that way` (+4 more) | coa15-tests-ch6.l4 |
| s 727(1) | 9548-9550 | encoded | `s 727(1) the company may dispose of the shares in that way` | coa15-tests-ch6.l4 |
| s 727(1)(a) | 9549-9549 | encoded | `s 727(1) the company may dispose of the shares in that way` | coa15-tests-ch6.l4 |
| s 727(1)(b) | 9550-9550 | encoded | `s 727(1) the company may dispose of the shares in that way` | coa15-tests-ch6.l4 |
| s 727(2) | 9551-9557 | encoded | `s 727(2) the consideration is a cash consideration`; `s 727(2) the money is cash` | coa15-tests-ch6.l4 |
| term: “cash consideration” | 9551-9551 | encoded | `s 727(2) the consideration is a cash consideration` | coa15-tests-ch6.l4 |
| s 727(2)(a) | 9552-9552 | encoded | `s 727(2) the consideration is a cash consideration` | coa15-tests-ch6.l4 |
| s 727(2)(b) | 9553-9553 | encoded | `s 727(2) the consideration is a cash consideration` | coa15-tests-ch6.l4 |
| s 727(2)(c) | 9554-9554 | encoded | `s 727(2) the consideration is a cash consideration` | coa15-tests-ch6.l4 |
| s 727(2)(d) | 9555-9555 | encoded | `s 727(2) the consideration is a cash consideration` | coa15-tests-ch6.l4 |
| s 727(2)(e) | 9556-9557 | encoded | `s 727(2) the money is cash`; `s 727(2) the consideration is a cash consideration` | coa15-tests-ch6.l4 |
| term: “cash” | 9557-9557 | encoded | `s 727(2) the money is cash` | coa15-tests-ch6.l4 |
| s 727(3) | 9558-9558 | encoded | `s 727(3) the means of payment is regarded as falling within subsection ...` | coa15-tests-ch6.l4 |
| s 727(4) | 9559-9559 | encoded | `s 727(4) the company shant sell or transfer the shares except to the pe...`; `s 727(4) the sale or transfer is barred` | coa15-tests-ch6.l4 |
| s 727(5) | 9560-9560 | inert (reason 2) | machinery: the procedure for an order-making power (negative resolution) |  |
| s 728 Treasury shares: notice of disposal | 9561-9573 | fork F-empty-list, F-must, F-not-in-default, F-penalty | `s 728(1) the company must deliver a return to the registrar`; `s 728(1) the last day for delivering the return to the registrar` (+5 more) | coa15-tests-ch6.l4 |
| s 728(1) | 9562-9565 | encoded | `s 728(1) the company must deliver a return to the registrar`; `s 728(1) the last day for delivering the return to the registrar` (+1 more) | coa15-tests-ch6.l4 |
| s 728(1)(a) | 9563-9563 | encoded | `s 728(1) the company must deliver a return to the registrar`; `s 728(1) the last day for delivering the return to the registrar` (+1 more) | coa15-tests-ch6.l4 |
| s 728(1)(b) | 9564-9565 | encoded | `s 728(1) the company must deliver a return to the registrar`; `s 728(1) the last day for delivering the return to the registrar` (+1 more) | coa15-tests-ch6.l4 |
| s 728(2) | 9566-9568 | fork F-empty-list, F-must | `s 728(2) the return states what the section requires` | coa15-tests-ch6.l4 |
| s 728(2)(a) | 9567-9567 | fork F-empty-list, F-must | `s 728(2) the return states what the section requires` | coa15-tests-ch6.l4 |
| s 728(2)(b) | 9568-9568 | fork F-empty-list, F-must | `s 728(2) the return states what the section requires` | coa15-tests-ch6.l4 |
| s 728(3) | 9569-9569 | encoded | `s 728(3) the particulars may be included in a single return` | coa15-tests-ch6.l4 |
| s 728(4) | 9570-9570 | fork F-not-in-default | `s 728(4) the person commits an offence` | coa15-tests-ch6.l4 |
| s 728(5) | 9571-9573 | fork F-penalty | `s 728(5) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 728(5)(a) | 9572-9572 | encoded | `s 728(5) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 728(5)(b) | 9573-9573 | fork F-penalty | `s 728(5) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 729 Treasury shares: cancellation | 9574-9579 | encoded | `s 729(1) the company may cancel the shares`; `s 729(4) the amount of the company's share capital after the cancellation` (+1 more) | coa15-tests-ch6.l4 |
| s 729(1) | 9575-9575 | encoded | `s 729(1) the company may cancel the shares` | coa15-tests-ch6.l4 |
| s 729(2) | 9576-9576 | repealed or blank in this text | the text shows a row of dots |  |
| s 729(3) | 9577-9577 | repealed or blank in this text | the text shows a row of dots |  |
| s 729(4) | 9578-9578 | encoded | `s 729(4) the amount of the company's share capital after the cancellation` | coa15-tests-ch6.l4 |
| s 729(5) | 9579-9579 | encoded | `s 729(5) the directors may take the steps without complying with Chapte...` | coa15-tests-ch6.l4 |
| s 730 Treasury shares: notice of cancellation | 9580-9600 | fork F-empty-list, F-must, F-not-in-default | `s 730(5) the statement of capital states what the section requires`; `s 730(2) the return states what the section requires` (+7 more) | coa15-tests-ch6.l4 |
| s 730(1) | 9581-9582 | encoded | `s 730(1) the company must deliver a return to the registrar`; `s 730(1) the last day for delivering the return to the registrar` (+1 more) | coa15-tests-ch6.l4 |
| s 730(2) | 9583-9585 | fork F-empty-list, F-must | `s 730(2) the return states what the section requires` | coa15-tests-ch6.l4 |
| s 730(2)(a) | 9584-9584 | fork F-empty-list, F-must | `s 730(2) the return states what the section requires` | coa15-tests-ch6.l4 |
| s 730(2)(b) | 9585-9585 | fork F-empty-list, F-must | `s 730(2) the return states what the section requires` | coa15-tests-ch6.l4 |
| s 730(3) | 9586-9586 | encoded | `s 730(3) the particulars may be included in a single return` | coa15-tests-ch6.l4 |
| s 730(4) | 9587-9587 | fork F-must | `s 730(4) the notice is accompanied by a statement of capital` | coa15-tests-ch6.l4 |
| s 730(5) | 9588-9596 | encoded | `s 730(5) the statement of capital states what the section requires` | coa15-tests-ch6.l4 |
| s 730(5)(a) | 9589-9589 | encoded | `s 730(5) the statement of capital states what the section requires` | coa15-tests-ch6.l4 |
| s 730(5)(b) | 9590-9590 | encoded | `s 730(5) the statement of capital states what the section requires` | coa15-tests-ch6.l4 |
| s 730(5)(ba) | 9591-9591 | encoded | `s 730(5) the statement of capital states what the section requires` | coa15-tests-ch6.l4 |
| s 730(5)(c) | 9592-9595 | encoded | `s 730(5) the statement of capital states what the section requires` | coa15-tests-ch6.l4 |
| s 730(5)(d) | 9596-9596 | repealed or blank in this text | the text shows a row of dots |  |
| s 730(6) | 9597-9599 | fork F-not-in-default | `s 730(6) the person commits an offence` | coa15-tests-ch6.l4 |
| s 730(6)(a) | 9598-9598 | fork F-not-in-default | `s 730(6) the person commits an offence` | coa15-tests-ch6.l4 |
| s 730(6)(b) | 9599-9599 | fork F-not-in-default | `s 730(6) the person commits an offence` | coa15-tests-ch6.l4 |
| s 730(7) | 9600-9600 | encoded | `s 730(7) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 731 Treasury shares: treatment of proceed... | 9601-9609 | fork F-weighted | `s 731(3)(b) the amount to be transferred to the company's share premium...`; `s 731(4)(b) the purchase price paid for the shares` (+4 more) | coa15-tests-ch6.l4 |
| s 731(1) | 9602-9602 | encoded | `s 731(1) this section applies to the proceeds of sale`; `s 731(2) the amount treated as a realised profit of the company for the...` | coa15-tests-ch6.l4 |
| s 731(2) | 9603-9603 | encoded | `s 731(2) the amount treated as a realised profit of the company for the...` | coa15-tests-ch6.l4 |
| s 731(3) | 9604-9606 | encoded | `s 731(3)(b) the amount to be transferred to the company's share premium...`; `s 731(3)(a) the amount treated as a realised profit of the company` | coa15-tests-ch6.l4 |
| s 731(3)(a) | 9605-9605 | encoded | `s 731(3)(a) the amount treated as a realised profit of the company`; `s 731(3)(b) the amount to be transferred to the company's share premium...` | coa15-tests-ch6.l4 |
| s 731(3)(b) | 9606-9606 | encoded | `s 731(3)(b) the amount to be transferred to the company's share premium...` | coa15-tests-ch6.l4 |
| s 731(4) | 9607-9609 | fork F-weighted | `s 731(4)(b) the purchase price paid for the shares`; `s 731(4)(a) the purchase price paid by the company for the shares sold` | coa15-tests-ch6.l4 |
| s 731(4)(a) | 9608-9608 | fork F-weighted | `s 731(4)(a) the purchase price paid by the company for the shares sold`; `s 731(4)(b) the purchase price paid for the shares` | coa15-tests-ch6.l4 |
| s 731(4)(b) | 9609-9609 | encoded | `s 731(4)(b) the purchase price paid for the shares` | coa15-tests-ch6.l4 |
| s 732 Treasury shares: offences | 9610-9616 | fork F-not-in-default | `s 732(1) the person commits an offence`; `s 732(2) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 732(1) | 9611-9613 | fork F-not-in-default | `s 732(1) the person commits an offence` | coa15-tests-ch6.l4 |
| s 732(1)(a) | 9612-9612 | fork F-not-in-default | `s 732(1) the person commits an offence` | coa15-tests-ch6.l4 |
| s 732(1)(b) | 9613-9613 | fork F-not-in-default | `s 732(1) the person commits an offence` | coa15-tests-ch6.l4 |
| s 732(2) | 9614-9616 | encoded | `s 732(2) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 732(2)(a) | 9615-9615 | encoded | `s 732(2) the penalty on conviction` | coa15-tests-ch6.l4 |
| s 732(2)(b) | 9616-9616 | encoded | `s 732(2) the penalty on conviction` | coa15-tests-ch6.l4 |
| heading: Chapter 7 — Supplementary provisions | 9617-9617 | inert (reason 1) | a heading: not operative |  |
| s 733 The capital redemption reserve | 9618-9631 | encoded | `s 733(3) the amount of the difference to be transferred to the capital ...`; `s 733(2) the amount to be transferred to the capital redemption reserve` (+4 more) | coa15-tests-ch7.l4 |
| s 733(1) | 9619-9619 | encoded | `s 733(1) the company must transfer the amount to the capital redemption...` | coa15-tests-ch7.l4 |
| term: “capital redemption reserve” | 9619-9619 | encoded | `s 733(1) the company must transfer the amount to the capital redemption...` | coa15-tests-ch7.l4 |
| s 733(2) | 9620-9623 | encoded | `s 733(2) the amount to be transferred to the capital redemption reserve` | coa15-tests-ch7.l4 |
| s 733(2)(a) | 9621-9621 | encoded | `s 733(2) the amount to be transferred to the capital redemption reserve` | coa15-tests-ch7.l4 |
| s 733(2)(b) | 9622-9623 | encoded | `s 733(2) the amount to be transferred to the capital redemption reserve` | coa15-tests-ch7.l4 |
| s 733(3) | 9624-9628 | encoded | `s 733(3) the amount of the difference to be transferred to the capital ...` | coa15-tests-ch7.l4 |
| s 733(3)(a) | 9625-9625 | encoded | `s 733(3) the amount of the difference to be transferred to the capital ...` | coa15-tests-ch7.l4 |
| s 733(3)(b) | 9626-9628 | encoded | `s 733(3) the amount of the difference to be transferred to the capital ...` | coa15-tests-ch7.l4 |
| s 733(4) | 9629-9629 | encoded | `s 733(4) the amount to be transferred to the capital redemption reserve` | coa15-tests-ch7.l4 |
| s 733(5) | 9630-9630 | encoded | `s 733(5) the company may use the capital redemption reserve to pay up t...` | coa15-tests-ch7.l4 |
| s 733(6) | 9631-9631 | encoded | `s 733(6) the paid up share capital to take for the provision` | coa15-tests-ch7.l4 |
| s 734 Accounting consequences of payment ou... | 9632-9640 | encoded | `s 734(3) the amount may be reduced`; `s 734(3) the most by which the amounts may be reduced` (+4 more) | coa15-tests-ch7.l4 |
| s 734(1) | 9633-9633 | encoded | `s 734(1) this section applies` | coa15-tests-ch7.l4 |
| s 734(1A) | 9634-9634 | encoded | `s 734(1A) the permissible capital payment for a payment under section 6...` | coa15-tests-ch7.l4 |
| s 734(2) | 9635-9635 | encoded | `s 734(2) the amount to be transferred to the capital redemption reserve` | coa15-tests-ch7.l4 |
| s 734(3) | 9636-9639 | encoded | `s 734(3) the amount may be reduced`; `s 734(3) the most by which the amounts may be reduced` | coa15-tests-ch7.l4 |
| s 734(3)(a) | 9637-9637 | encoded | `s 734(3) the amount may be reduced`; `s 734(3) the most by which the amounts may be reduced` | coa15-tests-ch7.l4 |
| s 734(3)(b) | 9638-9639 | encoded | `s 734(3) the amount may be reduced`; `s 734(3) the most by which the amounts may be reduced` | coa15-tests-ch7.l4 |
| s 734(4) | 9640-9640 | encoded | `s 734(4) the amount to read as the permissible capital payment in subse...` | coa15-tests-ch7.l4 |
| s 735 Effect of company's failure to redeem... | 9641-9659 | fork F-grant-735-4 | `s 735(5) subsection (4) does not apply`; `s 735(6) the claim is paid in priority to any amount the company is lia...` (+7 more) | coa15-tests-ch7.l4 |
| s 735(1) | 9642-9644 | encoded | `s 735(1) this section applies` | coa15-tests-ch7.l4 |
| s 735(1)(a) | 9643-9643 | encoded | `s 735(1) this section applies` | coa15-tests-ch7.l4 |
| s 735(1)(b) | 9644-9644 | encoded | `s 735(1) this section applies` | coa15-tests-ch7.l4 |
| s 735(2) | 9645-9646 | encoded | `s 735(2) the company is liable in damages for the failure`; `s 735(2) the holder's right survives the failure` | coa15-tests-ch7.l4 |
| s 735(3) | 9647-9647 | encoded | `s 735(3) the court shall not grant specific performance`; `s 735(3) the court shant grant an order for specific performance` | coa15-tests-ch7.l4 |
| s 735(4) | 9648-9649 | fork F-grant-735-4 | `s 735(4) the terms of redemption or purchase may be enforced against th...`; `s 735(4) the shares are treated as cancelled` | coa15-tests-ch7.l4 |
| s 735(5) | 9650-9655 | encoded | `s 735(5) subsection (4) does not apply` | coa15-tests-ch7.l4 |
| s 735(5)(a) | 9651-9651 | encoded | `s 735(5) subsection (4) does not apply` | coa15-tests-ch7.l4 |
| s 735(5)(b) | 9652-9655 | encoded | `s 735(5) subsection (4) does not apply` | coa15-tests-ch7.l4 |
| s 735(6) | 9656-9659 | encoded | `s 735(6) the claim is paid in priority to any amount the company is lia...` | coa15-tests-ch7.l4 |
| s 735(6)(a) | 9657-9657 | encoded | `s 735(6) the claim is paid in priority to any amount the company is lia...` | coa15-tests-ch7.l4 |
| s 735(6)(b) | 9658-9659 | encoded | `s 735(6) the claim is paid in priority to any amount the company is lia...` | coa15-tests-ch7.l4 |
| s 736 Meaning of “distributable profits” | 9660-9661 | encoded | `s 736 the profits are distributable profits in relation to the payment` | coa15-tests-ch7.l4 |
| term: “distributable profits” | 9661-9661 | encoded | `s 736 the profits are distributable profits in relation to the payment` | coa15-tests-ch7.l4 |
| s 737 General power to make further provisi... | 9662-9668 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |
| s 737(1) | 9663-9663 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |
| s 737(2) | 9664-9666 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |
| s 737(2)(a) | 9665-9665 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |
| s 737(2)(b) | 9666-9666 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |
| s 737(3) | 9667-9667 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |
| s 737(4) | 9668-9668 | inert (reason 2) | machinery: a regulation-making power (s 737) |  |

## Audit of the coverage table

- Text lines in the range: 924 (lines 8745-9668 of `ukpga-2006-46.txt`), 924 of them non-blank.
- Units counted by `work/units.py`: 809 (28 headings, 83 sections, 332 subsections, 344 paragraphs, 22 defined terms). Every non-blank line falls inside at least one unit (the script lists the uncovered lines, and there are none).
- Rows in the table before the audit's additions: 809. After: 815. The audit added 6 defined terms the script's pattern missed ("off-market", "marketing arrangement", "market purchase", "vests in possession", "in the same group", "holding shares as treasury shares").
- Dispositions: encoded 529, fork 241, inert reason 1 28, inert reason 2 8, repealed or blank in this text 9. Total 815.
- Rows with no declaration, no inert reason and no blank text (UNMAPPED): 0.

## Fork register (coa15)

A fork is a place where the text can be read two ways with different outcomes. For each: the provisions, the answer taken, the other reading, and the text that licenses the choice. The sites are listed from the `-- fork F-...` comments in the `.l4` files, so a site cannot be named here without being tagged there. The rows of the coverage table that rest on a fork say `fork F-...`.

| fork | provision | sites in the L4 | answer taken | the other reading | licence |
| --- | --- | --- | --- | --- | --- |
| F-must: A bare "must" that is not done | e.g. s 714(2): "The statement must specify the amount of the permissible capital payment"; s 702(3): the copy "must be kept available for inspection"; s 728(2): the return "must state" the number and nominal value. | s 663(2), s 663(3), s 664(3), s 664(4), s 665(3), s 689(2), s 692(1B), s 693A(3), s 693A(5), s 694(2), s 696(2)(a), s 696(2)(b), s 696(3), s 696(4), s 697(2), s 699(3), s 700(2), s 702(2), s 702(3), s 702(4), s 707(2), s 707(3), s 707(4), s 708(2), s 714(2), s 714(3), s 714(4), s 714(5), s 714(6), s 714, s 716(1), s 718(2)(b), s 719(1), s 719(2), s 720(1), s 720(2), s 720A(4), s 720B(5), s 721(4), s 728(2), s 730(2), s 730(4) | The function answers whether the requirement is met: `JUST TRUE` if it is, `JUST FALSE` if it is not (the requirement is the text's own, introduced by "must"). | `NOTHING`: a duty that is not done is a breach, and the text does not tie a breach to "the requirement is not met". The same duty is also a `DEONTIC` where the text gives a party and an act. | the maintainer, 2026-11-05 (cases decided at encoding time); ruling N2 (flat negatives count as the text's no). |
| F-not-in-default: An officer who is not in default | Every offence of the Part charges "every officer of the company who is in default" (or every director in default): s 658(2)(a), 663(4), 667(2), 680(1), 689(4), 703(1), 707(6), 708(4), 715(1), 720(5), 720B(7) and (8), 722(4), 728(4), 730(6), 732(1). | s 658(2)(a), s 663(4), s 667(2), s 680(1), s 689(4), s 703(1), s 707(6), s 708(4), s 715(1), s 720(5), s 720B(7), s 720B(8), s 722(4), s 728(4), s 730(6), s 732(1) | `NOTHING` for an officer (or director) the facts say is not in default: the text charges officers in default and does not say what is true of one who is not (a limit on its own wording). | `JUST FALSE`: an officer not in default commits no offence. | Ruling of 2026-11-05 (c): a scope limit with no "only" answers `NOTHING`. |
| F-are: A list closed by "are" | s 681(2): "Those transactions are— (a) ... (g)"; s 682(2): "The transactions to which this section applies are— (a) ... (d)". | s 681(1), s 682(2) | A transaction not in the list is answered `JUST FALSE` for that section (the list is a definition: it "are"). | `NOTHING`: the list is not closed with "only". | The text's own words: a list introduced by "are" defines the transactions of the section; ruling N2. |
| F-penalty: Two wordings of the daily default fine run together | s 707(7)(b) (line 9300) and s 728(5)(b) (line 9573): "one-tenth of the statutory maximumone-tenth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale for summary offences". | s 707(7), s 728(5) | An input `the wording that substitutes the greater of £5,000 and the level 4 amount is in force` (`MAYBE BOOLEAN`): `JUST TRUE` gives one-tenth of the greater of £5,000 and level 4, `JUST FALSE` gives one-tenth of the statutory maximum, `NOTHING` gives `NOTHING`. | Take the second wording as the law in force (a substitution) and answer it always; or the first (the text before the amendment). | Lines 9300 and 9573 of the rendering; `NEEDS-CORE.md` items 1 and 2. |
| F-immediately: "immediately" | s 722(1): the applicants "must immediately give notice to the registrar"; s 722(2): the company "must immediately give notice". | s 722(1), s 722(2) | The day of the event: `WITHIN 0`, so a notice the day after is a breach. | A short time after the event (the next day, or a reasonable time). | The word "immediately"; no period is stated. |
| F-end: An application on the last day of the period | s 666(1): a public company that "fails to do so before the end of the period specified in subsection (3)" of s 662. | s 666(1) | An application made on the last day of the period is in time (`s 666(1)` answers `JUST FALSE`); one made the day after is late. | "Before the end" means before the last day: an application on the last day is late. | The words "before the end of the period" (the period ends at the end of its last day). |
| F-permissible: Negative available profits | s 710(1): the permissible capital payment is the amount required to meet the price "after applying for that purpose any available profits ... and the proceeds of any fresh issue". | s 710(1) | A negative amount of available profits applies nothing: it counts as 0, so the permissible capital payment never exceeds the price. | A negative amount increases the permissible capital payment above the price. | "applying ... any available profits": a loss is not applied. |
| F-signpost: "This section is subject to ..." | ss 687(6) and 692(5) ("subject to section 735(4)"), s 709(3) ("This Chapter is subject to section 692(1ZA)"). | s 687(6), s 692(5), s 709(3) | A function takes the named provision's answer (or the fact that makes it apply) as an input: `JUST TRUE` where it applies (the section is displaced), `NOTHING` otherwise. The Part-wide signposts (s 658(1) "in accordance with the provisions of this Part"; ss 678(5) and 679(5), which compose ss 681 and 682) are likewise taken from the named provisions or as plain inputs, never restated. | Leave the signposts inert, or answer `JUST FALSE` where the named provision does not apply. | Ruling of 2026-11-05 (c); the Guide's rule that a rule is stated once. |
| F-month: "within one month after" | s 663(1) and s 689(1): the company "must within one month after the shares are cancelled (redeemed) give notice to the registrar". | s 663(1), s 689(1) | The last day is the corresponding date one month on, clamped to the end of the month (15 January gives 15 February; 31 January gives 28 February). | The last day is the day before the corresponding date (14 February). | The words "within one month after". |
| F-ten-years: "the end of the period of ten years beginning with" a date | s 702(3): the copy must be kept available until "the end of the period of ten years beginning with" the completion of the purchase or the date the contract otherwise determines. | s 702(3) | The last day is the day before the tenth anniversary (1 January 2026 gives 31 December 2035). | The tenth anniversary itself (1 January 2036). | The words "the period of ten years beginning with" a date (a period beginning with a day includes that day). |
| F-period-start: "the period of three months ending with the date" | s 712(7): "the relevant period" means the period of three months ending with the date on which the directors' statement (or solvency statement) is made. | s 712(7) | The period begins the day after the date three months earlier (a statement on 15 June gives a period beginning 16 March). | The period begins on the date three months earlier (15 March). | The words "the period of three months ending with the date". |
| F-empty-list: No class entry in the facts | s 663(3) (and so ss 689(3), 708(3), 720B(2), 730(5)), s 728(2), s 730(2): the statement or return "must state, with respect to each class". | s 663(3), s 728(2), s 730(2) | `NOTHING`: with no class entry in the facts the facts do not say that the company has a class of shares, so the rule has no case. | `JUST TRUE` (every one of no entries states the items) or `JUST FALSE` (a statement with no entry fails to state the classes). | "each class": a universal over what the facts give. |
| F-omitted-word: "a . . . resolution" | ss 694(2)(a) and (b), 694(4), 697(2), 697(3), 700(2), 700(3) (lines 9146, 9147, 9149, 9176, 9177, 9205, 9206). | s 694(2), s 694(4), s 697(2), s 697(3), s 700(2), s 700(3) | The omitted word is not supplied: the rule asks whether the terms were authorised by "a resolution of the company", taken as a plain fact. | The omitted word was "special", so the rule needs a special resolution; or "ordinary", so an ordinary resolution suffices. | The rendering shows dots where a word stood; s 685(2) ("may be an ordinary resolution") says nothing of these sections. |
| F-other-than: "(other than directors)" | s 682(2)(d): loans "to persons (other than directors) employed in good faith by the company". | s 682(2)(d) | A loan to a director is outside limb (d): that limb answers `JUST FALSE`, and another limb of s 682(2) may still apply. | `NOTHING` for a loan to a director. | The words "(other than directors)" are an exclusion in the text's own words. |
| F-weighted: "a weighted average price method" | s 731(4)(a): "the purchase price paid by the company must be determined by the application of a weighted average price method". | s 731(4)(a) | The plain weighted average over the class held: the total price paid for the treasury shares of the class held, divided by the number held, times the number sold; `NOTHING` where no shares are held. | Another method (a moving average, or first in first out). | The words "weighted average price method", which the Act does not define. |
| F-grant-661-3: A grant or power whose "if" gate fails: s 661(3) the court may relieve the subscriber or director from his liability | s 661(3): "If in proceedings for the recovery of an amount under subsection (2) it appears to the court that the subscriber or director (a) has acted honestly and reasonably, and (b) ought fairly to be relieved ..., the court may relieve him". | s 661(3) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-661-4a: A grant or power whose "if" gate fails: s 661(4)(a) the subscriber or director may apply to the court for relief | s 661(4): "If a subscriber ... or a director ... has reason to apprehend that a claim will or might be made ..., (a) he may apply to the court for relief". | s 661(4)(a) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-661-4b: A grant or power whose "if" gate fails: s 661(4)(b) the court has the power to relieve him | s 661(4)(b): "the court has the same power to relieve him as it would have had in proceedings for recovery" (answers as s 661(4)(a) and s 661(3) do). | s 661(4)(b) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-685-1: A grant or power whose "if" gate fails: s 685(1) the directors may determine the terms, conditions and manner of redemption | s 685(1): "The directors of a limited company may determine the terms, conditions and manner of redemption of shares if they are authorised to do so". | s 685(1) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-690-1: A grant or power whose "if" gate fails: s 690(1) the limited company may purchase its own shares | s 690(1): "may purchase its own shares ..., subject to ... any restriction or prohibition in the company's articles" (the articles-restrict branch). | s 690(1) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-693A-1: A grant or power whose "if" gate fails: s 693A(1) the company may make the off-market purchase | s 693A(1): "may make an off-market purchase of its own shares for the purposes of or pursuant to an employees' share scheme if the purchase has first been authorised by a resolution". | s 693A(1) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-693A-6: A grant or power whose "if" gate fails: s 693A(6) the company may make a purchase of its own shares after the expiry of the time limit | s 693A(6): "may make a purchase of its own shares after the expiry of the time limit specified if (a) ... and (b) ...". | s 693A(6) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-701-6: A grant or power whose "if" gate fails: s 701(6) the company may make a purchase of its own shares after the expiry of the time limit | s 701(6): the same words as s 693A(6), answered by it. | s 701(6) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-709-1: A grant or power whose "if" gate fails: s 709(1) the private limited company may make the payment out of capital | s 709(1): "may in accordance with this Chapter, but subject to any restriction or prohibition in the company's articles, make a payment" (the articles-restrict branch; the branch where the payment is not in accordance with Chapter 5 keeps JUST FALSE, closed by s 713(1) "not lawful unless"). | s 709(1) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-721-5: A grant or power whose "if" gate fails: s 721(5) the court may by order alter or extend the date or period | s 721(5): "If the court confirms the resolution, it may by order alter or extend any date or period of time". | s 721(5) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-721-6: A grant or power whose "if" gate fails: s 721(6) the court's order may provide for the purchase of a member's shares and alter the articles | s 721(6): "The court's order may, if the court thinks fit, ...". | s 721(6) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-721-7: A grant or power whose "if" gate fails: s 721(7) the court's order may restrict amendments of the articles | s 721(7): "The court's order may, if the court thinks fit, require the company not to make any ... amendments of its articles". | s 721(7) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |
| F-grant-735-4: A grant or power whose "if" gate fails: s 735(4) the terms of redemption or purchase may be enforced against the company | s 735(4): "If the company is wound up and at the commencement of the winding up any of the shares have not been redeemed or purchased, the terms of redemption or purchase may be enforced against the company" (the branch where s 735(5) takes the case out keeps JUST FALSE, the text's own "does not apply"). | s 735(4) | `NOTHING` where the gate fails: the function is named for a grant or a power, the text limits it in its own words ("if", not "only if") and says nothing of the case outside the limit (Guide section 5, "In short"). | `JUST FALSE`: a failed "if" read as the text's own no, so that the grant reads as "may not". | Guide section 5 (a grant limited in its own wording answers `NOTHING` outside the limit); the lead's name-test sweep of 2026-11-12. |

### Left unsettled by the name-test sweep of 2026-11-12 (not flipped)

A function named for a grant whose gate is "where", "when" or "upon" answers `JUST FALSE` here, as ruling (b) of the periods ruling and ruling (c) of the 2026-11-05 delegated ruling say; the Guide's line on grants points to `NOTHING`. That conflict is a question for the maintainer or a lawyer; the sweep does not settle it. An "entitled"-named function is a claim, not a power, which the Guide does not settle.

| function | kind | the text and the open question |
| --- | --- | --- |
| `s 664(1) the directors may resolve that the company should be re-registered as a private company` | "may" with where/when/upon | "Where a company is obliged to re-register as a private company to comply with section 662, the directors may resolve". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 703(3) the court may order an immediate inspection` | "may" with where/when/upon | "In the case of refusal of an inspection required under section 702(6) the court may by order compel an immediate inspection". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 706(a) the shares may be held and dealt with in accordance with Chapter 6` | "may" with where/when/upon | "Where a limited company makes a purchase of its own shares in accordance with this Chapter, (a) if the purchase was made out of distributable profits, the company may hold the shares": the "Where" gate answers JUST FALSE for a purchase not in accordance with Chapter 4 (the "(b) otherwise" limb closes the profits gate). Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 720(7) the court may order an immediate inspection` | "may" with where/when/upon | "In the case of a refusal of an inspection required by subsection (4), the court may by order compel an immediate inspection". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 721(1) the person may apply to the court for the cancellation of the resolution` | "may" with where/when/upon | "Where a private company passes a special resolution approving a payment out of capital ..., any member of the company other than one who consented to or voted in favour of the resolution, or any creditor of the company, may apply to the court". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 721(3) the court may adjourn the proceedings and give directions and make orders` | "may" with where/when/upon | "On an application under this section the court may if it thinks fit—" (an "On an application" gate and an "if it thinks fit" gate). Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 724(3) the company may do it with the shares` | "may" with where/when/upon | "Where this section applies the company may— (a) hold the shares ..., or (b) deal with any of them". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 727(1) the company may dispose of the shares in that way` | "may" with where/when/upon | "Where shares are held as treasury shares, the company may at any time— (a) sell ..., or (b) transfer". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 729(1) the company may cancel the shares` | "may" with where/when/upon | "Where shares are held as treasury shares, the company may at any time cancel the shares". Answers `JUST FALSE` where the gate fails (ruling (b)); the other reading answers `NOTHING` (a grant limited in its own wording). |
| `s 664(6) the registrar may accept the statement as sufficient evidence that the company is entitled to be re-registered` | "entitled" | named for a power ("the registrar may accept"), not for an entitlement; it already answers `NOTHING` outside the statement of compliance. The open question is whether an entitlement's failed gate is `JUST FALSE` or `NOTHING`. |
| `s 721(2)(b) the application may be made on behalf of the persons entitled by the person` | "entitled" | named for a power to apply on behalf of "the persons entitled"; it already answers `NOTHING` outside its gate. The open question is whether an entitlement's failed gate is `JUST FALSE` or `NOTHING`. |

### Rulings the encoding follows (copied word for word from the brief)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.
- **Lists:** write a list of strings as a vertical `LIST` block, one string per line, not with `•` bullets (those are a parse error on the stable binary).

## Jural relations (coa15)

One row per subsection (or per section with no subsections) of the range. Hohfeld's correlatives: a claim is the other's duty; a privilege is the other's no-right; a power is the other's liability; an immunity is the other's disability. Where the text names no party who holds the claim or the privilege the cell says `none named in the text`: no claim-holder, prosecutor or sentencing court is invented (the court appears as the party who sentences because the offence provisions speak of liability on conviction). A provision that creates no relation (a definition, a counting rule, an applicability rule, a cross-reference) is listed once as `none`. The L4 column is the first declaration whose `@ref` locator reaches the unit.

| provision | holder (right) | bearer (correlative) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 658(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 658(1) a limited company must not make the acquisition` |
| s 658(2) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default (offence); the company (the purported acquisition is void) | liability (offence) | `s 658(2)(a) the person commits an offence` |
| s 658(3) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 658(3) the penalty on conviction` |
| s 659(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 659(1) a limited company may acquire its own shares` |
| s 659(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 659(2) section 658 does not prohibit the acquisition` |
| s 660(1) | none | none | none | none |
| s 660(2) | none | none | none | none |
| s 660(3) | none | none | none | none |
| s 661(1) | none | none | none | none |
| s 661(2) | claim: the company (the claim to the unpaid amount) | duty: the other subscribers or the directors, jointly and severally with the nominee | claim / duty | `s 661(2) the person is jointly and severally liable with the nominee to pay t...` |
| s 661(3) | power: the court (relieves) | liability: the company (loses the claim to that extent) | power / liability | `s 661(3) the court may relieve the subscriber or director from his liability` |
| s 661(4) | privilege: a subscriber or a director (to apply for relief) | no-right: none named in the text | privilege / no-right | `s 661(4)(a) the subscriber or director may apply to the court` |
| s 661(5) | none | none | none | none |
| s 662(1) | none | none | none | none |
| s 662(2) | claim: none named in the text | duty: a public company | claim / duty | `s 662(2)(a) the company must cancel the shares` |
| s 662(3) | claim: none named in the text | duty: a public company | claim / duty | `s 662(3) the company cancelled the shares in time` |
| s 662(4) | privilege: the directors | no-right: none named in the text | privilege / no-right | `s 662(4) the directors may take the steps without complying with Chapter 10 o...` |
| s 662(5) | claim: none named in the text | duty not to act: the company, and a nominee or other shareholder where (1)(d) or (e) applies | claim / duty not to act | `s 662(5) the person may exercise voting rights in respect of the shares` |
| s 662(6) | immunity: none named in the text | disability: the company (a purported exercise of the rights is void) | disability (the thing is void or not effective) | `s 662(6) the purported exercise of the voting rights is void` |
| s 663(1) | claim: none named in the text | duty: the company (to give notice to the registrar) | claim / duty | `s 663(1) the company must give notice to the registrar` |
| s 663(2) | claim: none named in the text | duty: the company | claim / duty | `s 663(2) the notice is accompanied by a statement of capital` |
| s 663(3) | claim: none named in the text | duty: the company (content of the statement of capital) | claim / duty | `s 663(3) the statement of capital states what the section requires` |
| s 663(4) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 663(4) the person commits an offence` |
| s 663(5) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 663(5) the penalty on conviction` |
| s 664(1) | privilege: the directors | no-right: none named in the text | privilege / no-right | `s 664(1) Chapter 3 of Part 3 applies to the resolution` |
| s 664(2) | privilege: the company (by its resolution) | no-right: none named in the text | privilege / no-right | `s 664(2) the resolution may make the change` |
| s 664(3) | claim: none named in the text | duty: the company | claim / duty | `s 664(3) the application contains what the section requires` |
| s 664(4) | claim: none named in the text | duty: the company | claim / duty | `s 664(4) the application is accompanied as the section requires` |
| s 664(5) | none | none | none | none |
| s 664(6) | power: the registrar (accepts the statement of compliance as sufficient evidence) | liability: the company | power / liability | `s 664(6) the registrar may accept the statement as sufficient evidence that t...` |
| s 665(1) | claim: none named in the text | duty: the registrar | claim / duty | `s 665(1) the company shall be re-registered as a private company` |
| s 665(2) | claim: none named in the text | duty: the registrar | claim / duty | `s 665(2) the registrar must issue a certificate of incorporation` |
| s 665(3) | claim: none named in the text | duty: the registrar | claim / duty | `s 665(3) the certificate states what the section requires` |
| s 665(4) | power: the registrar (by issuing the certificate) | liability: the company (becomes a private company; the name and articles change) | power / liability | `s 665(4)(a) the company becomes a private company by virtue of the issue of t...` |
| s 665(5) | immunity: the company | disability: any person who would challenge the re-registration | immunity / disability | `s 665(5) the certificate is conclusive evidence that the requirements as to r...` |
| s 666(1) | power (to sentence): none named in the text | liability to the penalty: a public company (treated as private for Chapter 1 of Part 20) | liability (penalty) | `s 666(1) Chapter 1 of Part 20 applies to the company as if it were a private ...` |
| s 666(2) | none | none | none | none |
| s 667(1) | none | none | none | none |
| s 667(2) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 667(2) the person commits an offence` |
| s 667(3) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 667(3) the penalty on conviction` |
| s 668(1) | none | none | none | none |
| s 668(2) | none | none | none | none |
| s 668(3) | none | none | none | none |
| s 669(1) | claim: none named in the text | duty: a public company | claim / duty | `s 669(1) an amount must be transferred out of profits available for dividend ...` |
| s 669(2) | none | none | none | none |
| s 670(1) | immunity: none named in the text | disability: a public company (a lien or charge on its own shares is void) | disability (the thing is void or not effective) | `s 670(1) the lien or charge is void` |
| s 670(2) | privilege: the company | no-right: the shareholder | privilege / no-right | `s 670(1) lien or charge of a company on its own shares` |
| s 670(3) | privilege: the company | no-right: the shareholder | privilege / no-right | `s 670(3) the charge is permitted` |
| s 670(4) | privilege: the company | no-right: the shareholder | privilege / no-right | `s 670(4) the charge is permitted` |
| s 671 | none | none | none | none |
| s 672(1) | none | none | none | none |
| s 672(2) | none | none | none | none |
| s 672(3) | none | none | none | none |
| s 672(4) | none | none | none | none |
| s 672(5) | none | none | none | none |
| s 672(6) | none | none | none | none |
| s 673(1) | none | none | none | none |
| s 673(2) | none | none | none | none |
| s 674 | none | none | none | none |
| s 675(1) | none | none | none | none |
| s 675(2) | none | none | none | none |
| s 676 | none | none | none | none |
| s 677(1) | none | none | none | none |
| s 677(2) | none | none | none | none |
| s 677(3) | none | none | none | none |
| s 678(1) | claim: none named in the text | duty not to act: a public company and its subsidiaries | claim / duty not to act | `s 678(1) it is not lawful for the company to give the financial assistance` |
| s 678(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 678(2) subsection (1) does not prohibit the assistance` |
| s 678(3) | claim: none named in the text | duty not to act: the company and its subsidiaries | claim / duty not to act | `s 678(3) it is not lawful for the company to give the financial assistance to...` |
| s 678(4) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 678(4) subsection (3) does not prohibit the assistance` |
| s 678(5) | none | none | none | none |
| s 679(1) | claim: none named in the text | duty not to act: a public company that is a subsidiary of a private company | claim / duty not to act | `s 679(1) it is not lawful for the public company to give the financial assist...` |
| s 679(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 679(2) subsection (1) does not prohibit the assistance` |
| s 679(3) | claim: none named in the text | duty not to act: a public company that is a subsidiary of a private company | claim / duty not to act | `s 679(3) it is not lawful for the public company to give the financial assist...` |
| s 679(4) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 679(4) subsection (3) does not prohibit the assistance` |
| s 679(5) | none | none | none | none |
| s 680(1) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 680(1) the person commits an offence` |
| s 680(2) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 680(2) the penalty on conviction` |
| s 681(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 681(1) neither section 678 nor section 679 prohibits the transaction` |
| s 681(2) | none | none | none | none |
| s 682(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 682(1) neither section 678 nor section 679 prohibits the transaction` |
| s 682(2) | none | none | none | none |
| s 682(3) | none | none | none | none |
| s 682(4) | none | none | none | none |
| s 682(5) | none | none | none | none |
| s 683(1) | none | none | none | none |
| s 683(2) | none | none | none | none |
| s 684(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 684(1) the company may issue redeemable shares` |
| s 684(2) | privilege: a private company (through its articles) | no-right: none named in the text | privilege / no-right | `s 684(2) the articles may exclude or restrict the issue of redeemable shares` |
| s 684(3) | privilege: a public company (only if its articles authorise) | no-right: none named in the text | privilege / no-right | `s 684(3) the public limited company may issue redeemable shares` |
| s 684(4) | immunity: none named in the text | disability: the company (no redeemable shares may be issued) | disability (the thing is void or not effective) | `s 684(4) the issue of redeemable shares is barred` |
| s 685(1) | power: the directors | liability: the company (bound by the terms the directors fix) | power / liability | `s 685(1) the directors may determine the terms, conditions and manner of rede...` |
| s 685(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 685(2) the resolution is a good resolution under subsection (1)(b)` |
| s 685(3) | claim: none named in the text | duty: the directors | claim / duty | `s 685(3)(b) the obligation to state the rights extends to the terms, conditio...` |
| s 685(4) | claim: none named in the text | duty: the company (to state the terms in its articles) | claim / duty | `s 685(4) the terms, conditions and manner of redemption must be stated in the...` |
| s 686(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 686(1) the redemption is barred` |
| s 686(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 686(2) the terms of redemption may provide for payment on a later date` |
| s 686(3) | claim: none named in the text | duty: the company | claim / duty | `s 686(3) the company must pay for the shares on redemption` |
| s 687(1) | privilege: a private company | no-right: none named in the text | privilege / no-right | `s 687(1) the private limited company may redeem the shares out of capital` |
| s 687(2) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 687(2) the redemption is out of a source the section permits` |
| s 687(3) | claim: none named in the text | duty: the company | claim / duty | `s 687(3) the part of the premium that must be paid out of distributable profits` |
| s 687(4) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 687(4) the most of the premium that may be paid out of the proceeds of a fr...` |
| s 687(5) | none | none | none | none |
| s 687(6) | none | none | none | none |
| s 688 | none | none | none | none |
| s 689(1) | claim: none named in the text | duty: the company | claim / duty | `s 689(1) the company must give notice to the registrar` |
| s 689(2) | claim: none named in the text | duty: the company | claim / duty | `s 689(2) the notice is accompanied by a statement of capital` |
| s 689(3) | claim: none named in the text | duty: the company | claim / duty | `s 689(3) the statement of capital states what the section requires` |
| s 689(4) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 689(4) the person commits an offence` |
| s 689(5) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 689(5) the penalty on conviction` |
| s 690(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 690(1) the limited company may purchase its own shares` |
| s 690(2) | immunity: none named in the text | disability: the company | disability (the thing is void or not effective) | `s 690(2) the purchase is barred` |
| s 691(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 691(1) the purchase is barred` |
| s 691(2) | claim: none named in the text | duty: the company | claim / duty | `s 691(2) the company must pay for the shares on purchase` |
| s 691(3) | privilege: a private company | no-right: none named in the text | privilege / no-right | `s 691(3) subsection (2) does not apply` |
| s 692(1) | privilege: a private company | no-right: none named in the text | privilege / no-right | `s 692(1) the private limited company may purchase its own shares out of capital` |
| s 692(1A) | none | none | none | none |
| s 692(1B) | none | none | none | none |
| s 692(1ZA) | privilege: a private company (if its articles authorise) | no-right: none named in the text | privilege / no-right | `s 692(1ZA) the most the company may pay out of capital in the financial year` |
| s 692(2) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 692(2)(a) the purchase is out of a source the section permits` |
| s 692(3) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 692(3) the most of the premium that may be paid out of the proceeds of a fr...` |
| s 692(4) | none | none | none | none |
| s 692(5) | none | none | none | none |
| s 693(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 693(1) the limited company may make the purchase` |
| s 693(2) | none | none | none | none |
| s 693(3) | none | none | none | none |
| s 693(4) | none | none | none | none |
| s 693(5) | none | none | none | none |
| s 693A(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 693A(1) the company may make the off-market purchase` |
| s 693A(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 693A(2) the authority may take that form` |
| s 693A(3) | claim: none named in the text | duty: the company (in the resolution) | claim / duty | `s 693A(3) the authority contains what the subsection requires` |
| s 693A(4) | power: the company (by resolution) | liability: none named in the text | power / liability | `s 693A(4) the authority may be varied, revoked or renewed` |
| s 693A(5) | claim: none named in the text | duty: the company (in the resolution) | claim / duty | `s 693A(5) the latest date on which the authority may be specified to expire` |
| s 693A(6) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 693A(6) the company may make a purchase of its own shares after the expiry ...` |
| s 693A(7) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 693A(7) the resolution may determine the price in that way` |
| s 693A(8) | none | none | none | none |
| s 694(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 694(1) the company may make the off-market purchase` |
| s 694(2) | claim: none named in the text | duty: the company | claim / duty | `s 694(2) the contract is approved in the way the subsection requires` |
| s 694(3) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 694(3) the contract is a contract within section 694` |
| s 694(4) | power: the company (by resolution) | liability: none named in the text | power / liability | `s 694(4) the authority may be varied, revoked or renewed` |
| s 694(5) | claim: none named in the text | duty: a public company (in the resolution) | claim / duty | `s 694(5) the resolution specifies a date of expiry that is not later than fiv...` |
| s 694(6) | none | none | none | none |
| s 695(1) | none | none | none | none |
| s 695(2) | immunity: none named in the text | disability: a member holding shares to which the resolution relates (not an eligible member) | disability (the thing is void or not effective) | `s 695(2) the member is not an eligible member` |
| s 695(3) | immunity: none named in the text | disability: the resolution (not effective) | disability (the thing is void or not effective) | `s 695(3) the resolution is not effective` |
| s 695(4) | none | none | none | none |
| s 696(1) | none | none | none | none |
| s 696(2) | claim: a member (to inspect and to be sent the copy) | duty: the company | claim / duty | `s 696(2) the company must make the copy or memorandum available to members` |
| s 696(3) | claim: a member | duty: the company | claim / duty | `s 696(3) the memorandum includes what the subsection requires` |
| s 696(4) | claim: a member | duty: the company | claim / duty | `s 696(4) the copy has annexed to it what the subsection requires` |
| s 696(5) | immunity: none named in the text | disability: the resolution (not validly passed) | disability (the thing is void or not effective) | `s 696(5) the resolution is not validly passed` |
| s 697(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 697(1) the company may agree to the variation` |
| s 697(2) | claim: none named in the text | duty: the company | claim / duty | `s 697(2) the variation is authorised in the way the subsection requires` |
| s 697(3) | power: the company (by resolution) | liability: none named in the text | power / liability | `s 697(3) the authority may be varied, revoked or renewed` |
| s 697(4) | claim: none named in the text | duty: a public company | claim / duty | `s 697(4) the resolution specifies a date of expiry that is not later than fiv...` |
| s 697(5) | none | none | none | none |
| s 698(1) | none | none | none | none |
| s 698(2) | immunity: none named in the text | disability: a member holding shares to which the resolution relates (not an eligible member) | disability (the thing is void or not effective) | `s 698(2) the member is not an eligible member` |
| s 698(3) | immunity: none named in the text | disability: the resolution (not effective) | disability (the thing is void or not effective) | `s 698(3) the resolution is not effective` |
| s 698(4) | none | none | none | none |
| s 699(1) | none | none | none | none |
| s 699(2) | claim: a member | duty: the company | claim / duty | `s 699(2)(b) the copy or memorandum was made available to members for a resolu...` |
| s 699(3) | claim: a member | duty: the company | claim / duty | `s 699(3) the original contract is also made available` |
| s 699(4) | claim: a member | duty: the company | claim / duty | `s 699(4) the memorandum includes what the subsection requires` |
| s 699(5) | claim: a member | duty: the company | claim / duty | `s 699(5) the copy has annexed to it what the subsection requires` |
| s 699(6) | immunity: none named in the text | disability: the resolution (not validly passed) | disability (the thing is void or not effective) | `s 699(6) the resolution is not validly passed` |
| s 700(1) | immunity: none named in the text | disability: the company (the release agreement is void) | disability (the thing is void or not effective) | `s 700(1) the release agreement is void` |
| s 700(2) | claim: none named in the text | duty: the company | claim / duty | `s 700(2) the release agreement is authorised in the way the subsection requires` |
| s 700(3) | power: the company (by resolution) | liability: none named in the text | power / liability | `s 700(3) the authority may be varied, revoked or renewed` |
| s 700(4) | claim: none named in the text | duty: a public company | claim / duty | `s 700(4) the resolution specifies a date of expiry that is not later than fiv...` |
| s 700(5) | none | none | none | none |
| s 701(1) | claim: none named in the text | duty not to act: the company | claim / duty not to act | `s 701(1) the company may make the market purchase` |
| s 701(2) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 701(2) the authority may take that form` |
| s 701(3) | claim: none named in the text | duty: the company (in the resolution) | claim / duty | `s 701(3) the authority contains what the subsection requires` |
| s 701(4) | power: the company (by resolution) | liability: none named in the text | power / liability | `s 701(4) the authority may be varied, revoked or renewed` |
| s 701(5) | claim: none named in the text | duty: the company (in the resolution) | claim / duty | `s 701(5) the resolution specifies a date of expiry that is not later than fiv...` |
| s 701(6) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 701(6) the company may make a purchase of its own shares after the expiry o...` |
| s 701(7) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 701(7) the resolution may determine the price in that way` |
| s 701(8) | none | none | none | none |
| s 702(1) | none | none | none | none |
| s 702(2) | claim: none named in the text | duty: the company | claim / duty | `s 702(2) the company has kept the copy or memorandum available for inspection` |
| s 702(3) | claim: none named in the text | duty: the company | claim / duty | `s 702(3) the copy or memorandum was kept available for the period` |
| s 702(4) | claim: none named in the text | duty: the company | claim / duty | `s 702(4) the copy or memorandum is kept at a place the subsection allows` |
| s 702(5) | claim: none named in the text | duty: the company (to give notice to the registrar) | claim / duty | `s 702(5) the company must give notice to the registrar of the place` |
| s 702(6) | claim: a member (to inspect without charge) | duty: the company | claim / duty | `s 702(6) the person may inspect the copy or memorandum without charge` |
| s 702(7) | none | none | none | none |
| s 703(1) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 703(1) the company is in default as the subsection describes` |
| s 703(2) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 703(2) the penalty on conviction` |
| s 703(3) | power: the court (orders an immediate inspection) | liability: the company | power / liability | `s 703(3) the court may order an immediate inspection` |
| s 704 | immunity: none named in the text | disability: the company (its right to purchase is not capable of being assigned) | disability (the thing is void or not effective) | `s 704 the company's right under the contract is capable of being assigned` |
| s 705(1) | claim: none named in the text | duty: the company (to pay out of distributable profits) | claim / duty | `s 705(1) the payment must be made out of the company's distributable profits` |
| s 705(2) | immunity: none named in the text | disability: the company (no purchase under the contract; no purchase after the variation; the release is void) | disability (the thing is void or not effective) | `s 705(2) the consequence of the requirement not being met` |
| s 706 | privilege: the company (to hold the shares as treasury shares where s 724 applies) | no-right: none named in the text | privilege / no-right | `s 706(b)(ii) the amount of the company's issued share capital after the purchase` |
| s 707(1) | claim: none named in the text | duty: the company (to deliver a return to the registrar) | claim / duty | `s 707(1) the company must deliver a return to the registrar` |
| s 707(2) | claim: none named in the text | duty: the company | claim / duty | `s 707(2) the return distinguishes what the subsection requires` |
| s 707(3) | claim: none named in the text | duty: the company | claim / duty | `s 707(3) the return states what the subsection requires` |
| s 707(4) | claim: none named in the text | duty: a public company | claim / duty | `s 707(4) the return also states what the subsection requires` |
| s 707(5) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 707(5) the amount to state under subsection (4)(a) in a single return` |
| s 707(6) | power (to prosecute): none named in the text | liability to conviction: every officer in default | liability (offence) | `s 707(6) the person commits an offence` |
| s 707(7) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 707(7) the penalty on conviction` |
| s 708(1) | claim: none named in the text | duty: the company (to give notice to the registrar) | claim / duty | `s 708(1) the company must give notice of cancellation to the registrar` |
| s 708(2) | claim: none named in the text | duty: the company | claim / duty | `s 708(2) a statement of capital must accompany the notice` |
| s 708(3) | claim: none named in the text | duty: the company | claim / duty | `s 708(3) the statement of capital states what the subsection requires` |
| s 708(4) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 708(4) the person commits an offence` |
| s 708(5) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 708(5) the penalty on conviction` |
| s 709(1) | privilege: a private company (subject to its articles) | no-right: none named in the text | privilege / no-right | `s 709(1) the private limited company may make the payment out of capital` |
| s 709(2) | none | none | none | none |
| s 709(3) | none | none | none | none |
| s 710(1) | none | none | none | none |
| s 710(2) | none | none | none | none |
| s 711(1) | none | none | none | none |
| s 711(2) | none | none | none | none |
| s 712(1) | none | none | none | none |
| s 712(2) | none | none | none | none |
| s 712(3) | none | none | none | none |
| s 712(4) | none | none | none | none |
| s 712(5) | none | none | none | none |
| s 712(6) | none | none | none | none |
| s 712(7) | none | none | none | none |
| s 713(1) | claim: none named in the text | duty not to act: a private company | claim / duty not to act | `s 713(1) the payment out of capital is not lawful` |
| s 713(2) | none | none | none | none |
| s 714(1) | claim: none named in the text | duty: the directors | claim / duty | `s 714(1) the directors must make a statement` |
| s 714(2) | claim: none named in the text | duty: the directors | claim / duty | `s 714(2) the statement specifies the amount of the permissible capital payment` |
| s 714(3) | claim: none named in the text | duty: the directors | claim / duty | `s 714(3) the statement states what the subsection requires` |
| s 714(4) | claim: none named in the text | duty: the directors | claim / duty | `s 714(4) the directors took into account the liabilities the subsection requires` |
| s 714(5) | claim: none named in the text | duty: the directors | claim / duty | `s 714(5) the statement is in the form and contains the information the subsec...` |
| s 714(6) | claim: none named in the text | duty: the directors | claim / duty | `s 714(6) the statement has annexed to it the report the subsection requires` |
| s 715(1) | power (to prosecute): none named in the text | liability to conviction: the directors in default | liability (offence) | `s 715(1) the person commits an offence` |
| s 715(2) | power (to sentence): the court (sentences) | liability to the penalty: the director guilty of the offence | liability (penalty) | `s 715(2) the penalty on conviction` |
| s 716(1) | claim: none named in the text | duty: a private company | claim / duty | `s 716(1) the payment is approved as the subsection requires` |
| s 716(2) | claim: none named in the text | duty: a private company | claim / duty | `s 716(2) the last day for passing the resolution` |
| s 716(3) | none | none | none | none |
| s 717(1) | none | none | none | none |
| s 717(2) | immunity: none named in the text | disability: a member holding shares to which the resolution relates (not an eligible member) | disability (the thing is void or not effective) | `s 717(2) the member is not an eligible member` |
| s 717(3) | immunity: none named in the text | disability: the resolution (not effective) | disability (the thing is void or not effective) | `s 717(3) the resolution is not effective` |
| s 717(4) | none | none | none | none |
| s 718(1) | none | none | none | none |
| s 718(2) | claim: a member | duty: the company | claim / duty | `s 718(2)(b) the copy was made available to members for a resolution at a meeting` |
| s 718(3) | immunity: none named in the text | disability: the resolution (ineffective) | disability (the thing is void or not effective) | `s 718(3) the resolution is ineffective` |
| s 719(1) | claim: none named in the text | duty: the company | claim / duty | `s 719(1) the last day for publishing the notice in the Gazette` |
| s 719(2) | claim: a creditor (where the notice is given to creditors) | duty: the company | claim / duty | `s 719(2) the company must publish or give the notice` |
| s 719(3) | none | none | none | none |
| s 719(4) | claim: none named in the text | duty: the company (to deliver a copy to the registrar) | claim / duty | `s 719(4) the company must deliver a copy of the statement and report to the r...` |
| s 720(1) | claim: none named in the text | duty: the company | claim / duty | `s 720(1) the first day of the period` |
| s 720(2) | claim: none named in the text | duty: the company | claim / duty | `s 720(2) the statement and report are kept at a place the subsection allows` |
| s 720(3) | claim: none named in the text | duty: the company (to give notice to the registrar) | claim / duty | `s 720(3) the company must give notice to the registrar of the place` |
| s 720(4) | claim: a member and a creditor (to inspect without charge) | duty: the company | claim / duty | `s 720(4) the person may inspect the statement and report without charge` |
| s 720(5) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 720(5) the company is in default as the subsection describes` |
| s 720(6) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 720(6) the penalty on conviction` |
| s 720(7) | power: the court (orders an immediate inspection) | liability: the company | power / liability | `s 720(7) the court may order an immediate inspection` |
| s 720A(1) | privilege: a private company | no-right: none named in the text | privilege / no-right | `s 720A(1) section 713(1) does not apply` |
| s 720A(2) | none | none | none | none |
| s 720A(3) | claim: a member | duty: the company | claim / duty | `s 720A(3) the copy of the solvency statement was sent or submitted in time` |
| s 720A(4) | claim: a member | duty: the company | claim / duty | `s 720A(4) the copy of the solvency statement was made available at the meeting` |
| s 720A(5) | immunity: none named in the text | disability: the resolution (its validity is not affected) | immunity / disability | `s 720A(5) the validity of the resolution is affected by the failure` |
| s 720A(6) | none | none | none | none |
| s 720B(1) | claim: none named in the text | duty: the company (to deliver the documents to the registrar) | claim / duty | `s 720B(1) the company must deliver the documents to the registrar` |
| s 720B(2) | claim: none named in the text | duty: the company | claim / duty | `s 720B(2) the statement of capital states what the subsection requires` |
| s 720B(3) | claim: none named in the text | duty: the registrar | claim / duty | `s 720B(3) the registrar must register the documents` |
| s 720B(4) | immunity: none named in the text | disability: the resolution (does not take effect until the documents are registered) | disability (the thing is void or not effective) | `s 720B(4) the resolution cannot yet take effect` |
| s 720B(5) | claim: none named in the text | duty: the company (to deliver the directors' statement to the registrar) | claim / duty | `s 720B(5) the company must deliver the directors' statement to the registrar` |
| s 720B(6) | immunity: none named in the text | disability: the resolution (its validity is not affected) | immunity / disability | `s 720B(6) the validity of the resolution is affected by the failure` |
| s 720B(7) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 720B(7) the person commits an offence` |
| s 720B(8) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 720B(8) the person commits an offence` |
| s 720B(9) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 720B(9) the penalty on conviction` |
| s 721(1) | power: a member who did not consent, or a creditor (to apply to the court to cancel the resolution) | liability: the company (subject to the court's order) | power / liability | `s 721(1) the member or creditor may apply to the court` |
| s 721(2) | none | none | none | none |
| s 721(3) | power: the court | liability: the parties to the application | power / liability | `s 721(3) the court may adjourn the proceedings and give directions and make o...` |
| s 721(4) | claim: none named in the text | duty: the court | claim / duty | `s 721(4) the court has made the order the subsection requires` |
| s 721(5) | power: the court | liability: the company and the applicants | power / liability | `s 721(5) the court may by order alter or extend the date or period` |
| s 721(6) | power: the court | liability: the company and its members | power / liability | `s 721(6) the court's order may provide for the purchase of a member's shares ...` |
| s 721(7) | power: the court | liability: the company | power / liability | `s 721(7) the court's order may restrict amendments of the articles` |
| s 722(1) | claim: none named in the text | duty: the applicants (to give notice to the registrar) | claim / duty | `s 722(1) the applicants must give notice to the registrar` |
| s 722(2) | claim: none named in the text | duty: the company (to give notice to the registrar) | claim / duty | `s 722(2) the company must give notice to the registrar` |
| s 722(3) | claim: none named in the text | duty: the company (to deliver a copy of the order to the registrar) | claim / duty | `s 722(3) the company must deliver a copy of the order to the registrar` |
| s 722(4) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 722(4) the person commits an offence` |
| s 722(5) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 722(5) the penalty on conviction` |
| s 723(1) | claim: none named in the text | duty not to act: the company (to make the payment out of capital before or after the window) | claim / duty not to act | `s 723(1) the company must make the payment out of capital by the closing day` |
| s 723(1A) | claim: none named in the text | duty: the company (to have the shares surrendered in the window) | claim / duty | `s 723(1A) the shares were surrendered in the window` |
| s 723(2) | none | none | none | none |
| s 724(1) | none | none | none | none |
| s 724(2) | none | none | none | none |
| s 724(3) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 724(3) the company may do it with the shares` |
| s 724(4) | claim: none named in the text | duty: the company | claim / duty | `s 724(4) the company must be entered in its register of members` |
| s 724(5) | none | none | none | none |
| s 725 | none | none | none | none |
| s 726(1) | none | none | none | none |
| s 726(2) | claim: none named in the text | duty not to act: the company (a purported exercise is also void) | claim / duty not to act | `s 726(2) the company may exercise a right in respect of the treasury shares` |
| s 726(3) | claim: none named in the text | duty not to act: the company (to be paid no dividend or distribution) | claim / duty not to act | `s 726(3) a dividend or other distribution may be paid or made to the company ...` |
| s 726(4) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 726(4) section 726 prevents the transaction` |
| s 726(5) | none | none | none | none |
| s 727(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 727(1) the company may dispose of the shares in that way` |
| s 727(2) | none | none | none | none |
| s 727(3) | power: the Secretary of State | liability: none named in the text | power / liability | `s 727(3) the means of payment is regarded as falling within subsection (2)(e)` |
| s 727(4) | claim: a person who gave a section 979 notice | duty not to act: the company | claim / duty not to act | `s 727(4) the company shant sell or transfer the shares except to the person w...` |
| s 727(5) | none | none | none | none |
| s 728(1) | claim: none named in the text | duty: the company (to deliver a return to the registrar) | claim / duty | `s 728(1) the company must deliver a return to the registrar` |
| s 728(2) | claim: none named in the text | duty: the company | claim / duty | `s 728(2) the return states what the section requires` |
| s 728(3) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 728(3) the particulars may be included in a single return` |
| s 728(4) | power (to prosecute): none named in the text | liability to conviction: every officer in default | liability (offence) | `s 728(4) the person commits an offence` |
| s 728(5) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 728(5) the penalty on conviction` |
| s 729(1) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 729(1) the company may cancel the shares` |
| s 729(2) | none | none | none | none |
| s 729(3) | none | none | none | none |
| s 729(4) | none | none | none | none |
| s 729(5) | immunity: the directors (from Chapter 10 of Part 17) | disability: none named in the text | immunity / disability | `s 729(5) the directors may take the steps without complying with Chapter 10 o...` |
| s 730(1) | claim: none named in the text | duty: the company (to deliver a return to the registrar) | claim / duty | `s 730(1) the company must deliver a return to the registrar` |
| s 730(2) | claim: none named in the text | duty: the company | claim / duty | `s 730(2) the return states what the section requires` |
| s 730(3) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 730(3) the particulars may be included in a single return` |
| s 730(4) | claim: none named in the text | duty: the company | claim / duty | `s 730(4) the notice is accompanied by a statement of capital` |
| s 730(5) | claim: none named in the text | duty: the company | claim / duty | `s 730(5) the statement of capital states what the section requires` |
| s 730(6) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 730(6) the person commits an offence` |
| s 730(7) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 730(7) the penalty on conviction` |
| s 731(1) | claim: none named in the text | duty: the company | claim / duty | `s 731(1) this section applies to the proceeds of sale` |
| s 731(2) | claim: none named in the text | duty: the company | claim / duty | `s 731(2) the amount treated as a realised profit of the company for the purpo...` |
| s 731(3) | claim: none named in the text | duty: the company | claim / duty | `s 731(3)(b) the amount to be transferred to the company's share premium account` |
| s 731(4) | none | none | none | none |
| s 732(1) | power (to prosecute): none named in the text | liability to conviction: the company and every officer in default | liability (offence) | `s 732(1) the person commits an offence` |
| s 732(2) | power (to sentence): the court (sentences) | liability to the penalty: the person guilty of the offence | liability (penalty) | `s 732(2) the penalty on conviction` |
| s 733(1) | claim: none named in the text | duty: the company (to transfer amounts to the capital redemption reserve) | claim / duty | `s 733(1) the company must transfer the amount to the capital redemption reserve` |
| s 733(2) | claim: none named in the text | duty: the company | claim / duty | `s 733(2) the amount to be transferred to the capital redemption reserve` |
| s 733(3) | claim: none named in the text | duty: the company | claim / duty | `s 733(3) the amount of the difference to be transferred to the capital redemp...` |
| s 733(4) | claim: none named in the text | duty: the company | claim / duty | `s 733(4) the amount to be transferred to the capital redemption reserve` |
| s 733(5) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 733(5) the company may use the capital redemption reserve to pay up the new...` |
| s 733(6) | none | none | none | none |
| s 734(1) | none | none | none | none |
| s 734(1A) | none | none | none | none |
| s 734(2) | claim: none named in the text | duty: the company | claim / duty | `s 734(2) the amount to be transferred to the capital redemption reserve` |
| s 734(3) | privilege: the company | no-right: none named in the text | privilege / no-right | `s 734(3) the amount may be reduced` |
| s 734(4) | none | none | none | none |
| s 735(1) | none | none | none | none |
| s 735(2) | immunity: the company (from damages for the failure) | disability: the holder of the shares (no right to sue for damages) | immunity / disability | `s 735(2) the company is liable in damages for the failure` |
| s 735(3) | immunity: the company (from specific performance) | disability: the court (shall not grant the order) | immunity / disability | `s 735(3) the court shall not grant specific performance` |
| s 735(4) | claim: the holder of the shares (to enforce the terms in the winding up) | duty: the company | claim / duty | `s 735(4) the terms of redemption or purchase may be enforced against the company` |
| s 735(5) | immunity: the company | disability: the holder of the shares | immunity / disability | `s 735(5) subsection (4) does not apply` |
| s 735(6) | claim: creditors and holders of preferred rights | duty: the company in liquidation | claim / duty | `s 735(6) the claim is paid in priority to any amount the company is liable un...` |
| s 736 | none | none | none | none |
| s 737(1) | power: the Secretary of State | liability: the persons the regulations bind | power / liability | (none) |
| s 737(2) | none | none | none | none |
| s 737(3) | none | none | none | none |
| s 737(4) | none | none | none | none |

## Marginal readings for a lawyer (coa15)

These are not settled here; they are the status quo this corpus takes, put to a lawyer. Two readings carry them.

- **(a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if"; a flat negative counts as the text's no.** An inference: "if A then B" does not itself say "if not A then not B". Every branch below that answers `JUST FALSE` rests on it (or, for a "means" definition or a period the text fixes in its own words, on the rulings of 2026-11-04 and 2026-11-05). **The other reading:** the branch answers `NOTHING`.
- **(b) A prohibition or grant limited by its own wording does not say no outside the limit.** Every branch below that answers `NOTHING` with `limited by its own wording` rests on it. **The other reading:** the branch answers `JUST FALSE`.

The tables list every branch of the layer-1 modules that rests on either reading (261 branches of reading (a); 179 of reading (b)); the quoted words are the ones the comment in the `.l4` file quotes.

### Reading (a): branches that answer `JUST FALSE` (the other reading: `NOTHING`)

| module | rule | the words that say no |
| --- | --- | --- |
| chh | `s 658(1) a limited company must not make the acquisition` | except in accordance with the provisions of this Part |
| chh | `s 658(2)(a) the person commits an offence` | If a company purports to act in contravention of this section |
| chh | `s 658(2)(b) the purported acquisition is void` | If a company purports to act in contravention of this section |
| chh | `s 660(1) this section applies to the shares` | This section applies where shares in a limited company— |
| chh | `s 660(1) this section applies to the shares` | This section applies where shares in a limited company— (a) ... (b) ... (c) ... |
| chh | `s 660(3)(a) section 660 does not apply to the shares` | where, (i) a person acquires shares in the company with financial assistance given to him, direct... |
| chh | `s 660(3)(b) section 660 does not apply to the shares` | when the company has no beneficial interest in the shares |
| chh | `s 660(2)(a) the shares are treated as held by the nominee on his ow...` | This section does not apply— |
| chh | `s 660(2)(a) the shares are treated as held by the nominee on his ow...` | This section does not apply— |
| chh | `s 661(1) this section applies to the shares` | This section does not apply to shares acquired by a nominee of the company when the company has n... |
| chh | `s 661(1) this section applies to the shares` | This section applies where shares in a limited company— |
| chh | `s 661(1) this section applies to the shares` | This section applies where shares in a limited company— (a) ... (b) ... (c) ... |
| chh | `s 661(5) section 661 does not apply to the shares` | when the company has no beneficial interest in the shares |
| chh | `s 661(2) the person is jointly and severally liable with the nomine...` | This section applies where shares in a limited company— |
| chh | `s 661(2) the person is jointly and severally liable with the nomine...` | fails to pay that amount within 21 days from being called on to do so, then |
| chh | `s 661(2) the person is jointly and severally liable with the nomine...` | fails to pay that amount within 21 days from being called on to do so, then |
| chh | `s 662(1) this section applies to the shares` | This section applies in the case of a public company— (a) where ... (b) where ... (c) where ... (... |
| chh | `s 662(1) this section applies to the shares` | and the company has a beneficial interest in the shares |
| chh | `s 662(2)(a) the company must cancel the shares` | Unless the shares or any interest of the company in them are previously disposed of |
| chh | `s 662(2)(a) the company must cancel the shares` | This section applies in the case of a public company |
| chh | `s 662(2)(b) the company must apply for re-registration as a private...` | where the effect is that the nominal value of the company's allotted share capital is brought bel... |
| chh | `s 662(2)(b) the company must apply for re-registration as a private...` | Unless the shares or any interest of the company in them are previously disposed of, the company ... |
| chh | `s 662(3) the company cancelled the shares in time` | It must do so no later than— ... three years from the date ... one year from the date |
| chh | `s 662(5) the person may exercise voting rights in respect of the sh...` | Neither the company ... may exercise any voting rights in respect of the shares |
| chh | `s 662(5) the person may exercise voting rights in respect of the sh...` | in a case within subsection (1)(d) or (e), the nominee or other shareholder may [not] exercise an... |
| chh | `s 662(5) the person may exercise voting rights in respect of the sh...` | in a case within subsection (1)(d) or (e), the nominee or other shareholder may [not] exercise an... |
| chh | `s 663(1) the notice was given within one month after the shares wer...` | it must within one month after the shares are cancelled give notice to the registrar |
| chh | `s 663(2) the notice is accompanied by a statement of capital` | The notice must be accompanied by a statement of capital. |
| chh | `s 663(3) the statement of capital states what the section requires` | The statement of capital must state ... (a) the total number of shares of the company, (b) the ag... |
| chh | `s 663(3) the statement of capital states what the section requires` | (c) for each class of shares— (i) prescribed particulars of the rights attached to the shares, (i... |
| chh | `s 663(4) the person commits an offence` | If default is made in complying with this section |
| chh | `s 664(1) the directors may resolve that the company should be re-re...` | Where a company is obliged to re-register as a private company to comply with section 662, the di... |
| chh | `s 664(3) the application contains what the section requires` | The application for re-registration must contain a statement of the company's proposed name on re... |
| chh | `s 664(4) the application is accompanied as the section requires` | The application must be accompanied by— (a) a copy of the resolution (unless a copy has already b... |
| chh | `s 664(5) the statement is the statement of compliance required` | The statement of compliance required is a statement that the requirements of this section as to r... |
| chh | `s 665(1) the company shall be re-registered as a private company` | If on an application under section 664 the registrar is satisfied that the company is entitled to... |
| chh | `s 665(3) the certificate states what the section requires` | The certificate must state that it is issued on re-registration and the date on which it is issued. |
| chh | `s 665(4)(a) the company becomes a private company by virtue of the ...` | On the issue of the certificate— (a) the company by virtue of the issue of the certificate become... |
| chh | `s 665(4)(b) the changes in the company's name and articles take effect` | On the issue of the certificate— ... (b) the changes in the company's name and articles take effect. |
| chh | `s 666(1) Chapter 1 of Part 20 applies to the company as if it were ...` | If a public company that is required by section 662 to apply to be re-registered as a private com... |
| chh | `s 666(1) Chapter 1 of Part 20 applies to the company as if it were ...` | If a public company that is required by section 662 to apply to be re-registered as a private com... |
| chh | `s 666(2) the company continues to be treated as a public company` | until it is so re-registered |
| chh | `s 667(2) the person commits an offence` | This section applies where a company, when required to do by section 662— |
| chh | `s 668(1) this section applies to the shares` | This section applies where, after shares in a private company— ... the company is re-registered a... |
| chh | `s 668(1) this section applies to the shares` | This section applies where, after shares in a private company— (a) ... (b) ... (c) ... (d) ... |
| chh | `s 668(1) this section applies to the shares` | the company having a beneficial interest in the shares |
| chh | `s 669(1) an amount must be transferred out of profits available for...` | Where— (a) a public company, or a nominee of a public company, acquires shares in the company, an... |
| chh | `s 669(1) the amount to be transferred to the reserve fund` | Where— (a) ... and (b) ... |
| chh | `s 669(1) the amount transferred is available for distribution` | and is not then available for distribution |
| chh | `s 670(2) the charge is permitted` | a charge is permitted if the shares are not fully paid up and the charge is for an amount payable... |
| chh | `s 670(3) the charge is permitted` | a charge is permitted (whether the shares are fully paid or not) if it arises in connection with ... |
| chh | `s 670(4) the charge is permitted` | a charge is permitted if it was in existence immediately before the application for re-registration |
| chh | `s 670(1) the lien or charge is void` | is void, except as permitted by this section |
| chh | `s 672(2) the right is a residual interest` | A “residual interest” means a right of the company to receive any of the trust property in the ev... |
| chh | `s 672(2) the right is a residual interest` | A “residual interest” means a right of the company to receive any of the trust property |
| chh | `s 672(4) the residual interest vests in possession` | in a case within subsection (2)(a), on the occurrence of the event mentioned there (whether or no... |
| chh | `s 672(4) the residual interest vests in possession` | in a case within subsection (2)(b) or (c), when the company becomes entitled to require the trust... |
| chh | `s 672(4) the residual interest vests in possession` | in a case within subsection (2)(b) or (c), when the company becomes entitled to require the trust... |
| chh | `s 675(1) the scheme is a pension scheme` | In this Chapter “pension scheme” means a scheme for the provision of benefits consisting of or in... |
| chh | `s 675(2) the benefit is a relevant benefit` | “relevant benefits” means any pension, lump sum, gratuity or other like benefit |
| chh | `s 675(2) the benefit is a relevant benefit` | given or to be given on retirement or on death or in anticipation of retirement or, in connection... |
| chh | `s 677(1) the assistance given by the company is financial assistance` | “financial assistance” means— ... (b) financial assistance given— (i) by way of guarantee, securi... |
| chh | `s 677(1) the assistance given by the company is financial assistance` | (d) any other financial assistance given by a company where (i) the net assets of the company are... |
| chh | `s 678(1) it is not lawful for the company to give the financial ass...` | Where a person is acquiring or proposing to acquire shares in a public company |
| chh | `s 678(1) it is not lawful for the company to give the financial ass...` | financial assistance directly or indirectly for the purpose of the acquisition before or at the s... |
| chh | `s 678(2) subsection (1) does not prohibit the assistance` | does not prohibit a company from giving financial assistance ... if (a) ... or (b) ..., and the a... |
| chh | `s 678(3) it is not lawful for the company to give the financial ass...` | Where— (a) a person has acquired shares in a company, and (b) a liability has been incurred (by t... |
| chh | `s 678(3) it is not lawful for the company to give the financial ass...` | for the purpose of reducing or discharging the liability if, at the time the assistance is given,... |
| chh | `s 678(4) subsection (3) does not prohibit the assistance` | does not prohibit a company from giving financial assistance if (a) ... or (b) ..., and the assis... |
| chh | `s 678(5) the assistance is prohibited by section 678 as it has effe...` | Subsection (1) does not prohibit |
| chh | `s 679(1) it is not lawful for the public company to give the financ...` | Where a person is acquiring or proposing to acquire shares in a private company |
| chh | `s 679(1) it is not lawful for the public company to give the financ...` | financial assistance directly or indirectly for the purpose of the acquisition before or at the s... |
| chh | `s 679(2) subsection (1) does not prohibit the assistance` | does not prohibit a company from giving financial assistance for the acquisition of shares in its... |
| chh | `s 679(3) it is not lawful for the public company to give the financ...` | Where— (a) a person has acquired shares in a private company, and (b) a liability has been incurr... |
| chh | `s 679(3) it is not lawful for the public company to give the financ...` | financial assistance directly or indirectly for the purpose of reducing or discharging the liability |
| chh | `s 679(4) subsection (3) does not prohibit the assistance` | does not prohibit a company from giving financial assistance if (a) ... or (b) ..., and the assis... |
| chh | `s 679(5) the assistance is prohibited by section 679 as it has effe...` | Subsection (1) does not prohibit |
| chh | `s 680(1) the person commits an offence` | If a company contravenes section 678(1) or (3) or section 679(1) or (3) (prohibited financial ass... |
| chh | `s 681(1) neither section 678 nor section 679 prohibits the transaction` | Those transactions are— (a) ... (g) |
| chh | `s 682(2)(a) the transaction is a lending of money in the ordinary c...` | where the lending of money is part of the ordinary business of the company, the lending of money ... |
| chh | `s 682(2)(b) the transaction is the provision of assistance for the ...` | the provision by the company, in good faith in the interests of the company or its holding compan... |
| chh | `s 682(2)(b) the transaction is the provision of assistance for the ...` | for the purposes of an employees' share scheme |
| chh | `s 682(2)(c) the transaction is assistance in connection with transa...` | (c) the provision of financial assistance by the company for the purposes of or in connection wit... |
| chh | `s 682(2)(d) the transaction is a loan to a person other than a dire...` | (d) the making by the company of loans to persons (other than directors) employed in good faith b... |
| chh | `s 682(2) the transaction is one to which section 682 applies` | The transactions to which this section applies are— (a) ... (b) ... (c) ... (d) ... |
| chh | `s 682(1) neither section 678 nor section 679 prohibits the transaction` | prohibits a transaction to which this section applies |
| chh | `s 682(1) neither section 678 nor section 679 prohibits the transaction` | (a) if the company giving the assistance is a private company, or (b) if the company giving the a... |
| chh | `s 682(5) the company is in the same group as the other company` | a company is in the same group as another company if it is a holding company or subsidiary of tha... |
| chh | `s 683(1) the payment is a distribution for the purposes of Chapter 2` | “distribution” has the same meaning as in Part 23 (distributions) (see section 829) |
| chh | `s 684(1) the shares are redeemable shares` | shares that are to be redeemed or are liable to be redeemed at the option of the company or the s... |
| chh | `s 684(3) the public limited company may issue redeemable shares` | may only issue redeemable shares if it is authorised to do so by its articles |
| chh | `s 684(4) the issue of redeemable shares is barred` | No redeemable shares may be issued at a time when there are no issued shares of the company that ... |
| chh | `s 685(3)(a) the directors determined the terms before the shares we...` | Where the directors are authorised under subsection (1) to determine the terms, conditions and ma... |
| chh | `s 685(3)(a) the directors determined the terms before the shares we...` | they must do so before the shares are allotted |
| chh | `s 685(3)(b) the obligation to state the rights extends to the terms...` | Where the directors are authorised under subsection (1) ... any obligation of the company to stat... |
| chh | `s 685(4) the terms, conditions and manner of redemption must be sta...` | Where the directors are not so authorised |
| chh | `s 686(1) the redemption is barred` | may not be redeemed unless they are fully paid |
| chh | `s 686(3) the shares must be paid for on redemption` | Unless redeemed in accordance with a provision authorised by subsection (2) |
| chh | `s 687(1) the private limited company may redeem the shares out of c...` | in accordance with Chapter 5 |
| chh | `s 687(2) the redemption is out of a source the section permits` | redeemable shares in a limited company may only be redeemed out of— (a) distributable profits of ... |
| chh | `s 687(4) the most of the premium that may be paid out of the procee...` | If the redeemable shares were issued at a premium |
| chh | `s 688(a) the shares are treated as cancelled` | Where shares in a limited company are redeemed |
| chh | `s 688(b) the amount of the company's issued share capital after the...` | Where shares in a limited company are redeemed |
| chh | `s 689(1) the notice was given within one month after the redemption` | it must within one month after doing so give notice to the registrar |
| chh | `s 689(2) the notice is accompanied by a statement of capital` | The notice must be accompanied by a statement of capital. |
| chh | `s 689(4) the person commits an offence` | If default is made in complying with this section |
| chh | `s 690(2) the purchase is barred` | may not purchase its own shares if as a result of the purchase there would no longer be any issue... |
| chh | `s 691(1) the purchase is barred` | may not purchase its own shares unless they are fully paid |
| chh | `s 691(3) subsection (2) does not apply` | in a case where a private limited company is purchasing shares for the purposes of or pursuant to... |
| chh | `s 691(3) subsection (2) does not apply` | in a case where a private limited company is purchasing shares for the purposes of or pursuant to... |
| chh | `s 691(2) the shares must be paid for on purchase` | But subsection (2) does not apply in a case where a private limited company is purchasing shares ... |
| chh | `s 692(1) the private limited company may purchase its own shares ou...` | in accordance with Chapter 5 |
| chh | `s 692(1B) the rate is the rate the subsection requires` | The rate must be a rate prevailing on a day specified in the resolution authorising the purchase ... |
| chh | `s 692(1ZA) the most the company may pay out of capital in the finan...` | If authorised to do so by its articles |
| chh | `s 692(2)(a) the purchase is out of a source the section permits` | a limited company may only purchase its own shares out of— (i) distributable profits of the compa... |
| chh | `s 692(3) the most of the premium that may be paid out of the procee...` | If the shares to be purchased were issued at a premium |
| chh | `s 693(1) the limited company may make the purchase` | A limited company may only purchase its own shares— (a) by an off-market purchase, authorised in ... |
| chh | `s 693(1) the limited company may make the purchase` | A limited company may only purchase its own shares— ... (b) by a market purchase, authorised in a... |
| chh | `s 693(3) the shares are subject to a marketing arrangement on the e...` | a company's shares are subject to a marketing arrangement on a recognised investment exchange if—... |
| chh | `s 693(2) the purchase is an off-market purchase` | A purchase is “off-market” if the shares either— (a) are purchased otherwise than on a recognised... |
| chh | `s 693(4) the purchase is a market purchase` | A purchase is a “market purchase” if it is made on a recognised investment exchange |
| chh | `s 693(4) the purchase is a market purchase` | and is not an off-market purchase by virtue of subsection (2)(b) |
| chh | `s 693(5) the exchange is a recognised investment exchange` | other than an overseas exchange (within the meaning of that Part) |
| chh | `s 693(5) the exchange is a recognised investment exchange` | “recognised investment exchange” means a recognised investment exchange (within the meaning of Pa... |
| chh | `s 693(5) the exchange is a recognised investment exchange` | other than an overseas exchange (within the meaning of that Part) |
| chh | `s 693A(3) the authority contains what the subsection requires` | The authority must— (a) specify the maximum number of shares authorised to be acquired, and (b) d... |
| chh | `s 693A(5) the resolution specifies a date of expiry that is not lat...` | must specify a date on which it is to expire |
| chh | `s 693A(5) the resolution specifies a date of expiry that is not lat...` | which must not be later than five years after the date on which the resolution is passed |
| chh | `s 694(1) the company may make the off-market purchase` | A company may only make an off-market purchase of its own shares in pursuance of a contract appro... |
| chh | `s 694(2) the contract is approved in the way the subsection requires` | Either— (a) the terms of the contract must be authorised by a . . . resolution of the company bef... |
| chh | `s 694(6) the resolution is barred by section 695 or section 696` | is subject to— section 695 (exercise of voting rights), and section 696 (disclosure of details of... |
| chh | `s 695(2) the member is not an eligible member` | Where the resolution is proposed as a written resolution, a member who holds shares to which the ... |
| chh | `s 695(3) the resolution is not effective` | Where the resolution is proposed at a meeting of the company, it is not effective if— (a) any mem... |
| chh | `s 696(2)(a) the copy or memorandum was made available to members fo...` | A copy of the contract (if it is in writing) or a memorandum setting out its terms (if it is not)... |
| chh | `s 696(2)(b) the copy or memorandum was made available to members fo...` | (b) in the case of a resolution at a meeting, by being made available for inspection by members o... |
| chh | `s 696(3) the memorandum includes what the subsection requires` | must include the names of the members holding shares to which the contract relates |
| chh | `s 696(4) the copy has annexed to it what the subsection requires` | must have annexed to it a written memorandum specifying such of those names as do not appear in t... |
| chh | `s 696(5) the resolution is not validly passed` | if the requirements of this section are not complied with |
| chh | `s 697(1) the company may agree to the variation` | may only agree to a variation of a contract authorised under section 694 (authority for off-marke... |
| chh | `s 697(2) the variation is authorised in the way the subsection requ...` | The terms of the variation must be authorised by a . . . resolution of the company before it is a... |
| chh | `s 697(5) the resolution is barred by section 698 or section 699` | is subject to— section 698 (exercise of voting rights), and section 699 (disclosure of details of... |
| chh | `s 699(3) the original contract is also made available` | There must also be made available as mentioned in subsection (2) a copy of the original contract ... |
| chh | `s 700(1) the release agreement is void` | is void unless the terms of the release agreement are approved in advance in accordance with this... |
| chh | `s 700(2) the release agreement is authorised in the way the subsect...` | The terms of the proposed agreement must be authorised by a . . . resolution of the company befor... |
| chh | `s 701(1) the company may make the market purchase` | A company may only make a market purchase of its own shares if the purchase has first been author... |
| chh | `s 702(1) this section applies` | This section applies where a company has entered into— (a) a contract approved under section 694 ... |
| chh | `s 702(2) the company has kept the copy or memorandum available for ...` | This section applies where a company has entered into— |
| chh | `s 702(2) the company has kept the copy or memorandum available for ...` | The company must keep available for inspection— (a) a copy of the contract, or (b) if the contrac... |
| chh | `s 702(3) the copy or memorandum was kept available for the period` | The copy or memorandum must be kept available for inspection from the conclusion of the contract ... |
| chh | `s 702(4) the copy or memorandum is kept at a place the subsection a...` | The copy or memorandum must be kept available for inspection— (a) at the company's registered off... |
| chh | `s 702(5) the company must give notice to the registrar of the place` | unless it has at all times been kept at the company's registered office |
| chh | `s 703(1) the company is in default as the subsection describes` | If default is made in complying with section 702(2), (3) or (4) or default is made for 14 days in... |
| chh | `s 703(1) the person commits an offence` | If default is made in complying with section 702(2), (3) or (4) or default is made for 14 days in... |
| chh | `s 703(3) the court may order an immediate inspection` | In the case of refusal of an inspection required under section 702(6) the court may by order comp... |
| chh | `s 704 the company's right under the contract is capable of being as...` | are not capable of being assigned |
| chh | `s 706(a) the shares may be held and dealt with in accordance with C...` | Where a limited company makes a purchase of its own shares in accordance with this Chapter, then |
| chh | `s 706(b)(i) the shares are treated as cancelled` | Where a limited company makes a purchase of its own shares in accordance with this Chapter, then |
| chh | `s 706(b)(i) the shares are treated as cancelled` | (b) if that section does not apply |
| chh | `s 706(b)(ii) the amount of the company's issued share capital after...` | (b) if that section does not apply— (ii) the amount of the company's issued share capital is dimi... |
| chh | `s 707(1) the return was delivered within the period of 28 days begi...` | it must deliver a return to the registrar within the period of 28 days beginning with the date on... |
| chh | `s 707(2) the return distinguishes what the subsection requires` | The return must distinguish— (a) shares in relation to which section 724 (treasury shares) applie... |
| chh | `s 707(3) the return states what the subsection requires` | The return must state, with respect to shares of each class purchased— (a) the number and nominal... |
| chh | `s 707(4) the return also states what the subsection requires` | In the case of a public company the return must also state— (a) the aggregate amount paid by the ... |
| chh | `s 707(6) the person commits an offence` | If default is made in complying with this section |
| chh | `s 708(1) the company must give notice of cancellation to the registrar` | (b) that section applies but the shares are cancelled forthwith (under section 729 (cancellation ... |
| chh | `s 708(1) the notice of cancellation was given within the period of ...` | the company must give notice of cancellation to the registrar, within the period of 28 days begin... |
| chh | `s 708(2) a statement of capital must accompany the notice` | except where the statement of capital would be the same as a statement of capital that is require... |
| chh | `s 708(2) the notice is accompanied as the subsection requires` | The notice must be accompanied by a statement of capital |
| chh | `s 708(4) the person commits an offence` | If default is made in complying with this section |
| chh | `s 709(1) the private limited company may make the payment out of ca...` | may in accordance with this Chapter |
| chh | `s 712(4) the payment is an other relevant payment lawfully made` | a distribution is the other limb of subsection (3), "(a) any distribution lawfully made by the co... |
| chh | `s 712(4) the payment is an other relevant payment lawfully made` | financial assistance lawfully given out of distributable profits |
| chh | `s 712(6) the accounts are the relevant accounts` | “the relevant accounts” are any accounts that— (a) are prepared as at a date within the relevant ... |
| chh | `s 713(1) the payment out of capital is not lawful` | is not lawful unless the requirements of the following sections are met |
| chh | `s 714(2) the statement specifies the amount of the permissible capi...` | The statement must specify the amount of the permissible capital payment for the shares in question. |
| chh | `s 714(3) the statement states what the subsection requires` | It must state that, having made full inquiry into the affairs and prospects of the company, the d... |
| chh | `s 714(4) the directors took into account the liabilities the subsec...` | the directors must take into account all of the company's liabilities (including any contingent o... |
| chh | `s 714(5) the statement is in the form and contains the information ...` | The directors' statement must be in the prescribed form and must contain such information with re... |
| chh | `s 714(6) the statement has annexed to it the report the subsection ...` | It must in addition have annexed to it a report addressed to the directors by the company's audit... |
| chh | `s 714 the statement and report contain everything section 714 requires` | The statement must ... |
| chh | `s 715(1) the person commits an offence` | If the directors make a statement under section 714 without having reasonable grounds for the opi... |
| chh | `s 716(1) the payment is approved as the subsection requires` | The payment out of capital must be approved by a special resolution of the company. |
| chh | `s 716(1) the payment is approved as the subsection requires` | must be approved by a special resolution of the company |
| chh | `s 716(2) the resolution was passed in time` | The resolution must be passed on, or within the week immediately following, the date on which the... |
| chh | `s 716(3) the resolution is barred by section 717 or section 718` | A resolution under this section is subject to section 717 (exercise of voting rights), and sectio... |
| chh | `s 718(2)(b) the copy was made available to members for a resolution...` | A copy of the directors' statement and auditor's report under section 714 must be made available ... |
| chh | `s 718(3) the resolution is ineffective` | if this requirement is not complied with |
| chh | `s 719(1) the notice was published in the Gazette in time` | Within the week immediately following the date of the resolution under section 716 the company mu... |
| chh | `s 719(1) the notice states what the subsection requires` | a notice— (a) stating that the company has approved a payment out of capital ..., (b) specifying—... |
| chh | `s 719(2) the company published or gave the notice in time` | Within the week immediately following the date of the resolution the company must also either— (a... |
| chh | `s 719(3) the newspaper is an appropriate national newspaper` | “An appropriate national newspaper” means a newspaper circulating throughout the part of the Unit... |
| chh | `s 719(4) the copy was delivered to the registrar in time` | Not later than the day on which the company— (a) first publishes the notice required by subsectio... |
| chh | `s 720(1) the statement and report were kept available throughout th...` | must be kept available for inspection throughout the period— (a) beginning with the day on which ... |
| chh | `s 720(2) the statement and report are kept at a place the subsectio...` | They must be kept available for inspection— (a) at the company's registered office, or (b) at a p... |
| chh | `s 720(3) the company must give notice to the registrar of the place` | unless they have at all times been kept at the company's registered office |
| chh | `s 720(5) the company is in default as the subsection describes` | If default is made for 14 days in complying with subsection (3), or an inspection under subsectio... |
| chh | `s 720(5) the person commits an offence` | If default is made for 14 days in complying with subsection (3), or an inspection under subsectio... |
| chh | `s 720(7) the court may order an immediate inspection` | In the case of a refusal of an inspection required by subsection (4), the court may by order comp... |
| chh | `s 720A(1) section 713(1) does not apply` | Section 713(1) does not apply to the purchase out of capital ... for the purposes of or pursuant ... |
| chh | `s 720A(2) the resolution is supported by a solvency statement` | a resolution is supported by a solvency statement if— (a) the directors of the company make a sol... |
| chh | `s 720A(2) the resolution is supported by a solvency statement` | (a) ... not more than 15 days before the date on which the resolution is passed, and (b) the reso... |
| chh | `s 720A(4) the copy of the solvency statement was made available at ...` | Where the resolution is proposed at a general meeting, a copy of the solvency statement must be m... |
| chh | `s 720A(5) the validity of the resolution is affected by the failure` | The validity of a resolution is not affected by a failure to comply with subsection (3) or (4). |
| chh | `s 720B(1) the documents were delivered within 15 days after the res...` | Within 15 days after the passing of the resolution ... the company must deliver to the registrar |
| chh | `s 720B(4) the resolution cannot yet take effect` | The resolution does not take effect until those documents are registered |
| chh | `s 720B(5) the directors' statement was delivered within 15 days aft...` | The company must also deliver to the registrar, within 15 days after the resolution is passed, a ... |
| chh | `s 720B(5) the statement confirms what the subsection requires` | a statement by the directors confirming that the solvency statement was— (a) made not more than 1... |
| chh | `s 720B(6) the validity of the resolution is affected by the failure` | The validity of a resolution is not affected by— (a) a failure to deliver the documents ... withi... |
| chh | `s 720B(7) the person commits an offence` | If the company delivers to the registrar a solvency statement that was not provided to members in... |
| chh | `s 720B(8) the person commits an offence` | If default is made in complying with this section |
| chh | `s 721(1) the person may apply to the court for the cancellation of ...` | Where a private company passes a special resolution approving a payment out of capital for the re... |
| chh | `s 721(1) the person may apply to the court for the cancellation of ...` | Where a private company passes a special resolution approving a payment out of capital |
| chh | `s 721(1) the person may apply to the court for the cancellation of ...` | (other than one who consented to or voted in favour of the resolution) |
| chh | `s 721(2)(a) the application was made within five weeks after the pa...` | The application— (a) must be made within five weeks after the passing of the resolution |
| chh | `s 721(3) the court may adjourn the proceedings and give directions ...` | On an application under this section the court may if it thinks fit— |
| chh | `s 721(4) the court has made the order the subsection requires` | Subject to that, the court must make an order either cancelling or confirming the resolution |
| chh | `s 722(3) the copy of the order was delivered in time` | Within 15 days of the making of the court's order, or such longer period as the court may at any ... |
| chh | `s 722(4) the person commits an offence` | If a company fails to comply with subsection (2) or (3) |
| chh | `s 723(1) the payment out of capital was made in the window` | must be made— (a) no earlier than five weeks after the date on which the resolution under section... |
| chh | `s 723(1A) the shares were surrendered in the window` | must be surrendered— (a) no earlier than five weeks after the date on which the resolution under ... |
| chh | `s 723(2) the dates and periods of subsection (1) are displaced by t...` | This is subject to any exercise of the court's powers under section 721(5) |
| chh | `s 724(1) this section applies` | This section applies where– (a) a limited company makes a purchase of its own shares in accordanc... |
| chh | `s 724(3) the company may do it with the shares` | Where this section applies the company may |
| chh | `s 724(4) the company must be entered in its register of members as ...` | Where shares are held by the company |
| chh | `s 724(5) the company holds the shares as treasury shares` | references to a company holding shares as treasury shares are to the company holding shares that—... |
| chh | `s 726(1) this section applies` | This section applies where shares are held by a company as treasury shares |
| chh | `s 726(2) the company may exercise a right in respect of the treasur...` | The company must not exercise any right in respect of the treasury shares |
| chh | `s 726(3) a dividend or other distribution may be paid or made to th...` | No dividend may be paid, and no other distribution (whether in cash or otherwise) of the company'... |
| chh | `s 726(4) section 726 prevents the transaction` | Nothing in this section prevents— (a) an allotment of shares as fully paid bonus shares in respec... |
| chh | `s 726(4) section 726 prevents the transaction` | Nothing in this section prevents— ... (b) the payment of any amount payable on the redemption of ... |
| chh | `s 727(1) the company may dispose of the shares in that way` | Where shares are held as treasury shares, the company may at any time |
| chh | `s 727(2) the consideration is a cash consideration` | “cash consideration” means— ... (b) a cheque received by the company in good faith that the direc... |
| chh | `s 727(2) the consideration is a cash consideration` | an undertaking to pay cash to the company on or before a date not more than 90 days after the dat... |
| chh | `s 727(2) the consideration is a cash consideration` | “cash consideration” means— (a) ... (e) ... |
| chh | `s 727(4) the sale or transfer is barred` | If the company receives a notice under section 979 ... the company must not sell or transfer the ... |
| chh | `s 728(1) the return was delivered not later than 28 days after the ...` | the company must deliver a return to the registrar not later than 28 days after the shares are di... |
| chh | `s 728(2) the return states what the section requires` | The return must state with respect to shares of each class disposed of— (a) the number and nomina... |
| chh | `s 728(4) the person commits an offence` | If default is made in complying with this section |
| chh | `s 729(1) the company may cancel the shares` | Where shares are held as treasury shares, the company may at any time cancel the shares |
| chh | `s 729(4) the amount of the company's share capital after the cancel...` | If company cancels shares held as treasury shares |
| chh | `s 730(1) the return was delivered not later than 28 days after the ...` | the company must deliver a return to the registrar not later than 28 days after the shares are ca... |
| chh | `s 730(2) the return states what the section requires` | The return must state with respect to shares of each class cancelled— (a) the number and nominal ... |
| chh | `s 730(4) the notice is accompanied by a statement of capital` | The notice must be accompanied by a statement of capital. |
| chh | `s 730(6) the person commits an offence` | If default is made in complying with this section |
| chh | `s 731(1) this section applies to the proceeds of sale` | Where shares held as treasury shares are sold, the proceeds of sale must be dealt with in accorda... |
| chh | `s 732(1) the person commits an offence` | If a company contravenes any of the provisions of this Chapter (except section 730 (notice of can... |
| chh | `s 733(2) the amount to be transferred to the capital redemption res...` | Where under this Part shares of a limited company are redeemed or purchased wholly out of the com... |
| chh | `s 733(3) the amount of the difference to be transferred to the capi...` | If— (a) ..., and (b) ..., the amount of the difference must be transferred |
| chh | `s 733(4) the amount to be transferred to the capital redemption res...` | The amount by which a company's share capital is diminished in accordance with section 729(4) (on... |
| chh | `s 734(1) this section applies` | This section applies where a payment out of capital is made in accordance with Chapter 5 (...) or... |
| chh | `s 734(4) the amount to read as the permissible capital payment in s...` | Where the proceeds of a fresh issue are applied by the company in making a redemption or purchase... |
| chh | `s 734(2) the amount to be transferred to the capital redemption res...` | If the permissible capital payment is less than the nominal amount of the shares redeemed or purc... |
| chh | `s 734(3) the most by which the amounts may be reduced` | If the permissible capital payment is greater than the nominal amount of the shares redeemed or p... |
| chh | `s 735(1) this section applies` | This section applies where a company— (a) issues shares on terms that they are or are liable to b... |
| chh | `s 735(2) the company is liable in damages for the failure` | The company is not liable in damages in respect of any failure on its part to redeem or purchase ... |
| chh | `s 735(2) the holder's right survives the failure` | other than his right to sue the company for damages in respect of its failure |
| chh | `s 735(3) the court shall not grant specific performance` | if the company shows that it is unable to meet the costs of redeeming or purchasing the shares in... |
| chh | `s 735(4) the terms of redemption or purchase may be enforced agains...` | Subsection (4) does not apply if |
| chh | `s 735(5) subsection (4) does not apply` | Subsection (4) does not apply if— (a) the terms provided for the redemption or purchase to take p... |
| chh | `s 735(6) the claim is paid in priority to any amount the company is...` | Subject to that, any such amount shall be paid in priority to any amounts due to members in satis... |
| chh | `s 736 the profits are distributable profits in relation to the payment` | “distributable profits”, in relation to the making of any payment by a company, means profits out... |

### Reading (b): branches that answer `NOTHING` because the text limits itself (the other reading: `JUST FALSE`)

| module | rule | the limit |
| --- | --- | --- |
| chh | `s 658(1) a limited company must not make the acquisition` | A limited company must not acquire its own shares |
| chh | `s 658(2)(a) the person commits an offence` | every officer of the company who is in default |
| chh | `s 658(2)(a) the person commits an offence` | every officer of the company who is in default |
| chh | `s 658(2)(a) the person commits an offence` | the offence is committed by the company and every officer in default |
| chh | `s 659(1) a limited company may acquire its own shares` | any of its own fully paid shares otherwise than for valuable consideration |
| chh | `s 660(3)(a) section 660 does not apply to the shares` | does not apply— (a) to shares acquired otherwise than by subscription by a nominee of a public co... |
| chh | `s 660(3)(b) section 660 does not apply to the shares` | to shares acquired by a nominee of the company |
| chh | `s 661(5) section 661 does not apply to the shares` | This section does not apply to shares acquired by a nominee of the company |
| chh | `s 661(2) the person is jointly and severally liable with the nomine...` | (a) in the case of shares that he agreed to take as subscriber to the memorandum, the other subsc... |
| chh | `s 661(2) the person is jointly and severally liable with the nomine...` | (b) in any other case, the directors of the company when the shares were issued to or acquired by... |
| chh | `s 661(2) the person is jointly and severally liable with the nomine...` | the text names the other subscribers and the directors |
| chh | `s 661(3) the court may relieve the subscriber or director from his ...` | If in proceedings for the recovery of an amount under subsection (2) it appears to the court that... |
| chh | `s 661(4)(a) the subscriber or director may apply to the court for r...` | If a subscriber to a company's memorandum or a director of a company |
| chh | `s 661(4)(a) the subscriber or director may apply to the court for r...` | has reason to apprehend that a claim will or might be made for the recovery of any such amount fr... |
| chh | `s 661(4)(b) the court has the power to relieve him` | If a subscriber to a company's memorandum or a director of a company has reason to apprehend that... |
| chh | `s 662(1) this section applies to the shares` | This section applies in the case of a public company |
| chh | `s 662(2)(a) the company must cancel the shares` | This section applies in the case of a public company |
| chh | `s 662(2)(b) the company must apply for re-registration as a private...` | This section applies in the case of a public company |
| chh | `s 662(4) the directors may take the steps without complying with Ch...` | may take any steps necessary to enable the company to comply with this section |
| chh | `s 662(5) the person may exercise voting rights in respect of the sh...` | in a case within subsection (1)(d) or (e) |
| chh | `s 662(5) the person may exercise voting rights in respect of the sh...` | This section applies in the case of a public company |
| chh | `s 662(6) the purported exercise of the voting rights is void` | Any purported exercise of those rights is void |
| chh | `s 663(4) the person commits an offence` | who is in default |
| chh | `s 663(4) the person commits an offence` | who is in default |
| chh | `s 663(4) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 664(1) Chapter 3 of Part 3 applies to the resolution` | applies to any such resolution |
| chh | `s 664(2) the resolution may make the change` | such changes— (a) in the company's name, and (b) in the company's articles, as are necessary in c... |
| chh | `s 664(6) the registrar may accept the statement as sufficient evide...` | may accept the statement of compliance as sufficient evidence |
| chh | `s 665(5) the certificate is conclusive evidence that the requiremen...` | The certificate is conclusive evidence |
| chh | `s 666(2) the company continues to be treated as a public company` | the company continues to be treated as a public company |
| chh | `s 667(2) the person commits an offence` | who is in default |
| chh | `s 667(2) the person commits an offence` | who is in default |
| chh | `s 667(2) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 668(3) the date from which the period specified in section 662(3)...` | subject to the following modification |
| chh | `s 669(1) the amount transferred is available for distribution` | an amount equal to the value of the shares must be transferred out of profits available for divid... |
| chh | `s 670(1) the lien or charge is void` | A lien or other charge of a public company on its own shares |
| chh | `s 671 the interest is to be disregarded in determining whether the ...` | there shall be disregarded any such interest as is mentioned in section 672, 673 or 674 |
| chh | `s 672(1) the residual interest is to be disregarded` | any residual interest of the company that has not vested in possession |
| chh | `s 672(5) the date on which sections 660 and 661 are treated as appl...` | Where by virtue of this section shares are exempt from section 660 or 661 ... but the residual in... |
| chh | `s 672(6) the date on which sections 662 to 668 are treated as apply...` | Where by virtue of this section shares are exempt from sections 662 to 668 ... but the residual i... |
| chh | `s 673(1)(a) the charge, lien or set-off is to be disregarded` | Where the shares are held on trust for the purposes of a pension scheme there shall be disregarde... |
| chh | `s 673(1)(b) the right is to be disregarded` | (b) any right to receive from the trustee of the scheme, or as trustee of the scheme to retain, a... |
| chh | `s 673(2) the charge, lien or set-off is to be disregarded` | Where the shares are held on trust for the purposes of an employees' share scheme there shall be ... |
| chh | `s 674 the right is to be disregarded` | any rights that the company has in that capacity |
| chh | `s 674 the right is to be disregarded` | Where the company is a personal representative or trustee |
| chh | `s 676 the director is treated as employed by the company` | references to “employer” and “employee”, in the context of a pension scheme or employees' share s... |
| chh | `s 678(1) it is not lawful for the company to give the financial ass...` | for that company, or a company that is a subsidiary of that company, to give financial assistance |
| chh | `s 678(3) it is not lawful for the company to give the financial ass...` | for that company, or a company that is a subsidiary of that company, to give financial assistance |
| chh | `s 679(1) it is not lawful for the public company to give the financ...` | it is not lawful for a public company that is a subsidiary of that company to give financial assi... |
| chh | `s 679(3) it is not lawful for the public company to give the financ...` | it is not lawful for a public company that is a subsidiary of that company to give financial assi... |
| chh | `s 680(1) the person commits an offence` | who is in default |
| chh | `s 680(1) the person commits an offence` | who is in default |
| chh | `s 680(1) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 684(1) the company may issue redeemable shares` | A limited company having a share capital may issue shares that are to be redeemed |
| chh | `s 684(2) the articles may exclude or restrict the issue of redeemab...` | The articles of a private limited company may exclude or restrict the issue of redeemable shares |
| chh | `s 684(3) the public limited company may issue redeemable shares` | A public limited company may only issue redeemable shares |
| chh | `s 685(1) the directors may determine the terms, conditions and mann...` | The directors of a limited company may determine |
| chh | `s 685(1) the directors may determine the terms, conditions and mann...` | if they are authorised to do so— (a) by the company's articles, or (b) by a resolution of the com... |
| chh | `s 685(2) the resolution is a good resolution under subsection (1)(b)` | may be an ordinary resolution |
| chh | `s 685(2) the resolution is a good resolution under subsection (1)(b)` | A resolution under subsection (1)(b) |
| chh | `s 686(2) the terms of redemption may provide for payment on a later...` | The terms of redemption of shares in a limited company may provide that the amount payable on red... |
| chh | `s 687(1) the private limited company may redeem the shares out of c...` | A private limited company may redeem redeemable shares out of capital |
| chh | `s 687(6) the limits of section 687 on the source of payment are dis...` | This section is subject to section 735(4) |
| chh | `s 689(4) the person commits an offence` | who is in default |
| chh | `s 689(4) the person commits an offence` | who is in default |
| chh | `s 689(4) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 690(1) the limited company may purchase its own shares` | A limited company having a share capital may purchase its own shares |
| chh | `s 690(1) the limited company may purchase its own shares` | subject to— (b) any restriction or prohibition in the company's articles |
| chh | `s 692(1) the private limited company may purchase its own shares ou...` | A private limited company may purchase its own shares out of capital |
| chh | `s 692(1ZA) the most the company may pay out of capital in the finan...` | If authorised to do so by its articles, a private limited company may purchase its own shares out... |
| chh | `s 692(5) the limits of section 692 on the source of payment are dis...` | This section has effect subject to section 735(4) |
| chh | `s 693A(1) the company may make the off-market purchase` | A company may make an off-market purchase of its own shares for the purposes of or pursuant to an... |
| chh | `s 693A(1) the company may make the off-market purchase` | if the purchase has first been authorised by a resolution of the company under this section |
| chh | `s 693A(2) the authority may take that form` | That authority— (a) may be general or limited to the purchase of shares of a particular class or ... |
| chh | `s 693A(4) the authority may be varied, revoked or renewed` | The authority may be varied, revoked or from time to time renewed by a resolution of the company |
| chh | `s 693A(6) the company may make a purchase of its own shares after t...` | A company may make a purchase of its own shares after the expiry of the time limit specified if— ... |
| chh | `s 693A(7) the resolution may determine the price in that way` | (but without reference to any person's discretion or opinion) |
| chh | `s 693A(8) Chapter 3 of Part 3 applies to the resolution` | applies to a resolution under this section |
| chh | `s 694(3) the contract is a contract within section 694` | The contract may be a contract, entered into by the company and relating to shares in the company... |
| chh | `s 694(4) the authority may be varied, revoked or renewed` | The authority conferred by a resolution under this section may be varied, revoked or from time to... |
| chh | `s 694(5) the resolution specifies a date of expiry that is not late...` | In the case of a public company a resolution conferring, varying or renewing authority must speci... |
| chh | `s 695(1) this section applies to the resolution` | This section applies to a resolution to confer, vary, revoke or renew authority for the purposes ... |
| chh | `s 695(4)(b) the person may demand a poll on that question` | any member of the company may demand a poll on that question |
| chh | `s 695(4)(c) the vote or demand is the same as a vote or demand by t...` | a vote and a demand for a poll by a person as proxy for a member |
| chh | `s 696(1) this section applies to the resolution` | This section applies in relation to a resolution to confer, vary, revoke or renew authority for t... |
| chh | `s 696(3) the memorandum includes what the subsection requires` | A memorandum of contract terms so made available |
| chh | `s 696(4) the copy has annexed to it what the subsection requires` | A copy of the contract so made available |
| chh | `s 697(1) the company may agree to the variation` | A company may only agree to a variation of a contract authorised under section 694 |
| chh | `s 697(3) the authority may be varied, revoked or renewed` | That authority may be varied, revoked or from time to time renewed by a . . . resolution of the c... |
| chh | `s 697(4) the resolution specifies a date of expiry that is not late...` | In the case of a public company a resolution conferring, varying or renewing authority must speci... |
| chh | `s 699(1) this section applies to the resolution` | This section applies in relation to a resolution under section 697 |
| chh | `s 700(3) the authority may be varied, revoked or renewed` | That authority may be varied, revoked or from time to time renewed by a . . . resolution of the c... |
| chh | `s 700(4) the resolution specifies a date of expiry that is not late...` | In the case of a public company a resolution conferring, varying or renewing authority must speci... |
| chh | `s 700(5) sections 698 and 699 apply to the resolution` | apply to a resolution authorising a proposed release agreement |
| chh | `s 701(8) Chapter 3 of Part 3 applies to the resolution` | applies to a resolution under this section |
| chh | `s 702(6) the person may inspect the copy or memorandum without charge` | (b) in the case of a public company, by any other person |
| chh | `s 702(7) section 702 applies to the document as it applies to the o...` | apply to a variation of a contract |
| chh | `s 703(1) the person commits an offence` | who is in default |
| chh | `s 703(1) the person commits an offence` | who is in default |
| chh | `s 703(1) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 704 the company's right under the contract is capable of being as...` | The rights of a company under a contract authorised under— (za) section 693A ..., (a) section 694... |
| chh | `s 705(1) the payment must be made out of the company's distributabl...` | A payment made by a company in consideration of— (a) ..., (b) ..., or (c) ... |
| chh | `s 707(4) the return also states what the subsection requires` | In the case of a public company the return must also state |
| chh | `s 707(6) the person commits an offence` | the text charges every officer of the company who is in default |
| chh | `s 707(6) the person commits an offence` | who is in default |
| chh | `s 707(6) the person commits an offence` | who is in default |
| chh | `s 707(6) the person commits an offence` | the text charges every officer of the company who is in default |
| chh | `s 708(4) the person commits an offence` | who is in default |
| chh | `s 708(4) the person commits an offence` | who is in default |
| chh | `s 708(4) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 709(1) the private limited company may make the payment out of ca...` | A private limited company may in accordance with this Chapter |
| chh | `s 709(1) the private limited company may make the payment out of ca...` | but subject to any restriction or prohibition in the company's articles |
| chh | `s 709(2) the payment is a payment out of capital for the purposes o...` | to any payment so made |
| chh | `s 709(3) the requirements of Chapter 5 are displaced by section 692...` | This Chapter is subject to section 692(1ZA) |
| chh | `s 713(1) the payment out of capital is not lawful` | A payment out of capital by a private company |
| chh | `s 713(2) subsection (1) does not apply to the payment` | This is subject to section 720A and to any order of the court under section 721 |
| chh | `s 715(1) the person commits an offence` | the text charges every director who is in default |
| chh | `s 715(1) the person commits an offence` | the text charges every director who is in default |
| chh | `s 715(1) the person commits an offence` | who is in default |
| chh | `s 715(1) the person commits an offence` | the text charges every director who is in default |
| chh | `s 718(1) this section applies to the resolution` | This section applies to a resolution under section 716 |
| chh | `s 720(4) the person may inspect the statement and report without ch...` | any member or creditor of the company |
| chh | `s 720(5) the person commits an offence` | who is in default |
| chh | `s 720(5) the person commits an offence` | who is in default |
| chh | `s 720(5) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 720A(1) section 713(1) does not apply` | the purchase out of capital by a private company of its own shares |
| chh | `s 720A(5) the validity of the resolution is affected by the failure` | a failure to comply with subsection (3) or (4) |
| chh | `s 720A(6) section 717 applies to the resolution` | applies to a resolution under this section |
| chh | `s 720B(3) the registrar must register the documents on receipt` | the documents delivered to him under subsection (1) |
| chh | `s 720B(6) the validity of the resolution is affected by the failure` | a failure to deliver the documents ... within the time specified in that subsection, or ... a fai... |
| chh | `s 720B(7) the person commits an offence` | the text charges every officer of the company who is in default |
| chh | `s 720B(7) the person commits an offence` | who is in default |
| chh | `s 720B(7) the person commits an offence` | who is in default |
| chh | `s 720B(7) the person commits an offence` | the text charges every officer of the company who is in default |
| chh | `s 720B(8) the person commits an offence` | who is in default |
| chh | `s 720B(8) the person commits an offence` | who is in default |
| chh | `s 720B(8) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 721(1) the person may apply to the court for the cancellation of ...` | (a) any member of the company ..., and (b) any creditor of the company, may apply to the court |
| chh | `s 721(2)(b) the application may be made on behalf of the persons en...` | on behalf of the persons entitled to make it by such one or more of their number as they may appo... |
| chh | `s 721(4) the court has made the order the subsection requires` | an order either cancelling or confirming the resolution |
| chh | `s 721(5) the court may by order alter or extend the date or period` | If the court confirms the resolution, it may by order alter or extend |
| chh | `s 721(5) the court may by order alter or extend the date or period` | any date or period of time specified— (a) in the resolution, or (b) in any provision of this Chap... |
| chh | `s 721(6) the court's order may provide for the purchase of a member...` | The court's order may, if the court thinks fit |
| chh | `s 721(7) the court's order may restrict amendments of the articles` | The court's order may, if the court thinks fit, require the company not to make any, or any speci... |
| chh | `s 722(4) the person commits an offence` | who is in default |
| chh | `s 722(4) the person commits an offence` | who is in default |
| chh | `s 722(4) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 724(3) the company may do it with the shares` | (a) hold the shares (or any of them), or (b) deal with any of them, at any time, in accordance wi... |
| chh | `s 726(2) the company may exercise a right in respect of the treasur...` | This section applies where shares are held by a company as treasury shares |
| chh | `s 726(2) the purported exercise of the right is void` | any purported exercise of such a right is void |
| chh | `s 726(3) a dividend or other distribution may be paid or made to th...` | This section applies where shares are held by a company as treasury shares |
| chh | `s 726(4) section 726 prevents the transaction` | (if they are redeemable shares) |
| chh | `s 726(4) section 726 prevents the transaction` | This section applies where shares are held by a company as treasury shares |
| chh | `s 726(5) the shares are treated as purchased by the company, at the...` | Shares allotted as fully paid bonus shares in respect of the treasury shares |
| chh | `s 728(3) the particulars may be included in a single return` | Particulars of shares disposed of on different dates may be included in a single return |
| chh | `s 728(4) the person commits an offence` | the text charges every officer of the company who is in default |
| chh | `s 728(4) the person commits an offence` | who is in default |
| chh | `s 728(4) the person commits an offence` | who is in default |
| chh | `s 728(4) the person commits an offence` | the text charges every officer of the company who is in default |
| chh | `s 729(5) the directors may take the steps without complying with Ch...` | to enable the company to cancel its shares under this section |
| chh | `s 730(1) the return was delivered not later than 28 days after the ...` | This does not apply to shares that are cancelled forthwith on their acquisition by the company (s... |
| chh | `s 730(3) the particulars may be included in a single return` | Particulars of shares cancelled on different dates may be included in a single return |
| chh | `s 730(6) the person commits an offence` | who is in default |
| chh | `s 730(6) the person commits an offence` | who is in default |
| chh | `s 730(6) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 731(2) the amount treated as a realised profit of the company for...` | If the proceeds of sale are equal to or less than the purchase price paid by the company for the ... |
| chh | `s 731(3)(a) the amount treated as a realised profit of the company` | If the proceeds of sale exceed the purchase price paid by the company |
| chh | `s 731(3)(b) the amount to be transferred to the company's share pre...` | If the proceeds of sale exceed the purchase price paid by the company |
| chh | `s 731(4)(b) the purchase price paid for the shares` | if the shares were allotted to the company as fully paid bonus shares |
| chh | `s 732(1) the person commits an offence` | who is in default |
| chh | `s 732(1) the person commits an offence` | who is in default |
| chh | `s 732(1) the person commits an offence` | the text charges the company and every officer of the company who is in default |
| chh | `s 733(5) the company may use the capital redemption reserve to pay ...` | The company may use the capital redemption reserve to pay up new shares to be allotted to members... |
| chh | `s 733(6) the paid up share capital to take for the provision` | the rule is for "the provisions of the Companies Acts relating to the reduction of a company's sh... |
| chh | `s 735(2) the company is liable in damages for the failure` | in respect of any failure on its part to redeem or purchase |
| chh | `s 735(2) the company is liable in damages for the failure` | This section applies where |
| chh | `s 735(4) the terms of redemption or purchase may be enforced agains...` | If the company is wound up and at the commencement of the winding up any of the shares have not b... |
| chh | `s 735(4) the shares are treated as cancelled` | When shares are redeemed or purchased under this subsection, they are treated as cancelled |
| chh | `s 736 the profits are distributable profits in relation to the payment` | In this Part (except in Chapter 2 (financial assistance): see section 683) |

### Reading (b), added by the name-test sweep of 2026-11-12: grants whose "if" gate fails answer `NOTHING` (the other reading: `JUST FALSE`)

| fork | function |
| --- | --- |
| F-grant-661-3 | `s 661(3) the court may relieve the subscriber or director from his liability` |
| F-grant-661-4a | `s 661(4)(a) the subscriber or director may apply to the court for relief` |
| F-grant-661-4b | `s 661(4)(b) the court has the power to relieve him` |
| F-grant-685-1 | `s 685(1) the directors may determine the terms, conditions and manner of redemption` |
| F-grant-690-1 | `s 690(1) the limited company may purchase its own shares` |
| F-grant-693A-1 | `s 693A(1) the company may make the off-market purchase` |
| F-grant-693A-6 | `s 693A(6) the company may make a purchase of its own shares after the expiry of the time limit` |
| F-grant-701-6 | `s 701(6) the company may make a purchase of its own shares after the expiry of the time limit` |
| F-grant-709-1 | `s 709(1) the private limited company may make the payment out of capital` |
| F-grant-721-5 | `s 721(5) the court may by order alter or extend the date or period` |
| F-grant-721-6 | `s 721(6) the court's order may provide for the purchase of a member's shares and alter the articles` |
| F-grant-721-7 | `s 721(7) the court's order may restrict amendments of the articles` |
| F-grant-735-4 | `s 735(4) the terms of redemption or purchase may be enforced against the company` |

### Reading a result: FALSE and NOTHING (coa15)

A rule of this encoding answers `JUST TRUE`, `JUST FALSE` or `NOTHING`; a number or a date is answered plainly.

**`JUST TRUE` is the text's yes.** The facts bring the case within the provision in its own words: the company may buy back its shares (s 690(1)); the directors' statement has everything s 714 requires; the payment is in the window of s 723(1).

**`JUST FALSE` is the text's own no, never "not mentioned".** Part 18 says no in these ways, and each answer carries a `-- FALSE-kind` comment quoting the words:

- a condition the text introduces with "if", "where", "unless", "only if" or "when" is not met: `s 724(3)` where s 724 does not apply, `s 662(2)(a)` where the shares were already disposed of ("Unless the shares ... are previously disposed of");
- a period the text fixes in its own words is missed: `s 663(1)` after one month, `s 719(1)` after the week, `s 720B(1)` after 15 days (ruling of 2026-11-05, (a));
- a "means" definition is not satisfied: `s 677(1)`, `s 675(1)`, `s 693(3)`;
- a flat negative: the company must not exercise any right in respect of treasury shares (`s 726(2) the company may exercise a right ...` answers `JUST FALSE`), and no dividend may be paid to it on them (`s 726(3)`);
- a bare "must" not done: `s 714(2)` to `(6)`, `s 702(3)`, `s 728(2)`: the requirement is not met (fork F-must);
- no offence where there is no contravention or default: `s 680(1)` where the company did not contravene ss 678 or 679.

**`NOTHING` is "the text does not decide this case on these facts", and it never means no.** It carries a `-- NOTHING-kind` comment saying why, in one of six words:

- `limited by its own wording`: the text speaks only of a stated case and the facts are outside it, with no "only": s 662(1) applies "in the case of a public company", so for a private company the answer is `NOTHING`; ss 678(1) and 679(1) name the giver (the company whose shares are acquired, or its subsidiary; a public company that is a subsidiary of a private company), so another giver is `NOTHING`; s 659(1) lets a limited company acquire "fully paid shares otherwise than for valuable consideration", so shares not fully paid, or acquired for value, are `NOTHING`; s 662(5) forbids the company, so a vote by its nominee or another shareholder is `NOTHING`; an officer who is not in default is not charged by the offence provisions (fork F-not-in-default); a grant or power whose "if" gate fails (ss 661(3), 661(4), 685(1), 693A(1), 693A(6), 721(5) to (7), 735(4): see the name-test sweep and the F-grant forks);
- `list not closed`: s 659(2), s 726(4), s 727(1), s 734(3);
- `includes`: "cash includes foreign currency" (s 727(2)), "other relevant payment lawfully made includes" (s 712(4)), what a right or a liability includes (s 672(3)), a liability includes a change of financial position (s 683(2));
- `undefined term`: "weighted average price method" (s 731(4)(a));
- `points outside the text`: whether an officer is in default (s 1121), whether a scheme is an employees' share scheme (s 1166), whether a resolution is special (s 283), whether the directors made a solvency statement (s 643), whether another provision of the Part is met (a payment "in accordance with Chapter 5", whether s 724 or s 735(4) applies), the Secretary of State's orders under s 727(3), and the meaning in Part 23;
- `silent`: s 730(7) states no penalty on indictment, s 728(2) with no class entry in the facts.

**A caller must never turn `NOTHING` into `FALSE`.** `coa15-seat.l4` does not: where a layer-1 rule is MAYBE BOOLEAN the seat question is MAYBE BOOLEAN too, and the two seat questions that read a layer-1 `MAYBE BOOLEAN` answer (the offences of s 703(1) and s 720(5), which turn on whether the company is in default) pass `NOTHING` through.

**Numbers and dates.** Where a sum cannot be known the function returns `MAYBE NUMBER` (`s 692(1ZA)`, `s 711(2)`, `s 731`) and `NOTHING` is the text's silence.
Fines are answered as limits, never as pounds: the statutory maximum and the standard scale are not in the Act (the core's `Fine limit`), except where the Act states the sterling figure (the £15,000 and 5% of s 692(1ZA); the £5,000 and level 4 of ss 707(7) and 728(5)).

**Obligations.** A duty is a `DEONTIC`: it is exercised by `#TRACE`, and each trace ends `FULFILLED`, a breach, or a residual obligation that has no deadline in the text (waiting does not breach a duty with no `WITHIN`).
The same duty is also encoded as a decision function over the facts (for example `s 719(1) the notice was published in the Gazette in time`).

## Seams (coa15)

A seam is an answer another part computes. Each is an input of the rule that needs it, named for its section as `PLAN.md` section 4 says, declared once where it is asked, `MAYBE BOOLEAN` unless a number or a plain fact is wanted. A `NOTHING` input makes the answer `NOTHING` (`-- NOTHING-kind (points outside the text)`), never `FALSE`.

### Seams taken as `s N ...` inputs

| seam (PLAN.md) | input name in the L4 | type | asked by |
| --- | --- | --- | --- |
| s 1121 (coa24): officer in default | `s 1121 the officer is in default` | MAYBE BOOLEAN | every offence function: ss 658(2)(a), 663(4), 667(2), 680(1), 689(4), 703(1), 707(6), 708(4), 715(1), 720(5), 720B(7) and (8), 722(4), 728(4), 730(6), 732(1) |
| s 283 (coa7): special resolution | `s 283 the resolution is a special resolution` | MAYBE BOOLEAN | ss 716(1), 720A(1), 721(1) |
| s 282 (coa7): ordinary resolution | `s 282 the resolution is an ordinary resolution` | MAYBE BOOLEAN | s 685(2) |
| s 1166 (the keel, PLAN.md 4.1): employees' share scheme | `s 1166 the purchase is for the purposes of or pursuant to an employees' share scheme`; `s 1166 the scheme is an employees' share scheme` | MAYBE BOOLEAN | ss 691(3), 693A(1), 720A(1); s 682(2)(b) |
| s 1159(1) (the keel): holding company, subsidiary | `s 1159(1) the company is a holding company or a subsidiary of that company`; `s 1159(1) the company is a subsidiary of a holding company of that company` | MAYBE BOOLEAN | s 682(5) |
| s 643 (coa14): solvency statement | `s 643 the directors made a solvency statement` | MAYBE BOOLEAN | s 720A(2) |
| s 829 (coa18): distribution | `s 829 the payment is a distribution` | MAYBE BOOLEAN | s 683(1) |
| s 830 (coa18): profits available for distribution | `s 830 the profits available for distribution` | NUMBER | s 683(1), s 736 |
| s 846 (coa18): profit that would be available for a distribution of that character | `s 846 the profit that would be available for a distribution of that character` | NUMBER | s 683(1) |

### Seams taken as plain inputs or as a choice among named cases

| cross-reference in the range | taken as |
| --- | --- |
| s 396 (coa8): provisions of a kind specified by regulations (ss 677(3), 712(3)(i)) | NUMBER inputs: `the provisions of a kind specified ... by regulations under section 396` |
| s 1136 (coa25): a place specified in regulations (ss 702(4), 720(2)) | BOOLEAN inputs: `it is kept at a place specified in regulations under section 1136` |
| s 979 (coa21): notice that a person desires to acquire treasury shares (s 727(4)) | BOOLEAN input: `the company has received a notice under section 979 ...` |
| Chapter 3 of Part 3 (coa1): a resolution already forwarded (s 664(4)) | BOOLEAN input: `a copy of the resolution has already been forwarded under Chapter 3 of Part 3` |
| s 98 (coa2), s 759 (coa16), Part 30 (coa22): court orders under which shares are purchased (s 659(2)(b)); acquisitions otherwise than in accordance with Part 30 (ss 662(1)(c), 668(1)(b)) | constructors of `s 659(2) kind of acquisition`, `s 662(1) how the shares come to be held`, `s 668(1) how the shares came to be held by or for the private company` |
| Part 17 (coa13), Part 26 (coa20): a reduction of capital under Chapter 10 of Part 17; anything done under a court order under Part 26 or 26A (s 681(2)(c), (e)) | constructors of `s 681(2) transaction`; s 729(5)'s "without complying with Chapter 10 of Part 17" is a BOOLEAN input |
| Part 23 (coa18), ss 836 and 842: whether a company has profits available (s 711(2)); realised profit (s 731) | NUMBER inputs (the profits the relevant accounts show; the proceeds of sale and the price paid); the realised profit is an amount the rule returns |
| Part 20 (coa16): the consequence of a public company being treated as private (s 666(1)) | not modelled: `s 666(1)` answers whether Chapter 1 of Part 20 applies as if the company were private, and Part 20's own rule answers what follows |
| s 673 and "section 57 of the Pension Schemes (Northern Ireland) Act 1993" | not a seam: `PLAN.md` names `s 57 [coa2]`, but the text at line 8920 cites section 57 of another Act, which is a fact of the case (`s 673(1)(b) the right is to be disregarded` is encoded as stated) |
| s 693A(8) and s 701(8): "Chapter 3 of Part 3 applies to a resolution under this section" | encoded as one-line functions (`s 693A(8) Chapter 3 of Part 3 applies to the resolution`, `s 701(8) ...`): `JUST TRUE` where the resolution is one under the section, `NOTHING` otherwise; what Chapter 3 of Part 3 then requires is coa1's |

### Seams the plan lacks

- Every `s N ...` input above is named in `PLAN.md`: `s 1121`, `s 282`, `s 283`, `s 829` and `s 830` in the section 4.2 table, `s 1166` and `s 1159(1)` in section 4.1 (the keel's borrowed-term answers). `s 643` (the solvency statement) and `s 846` are named only in the coa15 row's list of cross-references, not in the section 4.2 table. The lead wires each answering part's function to the input at the merge.
- `s 1121 the officer is in default` is the heaviest seam: it is asked by every offence function (16 of them). The text of Part 18 itself never defines default.

## What the text turns out to say (numbered findings)

1. **The rendering runs two wordings of the daily default fine together** at line 9300 (s 707(7)(b)) and line 9573 (s 728(5)(b)): "one-tenth of the statutory maximumone-tenth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale for summary offences". The text does not say which wording is in force (an amendment that substituted one for the other, shown without its marker). Both functions take the fact as an input and answer `NOTHING` when it is not known (fork F-penalty, `NEEDS-CORE.md`).
2. **Provisions shown as rows of dots.** The rendering shows rows of dots in place of text at s 663(3)(d), s 689(3)(d), s 708(3)(d), s 720B(2)(d), s 724(2), s 725 (Treasury shares: maximum holdings), s 729(2), s 729(3), s 730(5)(d) (9 units). They are rows `repealed or blank in this text` in the coverage table. The index of Schedule 8 that `PLAN.md` quotes names s 724(2) as the definition of "qualifying shares", but this rendering shows s 724(2) as a row of dots, so nothing is encoded for that term.
3. **Seven lines read "a . . . resolution"**, with the word before "resolution" omitted: lines 9146 and 9147 (s 694(2)(a) and (b)), 9149 (s 694(4)), 9176 (s 697(2)), 9177 (s 697(3)), 9205 (s 700(2)) and 9206 (s 700(3)). The omitted word is not supplied; the resolution is a plain fact in each rule (fork F-omitted-word). s 685(2), by contrast, says in words that a resolution may be an ordinary resolution.
4. **A private company has three routes to pay for its own shares out of capital.** Chapter 5 (ss 709 to 723: the permissible capital payment, the directors' statement and auditor's report, a special resolution, notice in the Gazette, inspection, the five-to-seven-week window); the annual limit of s 692(1ZA) (authorised by the articles, the lower of £15,000 and the nominal value of 5% of the fully paid share capital at the start of the financial year, which is £15,000 for capital of £300,000 or more, with s 692(1A) converting capital not in sterling at a spot rate); and the solvency-statement route of ss 720A and 720B for a purchase for an employees' share scheme. s 713(1) makes a payment out of capital unlawful unless Chapter 5 is followed, and s 713(2) and s 709(3) make that subject to s 720A, an order under s 721 and s 692(1ZA).
5. **Every offence charges officers or directors in default, and the text states no test of "default".** ss 707(6), 720B(7) and 728(4) charge every officer in default and do not charge the company; s 715(1) charges every director in default; ss 658(2), 663(4), 667(2), 680(1), 689(4), 703(1), 708(4), 720(5), 720B(8), 722(4), 730(6) and 732(1) charge the company and every officer in default. Whether an officer is in default is s 1121, outside this range: every offence takes it as the input `s 1121 the officer is in default`.
6. **The penalties come in four shapes.** Imprisonment or a fine on indictment and by place on summary conviction (ss 658(3), 680(2), 715(2): two years, 12 months in England and Wales, six months in Scotland and Northern Ireland); a fine of level 3 with a daily default fine of one-tenth of level 3 (ss 663(5), 667(3), 689(5), 703(2), 708(5), 720(6), 722(5), 730(7)); a fine on indictment and the statutory maximum on summary conviction (ss 720B(9), 732(2)); and the statutory maximum with a daily default fine (ss 707(7), 728(5), the two with the doubled wording of finding 1). Where the text gives a penalty on summary conviction only (the level-3 group) the answer on indictment is `NOTHING`.
7. **"Distributable profits" is defined twice in the Part**: s 683(1) for financial assistance (profits out of which a distribution equal to the assistance could lawfully be made, and, where the assistance is a disposition of a non-cash asset, any profit that would be available for a distribution of that character, s 846) and s 736 for the rest of the Part, which excepts Chapter 2 in terms ("except in Chapter 2: see section 683"). The two are encoded separately, each under its own section label, and both take their figures from Part 23 (ss 829, 830, 846) as inputs.
8. **s 735(4) reaches back into ss 687 and 692.** In a winding up the terms of redemption or purchase may be enforced against the company, which ss 687(6) and 692(5) mark with "subject to section 735(4)"; s 735(5) takes later-dated terms and the case where no distribution could lawfully have been made out of subsection (4); s 735(6) ranks three kinds of claim. ss 687(6), 692(5) and 709(3) are signposts; each is encoded as a function that answers `JUST TRUE` where the named provision applies and `NOTHING` otherwise (fork F-signpost).
9. **The same five words recur for the statement of capital**: ss 663(3), 689(3), 708(3), 720B(2) and 730(5) each require the same items. One record (`s 663(3) statement of capital`, `coa15-nouns.l4`) and one helper (`s 663(3) the statement of capital states what the section requires`) serve all five.
10. **s 733(3) has a carve-out in an unnumbered closing sentence**: the transfer of the difference to the capital redemption reserve "does not apply in the case of a private company if, in addition to the proceeds of the fresh issue, the company applies a payment out of capital under Chapter 5 or under section 692(1ZA)". It is encoded with both facts as inputs.
11. **s 731(4)(a) names "a weighted average price method" and does not define it.** The plain weighted average is taken (fork F-weighted).
12. **The range has no table and no schedule.** The coverage rows are headings, sections, subsections, lettered paragraphs and defined terms.
13. **The seat questions are all "Under section N".** A person in the seat asks one question per rule, with plain inputs; where the Act's rule turns on a fact another section answers (an officer in default, a special resolution, a solvency statement) the seat asks the person for that fact and passes it in as `JUST TRUE` or `JUST FALSE`.

## Seat audit of 2026-11-12

The team lead asked for every seat question's name and `@export` text to be read against the layer-1 function its body calls, for a direction mismatch (a question titled as a permission over a function that returns the bar, or the reverse) and a subject mismatch (a question that asks one thing over a function that answers another).

- **Read:** 162 of 162 seat questions (the list below), each name against the function its body calls and that function's name and answer.
- **Direction mismatches: 1.** `Under section 695, is the resolution authorising the purchase effective, given how members holding the shares voted` returned `s 695(3) the resolution is not effective`, so `JUST TRUE` meant "not effective". Retitled `Under section 695(3), is the resolution authorising the purchase not effective because of how members holding the shares voted`, which is how `s 717` was already titled.
- **Subject mismatches: 2.** `Under section 686, is the redemption of these redeemable shares barred, and must they be paid for on redemption` returned only `s 686(1) the redemption is barred`; retitled `Under section 686(1), is the redemption of these redeemable shares barred because they are not fully paid`. `Under section 705, must a payment for a right, a variation or a release come out of distributable profits, and what follows if it does not` returned `s 705(2) the consequence of the requirement not being met` and did not answer the "must"; retitled `Under section 705(2), what follows if a payment for a right, a variation or a release is not paid out of distributable profits`.
- **Not changed:** the answers (no answer was negated), the inputs and their `@desc` texts, the facts and the expected values. `coa15-cases-seat.l4` calls each question by its section number, so no assertion changed; each of the three retitles is recorded with a `-- RECONCILED 2026-11-12` comment above that question's assertions. The count is still 575 assertions, all satisfied.
- **Questions that read close but are not mismatches.** The "unlawful" questions of ss 678(1), 678(3), 679(1) and 679(3) return `s 678(5)` and `s 679(5)` ("the assistance is prohibited ... as it has effect subject to sections 681 and 682"), so `JUST TRUE` is "unlawful" in both; ss 681 and 682 ask whether the section "lets" the transaction and return "neither section 678 nor section 679 prohibits the transaction", so `JUST TRUE` is "allowed" in both; s 713 asks whether a payment is "not lawful" and returns `s 713(1) the payment out of capital is not lawful`; ss 717 and 718 ask whether the resolution is "not effective" or "ineffective" and return exactly that.

### The 162 seat questions (in the text's order)

1. Under section 658(1), must my limited company not acquire its own shares in this way
2. Under section 658(2), am I guilty of an offence because my company acquired its own shares in contravention of section 658
3. Under section 658(2), is the purported acquisition of its own shares by my company void
4. Under section 658(3), what is the most I can be sentenced to if convicted of the offence
5. Under section 659(1), may my limited company acquire some of its own shares for nothing
6. Under section 659(2), does section 658 not prohibit this acquisition
7. Under section 660, are the shares held by my company's nominee treated as held by him on his own account
8. Under section 661(2), am I jointly and severally liable with the nominee to pay the amount he failed to pay on the shares
9. Under section 661(3), may the court relieve me from liability for the nominee's unpaid amount
10. Under section 661(4), may I apply to the court for relief before any claim is made against me
11. Under section 662(2), must my public company cancel these shares and reduce its share capital
12. Under section 662(2)(b), must my public company also apply to re-register as a private company
13. Under section 662(3), by what date must my public company cancel the shares (and apply for re-registration if it must)
14. Under section 662(5), may the company, or its nominee or other shareholder, vote the shares
15. Under section 663(1), by what date must my company give the registrar notice of the cancellation of the shares
16. Under section 663(3), does my company's statement of capital state everything the section requires
17. Under section 663(4), am I guilty of an offence because my company did not comply with section 663
18. Under section 663(5), what is the most I can be fined if convicted of that offence
19. Under section 664(1), may the directors resolve that my public company be re-registered as a private company
20. Under section 664(4), is my company's application for re-registration accompanied by everything the section requires
21. Under section 665(4), does my company become a private company when the registrar issues the certificate
22. Under section 666, does Chapter 1 of Part 20 apply to my public company as if it were a private company because it failed to re-register
23. Under section 667, am I guilty of an offence because my public company did not cancel the shares or re-register in time
24. Under section 667(3), what is the most I can be fined if convicted of the offence of failing to cancel the shares or to re-register in time
25. Under section 668, from what date does the period in section 662(3) run for my company that re-registered as a public company
26. Under section 669(1), how much must my public company transfer out of profits available for dividend to a reserve fund
27. Under section 670, is a lien or charge my public company holds on its own shares void
28. Under section 671, is the company's interest one to be disregarded in deciding whether it has a beneficial interest in the shares
29. Under section 675, is this scheme a pension scheme for the purposes of Chapter 1
30. Under section 676, is a director treated as employed by the company in a pension scheme or employees' share scheme
31. Under section 677, is what my company is giving financial assistance for the purposes of Chapter 2
32. Under section 678(1), is it unlawful for my public company, or its subsidiary, to give this financial assistance for an acquisition of its shares
33. Under section 678(3), is it unlawful for my company to give financial assistance to reduce or discharge a liability incurred for an acquisition of its shares while it is a public company
34. Under section 679(1), is it unlawful for my public company, a subsidiary of a private company, to give this financial assistance for an acquisition of shares in its private holding company
35. Under section 679(3), is it unlawful for my public company to give financial assistance to reduce or discharge a liability incurred for an acquisition of shares in its private holding company
36. Under section 680, am I guilty of an offence because my company gave prohibited financial assistance
37. Under section 680(2), what is the most I can be sentenced to if convicted of that offence
38. Under section 681, does section 681 let my company do this despite sections 678 and 679
39. Under section 682, does section 682 let my company give this financial assistance despite sections 678 and 679
40. Under section 683(1), how much are my company's distributable profits for this financial assistance
41. Under section 684(1), may my limited company having a share capital issue redeemable shares
42. Under section 684(2), may the articles of my private limited company exclude or restrict the issue of redeemable shares
43. Under section 684(3), may my public limited company issue redeemable shares
44. Under section 684(4), is the issue of redeemable shares barred because there are no issued shares that are not redeemable
45. Under section 685(1), may the directors of my company determine the terms, conditions and manner of redemption of the shares
46. Under section 685(3), did the directors determine the terms of redemption in time, before the shares were allotted
47. Under section 686(1), is the redemption of these redeemable shares barred because they are not fully paid
48. Under section 687, may my company redeem the shares out of this source of money
49. Under section 687(3) and (4), how much of the premium on redemption must come out of distributable profits
50. Under section 688, what is my company's issued share capital after redeeming these shares
51. Under section 689(1), by what date must my company give the registrar notice of the redemption
52. Under section 689(4), am I guilty of an offence because my company did not comply with section 689
53. Under section 689(5), what is the most I can be fined if convicted of the offence of failing to give notice of the redemption
54. Under section 690(1), may my limited company having a share capital purchase its own shares
55. Under section 690(2), is this purchase barred because no issued shares other than redeemable or treasury shares would remain
56. Under section 691(1), is the purchase barred because the shares are not fully paid
57. Under section 691(2), must my limited company pay for the shares on the purchase
58. Under section 692(1ZA), how much may my private limited company pay out of capital for its own shares in this financial year without following Chapter 5
59. Under section 692(2), may my company pay for the purchase out of this source of money
60. Under section 692(2)(b) and (3), how much of the premium on the purchase must come out of distributable profits
61. Under section 693, may my limited company make this purchase of its own shares, given how it was authorised
62. Under section 693(2), is this purchase of my company's own shares an off-market purchase
63. Under section 693(4), is this purchase of my company's own shares a market purchase
64. Under section 693A(5), is the expiry date in the resolution authorising a purchase one the Act allows (not later than five years after it is passed)
65. Under section 694(2), is the contract for my company's off-market purchase approved in the way the section requires
66. Under section 695(3), is the resolution authorising the purchase not effective because of how members holding the shares voted
67. Under section 696, was the contract disclosed to members as the section requires for a resolution at a meeting
68. Under section 696, was the contract disclosed to members as the section requires for a written resolution
69. Under section 696(5), is the resolution not validly passed because section 696 was not complied with
70. Under section 697(1), may my company agree to a variation of the contract
71. Under section 700(1), is the agreement releasing my company's rights under the contract void
72. Under section 701(1), may my company make this market purchase of its own shares
73. Under section 701(5), is the expiry date in the resolution authorising a market purchase one the Act allows
74. Under section 702(3), until what date must my company keep the copy of the contract or memorandum available for inspection
75. Under section 702(6), may I inspect the copy of the contract or memorandum without charge
76. Under section 703, am I guilty of an offence because my company did not keep the contract available or refused inspection
77. Under section 703(2), what is the most I can be fined if convicted of the offence of failing to keep the contract available or refusing inspection
78. Under section 704, can my company assign its right to purchase its own shares under this contract
79. Under section 705(2), what follows if a payment for a right, a variation or a release is not paid out of distributable profits
80. Under section 706(a), may the shares my company purchased be held and dealt with as treasury shares
81. Under section 706(b)(i), are the shares my company purchased treated as cancelled
82. Under section 706(b)(ii), what is my company's issued share capital after a purchase that cancels the shares
83. Under section 707(1), by what date must my company deliver the return of its purchase to the registrar
84. Under section 707(6), am I guilty of an offence because my company did not deliver the return
85. Under section 707(7), what is the most I can be fined if convicted of that offence
86. Under section 708, by what date must my company give the registrar notice of the cancellation of the shares it purchased
87. Under section 708(1), must my company give the registrar notice of the cancellation of the shares it purchased
88. Under section 708(4), am I guilty of an offence because my company did not give notice of the cancellation
89. Under section 708(5), what is the most I can be fined if convicted of the offence of failing to give notice of the cancellation of purchased shares
90. Under section 709(1), may my private limited company make a payment out of capital for redeeming or purchasing its own shares
91. Under section 710, how much is the permissible capital payment for the shares
92. Under section 712, what are my company's available profits for a payment out of capital
93. Under section 713, is my private company's payment out of capital not lawful because a requirement was not met
94. Under section 714, does the directors' statement and auditor's report contain everything the section requires
95. Under section 715, am I, a director, guilty of an offence because the statement was made without reasonable grounds for the opinion
96. Under section 715(2), what is the most I can be sentenced to if convicted of that offence
97. Under section 716, by what date must my private company pass the special resolution approving the payment out of capital
98. Under section 716(1), is the payment out of capital approved as the section requires
99. Under section 717, is the resolution approving the payment not effective because of how members holding the shares voted
100. Under section 718, is the resolution ineffective because the directors' statement and auditor's report were not made available to members
101. Under section 719, by what date must my company publish the notice of the proposed payment in the Gazette
102. Under section 719(4), by what day must my company deliver a copy of the directors' statement and auditor's report to the registrar
103. Under section 720(1), from what day must the directors' statement and auditor's report be kept available for inspection
104. Under section 720(1), until what day must the directors' statement and auditor's report be kept available for inspection
105. Under section 720(4), may I inspect the directors' statement and auditor's report without charge
106. Under section 720(5), am I guilty of an offence because my company did not comply with section 720 or refused inspection
107. Under section 720(6), what is the most I can be fined if convicted of the offence of failing to keep the statement and report available or refusing inspection
108. Under section 720A, does section 713(1) not apply to my private company's purchase out of capital for an employees' share scheme
109. Under section 720B(1), by what date must my company deliver the solvency statement, the resolution and a statement of capital to the registrar
110. Under section 720B(4), is the resolution still unable to take effect
111. Under section 720B(7), am I guilty of an offence because my company delivered a solvency statement that was not provided to members
112. Under section 720B(8), am I guilty of an offence because my company did not comply with section 720B
113. Under section 720B(9), what is the most I can be fined if convicted of an offence under section 720B
114. Under section 721(1), may I apply to the court to cancel the resolution approving the payment out of capital
115. Under section 721(2), by what date must I apply to the court to cancel the resolution
116. Under section 722(3), by what date must my company deliver a copy of the court's order to the registrar
117. Under section 722(4), am I guilty of an offence because my company did not give the registrar notice of the court application or deliver a copy of the order
118. Under section 722(5), what is the most I can be fined if convicted of the offence of failing to give notice of the court application or to deliver the order
119. Under section 723, was my company's payment out of capital made within the window the section allows
120. Under section 724(3), may my limited company hold, or deal with, the shares it purchased as treasury shares
121. Under section 724(4), must my company be entered in its register of members as the member holding the shares
122. Under section 724(5), does my company hold these shares as treasury shares
123. Under section 726(2), may my company exercise a right in respect of the treasury shares it holds
124. Under section 726(2), is a purported exercise of a right in respect of treasury shares void
125. Under section 726(3), may my company be paid a dividend or other distribution in respect of its treasury shares
126. Under section 726(4), does section 726 prevent my company from doing this in respect of its treasury shares
127. Under section 726(5), are the bonus shares allotted in respect of treasury shares treated as purchased by my company
128. Under section 727(1), may my company dispose of its treasury shares in this way
129. Under section 727(2), is what my company receives for the treasury shares a cash consideration
130. Under section 727(2), is foreign currency cash for this purpose
131. Under section 727(4), is my company barred from selling or transferring treasury shares to someone other than the person who gave a section 979 notice
132. Under section 728(1), by what date must my company deliver the return of treasury shares it sold or transferred for an employees' share scheme
133. Under section 728(4), am I guilty of an offence because my company did not deliver the return of shares disposed of
134. Under section 728(5), what is the most I can be fined if convicted of that offence
135. Under section 729(1), may my company cancel the shares it holds as treasury shares
136. Under section 729(4), what is my company's share capital after it cancels treasury shares
137. Under section 729(5), may the directors take the steps needed to cancel the shares without complying with Chapter 10 of Part 17
138. Under section 730(1), by what date must my company deliver the return of treasury shares it cancelled
139. Under section 730(5), does my company's statement of capital with the notice of cancellation state everything the section requires
140. Under section 730(6), am I guilty of an offence because my company did not deliver the return of shares cancelled
141. Under section 730(7), what is the most I can be fined if convicted of that offence
142. Under section 731(2), what part of the proceeds of selling treasury shares is treated as my company's realised profit if they are no more than the purchase price
143. Under section 731(3), how much of the proceeds above the purchase price goes to the share premium account
144. Under section 731(4), what purchase price is taken as paid for the shares sold, by the weighted average price method
145. Under section 732, am I guilty of an offence because my company contravened Chapter 6
146. Under section 732(2), what is the most I can be fined if convicted of that offence
147. Under section 733(2), how much must my company transfer to the capital redemption reserve after redeeming or purchasing shares wholly out of profits
148. Under section 733(3), how much must my company transfer to the capital redemption reserve when the proceeds of a fresh issue are less than the nominal value of the shares redeemed or purchased
149. Under section 733(4), how much must my company transfer to the capital redemption reserve when it cancels treasury shares
150. Under section 733(5), may my company use the capital redemption reserve to pay up bonus shares
151. Under section 733(6), how much share capital is counted for a reduction of capital once the capital redemption reserve is added
152. Under section 734, does the accounting section apply because my company made a payment out of capital
153. Under section 734(1A), what is the permissible capital payment for a payment under section 692(1ZA)
154. Under section 734(2), how much must my company transfer to the capital redemption reserve because the permissible capital payment is less than the nominal amount
155. Under section 734(3), by how much at most may my company reduce its reserves and share capital because the permissible capital payment exceeds the nominal amount
156. Under section 734(4), what amount is read as the permissible capital payment when a fresh issue is applied as well
157. Under section 735(2), is my company liable in damages for failing to redeem or purchase its shares
158. Under section 735(2), does the holder of the shares keep this right despite the company's failure to redeem or purchase
159. Under section 735(3), must the court refuse an order for specific performance of the company's terms of redemption or purchase
160. Under section 735(4), may I enforce the terms of redemption or purchase against my company in its winding up
161. Under section 735(6), is this claim paid in priority to what my company must pay under section 735(4)
162. Under section 736, are my company's profits distributable profits in relation to this payment

## Name-test sweep of 2026-11-12

The lead asked for every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" to be tested for a grant turned into a bar: a function named for a grant or a power that answers `JUST FALSE` because an "if" gate failed. The three tests were applied to the decision functions of Chapters 1 to 7 (the deontic duties and the numeric functions are outside the class: a number is not `JUST FALSE`).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 13 | 17 | 9 | 2 |

**Flipped to `NOTHING`** (each has one fork line in the fork register and one line under reading (b) of the marginal readings; the other reading is `JUST FALSE`):

- `s 661(3) the court may relieve the subscriber or director from his liability` (F-grant-661-3)
- `s 661(4)(a) the subscriber or director may apply to the court for relief` (F-grant-661-4a)
- `s 661(4)(b) the court has the power to relieve him` (F-grant-661-4b)
- `s 685(1) the directors may determine the terms, conditions and manner of redemption` (F-grant-685-1)
- `s 690(1) the limited company may purchase its own shares` (F-grant-690-1)
- `s 693A(1) the company may make the off-market purchase` (F-grant-693A-1)
- `s 693A(6) the company may make a purchase of its own shares after the expiry of the time limit` (F-grant-693A-6)
- `s 701(6) the company may make a purchase of its own shares after the expiry of the time limit` (F-grant-701-6)
- `s 709(1) the private limited company may make the payment out of capital` (F-grant-709-1)
- `s 721(5) the court may by order alter or extend the date or period` (F-grant-721-5)
- `s 721(6) the court's order may provide for the purchase of a member's shares and alter the articles` (F-grant-721-6)
- `s 721(7) the court's order may restrict amendments of the articles` (F-grant-721-7)
- `s 735(4) the terms of redemption or purchase may be enforced against the company` (F-grant-735-4)

**Kept `JUST FALSE`** (the text closes the gate with "only", "only if", "void, except as", or the function is a bar or a requirement, not a grant):

- `s 662(5) the person may exercise voting rights in respect of the shares`: a bar: "Neither the company nor ... may exercise voting rights"
- `s 670(2) the charge is permitted`: closed by s 670(1): the charge "is void, except as permitted by this section"
- `s 670(3) the charge is permitted`: closed by s 670(1), as s 670(2)
- `s 670(4) the charge is permitted`: closed by s 670(1), as s 670(2)
- `s 684(3) the public limited company may issue redeemable shares`: "may only issue redeemable shares if it is authorised to do so by its articles"
- `s 687(1) the private limited company may redeem the shares out of capital`: the Chapter 5 gate is closed by s 687(2): redeemable shares "may only be redeemed out of" profits or a fresh issue
- `s 687(2) the redemption is out of a source the section permits`: "may only be redeemed out of"
- `s 692(1) the private limited company may purchase its own shares out of capital`: the Chapter 5 gate is closed by s 692(2)(a): "a limited company may only purchase its own shares out of"
- `s 692(2)(a) the purchase is out of a source the section permits`: "may only purchase its own shares out of"
- `s 693(1) the limited company may make the purchase`: "A limited company may only purchase its own shares"
- `s 694(1) the company may make the off-market purchase`: "A company may only make an off-market purchase"
- `s 697(1) the company may agree to the variation`: "A company may only agree to a variation ... if"
- `s 697(2) the variation is authorised in the way the subsection requires`: a requirement ("must be authorised"), not a grant
- `s 700(2) the release agreement is authorised in the way the subsection requires`: a requirement ("must be authorised"), not a grant
- `s 701(1) the company may make the market purchase`: "A company may only make a market purchase of its own shares if"
- `s 726(2) the company may exercise a right in respect of the treasury shares`: a bar: "The company must not exercise any right"
- `s 726(3) a dividend or other distribution may be paid or made to the company in respect of the treasury shares`: a bar: "No dividend may be paid"

**Listed, not flipped: "may" with where/when/upon**:

- `s 664(1) the directors may resolve that the company should be re-registered as a private company`
- `s 703(3) the court may order an immediate inspection`
- `s 706(a) the shares may be held and dealt with in accordance with Chapter 6`
- `s 720(7) the court may order an immediate inspection`
- `s 721(1) the person may apply to the court for the cancellation of the resolution`
- `s 721(3) the court may adjourn the proceedings and give directions and make orders`
- `s 724(3) the company may do it with the shares`
- `s 727(1) the company may dispose of the shares in that way`
- `s 729(1) the company may cancel the shares`

**Listed, not flipped: "entitled"**:

- `s 664(6) the registrar may accept the statement as sufficient evidence that the company is entitled to be re-registered`
- `s 721(2)(b) the application may be made on behalf of the persons entitled by the person`

Assertions restated by the flips: 26 (18 in the layer-1 tests, 8 in `coa15-cases-seat.l4`), each in place with a `-- RECONCILED 2026-11-12: was ...` comment above it. The facts do not change; the expected value changes from `JUST FALSE` to `NOTHING`. `s 694(1)`, which asks whether a purchase is authorised under s 693A, now takes that fact as its own input and no longer reads the answer of `s 693A(1)`, so that a failed s 693A gate is still the text's "only" no there; its assertions are unchanged.

## What the stable binary does not accept

Each item below was met while writing this encoding, on `l4 1.6.110`, and either fixed in the source or worked around.

- **`AFTER` in a deontic is rejected** (parse error "unexpected AFTER", probed with a one-line module). A lower edge of a period therefore lives in the decision function (for example `s 716(2) the resolution was passed in time` tests both ends), and the deontic carries only the `WITHIN` bound.
- **A `DEONTIC` cannot be compared with `EQUALS`** (probed: "Trying to check equality on types that do not support it"). Every regulative rule is therefore exercised by `#TRACE`, and `work/trace-expect.py` checks the outcome of each trace against the `-- expect: FULFILLED | BREACH | RESIDUAL` comment above it. The same duty is also encoded as a decision function, which `#ASSERT` can test.
- **A permission (`MAY`) whose deadline passes unexercised ends `FULFILLED`, whatever its `LEST BREACH` says** (probed on both 1.6.110 and 1.6.109: `MAY ... WITHIN 3 ... LEST BREACH BY ...`, waited to day 9, result `FULFILLED`). A permission is not a duty, so no breach is asserted for it; every `MAY` in the encoding is also a decision function over the facts, and no test relies on the `LEST` branch.
- **`JUST Penalty WITH ...` does not parse**; the penalty is written positionally, `JUST (Penalty OF how, imprisonment, fine, daily fine, both)`, with a ruler comment above each use.
- **There is no `MIN` builtin**; the lower of two amounts is an `IF ... AT MOST ...`.
- **Prelude and library names are taken as they are** (`add months`, `add years`, `DATE PLUS n`, `Day date`). `add months` clamps to the last day of the month (31 January plus one month is 28 February), and a negative number of months works.
- **Every `NOT` is parenthesised, and every `#ASSERT` is on one line**, as PLAN.md section 5 asks.
- **`REFUSE "reason"`, `#ASSERT REFUSED` and `YMD y m d` are accepted by `1.6.110`** (probed with one-line modules; the main build `1.6.109` was not probed for them), but the brief and PLAN.md say the stable binary does not have them, so none is used: "not covered" is `NOTHING` or a named constructor, and dates are written `Date day month year`.
- **PLAN.md section 5 also lists** `BECAUSE` (except in `LEST BREACH BY ... BECAUSE`), sets, `TYPICALLY`, opaque `DECLARE` and section `GIVEN`. This encoding uses none of them, and was not tested against them.
- **Two functions that share a name are not safe**: three pairs (a decision function and the deontic of the same duty) compiled on both builds, but they were renamed (`... the company's duty to give notice to the registrar ...`) so that no name is defined twice.

## What check.sh printed

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa15-cases-seat.l4                            0       575       0        0         0 |      0       575       0        0  same
coa15-ch1.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch2.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch3.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch4.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch5.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch6.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-ch7.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa15-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa15-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa15-tests-ch1.l4                             0       285       0        0         0 |      0       285       0        0  same
coa15-tests-ch2.l4                             0       141       0        0         0 |      0       141       0        0  same
coa15-tests-ch3.l4                             0        84       0        0         0 |      0        84       0        0  same
coa15-tests-ch4.l4                             0       345       0        0         0 |      0       345       0        0  same
coa15-tests-ch5.l4                             0       297       0        0         0 |      0       297       0        0  same
coa15-tests-ch6.l4                             0       129       0        0         0 |      0       129       0        0  same
coa15-tests-ch7.l4                             0        68       0        0         0 |      0        68       0        0  same
TOTAL (19 modules)                             0      1924       0        0           |      0      1924       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

