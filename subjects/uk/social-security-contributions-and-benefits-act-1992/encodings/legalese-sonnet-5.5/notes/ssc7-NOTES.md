# NOTES -- ssc7 (lines 3718-4330 of `ukpga-1992-4.txt`)

The Social Security Contributions and Benefits Act 1992 (United Kingdom), 1992 c. 4.
Part agent `ssc7`, run `iaw-ssc7`, written 2026-11-04 for the stable binary 1.6.98.
The ranges are Part 12ZC, Statutory shared parental pay (ss 171ZU-171ZZ5), Part 12ZD, Statutory parental bereavement pay (ss 171ZZ6-171ZZ15), Part 12ZE, Statutory neonatal care pay (ss 171ZZ16-171ZZ24) and Part XIIA, Incapacity for work (ss 171A-171G).

**The text is a converter rendering.**
The source file `ukpga-1992-4.txt` is a plain-text rendering made by a converter script; it is not the official text, and nothing in these files is verified against the official text.
Every quotation in the `.l4` files was copied mechanically from that file (`-- src:N | ...` lines, built by `work/build.py` from `@@Q a b` placeholders), so the converter's slips are carried into the quotations (finding 12).

**Status, and how each claim was checked (2026-11-04).**

| claim | how it was checked |
| --- | --- |
| every module and test file checks and runs with no `DiagnosticSeverity_Error` or `_Warning` | `l4-stable-98 check` and `run` on each of the 10 `ssc7-*.l4` files, counting those strings and the two layout messages `is at the end of the file` and `follows code on its line`: 0 in every file |
| all assertions are satisfied, none failed, none refused | `check.sh` (pasted in the section "What `check.sh` prints" below): 978 satisfied, 0 failed, 0 refused, 0 errors, and the same four counts on the main build 1.6.108 for every module |
| written assertions equal satisfied assertions | `grep -c '^#ASSERT'` on each test file against the `check.sh` column: 353, 164, 147, 173 and 141 (cases), equal |
| the source locators are right | `python3 -I srcrefs.py check --refs` and `--strict` over all `ssc7-*.l4`: 449 `src:` lines, 182 runs, 182 locators, 0 problems |
| every "no" quotes the text | `work/check_false_quotes.py` normalises quote marks, dashes and spaces, splits each `FALSE-kind` comment's quoted words at `...`, and looks every piece up in lines 3718-4330 of the raw text: 78 `FALSE-kind` branches, 95 quoted pieces, 0 not found. (It found 4 composed quotations on its first run; they were rewritten as separate quoted pieces.) |
| the three regulative rules run the same on both binaries | the `#TRACE` of `s 171ZX(1)`, `s 171ZZ8(1)` and `s 171ZZ18(1)` prints `FULFILLED` on `l4-stable-98` and on `l4-main-108`; `check.sh` does not see a `#TRACE` outcome, so this was compared by hand |
| every line of the ranges is in a coverage row | `work/coverage.py` (below): 613 non-blank lines, 613 in some row, 0 missing |

Nothing is claimed beyond that.
In particular no test was written by a lawyer, the expected values are my reading of the text, and the "for a lawyer" readings in the section below are flagged and not decided.

**Where PLAN and the brief differ, and what I took.**

1. The brief says every provision of the ranges is encoded, with its conditions and arithmetic (its "whole" ruling of 2026-10-22).
   `inputs/PLAN.md` (the `ssc7` entry, lines 259-266) says what `ssc7` holds, asks and answers; it does not say how deep to encode ss 171ZU and 171ZV, which it names only as the askers of seams S27 and S28.
   Where PLAN is silent I took the brief: ss 171ZU and 171ZV are encoded in full, conditions, caps and counting rules.
2. PLAN lists `ssc7` as asking S24, S25, S27, S28, S29 and S30 and as answering S35.
   It does not list S26, the lower earnings limit of s 5(1)(a), for `ssc7` (it lists it for ss 164 and 171ZA); ss 171ZU, 171ZV, 171ZZ6 and 171ZZ16 need it, so `ssc7` takes S26 as an input too (Seams, below).
3. PLAN lists S25 for s 171ZZ3 (line 3967) and s 171ZZ13 (line 4089).
   Line 4216, s 171ZZ23(1)(c), says the same words ("continental shelf operations, as defined in section 120(2)"), so s 171ZZ23 asks S25 as well.
4. PLAN lists S30 as four `relevant week` seams (`s 164`, `s 171ZA(2)`, `s 171ZB(2)`, `s 171ZL(2)`).
   The text of s 171ZZ16(6)(a) defines its own relevant week from "the expected week of confinement (within the meaning of Part 12)", so `ssc7` asks the expected week of confinement and does not use `s 164 the relevant week`; it does take the other three.
5. The `employer` definition of ss 171ZZ4(1), 171ZZ14(1) and 171ZZ24(1) turns on s 6 (liability for secondary Class 1 contributions).
   PLAN lists no seam for that; `ssc7` takes three yes/no inputs named `s 6 ...` (Seams, below).
6. The brief points to "PLAN.md section 8" for the seams, and to PLAN sections 2, 3, 5 to 8, 11 and 12 for the rules.
   The copy of `PLAN.md` in `inputs/` numbers only sections 1 to 5, then "Not seams, though they look like one" and an appendix: rules in section 1, the core in section 2, the keel's answers in section 3, the parts in section 4, the seam register in section 5.
   I read the seam register as section 5 and the rules as section 1.

The sections the brief asks for follow, each suffixed (ssc7), and then the numbered findings, what the stable binary does not accept, what `check.sh` prints, the files, and how to rebuild.

## Coverage (ssc7)

Built by `work/coverage.py` from the text itself: one row per section, subsection, paragraph, defined term and heading of lines 3718-4330, each with exactly one disposition and the L4 name that carries it (or the reason it is inert).

**Audit (script output, 2026-11-04):** 613 non-blank lines in 3718-4330; 613 in some row; 0 missing; 584 rows before the audit and 584 after (the audit found no line outside a row, so it added none); 0 problems.

**Counts by disposition (584 rows):** encoded 368; fork 18; inert 1 (not operative: the 41 Part and section headings) 41; inert 2 (machinery: regulation-making powers and what regulations may contain) 157; inert 3 (text shown repealed or blank) 0; repealed or blank in this text 0.  No row is `out-of-scope` or `deferred`.

How to read the table.
- **encoded**: a rule, definition or table in a layer-1 module, tested, with `@ref` to the lines in the "lines" column; a row whose name column begins "intro words" is the lead-in of a list whose paragraphs are the rows below it.
- **fork Fn**: the text reads two or more ways; the row points to the fork register and to the rule that carries the chosen reading (or the explicit "not covered" value).
- **inert 1**: a heading, which creates no rule.
- **inert 2**: a power or duty to make regulations (and the paragraphs that list what regulations may contain), which has no consequence for a person until regulations are made.  Where a power has a consequence a module reads, either the power itself is an *encoded* row with a gate input (s 171ZW(1)(a) and s 171ZZ3(1) are), or the power is an inert row and its effect is the gate input of an encoded row (the power of s 171B(8) is inert; its effect on the 4 days and 8 weeks is the gate of the s 171B(3) rows).
- Rows for the `employer`, `local authority` and other definitions of ss 171ZZ4(1), 171ZZ14(1) and 171ZZ24(1) are separate rows per defined term.

| row | lines | disposition | L4 name or reason |
|---|---|---|---|
| Part 12ZC | 3718-3718 | inert 1 | heading: no rule of its own |
| s 171ZU | 3719-3719 | inert 1 | heading: no rule of its own |
| s 171ZU(1) | 3720-3720 | fork F1 | s 171ZU(1) the claimant mother is entitled to statutory shared parental pay |
| s 171ZU(2) | 3721-3721 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(a) @3722 | 3722-3722 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(b) @3723 | 3723-3723 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(i) @3724 | 3724-3724 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(ii) @3725 | 3725-3725 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(iii) @3726 | 3726-3726 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(c) @3727 | 3727-3727 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(d) @3728 | 3728-3728 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(e) @3729 | 3729-3729 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(f) @3730 | 3730-3730 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(g) @3731 | 3731-3731 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(h) @3732 | 3732-3732 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(i) @3733 | 3733-3733 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(i) @3734 | 3734-3734 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(ii) @3735 | 3735-3735 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(iii) @3736 | 3736-3736 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(j) @3737 | 3737-3737 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(k) @3738 | 3738-3738 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(i) @3739 | 3739-3739 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(ii) @3740 | 3740-3740 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(l) @3741 | 3741-3741 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(m) @3742 | 3742-3742 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(n) @3743 | 3743-3743 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(2)(o) @3744 | 3744-3744 | encoded | s 171ZU(2) all the conditions are satisfied |
| s 171ZU(3) | 3745-3745 | fork F1 | s 171ZU(3) the claimant is entitled to statutory shared parental pay |
| s 171ZU(4) | 3746-3746 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(a) @3747 | 3747-3747 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(b) @3748 | 3748-3748 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3749 | 3749-3749 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(ii) @3750 | 3750-3750 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(c) @3751 | 3751-3751 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3752 | 3752-3752 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(ii) @3753 | 3753-3753 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(d) @3754 | 3754-3754 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(e) @3755 | 3755-3755 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(f) @3756 | 3756-3756 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(g) @3757 | 3757-3757 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(h) @3758 | 3758-3758 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3759 | 3759-3759 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(ii) @3760 | 3760-3760 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3761 | 3761-3761 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3762 | 3762-3762 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(ii) @3763 | 3763-3763 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(j) @3764 | 3764-3764 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3765 | 3765-3765 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(ii) @3766 | 3766-3766 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(iii) @3767 | 3767-3767 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(k) @3768 | 3768-3768 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(l) @3769 | 3769-3769 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(i) @3770 | 3770-3770 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(ii) @3771 | 3771-3771 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(m) @3772 | 3772-3772 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(n) @3773 | 3773-3773 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(o) @3774 | 3774-3774 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(4)(p) @3775 | 3775-3775 | encoded | s 171ZU(4) all the conditions are satisfied |
| s 171ZU(5) | 3776-3776 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZU(5)(a) @3777 | 3777-3777 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZU(5)(b) @3778 | 3778-3778 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZU(6) | 3779-3779 | fork F2 | s 171ZU(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZU(6)(a) @3780 | 3780-3780 | encoded | s 171ZU(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZU(6)(i) @3781 | 3781-3781 | encoded | s 171ZU(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZU(6)(ii) @3782 | 3782-3782 | encoded | s 171ZU(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZU(6)(b) @3783 | 3783-3783 | encoded | s 171ZU(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZU(7) | 3784-3784 | fork F13 | s 171ZU(7)(a) the number of relevant weeks of maternity allowance; s 171ZU(7)(b) the number of relevant weeks of statutory maternity pay |
| s 171ZU(7)(a) @3785 | 3785-3785 | encoded | s 171ZU(7)(a) the number of relevant weeks of maternity allowance; s 171ZU(7)(b) the number of relevant weeks of statutory maternity pay |
| s 171ZU(7)(b) @3786 | 3786-3787 | encoded | s 171ZU(7)(a) the number of relevant weeks of maternity allowance; s 171ZU(7)(b) the number of relevant weeks of statutory maternity pay |
| s 171ZU(8) | 3788-3788 | encoded | s 171ZU(8) the number of weeks counting a part of a week as a week |
| s 171ZU(8)(a) @3789 | 3789-3789 | encoded | s 171ZU(8) the number of weeks counting a part of a week as a week |
| s 171ZU(8)(b) @3790 | 3790-3790 | encoded | s 171ZU(8) the number of weeks counting a part of a week as a week |
| s 171ZU(9) | 3791-3791 | encoded | s 171ZU(9) the two entitlements together are within what is available to one person |
| s 171ZU(10) | 3792-3792 | encoded | s 171ZU(10) a payment may be made in respect of the child |
| s 171ZU(11) | 3793-3793 | encoded | s 171ZU(11) a payment may be made to the mother |
| s 171ZU(12) | 3794-3794 | encoded | s 171ZU(12) V may vary the period or periods |
| s 171ZU(13) | 3795-3795 | encoded | s 171ZU(13) the conditions for varying the period or periods are satisfied |
| s 171ZU(13)(a) @3796 | 3796-3796 | encoded | s 171ZU(13) the conditions for varying the period or periods are satisfied |
| s 171ZU(13)(b) @3797 | 3797-3797 | encoded | s 171ZU(13) the conditions for varying the period or periods are satisfied |
| s 171ZU(13)(i) @3798 | 3798-3798 | encoded | s 171ZU(13) the conditions for varying the period or periods are satisfied |
| s 171ZU(13)(ii) @3799 | 3799-3799 | encoded | s 171ZU(13) the conditions for varying the period or periods are satisfied |
| s 171ZU(14) | 3800-3800 | encoded | s 171ZU(14) V may vary the number of weeks |
| s 171ZU(15) | 3801-3801 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(a) @3802 | 3802-3802 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(i) @3803 | 3803-3803 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(ii) @3804 | 3804-3804 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(iii) @3805 | 3805-3805 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(iv) @3806 | 3806-3806 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(b) @3807 | 3807-3807 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(i) @3808 | 3808-3808 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(ii) @3809 | 3809-3809 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(15)(c) @3810 | 3810-3810 | encoded | s 171ZU(15) the conditions for varying the number of weeks are satisfied |
| s 171ZU(16) | 3811-3811 | encoded | s 171ZU(16) the entitlement after the birth of more than one child |
| s 171ZV | 3812-3812 | inert 1 | heading: no rule of its own |
| s 171ZV(1) | 3813-3813 | fork F1 | s 171ZV(1) claimant A is entitled to statutory shared parental pay |
| s 171ZV(2) | 3814-3814 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(a) @3815 | 3815-3815 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(b) @3816 | 3816-3816 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(i) @3817 | 3817-3817 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(ii) @3818 | 3818-3818 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(iii) @3819 | 3819-3819 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(c) @3820 | 3820-3820 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(d) @3821 | 3821-3821 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(e) @3822 | 3822-3822 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(f) @3823 | 3823-3823 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(g) @3824 | 3824-3824 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(h) @3825 | 3825-3825 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(i) @3826 | 3826-3826 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(i) @3827 | 3827-3827 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(ii) @3828 | 3828-3828 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(iii) @3829 | 3829-3829 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(j) @3830 | 3830-3830 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(k) @3831 | 3831-3831 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(i) @3832 | 3832-3832 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(ii) @3833 | 3833-3833 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(l) @3834 | 3834-3834 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(m) @3835 | 3835-3835 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(n) @3836 | 3836-3836 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(2)(o) @3837 | 3837-3837 | encoded | s 171ZV(2) all the conditions are satisfied |
| s 171ZV(3) | 3838-3838 | fork F1 | s 171ZV(3) claimant B is entitled to statutory shared parental pay |
| s 171ZV(4) | 3839-3839 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(a) @3840 | 3840-3840 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(b) @3841 | 3841-3841 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(i) @3842 | 3842-3842 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(ii) @3843 | 3843-3843 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(c) @3844 | 3844-3844 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(i) @3845 | 3845-3845 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(ii) @3846 | 3846-3846 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(d) @3847 | 3847-3847 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(e) @3848 | 3848-3848 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(f) @3849 | 3849-3849 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(g) @3850 | 3850-3850 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(h) @3851 | 3851-3851 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(i) @3852 | 3852-3852 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(j) @3853 | 3853-3853 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(i) @3854 | 3854-3854 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(ii) @3855 | 3855-3855 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(iii) @3856 | 3856-3856 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(k) @3857 | 3857-3857 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(l) @3858 | 3858-3858 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(i) @3859 | 3859-3859 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(ii) @3860 | 3860-3860 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(m) @3861 | 3861-3861 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(n) @3862 | 3862-3862 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(o) @3863 | 3863-3863 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(4)(p) @3864 | 3864-3864 | encoded | s 171ZV(4) all the conditions are satisfied |
| s 171ZV(5) | 3865-3865 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZV(5)(a) @3866 | 3866-3866 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZV(5)(b) @3867 | 3867-3867 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZV(6) | 3868-3868 | encoded | s 171ZV(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZV(6)(a) @3869 | 3869-3869 | encoded | s 171ZV(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZV(6)(i) @3870 | 3870-3870 | encoded | s 171ZV(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZV(6)(ii) @3871 | 3871-3871 | encoded | s 171ZV(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZV(6)(b) @3872 | 3872-3872 | encoded | s 171ZV(6) the greatest number of weeks of statutory shared parental pay |
| s 171ZV(7) | 3873-3873 | encoded | s 171ZV(7) the number of relevant weeks of statutory adoption pay |
| s 171ZV(8) | 3874-3874 | encoded | s 171ZV(8) the number of weeks counting a part of a week as a week |
| s 171ZV(8)(a) @3875 | 3875-3875 | encoded | s 171ZV(8) the number of weeks counting a part of a week as a week |
| s 171ZV(8)(b) @3876 | 3876-3876 | encoded | s 171ZV(8) the number of weeks counting a part of a week as a week |
| s 171ZV(9) | 3877-3877 | encoded | s 171ZV(9) the two entitlements together are within what is available to one person |
| s 171ZV(10) | 3878-3878 | encoded | s 171ZV(10) a payment may be made in respect of the child |
| s 171ZV(11) | 3879-3879 | encoded | s 171ZV(11) a payment may be made to the person who became entitled to statutory adoption pay |
| s 171ZV(12) | 3880-3880 | encoded | s 171ZV(12) V may vary the period or periods |
| s 171ZV(13) | 3881-3881 | encoded | s 171ZV(13) the conditions for varying the period or periods are satisfied |
| s 171ZV(13)(a) @3882 | 3882-3882 | encoded | s 171ZV(13) the conditions for varying the period or periods are satisfied |
| s 171ZV(13)(b) @3883 | 3883-3883 | encoded | s 171ZV(13) the conditions for varying the period or periods are satisfied |
| s 171ZV(13)(i) @3884 | 3884-3884 | encoded | s 171ZV(13) the conditions for varying the period or periods are satisfied |
| s 171ZV(13)(ii) @3885 | 3885-3885 | encoded | s 171ZV(13) the conditions for varying the period or periods are satisfied |
| s 171ZV(14) | 3886-3886 | encoded | s 171ZV(14) V may vary the number of weeks |
| s 171ZV(15) | 3887-3887 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(a) @3888 | 3888-3888 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(i) @3889 | 3889-3889 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(ii) @3890 | 3890-3890 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(iii) @3891 | 3891-3891 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(iv) @3892 | 3892-3892 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(b) @3893 | 3893-3893 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(i) @3894 | 3894-3894 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(ii) @3895 | 3895-3895 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(15)(c) @3896 | 3896-3896 | encoded | s 171ZV(15) the conditions for varying the number of weeks are satisfied |
| s 171ZV(16) | 3897-3897 | encoded | s 171ZV(16) the entitlement after the placement for adoption of more than one child |
| s 171ZV(17) | 3898-3898 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZV(17)(a) @3899 | 3899-3899 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZV(17)(b) @3900 | 3900-3901 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZV(18) | 3902-3902 | encoded | s 171ZV(18) the placement counts as a placement for adoption |
| s 171ZV(18)(a) @3903 | 3903-3903 | encoded | s 171ZV(18) the placement counts as a placement for adoption |
| s 171ZV(18)(b) @3904 | 3904-3904 | encoded | s 171ZV(18) the placement counts as a placement for adoption |
| s 171ZW | 3905-3905 | inert 1 | heading: no rule of its own |
| s 171ZW(1) | 3906-3906 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(a) @3907 | 3907-3907 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(i) @3908 | 3908-3908 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(ii) @3909 | 3909-3909 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(iii) @3910 | 3910-3910 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(iv) @3911 | 3911-3911 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(v) @3912 | 3912-3912 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(vi) @3913 | 3913-3913 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(vii) @3914 | 3914-3914 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(viii) @3915 | 3915-3915 | encoded | s 171ZW(1)(a) the condition has effect in the case |
| s 171ZW(1)(b) @3916 | 3916-3916 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(c) @3917 | 3917-3917 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(d) @3918 | 3918-3918 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(i) @3919 | 3919-3919 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(ii) @3920 | 3920-3920 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(e) @3921 | 3921-3921 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(f) @3922 | 3922-3922 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(i) @3923 | 3923-3923 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(1)(ii) @3924 | 3924-3925 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZW(2) | 3926-3926 | encoded | s 171ZW(2) requirements about evidence and procedure may be imposed on the person |
| s 171ZW(2)(a) @3927 | 3927-3927 | encoded | s 171ZW(2) requirements about evidence and procedure may be imposed on the person |
| s 171ZW(2)(b) @3928 | 3928-3928 | encoded | s 171ZW(2) requirements about evidence and procedure may be imposed on the person |
| s 171ZW(3) | 3929-3929 | encoded | s 171ZW(3) the prescribed period in weeks |
| s 171ZX | 3930-3930 | inert 1 | heading: no rule of its own |
| s 171ZX(1) | 3931-3931 | encoded | s 171ZX(1) the person is liable to make payments of statutory shared parental pay; s 171ZX(1) the duty to make the payments |
| s 171ZX(2) | 3932-3932 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZX(3) | 3933-3933 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZY | 3934-3934 | inert 1 | heading: no rule of its own |
| s 171ZY(1) | 3935-3935 | encoded | s 171ZY(1) the weekly rate of statutory shared parental pay in pounds |
| s 171ZY(2) | 3936-3936 | encoded | s 171ZY(2) statutory shared parental pay is payable for the week |
| s 171ZY(3) | 3937-3937 | encoded | s 171ZY(3) the pay is payable for the week despite the intention to care |
| s 171ZY(3)(a) @3938 | 3938-3938 | encoded | s 171ZY(3) the pay is payable for the week despite the intention to care |
| s 171ZY(3)(b) @3939 | 3939-3939 | encoded | s 171ZY(3) the pay is payable for the week despite the intention to care |
| s 171ZY(4) | 3940-3940 | encoded | s 171ZY(4) the pay is payable for the week despite work for an employer |
| s 171ZY(5) | 3941-3941 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZY(6) | 3942-3942 | encoded | s 171ZY(6) the daily rate in pounds |
| s 171ZY(7) | 3943-3943 | fork F9 | s 171ZY(7) the week falls within a relevant period |
| s 171ZY(7)(a) @3944 | 3944-3944 | encoded | s 171ZY(7) the week falls within a relevant period |
| s 171ZY(7)(b) @3945 | 3945-3946 | encoded | s 171ZY(7) the week falls within a relevant period |
| s 171ZY(8) | 3947-3947 | encoded | s 171ZY(8) the week of the relevant period containing the day |
| s 171ZZ | 3948-3948 | inert 1 | heading: no rule of its own |
| s 171ZZ(1) | 3949-3949 | encoded | s 171ZZ(1) the agreement is void to that extent |
| s 171ZZ(1)(a) @3950 | 3950-3950 | encoded | s 171ZZ(1) the agreement is void to that extent |
| s 171ZZ(1)(b) @3951 | 3951-3951 | encoded | s 171ZZ(1) the agreement is void to that extent |
| s 171ZZ(2) | 3952-3952 | encoded | s 171ZZ(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ(2)(a) @3953 | 3953-3953 | encoded | s 171ZZ(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ(2)(b) @3954 | 3954-3954 | encoded | s 171ZZ(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ1 | 3955-3955 | inert 1 | heading: no rule of its own |
| s 171ZZ1(1) | 3956-3956 | encoded | s 171ZZ1(1) the entitlement affects the person's right to contractual remuneration |
| s 171ZZ1(2) | 3957-3957 | encoded | intro words; encoded in the rows below: s 171ZZ1(2)(a) the liability to pay statutory shared parental pay that remains; s 171ZZ1(2)(b) the liability to pay contractual remuneration that remains |
| s 171ZZ1(2)(a) @3958 | 3958-3958 | encoded | s 171ZZ1(2)(a) the liability to pay statutory shared parental pay that remains |
| s 171ZZ1(2)(b) @3959 | 3959-3959 | encoded | s 171ZZ1(2)(b) the liability to pay contractual remuneration that remains |
| s 171ZZ1(3) | 3960-3960 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ2 | 3961-3961 | inert 1 | heading: no rule of its own |
| s 171ZZ2 text | 3962-3962 | encoded | s 171ZZ2 the provisions of this Part apply to the person |
| s 171ZZ3 | 3963-3963 | inert 1 | heading: no rule of its own |
| s 171ZZ3(1) | 3964-3964 | encoded | s 171ZZ3(1) regulations may modify this Part in its application to the person |
| s 171ZZ3(1)(a) @3965 | 3965-3965 | encoded | s 171ZZ3(1) regulations may modify this Part in its application to the person |
| s 171ZZ3(1)(b) @3966 | 3966-3966 | encoded | s 171ZZ3(1) regulations may modify this Part in its application to the person |
| s 171ZZ3(1)(c) @3967 | 3967-3967 | encoded | s 171ZZ3(1) regulations may modify this Part in its application to the person |
| s 171ZZ3(2) | 3968-3968 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ3(2)(a) @3969 | 3969-3969 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ3(2)(b) @3970 | 3970-3970 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ3(2)(c) @3971 | 3971-3971 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ3(2)(d) @3972 | 3972-3972 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4 | 3973-3973 | inert 1 | heading: no rule of its own |
| s 171ZZ4(1) | 3974-3974 | encoded | intro words; encoded in the rows below: s 171ZZ4(1) adoption pay period; s 171ZZ4(1) the person is the employer of the employee |
| s 171ZZ4(1) “adoption pay period” | 3975-3975 | encoded | s 171ZZ4(1) adoption pay period |
| s 171ZZ4(1) “employer” | 3976-3980 | encoded | s 171ZZ4(1) the person is the employer of the employee |
| s 171ZZ4(1) “local authority” | 3981-3981 | encoded | s 171ZZ4(1) the body is a local authority |
| s 171ZZ4(1) “local authority foster parent” | 3982-3982 | encoded | s 171ZZ4(1) the person is a local authority foster parent |
| s 171ZZ4(1) “maternity allowance period” | 3983-3983 | encoded | s 171ZZ4(1) maternity allowance period |
| s 171ZZ4(1) “maternity pay period” | 3984-3984 | encoded | s 171ZZ4(1) maternity pay period |
| s 171ZZ4(1) “modifications” | 3985-3985 | encoded | s 171ZZ4(1) the change is a modification |
| s 171ZZ4(1) “prescribed” | 3986-3986 | encoded | s 171ZZ4(1) the matter is prescribed |
| s 171ZZ4(2) | 3987-3987 | fork F4 | s 171ZZ4(2) the person is an employee |
| s 171ZZ4(3) | 3988-3988 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ4(3)(a) @3989 | 3989-3989 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(3)(b) @3990 | 3990-3990 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(4) | 3991-3991 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ4(4)(a) @3992 | 3992-3992 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(4)(b) @3993 | 3993-3993 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(5) | 3994-3994 | encoded | s 171ZZ4(5) the week convention; s 171ZZ4(5) the first day of the week containing the day |
| s 171ZZ4(6) | 3995-3995 | encoded | s 171ZZ4(6) the person's normal weekly earnings in pounds |
| s 171ZZ4(7) | 3996-3996 | encoded | s 171ZZ4(6) the person's normal weekly earnings in pounds |
| s 171ZZ4(8) | 3997-3997 | encoded | s 171ZZ4(6) the person's normal weekly earnings in pounds |
| s 171ZZ4(9) | 3998-3998 | inert 2 | machinery: a power to make regulations (the election, or statutory declarations) |
| s 171ZZ4(9)(a) @3999 | 3999-3999 | inert 2 | machinery: what the regulations may provide or prescribe |
| s 171ZZ4(9)(b) @4000 | 4000-4000 | inert 2 | machinery: what the regulations may provide or prescribe |
| s 171ZZ4(9) sentence @4001 | 4001-4001 | inert 2 | machinery: a statement of what regulations may contain |
| s 171ZZ4(10) | 4002-4002 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ4(10)(a) @4003 | 4003-4003 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(10)(b) @4004 | 4004-4004 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(10)(c) @4005 | 4005-4005 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(10)(d) @4006 | 4006-4006 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(10)(e) @4007 | 4007-4007 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(10)(f) @4008 | 4008-4008 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ4(11) | 4009-4009 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ4(12) | 4010-4010 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ5 | 4011-4011 | inert 1 | heading: no rule of its own |
| s 171ZZ5(1) | 4012-4012 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ5(2) | 4013-4013 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ5(3) | 4014-4014 | inert 2 | machinery: a power to make regulations (the election, or statutory declarations) |
| s 171ZZ5(3)(a) @4015 | 4015-4015 | inert 2 | machinery: what the regulations may provide or prescribe |
| s 171ZZ5(3)(b) @4016 | 4016-4016 | inert 2 | machinery: what the regulations may provide or prescribe |
| Part 12ZD | 4017-4017 | inert 1 | heading: no rule of its own |
| s 171ZZ6 | 4018-4018 | inert 1 | heading: no rule of its own |
| s 171ZZ6(1) | 4019-4019 | encoded | s 171ZZ6(1) the person is entitled to statutory parental bereavement pay |
| s 171ZZ6(2) | 4020-4020 | encoded | s 171ZZ6(2) the person satisfies the conditions |
| s 171ZZ6(2)(a) @4021 | 4021-4021 | encoded | s 171ZZ6(2) the person satisfies the conditions; s 171ZZ6(2)(a) the person is a bereaved parent |
| s 171ZZ6(2)(b) @4022 | 4022-4022 | encoded | s 171ZZ6(2) the person satisfies the conditions; s 171ZZ6(2)(b) the person has been in employment for at least 26 weeks |
| s 171ZZ6(2)(c) @4023 | 4023-4023 | encoded | s 171ZZ6(2) the person satisfies the conditions; s 171ZZ6(2)(c) the person was entitled to be in that employment |
| s 171ZZ6(2)(d) @4024 | 4024-4024 | encoded | s 171ZZ6(2) the person satisfies the conditions; s 171ZZ6(2)(d) the normal weekly earnings are not less than the lower earnings limit |
| s 171ZZ6(2)(e) @4025 | 4025-4025 | encoded | s 171ZZ6(2) the person satisfies the conditions; s 171ZZ6(2)(e) the person has been in the employment from the end of the relevant week to the day the child dies |
| s 171ZZ6(3) | 4026-4026 | encoded | s 171ZZ6(3) the employee is a bereaved parent |
| s 171ZZ6(4) | 4027-4027 | inert 2 | machinery: a statement of what regulations may contain |
| s 171ZZ6(5) | 4028-4028 | encoded | s 171ZZ6(5) the relevant week; s 171ZZ6(5) the last day of the relevant week |
| s 171ZZ6(6) | 4029-4029 | encoded | s 171ZZ6(6) the number of children in respect of whom the person is entitled |
| s 171ZZ6(7) | 4030-4030 | encoded | s 171ZZ6(7) paragraph (c) of subsection (2) is omitted |
| s 171ZZ7 | 4031-4031 | inert 1 | heading: no rule of its own |
| s 171ZZ7(1) | 4032-4032 | encoded | s 171ZZ7(1) the person is entitled to payments for the weeks |
| s 171ZZ7(2) | 4033-4033 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ7(3) | 4034-4034 | encoded | s 171ZZ7(3) the notice satisfies the requirement as to writing |
| s 171ZZ7(4) | 4035-4035 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ7(4)(a) @4036 | 4036-4036 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(b) @4037 | 4037-4037 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(c) @4038 | 4038-4038 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(d) @4039 | 4039-4039 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(e) @4040 | 4040-4040 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(f) @4041 | 4041-4041 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(i) @4042 | 4042-4042 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(ii) @4043 | 4043-4043 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(g) @4044 | 4044-4044 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(h) @4045 | 4045-4045 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(i) @4046 | 4046-4046 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ7(4)(ii) @4047 | 4047-4048 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ8 | 4049-4049 | inert 1 | heading: no rule of its own |
| s 171ZZ8(1) | 4050-4050 | encoded | s 171ZZ8(1) the person is liable to make payments of statutory parental bereavement pay; s 171ZZ8(1) the duty to make the payments |
| s 171ZZ8(2) | 4051-4051 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ8(3) | 4052-4052 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ9 | 4053-4053 | inert 1 | heading: no rule of its own |
| s 171ZZ9(1) | 4054-4054 | encoded | s 171ZZ9(1) the weekly rate of statutory parental bereavement pay in pounds |
| s 171ZZ9(2) | 4055-4055 | encoded | s 171ZZ9(2) the pay payable for the weeks chosen in pounds |
| s 171ZZ9(2)(a) @4056 | 4056-4056 | encoded | s 171ZZ9(2) the pay payable for the weeks chosen in pounds |
| s 171ZZ9(2)(b) @4057 | 4057-4058 | encoded | s 171ZZ9(2) the pay payable for the weeks chosen in pounds |
| s 171ZZ9(3) | 4059-4059 | encoded | s 171ZZ9(3) the prescribed number of weeks is allowed |
| s 171ZZ9(4) | 4060-4060 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ9(5) | 4061-4061 | fork F12 | s 171ZZ9(5) the qualifying period is allowed |
| s 171ZZ9(6) | 4062-4062 | encoded | s 171ZZ9(6) the person is liable to pay for the statutory pay week |
| s 171ZZ9(7) | 4063-4063 | encoded | s 171ZZ9(7) the person is liable to pay for the statutory pay week whether or not the contract existed before |
| s 171ZZ9(8) | 4064-4064 | encoded | s 171ZZ9(8) the pay is payable for the statutory pay week |
| s 171ZZ9(9) | 4065-4065 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ9(10) | 4066-4066 | encoded | s 171ZZ9(10) the daily rate in pounds |
| s 171ZZ9(11) | 4067-4069 | encoded | s 171ZZ9(11) the period is a week; s 171ZZ9(11) the period is a statutory pay week; s 171ZZ9(11) the week convention |
| s 171ZZ10 | 4070-4070 | inert 1 | heading: no rule of its own |
| s 171ZZ10(1) | 4071-4071 | encoded | s 171ZZ10(1) the agreement is void to that extent |
| s 171ZZ10(1)(a) @4072 | 4072-4072 | encoded | s 171ZZ10(1) the agreement is void to that extent |
| s 171ZZ10(1)(b) @4073 | 4073-4073 | encoded | s 171ZZ10(1) the agreement is void to that extent |
| s 171ZZ10(2) | 4074-4074 | encoded | s 171ZZ10(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ10(2)(a) @4075 | 4075-4075 | encoded | s 171ZZ10(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ10(2)(b) @4076 | 4076-4076 | encoded | s 171ZZ10(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ11 | 4077-4077 | inert 1 | heading: no rule of its own |
| s 171ZZ11(1) | 4078-4078 | encoded | s 171ZZ11(1) the entitlement affects the person's right to contractual remuneration |
| s 171ZZ11(2) | 4079-4079 | encoded | intro words; encoded in the rows below: s 171ZZ11(2)(a) the liability to pay statutory parental bereavement pay that remains; s 171ZZ11(2)(b) the liability to pay contractual remuneration that remains |
| s 171ZZ11(2)(a) @4080 | 4080-4080 | encoded | s 171ZZ11(2)(a) the liability to pay statutory parental bereavement pay that remains |
| s 171ZZ11(2)(b) @4081 | 4081-4081 | encoded | s 171ZZ11(2)(b) the liability to pay contractual remuneration that remains |
| s 171ZZ11(3) | 4082-4082 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ12 | 4083-4083 | inert 1 | heading: no rule of its own |
| s 171ZZ12 text | 4084-4084 | encoded | s 171ZZ12 the provisions of this Part apply to the person |
| s 171ZZ13 | 4085-4085 | inert 1 | heading: no rule of its own |
| s 171ZZ13(1) | 4086-4086 | encoded | s 171ZZ13(1) regulations may modify this Part in its application to the person |
| s 171ZZ13(1)(a) @4087 | 4087-4087 | encoded | s 171ZZ13(1) regulations may modify this Part in its application to the person |
| s 171ZZ13(1)(b) @4088 | 4088-4088 | encoded | s 171ZZ13(1) regulations may modify this Part in its application to the person |
| s 171ZZ13(1)(c) @4089 | 4089-4089 | encoded | s 171ZZ13(1) regulations may modify this Part in its application to the person |
| s 171ZZ13(2) | 4090-4090 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ13(2)(a) @4091 | 4091-4091 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ13(2)(b) @4092 | 4092-4092 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ13(2)(c) @4093 | 4093-4093 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ13(2)(d) @4094 | 4094-4094 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14 | 4095-4095 | inert 1 | heading: no rule of its own |
| s 171ZZ14(1) | 4096-4096 | encoded | intro words; encoded in the rows below: s 171ZZ14(1) the person who died was a child; s 171ZZ14(1) the person is the employer of the employee |
| s 171ZZ14(1) “child” | 4097-4097 | encoded | s 171ZZ14(1) the person who died was a child |
| s 171ZZ14(1) “employer” | 4098-4102 | encoded | s 171ZZ14(1) the person is the employer of the employee |
| s 171ZZ14(1) “modifications” | 4103-4103 | encoded | s 171ZZ14(1) the change is a modification |
| s 171ZZ14(1) “prescribed” | 4104-4104 | encoded | s 171ZZ14(1) the matter is prescribed |
| s 171ZZ14(2) | 4105-4105 | fork F4 | s 171ZZ14(2) the person is an employee |
| s 171ZZ14(3) | 4106-4106 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ14(3)(a) @4107 | 4107-4107 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(3)(b) @4108 | 4108-4108 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(4) | 4109-4109 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ14(4)(a) @4110 | 4110-4110 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(4)(b) @4111 | 4111-4111 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(5) | 4112-4112 | encoded | s 171ZZ14(5) the week convention; s 171ZZ14(5) the first day of the week containing the day |
| s 171ZZ14(6) | 4113-4113 | encoded | s 171ZZ14(6) the person's normal weekly earnings in pounds |
| s 171ZZ14(7) | 4114-4114 | encoded | s 171ZZ14(6) the person's normal weekly earnings in pounds |
| s 171ZZ14(8) | 4115-4115 | encoded | s 171ZZ14(6) the person's normal weekly earnings in pounds |
| s 171ZZ14(9) | 4116-4116 | inert 2 | machinery: a power to make regulations (the election, or statutory declarations) |
| s 171ZZ14(10) | 4117-4117 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ14(10)(a) @4118 | 4118-4118 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(10)(b) @4119 | 4119-4119 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(10)(c) @4120 | 4120-4120 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(10)(d) @4121 | 4121-4121 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(10)(e) @4122 | 4122-4122 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(10)(f) @4123 | 4123-4123 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ14(11) | 4124-4124 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ14(12) | 4125-4125 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ15 | 4126-4126 | inert 1 | heading: no rule of its own |
| s 171ZZ15 text | 4127-4127 | encoded | intro words; encoded in the rows below: s 171ZZ15(a) the child stillborn after twenty-four weeks of pregnancy is a child; s 171ZZ15(b) the day taken as the day the child dies |
| s 171ZZ15(a) @4128 | 4128-4128 | fork F3 | s 171ZZ15(a) the child stillborn after twenty-four weeks of pregnancy is a child |
| s 171ZZ15(b) @4129 | 4129-4129 | encoded | s 171ZZ15(b) the day taken as the day the child dies |
| Part 12ZE | 4130-4130 | inert 1 | heading: no rule of its own |
| s 171ZZ16 | 4131-4131 | inert 1 | heading: no rule of its own |
| s 171ZZ16(1) | 4132-4132 | encoded | s 171ZZ16(1) the person is entitled to statutory neonatal care pay |
| s 171ZZ16(2) | 4133-4133 | encoded | s 171ZZ16(2) the conditions are satisfied |
| s 171ZZ16(2)(a) @4134 | 4134-4134 | encoded | s 171ZZ16(2) the conditions are satisfied |
| s 171ZZ16(2)(i) @4135 | 4135-4135 | encoded | s 171ZZ16(2) the conditions are satisfied |
| s 171ZZ16(2)(ii) @4136 | 4136-4136 | fork F11 | s 171ZZ16(2) the conditions are satisfied; s 171ZZ16(2)(a)(ii) the care has continued without interruption for at least seven days |
| s 171ZZ16(2)(b) @4137 | 4137-4137 | encoded | s 171ZZ16(2) the conditions are satisfied; s 171ZZ16(2)(b) the person has been in employment for at least 26 weeks |
| s 171ZZ16(2)(c) @4138 | 4138-4138 | encoded | s 171ZZ16(2) the conditions are satisfied; s 171ZZ16(2)(c) the person was entitled to be in that employment |
| s 171ZZ16(2)(d) @4139 | 4139-4139 | encoded | s 171ZZ16(2) the conditions are satisfied; s 171ZZ16(2)(d) the normal weekly earnings are not less than the lower earnings limit |
| s 171ZZ16(3) | 4140-4140 | encoded | s 171ZZ16(3) any condition prescribed under this subsection is satisfied |
| s 171ZZ16(3)(a) @4141 | 4141-4141 | encoded | s 171ZZ16(3) any condition prescribed under this subsection is satisfied |
| s 171ZZ16(3)(b) @4142 | 4142-4142 | encoded | s 171ZZ16(3) any condition prescribed under this subsection is satisfied |
| s 171ZZ16(4) | 4143-4143 | encoded | s 171ZZ16(4) the care is neonatal care |
| s 171ZZ16(4)(a) @4144 | 4144-4144 | encoded | s 171ZZ16(4) the care is neonatal care |
| s 171ZZ16(4)(b) @4145 | 4145-4145 | fork F10 | s 171ZZ16(4) the care is neonatal care |
| s 171ZZ16(5) | 4146-4146 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ16(6) | 4147-4147 | encoded | s 171ZZ16(6) the relevant week |
| s 171ZZ16(6)(a) @4148 | 4148-4148 | encoded | s 171ZZ16(6) the relevant week |
| s 171ZZ16(6)(b) @4149 | 4149-4149 | encoded | s 171ZZ16(6) the relevant week |
| s 171ZZ16(6)(c) @4150 | 4150-4150 | encoded | s 171ZZ16(6) the relevant week |
| s 171ZZ16(6)(d) @4151 | 4151-4151 | encoded | s 171ZZ16(6) the relevant week |
| s 171ZZ16(6)(e) @4152 | 4152-4152 | encoded | s 171ZZ16(6) the relevant week |
| s 171ZZ16(7) | 4153-4153 | encoded | s 171ZZ16(7) paragraph (c) of subsection (2) is omitted |
| s 171ZZ17 | 4154-4154 | inert 1 | heading: no rule of its own |
| s 171ZZ17(1) | 4155-4155 | encoded | s 171ZZ17(1) the person is entitled to payments for the weeks |
| s 171ZZ17(2) | 4156-4156 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ17(3) | 4157-4157 | encoded | s 171ZZ17(3) the notice satisfies the requirement as to writing |
| s 171ZZ17(4) | 4158-4158 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ17(4)(a) @4159 | 4159-4159 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(i) @4160 | 4160-4160 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(ii) @4161 | 4161-4161 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(b) @4162 | 4162-4162 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(c) @4163 | 4163-4163 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(d) @4164 | 4164-4164 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(e) @4165 | 4165-4165 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(f) @4166 | 4166-4166 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(g) @4167 | 4167-4167 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(h) @4168 | 4168-4168 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(i) @4169 | 4169-4169 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(ii) @4170 | 4170-4170 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(i) @4171 | 4171-4171 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(j) @4172 | 4172-4172 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(i) @4173 | 4173-4173 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ17(4)(ii) @4174 | 4174-4175 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ18 | 4176-4176 | inert 1 | heading: no rule of its own |
| s 171ZZ18(1) | 4177-4177 | encoded | s 171ZZ18(1) the person is liable to make payments of statutory neonatal care pay; s 171ZZ18(1) the duty to make the payments |
| s 171ZZ18(2) | 4178-4178 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ18(3) | 4179-4179 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ19 | 4180-4180 | inert 1 | heading: no rule of its own |
| s 171ZZ19(1) | 4181-4181 | encoded | s 171ZZ19(1) the weekly rate of statutory neonatal care pay in pounds |
| s 171ZZ19(2) | 4182-4182 | encoded | s 171ZZ19(2) the pay payable for the weeks chosen in pounds |
| s 171ZZ19(2)(a) @4183 | 4183-4183 | encoded | s 171ZZ19(2) the pay payable for the weeks chosen in pounds |
| s 171ZZ19(2)(b) @4184 | 4184-4185 | encoded | s 171ZZ19(2) the pay payable for the weeks chosen in pounds |
| s 171ZZ19(3) | 4186-4186 | encoded | s 171ZZ19(3) the prescribed number of weeks is allowed |
| s 171ZZ19(4) | 4187-4187 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ19(5) | 4188-4188 | fork F12 | s 171ZZ19(5) the qualifying period is allowed |
| s 171ZZ19(6) | 4189-4189 | encoded | s 171ZZ19(6) the person is liable to pay for the statutory pay week |
| s 171ZZ19(7) | 4190-4190 | encoded | s 171ZZ19(7) the person is liable to pay for the statutory pay week whether or not the contract existed before |
| s 171ZZ19(8) | 4191-4191 | encoded | s 171ZZ19(8) the pay is payable for the statutory pay week |
| s 171ZZ19(9) | 4192-4192 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ19(10) | 4193-4193 | encoded | s 171ZZ19(10) the daily rate in pounds |
| s 171ZZ19(11) | 4194-4196 | encoded | s 171ZZ19(11) the period is a week; s 171ZZ19(11) the period is a statutory pay week; s 171ZZ19(11) the week convention |
| s 171ZZ20 | 4197-4197 | inert 1 | heading: no rule of its own |
| s 171ZZ20(1) | 4198-4198 | encoded | s 171ZZ20(1) the agreement is void to that extent |
| s 171ZZ20(1)(a) @4199 | 4199-4199 | encoded | s 171ZZ20(1) the agreement is void to that extent |
| s 171ZZ20(1)(b) @4200 | 4200-4200 | encoded | s 171ZZ20(1) the agreement is void to that extent |
| s 171ZZ20(2) | 4201-4201 | encoded | s 171ZZ20(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ20(2)(a) @4202 | 4202-4202 | encoded | s 171ZZ20(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ20(2)(b) @4203 | 4203-4203 | encoded | s 171ZZ20(2) the agreement authorising deductions is not void by virtue of subsection (1)(a) |
| s 171ZZ21 | 4204-4204 | inert 1 | heading: no rule of its own |
| s 171ZZ21(1) | 4205-4205 | encoded | s 171ZZ21(1) the entitlement affects the person's right to contractual remuneration |
| s 171ZZ21(2) | 4206-4206 | encoded | intro words; encoded in the rows below: s 171ZZ21(2)(a) the liability to pay statutory neonatal care pay that remains; s 171ZZ21(2)(b) the liability to pay contractual remuneration that remains |
| s 171ZZ21(2)(a) @4207 | 4207-4207 | encoded | s 171ZZ21(2)(a) the liability to pay statutory neonatal care pay that remains |
| s 171ZZ21(2)(b) @4208 | 4208-4208 | encoded | s 171ZZ21(2)(b) the liability to pay contractual remuneration that remains |
| s 171ZZ21(3) | 4209-4209 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ22 | 4210-4210 | inert 1 | heading: no rule of its own |
| s 171ZZ22 text | 4211-4211 | encoded | s 171ZZ22 the provisions of this Part apply to the person |
| s 171ZZ23 | 4212-4212 | inert 1 | heading: no rule of its own |
| s 171ZZ23(1) | 4213-4213 | encoded | s 171ZZ23(1) regulations may modify this Part in its application to the person |
| s 171ZZ23(1)(a) @4214 | 4214-4214 | encoded | s 171ZZ23(1) regulations may modify this Part in its application to the person |
| s 171ZZ23(1)(b) @4215 | 4215-4215 | encoded | s 171ZZ23(1) regulations may modify this Part in its application to the person |
| s 171ZZ23(1)(c) @4216 | 4216-4216 | encoded | s 171ZZ23(1) regulations may modify this Part in its application to the person |
| s 171ZZ23(2) | 4217-4217 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ23(2)(a) @4218 | 4218-4218 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ23(2)(b) @4219 | 4219-4219 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ23(2)(c) @4220 | 4220-4220 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ23(2)(d) @4221 | 4221-4221 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24 | 4222-4222 | inert 1 | heading: no rule of its own |
| s 171ZZ24(1) | 4223-4223 | encoded | intro words; encoded in the rows below: s 171ZZ24(1) the person is the employer of the employee; s 171ZZ24(1) the change is a modification |
| s 171ZZ24(1) “employer” | 4224-4228 | encoded | s 171ZZ24(1) the person is the employer of the employee |
| s 171ZZ24(1) “modifications” | 4229-4229 | encoded | s 171ZZ24(1) the change is a modification |
| s 171ZZ24(1) “prescribed” | 4230-4230 | encoded | s 171ZZ24(1) the matter is prescribed |
| s 171ZZ24(2) | 4231-4231 | fork F4 | s 171ZZ24(2) the person is an employee |
| s 171ZZ24(3) | 4232-4232 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ24(3)(a) @4233 | 4233-4233 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(3)(b) @4234 | 4234-4234 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(4) | 4235-4235 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ24(4)(a) @4236 | 4236-4236 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(4)(b) @4237 | 4237-4237 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(5) | 4238-4238 | encoded | s 171ZZ24(5) the week convention; s 171ZZ24(5) the first day of the week containing the day |
| s 171ZZ24(6) | 4239-4239 | encoded | s 171ZZ24(6) the person's normal weekly earnings in pounds |
| s 171ZZ24(7) | 4240-4240 | encoded | s 171ZZ24(6) the person's normal weekly earnings in pounds |
| s 171ZZ24(8) | 4241-4241 | encoded | s 171ZZ24(6) the person's normal weekly earnings in pounds |
| s 171ZZ24(9) | 4242-4242 | inert 2 | machinery: a power to make regulations (the election, or statutory declarations) |
| s 171ZZ24(10) | 4243-4243 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ24(10)(a) @4244 | 4244-4244 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(10)(b) @4245 | 4245-4245 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(10)(c) @4246 | 4246-4246 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(10)(d) @4247 | 4247-4247 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(10)(e) @4248 | 4248-4248 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(10)(f) @4249 | 4249-4249 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171ZZ24(11) | 4250-4250 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171ZZ24(12) | 4251-4251 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| Part XIIA | 4252-4252 | inert 1 | heading: no rule of its own |
| s 171A | 4253-4253 | inert 1 | heading: no rule of its own |
| s 171A(1) | 4254-4254 | encoded | s 171A(1) this Part determines whether the person is capable or incapable of work; s 171A(1) the person is incapable of work |
| s 171A(2) | 4255-4255 | encoded | s 171A(2) the person is treated as capable of work |
| s 171A(2)(a) @4256 | 4256-4256 | encoded | s 171A(2) the person is treated as capable of work |
| s 171A(2)(b) @4257 | 4257-4258 | encoded | s 171A(2) the person is treated as capable of work |
| s 171A(2A) | 4259-4259 | encoded | s 171A(2A) the information or evidence is within subsection (2)(a) |
| s 171A(3) | 4260-4260 | encoded | s 171A(3) the person is treated as capable of work |
| s 171A(3)(a) @4261 | 4261-4261 | encoded | s 171A(3) the person is treated as capable of work |
| s 171A(3)(b) @4262 | 4262-4262 | encoded | s 171A(3) the person is treated as capable of work |
| s 171A(4) | 4263-4263 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171A(4)(a) @4264 | 4264-4264 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171A(4)(b) @4265 | 4265-4265 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171A(5) | 4266-4266 | encoded | s 171A(5) the information is information relating to social security |
| s 171B | 4267-4267 | inert 1 | heading: no rule of its own |
| s 171B(1) | 4268-4268 | fork F7 | s 171B(1) the own occupation test is applicable |
| s 171B(2) | 4269-4269 | encoded | s 171B(2) the person is incapable of work on the own occupation test |
| s 171B(3) | 4270-4270 | fork F5, F6 | s 171B(3) the status of the own occupation test on the day |
| s 171B(3)(a) @4271 | 4271-4271 | encoded | s 171B(3) the status of the own occupation test on the day |
| s 171B(3)(b) @4272 | 4272-4274 | encoded | s 171B(3) the series of consecutive days from; s 171B(3) the series of consecutive days of incapacity for work; s 171B(3) the spells merged from; s 171B(3) the spells of incapacity; s 171B(3) the spell in which the day falls; s 171B(3) the nth day of incapacity for work; s 171B(3) the 197th day of incapacity for work in the spell; s 171B(3) the status of the own occupation test within the spell; s 171B(3) the status of the own occupation test on the day |
| s 171B(4) | 4275-4275 | encoded | s 171B(4) the day is a day of incapacity for work |
| s 171B(4)(a) @4276 | 4276-4276 | encoded | s 171B(4) the day is a day of incapacity for work |
| s 171B(4)(b) @4277 | 4277-4277 | encoded | s 171B(4) the day is a day of incapacity for work |
| s 171B(4)(c) @4278 | 4278-4278 | encoded | s 171B(4) the day is a day of incapacity for work |
| s 171B(4)(d) @4279 | 4279-4279 | encoded | s 171B(4) the day is a day of incapacity for work |
| s 171B(5) | 4280-4280 | encoded | s 171B(5) the provision is disregarded for the purposes of section 171B |
| s 171B(6) | 4281-4281 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171B(6) sentence @4282 | 4282-4282 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171B(6)(a) @4283 | 4283-4283 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171B(6)(b) @4284 | 4284-4284 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171B(7) | 4285-4285 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171B(8) | 4286-4286 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171B(8)(a) @4287 | 4287-4287 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171B(8)(b) @4288 | 4288-4288 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171C | 4289-4289 | inert 1 | heading: no rule of its own |
| s 171C(1) | 4290-4290 | fork F8 | s 171C(1) the test that decides |
| s 171C(2) | 4291-4291 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171C(2)(a) @4292 | 4292-4292 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171C(2)(b) @4293 | 4293-4293 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171C(3) | 4294-4294 | encoded | s 171C(3) the person is treated as incapable of work in accordance with a personal capability assessment |
| s 171C(3)(a) @4295 | 4295-4295 | encoded | s 171C(3) the person is treated as incapable of work in accordance with a personal capability assessment |
| s 171C(3)(b) @4296 | 4296-4296 | encoded | s 171C(3) the person is treated as incapable of work in accordance with a personal capability assessment |
| s 171C(3) sentence @4297 | 4297-4297 | inert 2 | machinery: a statement of what regulations may contain |
| s 171C(4) | 4298-4298 | encoded | s 171C(4) the earlier assessment is as effective as a later one |
| s 171C(5) | 4299-4299 | encoded | s 171C(5) the Secretary of State may require the question to be determined afresh |
| s 171D | 4300-4300 | inert 1 | heading: no rule of its own |
| s 171D(1) | 4301-4301 | encoded | s 171D(1) the treatment of the person |
| s 171D(2) | 4302-4302 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171D(2) sentence @4303 | 4303-4303 | inert 2 | machinery: a statement of what regulations may contain |
| s 171E | 4304-4304 | inert 1 | heading: no rule of its own |
| s 171E(1) | 4305-4305 | encoded | s 171E(1) the person is disqualified for receiving a benefit, allowance or other advantage; s 171E(1) the person is treated as capable of work |
| s 171E(1)(a) @4306 | 4306-4306 | encoded | s 171E(1) the person is disqualified for receiving a benefit, allowance or other advantage; s 171E(1) the person is treated as capable of work |
| s 171E(1)(b) @4307 | 4307-4307 | encoded | s 171E(1) the person is disqualified for receiving a benefit, allowance or other advantage; s 171E(1) the person is treated as capable of work |
| s 171E(1)(c) @4308 | 4308-4308 | encoded | s 171E(1) the person is disqualified for receiving a benefit, allowance or other advantage; s 171E(1) the person is treated as capable of work |
| s 171E(2) | 4309-4309 | encoded | s 171E(2) the period of the disqualification or treatment as capable of work is allowed |
| s 171E(3) | 4310-4310 | inert 2 | machinery: a power or duty to make regulations, with no consequence for a person until regulations are made |
| s 171E(3)(a) @4311 | 4311-4311 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171E(3)(b) @4312 | 4312-4312 | inert 2 | machinery: what the regulations under the parent subsection may or must contain |
| s 171F | 4313-4313 | inert 1 | heading: no rule of its own |
| s 171F(1) | 4314-4314 | encoded | s 171F(1) the work is disregarded in determining whether the person is capable or incapable of work |
| s 171F(2) | 4315-4315 | encoded | s 171F(2) the person is a councillor |
| s 171F(2)(a) @4316 | 4316-4316 | encoded | s 171F(2) the person is a councillor |
| s 171F(2)(b) @4317 | 4317-4317 | encoded | s 171F(2) the person is a councillor |
| s 171F(3) | 4318-4318 | encoded | s 171F(3) the work counts as work undertaken as a councillor |
| s 171F(4) | 4319-4319 | encoded | s 171F(4) the person is treated as having been incapable of work on the day |
| s 171F(4)(a) @4320 | 4320-4320 | encoded | s 171F(4) the person is treated as having been incapable of work on the day |
| s 171F(4)(b) @4321 | 4321-4321 | encoded | s 171F(4) the person is treated as having been incapable of work on the day |
| s 171F(4) sentence @4322 | 4322-4322 | encoded | s 171F(4) the pre-commencement period |
| s 171G | 4323-4323 | inert 1 | heading: no rule of its own |
| s 171G(1) | 4324-4324 | encoded | s 171G(1) this Part applies for the purpose |
| s 171G(1)(a) @4325 | 4325-4325 | encoded | s 171G(1) this Part applies for the purpose |
| s 171G(1)(b) @4326 | 4326-4326 | encoded | s 171G(1) this Part applies for the purpose |
| s 171G(1)(c) @4327 | 4327-4327 | encoded | s 171G(1) this Part applies for the purpose |
| s 171G(2) | 4328-4330 | encoded | s 171G(2) the matter is prescribed; s 171G(2) the period is a week; s 171G(2) the week convention |

## Fork register (ssc7)

Thirteen forks.
Each row says what the text says, the readings I saw, the one I took, the words that license it, and the L4 rule that carries the chosen reading (the coverage table points back here by the fork number).
Where I took "not covered", the rule answers `NOTHING` (or a named "text does not say" constructor) and a test asserts it.

| fork | where | the text | readings seen | taken, and the licence | L4 rule |
| --- | --- | --- | --- | --- | --- |
| F1 | ss 171ZU(1), 171ZU(3), 171ZV(1), 171ZV(3) (src:3720, 3745, 3813, 3838) | "Regulations may provide that, where all the conditions in subsection (2) are satisfied in relation to a person who is the mother of a child (\"the claimant mother\"), the claimant mother is to be entitled ..." | **A.** The Act itself gives the entitlement when the conditions are met, and regulations only fill in detail: the answer is TRUE or FALSE from the conditions alone. **B.** The Act states the conditions and the entitlement exists only as regulations provide: with no such regulations the Act does not answer. | **B.** "Regulations may provide that ... is to be entitled" makes the entitlement a thing the regulations create. The conditions of subsections (2) and (4) are encoded as the Act states them; a plain input says whether regulations so provide; when it is false the answer is `NOTHING` (points outside the text), and when it is true a failed condition is `JUST FALSE` (a failed "where"; reading (a)). Regulations under s 171ZW(1)(a) may disapply or modify any condition in a case: a second input, and `NOTHING` when true. | `s 171ZU(1) the claimant mother is entitled to statutory shared parental pay`, `s 171ZU(3) ...`, `s 171ZV(1) ...`, `s 171ZV(3) ...`; the condition sets are `s 171ZU(2)`, `s 171ZU(4)`, `s 171ZV(2)`, `s 171ZV(4) all the conditions are satisfied` |
| F2 | s 171ZU(6) (src:3779-3783) | "the number of weeks of the maternity pay period reduced by ..." | **A.** Read "the maternity pay period" literally: a mother who gets maternity allowance has no maternity pay period, so there is no starting figure. **B.** Use the maternity allowance period as the starting figure when maternity allowance is what was paid. | **B.** Paragraphs (a) and (b) of the same subsection name maternity allowance and statutory maternity pay side by side, and (b) names both periods (the maternity allowance period reduced under s 35(3A), the maternity pay period reduced under s 165(3A)). A negative result is `NOTHING` (silent: the text does not say what a reduction larger than the period does). | `s 171ZU(6) the greatest number of weeks of statutory shared parental pay` |
| F3 | s 171ZZ15(a) (src:4128) | "references to a child include a child stillborn after twenty-four weeks of pregnancy" | **A.** "After twenty-four weeks" means more than 24 weeks have passed. **B.** It means 24 weeks or more. A second question is whether "include" closes the list. | **A** for the number (a child stillborn at 24 weeks exactly is not covered by this limb; 24 weeks and 1 day, that is 24 and 1/7 weeks, is). "Include" adds a case and does not close the list, so every other child is `NOTHING` (includes), never FALSE. | `s 171ZZ15(a) the child stillborn after twenty-four weeks of pregnancy is a child` |
| F4 | ss 171ZZ4(2), 171ZZ14(2), 171ZZ24(2) (src:3987, 4105, 4231) | "\"employee\" means a person who is gainfully employed in Great Britain either under a contract of service or in an office (including elective office) with general earnings (as defined by section 7 of the Income Tax (Earnings and Pensions) Act 2003)" (12ZC); the same with "with earnings (within the meaning of Parts 1 to 5)" (12ZD, 12ZE) | **A.** "Gainfully" adds a condition of its own (working for gain) beyond having the stated earnings. **B.** It adds nothing to "with general earnings" / "with earnings". | **B.** The sentence goes on to say with what earnings the person is gainfully employed; the earnings clause is the only test the sentence supplies. Whether the person has "general earnings" (ITEPA 2003 s 7) or "earnings" (Parts 1 to 5) is a borrowed fact, asked as a yes/no input in each Part's own words. The Act's own part (Great Britain, contract of service or office) is computed from the keel's `Employment` record. | `s 171ZZ4(2) the person is an employee`, `s 171ZZ14(2) ...`, `s 171ZZ24(2) ...` |
| F5 | s 171B(3) (src:4270-4274) | "that test remains applicable in his case until the end of the spell of incapacity ..., or until the 197th day of incapacity for work in that spell, whichever is the earlier" | **A.** The test still applies on the 197th day. **B.** It no longer applies on the 197th day. | **Neither.** "Until" does not say whether the 197th day is inside. The 197th day answers a named constructor `s 171B(3) the text does not say whether the test applies` (undefined term), asserted. Days before it: the test remains applicable; days after it: the stated period has ended. | `s 171B(3) the status of the own occupation test within the spell` |
| F6 | s 171B(3), last paragraph, with s 171B(4) (src:4270-4272, 4273-4274) | "a \"spell of incapacity\" means a series of 4 or more consecutive days of incapacity for work"; "any two such spells not separated by a period of more than 8 weeks shall be treated as one spell of incapacity" | **A.** The 197th day is counted over every day of incapacity that lies inside the merged spell, including days in a gap that are not part of any series of 4 or more. **B.** Only days that belong to a series of 4 or more count. | **A.** Once two spells are "treated as one spell", "the 197th day of incapacity for work in that spell" is a day of incapacity (s 171B(4)) that lies in that spell. A separation of exactly 8 weeks (56 days, s 171G(2)) is not "more than 8 weeks", so the spells merge. | `s 171B(3) the 197th day of incapacity for work in the spell` and the spell-building rules beside it |
| F7 | s 171B(1) (src:4268) | "engaged in remunerative work for more than 8 weeks in the 21 weeks immediately preceding the day" | **A.** The weeks are totalled within the 21. **B.** There must be more than 8 consecutive weeks. | **A.** The words "for more than 8 weeks in the 21 weeks" put no consecutiveness requirement. "Remunerative work" is defined by regulations (subsection (6)), so the count is a plain input. Eight weeks or fewer is `NOTHING` (limited by its own wording: the subsection says when the test "is applicable" and is silent otherwise); s 171C(1) takes up the case. | `s 171B(1) the own occupation test is applicable` |
| F8 | s 171C(1) (src:4290) | "Where the own occupation test is not applicable, or has ceased to apply, in the case of a person, the question ... shall be determined in accordance with a personal capability assessment" | **A.** "Not applicable" means s 171B(1) does not make it applicable, and "has ceased to apply" means s 171B(3) has ended it. **B.** "Not applicable" is judged on s 171B(1) alone, ignoring any carried-forward determination. | **A.** s 171B(3) says the test "remains applicable in his case" after a determination, so a person under 8 weeks of work who has a carried-forward determination is still on the own occupation test. Result: a typed answer (own occupation test / personal capability assessment / the text does not say which test decides). | `s 171C(1) the test that decides` |
| F9 | s 171ZY(7) (src:3943-3946) | "a week falls within a relevant period if it falls within a period specified in a notice under ... and is not afterwards excluded from such a period by a variation" | **A.** A week outside every specified period is FALSE (the sentence is a definition). **B.** It is not covered: the sentence says when a week "falls within", and an "if" is not an "only if". | **B** for a week outside every specified period (`NOTHING`, limited by its own wording); a week afterwards excluded by a variation is `JUST FALSE`, in the text's own words. This is a reading (a)/(b) point and is listed in the next section. | `s 171ZY(7) the week falls within a relevant period` |
| F10 | s 171ZZ16(4)(b) (src:4143-4145) | "care ... that starts before the end of a period of 28 days beginning with the day after the date of the child's birth" | **A.** The period runs from the day after the birth to the 28th day after it, so care that starts on the 28th day after the birth starts before the end of that day. **B.** "Before the end" excludes the last day. | **A.** Care starting 28 days after the birth is neonatal care and care starting 29 days after is not. | `s 171ZZ16(4) the care is neonatal care` |
| F11 | s 171ZZ16(2)(a)(ii) (src:4136) | "that care continues without interruption for a period of at least seven days beginning with the day after the day on which the care starts" | **A.** The seven days are the days after the start: the care must run to the seventh day after the day it starts. **B.** Seven days counting the day it starts. | **A.** The words "beginning with the day after the day on which the care starts" fix the first of the seven days. | `s 171ZZ16(2)(a)(ii) the care has continued without interruption for at least seven days` |
| F12 | ss 171ZZ9(5), 171ZZ19(5) (src:4061, 4188) | "the qualifying period is to be determined in accordance with regulations, which must secure that it is a period of at least 56 days beginning with the date of the child's death" (12ZD); "at least 68 weeks beginning with the date of the child's birth" (12ZE) | **A.** Both ends are counted (the first day is the date named, the length is last day minus first day plus one). **B.** The length is last day minus first day. | **A.** "A period of at least 56 days beginning with the date of ..." counts the date itself as the first day. A period that begins on another date is `JUST FALSE` ("must secure that it is a period of at least 56 days beginning with the date of the child's death"). | `s 171ZZ9(5) the qualifying period is allowed`, `s 171ZZ19(5) ...` |
| F13 | s 171ZU(7) (src:3784-3787) | "(a) where maternity allowance is payable to a mother, a week or part of a week falling before the time at which the mother takes action ...; (b) where statutory maternity pay is payable to a mother, a week falling before the week in which the mother takes action" | **A.** For maternity allowance a part of a week counts at either end (the first week may start mid-week; the week of the action counts up to the action). **B.** Only whole weeks count. | **A** for limb (a), where the text says "or part of a week"; **whole weeks only** for limb (b), where it says only "a week". The weeks of limb (a) are the s 122(1) weeks (Sunday start), those of limb (b) the s 165(8) weeks (starting on the day the maternity pay period begins), as the closing sentence of subsection (7) says. | `s 171ZU(7)(a) the number of relevant weeks of maternity allowance`, `s 171ZU(7)(b) ... of statutory maternity pay` |

## Jural relations (ssc7)

One row per section and subsection of the ranges that is not a heading.
Hohfeld's correlatives: a claim-right is the other party's duty; a privilege is the other party's no-right; a power is the other party's liability; an immunity is the other party's disability.
Each relation is stated once, from the holder's side, and named neutrally; a provision that creates no relation (a definition or a counting rule) is listed as `none` with what it is.
A rule of application that binds whoever decides (for example s 171B(1), which says when the own occupation test is to be applied) is listed as the claim-right of the person whose capacity is in question and the duty of the decision-maker; the text names no decision-maker in these provisions.
A rule that only limits what regulations may provide, or what a payer need pay, is listed as the limit it is: the payer's privilege and the claimant's no-right for "not payable" and "not liable", and the immunity of the person for "not affected" and "void".
The 41 headings (Part and section titles) create no relation and have no row here.
The table records the relation the words create; where a relation arises only if regulations say so, the row says so.
The correlative of a regulation-making power is the liability of the persons the regulations would bind, and a power the text gives to no named maker is given to "the maker of the regulations".
**Who "the person entitled" and "the payer" are.** In Part 12ZC the person entitled is the person entitled to statutory shared parental pay under s 171ZU or s 171ZV, and the payer is the person liable under s 171ZX (an employer or former employer; the Commissioners where regulations under s 171ZX(3) so provide). In Part 12ZD they are the person entitled under s 171ZZ6 (a bereaved parent who is an employee) and the person liable under s 171ZZ8, with s 171ZZ8(3) for the Commissioners. In Part 12ZE they are the person entitled under s 171ZZ16 and the person liable under s 171ZZ18, with s 171ZZ18(3).

| provision | relation (holder / correlative) | holds the right, privilege, power or immunity | bears the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- | --- |
| s 171ZU(1) | claim-right / duty (arises only if regulations so provide: fork F1) | the claimant mother | the payer | `s 171ZU(1) the claimant mother is entitled to statutory shared parental pay` |
| s 171ZU(2) | none (the conditions of the claim in (1)) | - | - | `s 171ZU(2) all the conditions are satisfied` |
| s 171ZU(3) | claim-right / duty (arises only if regulations so provide: fork F1) | the claimant (a person other than the mother) | the payer | `s 171ZU(3) the claimant is entitled to statutory shared parental pay` |
| s 171ZU(4) | none (the conditions of the claim in (3)) | - | - | `s 171ZU(4) all the conditions are satisfied` |
| s 171ZU(5) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZU(6) | none (a ceiling on the weeks of the claim: a limit regulations under (5)(a) must respect) | - | - | `s 171ZU(6) the greatest number of weeks of statutory shared parental pay` |
| s 171ZU(7) | none (a counting rule for (6)) | - | - | `s 171ZU(7)(a) the number of relevant weeks of maternity allowance`; `s 171ZU(7)(b) the number of relevant weeks of statutory maternity pay` |
| s 171ZU(8) | none (a counting rule for (6)) | - | - | `s 171ZU(8) the number of weeks counting a part of a week as a week` |
| s 171ZU(9) | none (a ceiling: two entitlements together may not exceed what one person could have) | - | - | `s 171ZU(9) the two entitlements together are within what is available to one person` |
| s 171ZU(10) | privilege / no-right (no payment after the prescribed period; a limit regulations under (5)(b) must respect) | the payer (no duty to pay later payments) | the person entitled (no claim to them) | `s 171ZU(10) a payment may be made in respect of the child` |
| s 171ZU(11) | privilege / no-right (no payment before the end of the maternity or adoption pay period; a limit regulations under (5)(b) must respect) | the payer (no duty to pay earlier payments) | the person entitled (no claim to them) | `s 171ZU(11) a payment may be made to the mother` |
| s 171ZU(12) | power / liability (if regulations so provide) | the person entitled (the "V" of the subsection) | the payer (bound by the varied period or periods) | `s 171ZU(12) V may vary the period or periods` |
| s 171ZU(13) | none (the conditions of the power in (12)) | - | - | `s 171ZU(13) the conditions for varying the period or periods are satisfied` |
| s 171ZU(14) | power / liability (if regulations so provide; subject to the consent in (15)(c)) | the person entitled (the "V" of the subsection) | the payer (bound by the varied number of weeks) | `s 171ZU(14) V may vary the number of weeks` |
| s 171ZU(15) | power / liability: P (the mother's partner) or M (the mother) holds a power to consent or withhold consent under (c), and V is under the liability of that decision; the rest are conditions | P (the mother's partner) or M (the mother) | V (the person entitled) | `s 171ZU(15) the conditions for varying the number of weeks are satisfied` |
| s 171ZU(16) | immunity / disability (the entitlement is not affected by the birth or placement of more than one child) | the person entitled | the payer and the maker of any regulations | `s 171ZU(16) the entitlement after the birth of more than one child` |
| s 171ZV(1) | claim-right / duty (arises only if regulations so provide: fork F1) | claimant A | the payer | `s 171ZV(1) claimant A is entitled to statutory shared parental pay` |
| s 171ZV(2) | none (the conditions of the claim in (1)) | - | - | `s 171ZV(2) all the conditions are satisfied` |
| s 171ZV(3) | claim-right / duty (arises only if regulations so provide: fork F1) | claimant B | the payer | `s 171ZV(3) claimant B is entitled to statutory shared parental pay` |
| s 171ZV(4) | none (the conditions of the claim in (3)) | - | - | `s 171ZV(4) all the conditions are satisfied` |
| s 171ZV(5) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZV(6) | none (a ceiling on the weeks of the claim: a limit regulations under (5)(a) must respect) | - | - | `s 171ZV(6) the greatest number of weeks of statutory shared parental pay` |
| s 171ZV(7) | none (a counting rule for (6)) | - | - | `s 171ZV(7) the number of relevant weeks of statutory adoption pay` |
| s 171ZV(8) | none (a counting rule for (6)) | - | - | `s 171ZV(8) the number of weeks counting a part of a week as a week` |
| s 171ZV(9) | none (a ceiling: two entitlements together may not exceed what one person could have) | - | - | `s 171ZV(9) the two entitlements together are within what is available to one person` |
| s 171ZV(10) | privilege / no-right (no payment after the prescribed period; a limit regulations under (5)(b) must respect) | the payer (no duty to pay later payments) | the person entitled (no claim to them) | `s 171ZV(10) a payment may be made in respect of the child` |
| s 171ZV(11) | privilege / no-right (no payment before the end of the maternity or adoption pay period; a limit regulations under (5)(b) must respect) | the payer (no duty to pay earlier payments) | the person entitled (no claim to them) | `s 171ZV(11) a payment may be made to the person who became entitled to statutory adoption pay` |
| s 171ZV(12) | power / liability (if regulations so provide) | the person entitled (the "V" of the subsection) | the payer (bound by the varied period or periods) | `s 171ZV(12) V may vary the period or periods` |
| s 171ZV(13) | none (the conditions of the power in (12)) | - | - | `s 171ZV(13) the conditions for varying the period or periods are satisfied` |
| s 171ZV(14) | power / liability (if regulations so provide; subject to the consent in (15)(c)) | the person entitled (the "V" of the subsection) | the payer (bound by the varied number of weeks) | `s 171ZV(14) V may vary the number of weeks` |
| s 171ZV(15) | power / liability: X or Y (the other adopter, or the person who became entitled to adoption pay) holds a power to consent or withhold consent under (c), and V is under the liability of that decision; the rest are conditions | X or Y (the other adopter, or the person who became entitled to adoption pay) | V (the person entitled) | `s 171ZV(15) the conditions for varying the number of weeks are satisfied` |
| s 171ZV(16) | immunity / disability (the entitlement is not affected by the birth or placement of more than one child) | the person entitled | the payer and the maker of any regulations | `s 171ZV(16) the entitlement after the placement for adoption of more than one child` |
| s 171ZV(17) | duty / claim-right (regulations are to provide for entitlement in a foster-placement case; not encoded: inert 2, a duty to make regulations) | the local authority foster parent approved as a prospective adopter (a future claim-right) | the maker of the regulations (the section does not name them) | not encoded (inert 2) |
| s 171ZV(18) | none (a reading rule for regulations under (17)) | - | - | `s 171ZV(18) the placement counts as a placement for adoption` |
| s 171ZW(1) | power / liability (encoded as the gate `s 171ZW(1)(a) regulations disapply or modify a condition`) | the maker of the regulations (the section does not name them) | the claimants and payers whose conditions are disapplied or modified | `s 171ZW(1)(a) the condition has effect in the case` |
| s 171ZW(2) | power / liability | the maker of the regulations (the section does not name them) | the persons on whom requirements may be imposed: a person who must satisfy conditions in connection with another person's claim, and an employer or former employer | `s 171ZW(2) requirements about evidence and procedure may be imposed on the person` |
| s 171ZW(3) | none (a definition: "the prescribed period") | - | - | `s 171ZW(3) the prescribed period in weeks` |
| s 171ZX(1) | duty / claim-right (a regulative rule: `PARTY ... MUST`) | the person entitled (the claim) | the payer (the duty) | `s 171ZX(1) the person is liable to make payments of statutory shared parental pay`; `s 171ZX(1) the duty to make the payments` |
| s 171ZX(2) | duty / claim-right (the regulation-maker must provide for a former employer's liability; not encoded: inert 2) | the former employee | the maker of the regulations (the section does not name them) | not encoded (inert 2) |
| s 171ZX(3) | power / liability (with the concurrence of the Commissioners for HMRC; not encoded: inert 2) | the Secretary of State | an employer whose liability is moved, and the Commissioners who take it | not encoded (inert 2) |
| s 171ZY(1) | claim-right / duty (the amount: the weekly rate regulations prescribe) | the person entitled | the payer | `s 171ZY(1) the weekly rate of statutory shared parental pay in pounds` |
| s 171ZY(2) | claim-right / duty (the extent: each week in a relevant period, up to the weeks determined under s 171ZU(5) or 171ZV(5)) | the person entitled | the payer | `s 171ZY(2) statutory shared parental pay is payable for the week` |
| s 171ZY(3) | privilege / no-right (not payable for a week if the person does not intend to care for the child, except as prescribed) | the payer (no duty to pay for that week) | the person entitled (no claim for that week) | `s 171ZY(3) the pay is payable for the week despite the intention to care` |
| s 171ZY(4) | privilege / no-right (not payable for a week in which the person works for any employer, except as prescribed) | the payer (no duty to pay for that week) | the person entitled (no claim for that week) | `s 171ZY(4) the pay is payable for the week despite work for an employer` |
| s 171ZY(5) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | persons who would otherwise be liable | not encoded (inert 2) |
| s 171ZY(6) | none (a counting rule: the daily rate is one seventh of the weekly rate) | - | - | `s 171ZY(6) the daily rate in pounds` |
| s 171ZY(7) | none (a definition: a week within a relevant period) | - | - | `s 171ZY(7) the week falls within a relevant period` |
| s 171ZY(8) | none (a definition: "week") | - | - | `s 171ZY(8) the week of the relevant period containing the day` |
| s 171ZZ(1) | immunity / disability (an agreement is void to the extent that it purports to exclude, limit or modify the Part, or to make the person contribute to the employer's costs) | the person entitled (as employee) | the employer or former employer, and anyone who would contract out of the Part (cannot do so) | `s 171ZZ(1) the agreement is void to that extent` |
| s 171ZZ(2) | privilege / no-right (an agreed deduction from statutory shared parental pay that could be made from contractual pay is not void) | the employer | the employee (no right against the agreed deduction) | `s 171ZZ(2) the agreement authorising deductions is not void by virtue of subsection (1)(a)` |
| s 171ZZ1(1) | immunity / disability (the entitlement does not affect the person's rights to contractual remuneration) | the employee | the employer (cannot treat the entitlement as reducing contractual rights) | `s 171ZZ1(1) the entitlement affects the person's right to contractual remuneration` |
| s 171ZZ1(2) | privilege / no-right (contractual pay goes towards discharging the liability for statutory shared parental pay and the reverse) | the employer (discharges one liability by paying the other) | the employee (no right to both) | `s 171ZZ1(2)(a) the liability to pay statutory shared parental pay that remains`; `s 171ZZ1(2)(b) the liability to pay contractual remuneration that remains` |
| s 171ZZ1(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ2 text | claim-right / duty (the Part applies to persons employed by or under the Crown as to others) | a person employed by or under the Crown | the Crown as employer, or the person liable under the Part | `s 171ZZ2 the provisions of this Part apply to the person` |
| s 171ZZ3(1) | power / liability (with the concurrence of the Treasury; encoded as a gate, `regulations may modify this Part`) | the Secretary of State | a person employed on a ship, vessel, hovercraft or aircraft, outside Great Britain, or in continental shelf employment | `s 171ZZ3(1) regulations may modify this Part in its application to the person` |
| s 171ZZ3(2) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | the same persons | not encoded (inert 2) |
| s 171ZZ4(1) | none (a definition or counting rule) | - | - | `s 171ZZ4(1) adoption pay period`; `s 171ZZ4(1) the person is the employer of the employee` |
| s 171ZZ4(2) | none (a definition or counting rule) | - | - | `s 171ZZ4(2) the person is an employee` |
| s 171ZZ4(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ4(4) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ4(5) | none (a definition or counting rule) | - | - | `s 171ZZ4(5) the week convention`; `s 171ZZ4(5) the first day of the week containing the day` |
| s 171ZZ4(6) | none (a definition or counting rule) | - | - | `s 171ZZ4(6) the person's normal weekly earnings in pounds` |
| s 171ZZ4(7) | none (a definition or counting rule) | - | - | `s 171ZZ4(6) the person's normal weekly earnings in pounds` |
| s 171ZZ4(8) | none (a definition or counting rule) | - | - | `s 171ZZ4(6) the person's normal weekly earnings in pounds` |
| s 171ZZ4(9) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ4(10) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ4(11) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ4(12) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ5(1) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ5(2) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ5(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ6(1) | claim-right / duty | the person entitled | the payer | `s 171ZZ6(1) the person is entitled to statutory parental bereavement pay` |
| s 171ZZ6(2) | none (the conditions of the claim in (1)) | - | - | `s 171ZZ6(2) the person satisfies the conditions` |
| s 171ZZ6(3) | none (a definition: "bereaved parent") | - | - | `s 171ZZ6(3) the employee is a bereaved parent` |
| s 171ZZ6(4) | none (a statement of what regulations may contain; not encoded: inert 2) | - | - | not encoded (inert 2) |
| s 171ZZ6(5) | none (a counting rule: the relevant week) | - | - | `s 171ZZ6(5) the relevant week`; `s 171ZZ6(5) the last day of the relevant week` |
| s 171ZZ6(6) | claim-right / duty (once for each child) | the person entitled | the payer | `s 171ZZ6(6) the number of children in respect of whom the person is entitled` |
| s 171ZZ6(7) | none (a transitional reading of subsection (2)(c)) | - | - | `s 171ZZ6(7) paragraph (c) of subsection (2) is omitted` |
| s 171ZZ7(1) | power / liability (notice naming the weeks is the condition for payment for those weeks) | the person entitled (by giving the notice) | the payer (becomes liable for the weeks named) | `s 171ZZ7(1) the person is entitled to payments for the weeks` |
| s 171ZZ7(2) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ7(3) | power / liability (a right to demand that the notice be in writing) | the payer | the person entitled (must put the notice in writing if asked) | `s 171ZZ7(3) the notice satisfies the requirement as to writing` |
| s 171ZZ7(4) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | claimants and payers | not encoded (inert 2) |
| s 171ZZ8(1) | duty / claim-right (a regulative rule: `PARTY ... MUST`) | the person entitled (the claim) | the payer (the duty) | `s 171ZZ8(1) the person is liable to make payments of statutory parental bereavement pay`; `s 171ZZ8(1) the duty to make the payments` |
| s 171ZZ8(2) | duty / claim-right (the regulation-maker must provide for a former employer's liability; not encoded: inert 2) | the former employee | the maker of the regulations (the section does not name them) | not encoded (inert 2) |
| s 171ZZ8(3) | power / liability (with the concurrence of the Commissioners for HMRC; not encoded: inert 2) | the Secretary of State | an employer whose liability is moved, and the Commissioners who take it | not encoded (inert 2) |
| s 171ZZ9(1) | claim-right / duty (the amount: the weekly rate regulations prescribe) | the person entitled | the payer | `s 171ZZ9(1) the weekly rate of statutory parental bereavement pay in pounds` |
| s 171ZZ9(2) | power / liability (the person entitled chooses the week or weeks within the qualifying period) | the person entitled | the payer (liable for the weeks chosen) | `s 171ZZ9(2) the pay payable for the weeks chosen in pounds` |
| s 171ZZ9(3) | none (a floor regulations under (2)(b) must respect) | - | - | `s 171ZZ9(3) the prescribed number of weeks is allowed` |
| s 171ZZ9(4) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ9(5) | none (a floor regulations must respect: the qualifying period) | - | - | `s 171ZZ9(5) the qualifying period is allowed` |
| s 171ZZ9(6) | privilege / no-right (no liability for a week in which the other works under a contract of service with the payer) | the payer (no duty to pay for that week) | the person entitled (no claim for that week) | `s 171ZZ9(6) the person is liable to pay for the statutory pay week` |
| s 171ZZ9(7) | none (it is immaterial which contract; a counting rule for (6)) | - | - | `s 171ZZ9(7) the person is liable to pay for the statutory pay week whether or not the contract existed before` |
| s 171ZZ9(8) | privilege / no-right (the pay is not payable for a week in which the person works for an employer not liable to pay it, except as prescribed) | the payer (no duty to pay for that week) | the person entitled (no claim for that week) | `s 171ZZ9(8) the pay is payable for the statutory pay week` |
| s 171ZZ9(9) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | persons who would otherwise be liable | not encoded (inert 2) |
| s 171ZZ9(10) | none (a counting rule: the daily rate is one seventh of the weekly rate) | - | - | `s 171ZZ9(10) the daily rate in pounds` |
| s 171ZZ9(11) | none (definitions: "statutory pay week", "week") | - | - | `s 171ZZ9(11) the period is a week`; `s 171ZZ9(11) the period is a statutory pay week`; `s 171ZZ9(11) the week convention` |
| s 171ZZ10(1) | immunity / disability (an agreement is void to the extent that it purports to exclude, limit or modify the Part, or to make the person contribute to the employer's costs) | the person entitled (as employee) | the employer or former employer, and anyone who would contract out of the Part (cannot do so) | `s 171ZZ10(1) the agreement is void to that extent` |
| s 171ZZ10(2) | privilege / no-right (an agreed deduction from statutory parental bereavement pay that could be made from contractual pay is not void) | the employer | the employee (no right against the agreed deduction) | `s 171ZZ10(2) the agreement authorising deductions is not void by virtue of subsection (1)(a)` |
| s 171ZZ11(1) | immunity / disability (the entitlement does not affect the person's rights to contractual remuneration) | the employee | the employer (cannot treat the entitlement as reducing contractual rights) | `s 171ZZ11(1) the entitlement affects the person's right to contractual remuneration` |
| s 171ZZ11(2) | privilege / no-right (contractual pay goes towards discharging the liability for statutory parental bereavement pay and the reverse) | the employer (discharges one liability by paying the other) | the employee (no right to both) | `s 171ZZ11(2)(a) the liability to pay statutory parental bereavement pay that remains`; `s 171ZZ11(2)(b) the liability to pay contractual remuneration that remains` |
| s 171ZZ11(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ12 text | claim-right / duty (the Part applies to persons employed by or under the Crown as to others) | a person employed by or under the Crown | the Crown as employer, or the person liable under the Part | `s 171ZZ12 the provisions of this Part apply to the person` |
| s 171ZZ13(1) | power / liability (with the concurrence of the Treasury; encoded as a gate, `regulations may modify this Part`) | the Secretary of State | a person employed on a ship, vessel, hovercraft or aircraft, outside Great Britain, or in continental shelf employment | `s 171ZZ13(1) regulations may modify this Part in its application to the person` |
| s 171ZZ13(2) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | the same persons | not encoded (inert 2) |
| s 171ZZ14(1) | none (a definition or counting rule) | - | - | `s 171ZZ14(1) the person who died was a child`; `s 171ZZ14(1) the person is the employer of the employee` |
| s 171ZZ14(2) | none (a definition or counting rule) | - | - | `s 171ZZ14(2) the person is an employee` |
| s 171ZZ14(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ14(4) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ14(5) | none (a definition or counting rule) | - | - | `s 171ZZ14(5) the week convention`; `s 171ZZ14(5) the first day of the week containing the day` |
| s 171ZZ14(6) | none (a definition or counting rule) | - | - | `s 171ZZ14(6) the person's normal weekly earnings in pounds` |
| s 171ZZ14(7) | none (a definition or counting rule) | - | - | `s 171ZZ14(6) the person's normal weekly earnings in pounds` |
| s 171ZZ14(8) | none (a definition or counting rule) | - | - | `s 171ZZ14(6) the person's normal weekly earnings in pounds` |
| s 171ZZ14(9) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ14(10) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ14(11) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ14(12) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ15 text | claim-right / duty (extends the claim of s 171ZZ6 to a parent of a child stillborn after twenty-four weeks of pregnancy) | the person entitled | the payer | `s 171ZZ15(a) the child stillborn after twenty-four weeks of pregnancy is a child`; `s 171ZZ15(b) the day taken as the day the child dies` |
| s 171ZZ16(1) | claim-right / duty | the person entitled | the payer | `s 171ZZ16(1) the person is entitled to statutory neonatal care pay` |
| s 171ZZ16(2) | none (the conditions of the claim in (1)) | - | - | `s 171ZZ16(2) the conditions are satisfied` |
| s 171ZZ16(3) | power / liability (any condition prescribed under the subsection is a further condition of the claim) | the maker of the regulations (the section does not name them) | the person entitled (must meet the prescribed condition) | `s 171ZZ16(3) any condition prescribed under this subsection is satisfied` |
| s 171ZZ16(4) | none (a definition: "neonatal care") | - | - | `s 171ZZ16(4) the care is neonatal care` |
| s 171ZZ16(5) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ16(6) | none (a definition: "relevant week") | - | - | `s 171ZZ16(6) the relevant week` |
| s 171ZZ16(7) | none (a transitional reading of subsection (2)(c)) | - | - | `s 171ZZ16(7) paragraph (c) of subsection (2) is omitted` |
| s 171ZZ17(1) | power / liability (notice naming the weeks is the condition for payment for those weeks) | the person entitled (by giving the notice) | the payer (becomes liable for the weeks named) | `s 171ZZ17(1) the person is entitled to payments for the weeks` |
| s 171ZZ17(2) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ17(3) | power / liability (a right to demand that the notice be in writing) | the payer | the person entitled (must put the notice in writing if asked) | `s 171ZZ17(3) the notice satisfies the requirement as to writing` |
| s 171ZZ17(4) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | claimants and payers | not encoded (inert 2) |
| s 171ZZ18(1) | duty / claim-right (a regulative rule: `PARTY ... MUST`) | the person entitled (the claim) | the payer (the duty) | `s 171ZZ18(1) the person is liable to make payments of statutory neonatal care pay`; `s 171ZZ18(1) the duty to make the payments` |
| s 171ZZ18(2) | duty / claim-right (the regulation-maker must provide for a former employer's liability; not encoded: inert 2) | the former employee | the maker of the regulations (the section does not name them) | not encoded (inert 2) |
| s 171ZZ18(3) | power / liability (with the concurrence of the Commissioners for HMRC; not encoded: inert 2) | the Secretary of State | an employer whose liability is moved, and the Commissioners who take it | not encoded (inert 2) |
| s 171ZZ19(1) | claim-right / duty (the amount: the weekly rate regulations prescribe) | the person entitled | the payer | `s 171ZZ19(1) the weekly rate of statutory neonatal care pay in pounds` |
| s 171ZZ19(2) | power / liability (the person entitled chooses the week or weeks within the qualifying period) | the person entitled | the payer (liable for the weeks chosen) | `s 171ZZ19(2) the pay payable for the weeks chosen in pounds` |
| s 171ZZ19(3) | none (a floor regulations under (2)(b) must respect) | - | - | `s 171ZZ19(3) the prescribed number of weeks is allowed` |
| s 171ZZ19(4) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ19(5) | none (a floor regulations must respect: the qualifying period) | - | - | `s 171ZZ19(5) the qualifying period is allowed` |
| s 171ZZ19(6) | privilege / no-right (no liability for a week in which the other works under a contract of service with the payer) | the payer (no duty to pay for that week) | the person entitled (no claim for that week) | `s 171ZZ19(6) the person is liable to pay for the statutory pay week` |
| s 171ZZ19(7) | none (it is immaterial which contract; a counting rule for (6)) | - | - | `s 171ZZ19(7) the person is liable to pay for the statutory pay week whether or not the contract existed before` |
| s 171ZZ19(8) | privilege / no-right (the pay is not payable for a week in which the person works for an employer not liable to pay it, except as prescribed) | the payer (no duty to pay for that week) | the person entitled (no claim for that week) | `s 171ZZ19(8) the pay is payable for the statutory pay week` |
| s 171ZZ19(9) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | persons who would otherwise be liable | not encoded (inert 2) |
| s 171ZZ19(10) | none (a counting rule: the daily rate is one seventh of the weekly rate) | - | - | `s 171ZZ19(10) the daily rate in pounds` |
| s 171ZZ19(11) | none (definitions: "statutory pay week", "week") | - | - | `s 171ZZ19(11) the period is a week`; `s 171ZZ19(11) the period is a statutory pay week`; `s 171ZZ19(11) the week convention` |
| s 171ZZ20(1) | immunity / disability (an agreement is void to the extent that it purports to exclude, limit or modify the Part, or to make the person contribute to the employer's costs) | the person entitled (as employee) | the employer or former employer, and anyone who would contract out of the Part (cannot do so) | `s 171ZZ20(1) the agreement is void to that extent` |
| s 171ZZ20(2) | privilege / no-right (an agreed deduction from statutory neonatal care pay that could be made from contractual pay is not void) | the employer | the employee (no right against the agreed deduction) | `s 171ZZ20(2) the agreement authorising deductions is not void by virtue of subsection (1)(a)` |
| s 171ZZ21(1) | immunity / disability (the entitlement does not affect the person's rights to contractual remuneration) | the employee | the employer (cannot treat the entitlement as reducing contractual rights) | `s 171ZZ21(1) the entitlement affects the person's right to contractual remuneration` |
| s 171ZZ21(2) | privilege / no-right (contractual pay goes towards discharging the liability for statutory neonatal care pay and the reverse) | the employer (discharges one liability by paying the other) | the employee (no right to both) | `s 171ZZ21(2)(a) the liability to pay statutory neonatal care pay that remains`; `s 171ZZ21(2)(b) the liability to pay contractual remuneration that remains` |
| s 171ZZ21(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ22 text | claim-right / duty (the Part applies to persons employed by or under the Crown as to others) | a person employed by or under the Crown | the Crown as employer, or the person liable under the Part | `s 171ZZ22 the provisions of this Part apply to the person` |
| s 171ZZ23(1) | power / liability (with the concurrence of the Treasury; encoded as a gate, `regulations may modify this Part`) | the Secretary of State | a person employed on a ship, vessel, hovercraft or aircraft, outside Great Britain, or in continental shelf employment | `s 171ZZ23(1) regulations may modify this Part in its application to the person` |
| s 171ZZ23(2) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | the same persons | not encoded (inert 2) |
| s 171ZZ24(1) | none (a definition or counting rule) | - | - | `s 171ZZ24(1) the person is the employer of the employee`; `s 171ZZ24(1) the change is a modification` |
| s 171ZZ24(2) | none (a definition or counting rule) | - | - | `s 171ZZ24(2) the person is an employee` |
| s 171ZZ24(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ24(4) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ24(5) | none (a definition or counting rule) | - | - | `s 171ZZ24(5) the week convention`; `s 171ZZ24(5) the first day of the week containing the day` |
| s 171ZZ24(6) | none (a definition or counting rule) | - | - | `s 171ZZ24(6) the person's normal weekly earnings in pounds` |
| s 171ZZ24(7) | none (a definition or counting rule) | - | - | `s 171ZZ24(6) the person's normal weekly earnings in pounds` |
| s 171ZZ24(8) | none (a definition or counting rule) | - | - | `s 171ZZ24(6) the person's normal weekly earnings in pounds` |
| s 171ZZ24(9) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ24(10) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ24(11) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171ZZ24(12) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | the persons the regulations would bind | not encoded (inert 2) |
| s 171A(1) | claim-right / duty (whether the person is capable of work is to be determined under this Part) | the person whose capacity for work is in question | the decision-maker (these provisions name none) | `s 171A(1) this Part determines whether the person is capable or incapable of work`; `s 171A(1) the person is incapable of work` |
| s 171A(2) | power / liability (regulations may treat the person as capable of work if without good cause the person fails to give information or evidence) | the maker of the regulations (the section does not name them) | the person who fails to give the information or evidence | `s 171A(2) the person is treated as capable of work` |
| s 171A(2A) | none (the information or evidence includes what helps the person obtain work) | - | - | `s 171A(2A) the information or evidence is within subsection (2)(a)` |
| s 171A(3) | power / liability (regulations may treat the person as capable of work if without good cause the person fails to attend a medical examination) | the maker of the regulations (the section does not name them) | the person who fails to attend or submit to the examination | `s 171A(3) the person is treated as capable of work` |
| s 171A(4) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | persons who must show good cause | not encoded (inert 2) |
| s 171A(5) | none (information supplied is information relating to social security) | - | - | `s 171A(5) the information is information relating to social security` |
| s 171B(1) | claim-right / duty (where the person has been engaged in remunerative work for more than 8 of the 21 weeks, the own occupation test is to be applied) | the person whose capacity for work is in question | the decision-maker (these provisions name none) | `s 171B(1) the own occupation test is applicable` |
| s 171B(2) | none (the content of the own occupation test) | - | - | `s 171B(2) the person is incapable of work on the own occupation test` |
| s 171B(3) | claim-right / duty (a determination on the own occupation test is to be carried forward to the end of the spell or the 197th day) | the person whose capacity for work is in question | the decision-maker (these provisions name none) | `s 171B(3) the status of the own occupation test on the day` |
| s 171B(4) | none (a definition: a day of incapacity for work) | - | - | `s 171B(4) the day is a day of incapacity for work` |
| s 171B(5) | none (provisions to be disregarded for the section) | - | - | `s 171B(5) the provision is disregarded for the purposes of section 171B` |
| s 171B(6) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | persons whose work is tested | not encoded (inert 2) |
| s 171B(7) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | persons with more than one occupation | not encoded (inert 2) |
| s 171B(8) | power (not encoded: inert 2, a power to make regulations) | the Secretary of State | persons whose spell length or gap changes | not encoded (inert 2) |
| s 171C(1) | claim-right / duty (where the own occupation test is not applicable or has ceased to apply, a personal capability assessment is to decide) | the person whose capacity for work is in question | the decision-maker (these provisions name none) | `s 171C(1) the test that decides` |
| s 171C(2) | duty on the regulation-maker (provision shall be made defining a personal capability assessment; not encoded: inert 2) | persons to be assessed | the maker of the regulations (the section does not name them) | not encoded (inert 2) |
| s 171C(3) | power / liability (regulations may treat a person as incapable of work pending an assessment) | the maker of the regulations (the section does not name them) | the benefit authority and the person assessed | `s 171C(3) the person is treated as incapable of work in accordance with a personal capability assessment` |
| s 171C(4) | claim-right / duty (an assessment made before subsection (1) applies is to be as effective as a later one, except in prescribed circumstances) | the person assessed | the decision-maker (these provisions name none) | `s 171C(4) the earlier assessment is as effective as a later one` |
| s 171C(5) | power / liability (the Secretary of State may require the question to be determined afresh by a further assessment) | the Secretary of State | the person assessed | `s 171C(5) the Secretary of State may require the question to be determined afresh` |
| s 171D(1) | power / liability (regulations may treat a person as capable, or as incapable, of work) | the maker of the regulations (the section does not name them) | the person treated | `s 171D(1) the treatment of the person` |
| s 171D(2) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | persons who do prescribed work | not encoded (inert 2) |
| s 171E(1) | power / liability (regulations may disqualify a person, or treat the person as capable of work, for misconduct, refusing treatment, or breaking rules of behaviour) | the maker of the regulations (the section does not name them) | the person who has become incapable through misconduct or who fails without good cause | `s 171E(1) the person is disqualified for receiving a benefit, allowance or other advantage`; `s 171E(1) the person is treated as capable of work` |
| s 171E(2) | immunity / disability (a disqualification or treatment as capable of work lasts no more than 6 weeks) | the person disqualified or treated as capable | the maker of the regulations (the section does not name them) (cannot provide a longer period) | `s 171E(2) the period of the disqualification or treatment as capable of work is allowed` |
| s 171E(3) | power (not encoded: inert 2, a power to make regulations) | the maker of the regulations (the section does not name them) | persons who must show good cause | not encoded (inert 2) |
| s 171F(1) | immunity / disability (work undertaken as a councillor is disregarded) | the person who works as a councillor | the decision-maker (must disregard that work) | `s 171F(1) the work is disregarded in determining whether the person is capable or incapable of work` |
| s 171F(2) | none (a definition: "councillor") | - | - | `s 171F(2) the person is a councillor` |
| s 171F(3) | none (the work taken to include work for the bodies named) | - | - | `s 171F(3) the work counts as work undertaken as a councillor` |
| s 171F(4) | immunity / disability (a day in the pre-commencement period is treated as a day of incapacity) | the person | the decision-maker (must treat the day as incapacity) | `s 171F(4) the person is treated as having been incapable of work on the day` |
| s 171G(1) | none (a rule of application: where this Part does not apply) | - | - | `s 171G(1) this Part applies for the purpose` |
| s 171G(2) | none (definitions: "prescribed", "week") | - | - | `s 171G(2) the matter is prescribed`; `s 171G(2) the period is a week`; `s 171G(2) the week convention` |

## Marginal readings for a lawyer (ssc7)

The two readings the brief flags "for a lawyer, not for you to decide" are taken as the status quo:
(a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no;
(b) a prohibition or grant limited by its own wording does not.
Below is every branch that rests on one of them, by function; the other reading is stated for each group.
The `FALSE-kind` branches not listed under (a) are flat negatives or closed definitions ("means", "is not payable", "not less than", "not exceeding"), which reading (a) also counts as a no but which do not depend on inferring a negative from an "if".

### (a) A failed "if" counted as the text's no

The other reading: "if A then B" does not itself say "if not A then not B"; each branch below would answer `NOTHING` (the text is silent on the failed case), and a caller would have to take it as "not covered" rather than "no".

| function (file) | branch, with the words relied on |
| --- | --- |
| `s 171ZU(1) the claimant mother is entitled to statutory shared parental pay` (ssc7-12zc, line 117) | "Regulations may provide that, where all the conditions in subsection (2) are satisfied in relation to a person who is the mother of a child (“the claimant mother”), the claimant mother is to be entitled" (a... |
| `s 171ZU(3) the claimant is entitled to statutory shared parental pay` (ssc7-12zc, line 222) | "Regulations may provide that, where all the conditions in subsection (4) are satisfied in relation to a person (“the claimant”), the claimant is to be entitled" (a failed "where"; reading (a)) |
| `s 171ZU(12) V may vary the period or periods` (ssc7-12zc, line 397) | "where the conditions in subsection (13) are satisfied ... V may vary" (a failed "where"; reading (a)) |
| `s 171ZU(14) V may vary the number of weeks` (ssc7-12zc, line 444) | "where the conditions in subsection (15) are satisfied ... V may vary" (a failed "where"; reading (a)) |
| `s 171ZV(1) claimant A is entitled to statutory shared parental pay` (ssc7-12zc, line 555) | "Regulations may provide that, where all the conditions in subsection (2) are satisfied in relation to a person with whom a child is, or is expected to be, placed for adoption under the law of any part of th... |
| `s 171ZV(3) claimant B is entitled to statutory shared parental pay` (ssc7-12zc, line 654) | "Regulations may provide that, where all the conditions in subsection (4) are satisfied in relation to a person (“claimant B”), claimant B is to be entitled" (a failed "where"; reading (a)) |
| `s 171ZV(12) V may vary the period or periods` (ssc7-12zc, line 786) | "where the conditions in subsection (13) are satisfied ... V may vary" (a failed "where"; reading (a)) |
| `s 171ZV(14) V may vary the number of weeks` (ssc7-12zc, line 827) | "where the conditions in subsection (15) are satisfied ... V may vary" (a failed "where"; reading (a)) |
| `s 171ZY(7) the week falls within a relevant period` (ssc7-12zc, line 993) | "and is not afterwards excluded from such a period by a variation" (a failed "if"; reading (a)) |
| `s 171ZZ(2) the agreement authorising deductions is not void by virtue of subsection (1)(a)` (ssc7-12zc, line 1104) | "is not void by virtue of subsection (1)(a) if the employer" is authorised, or would be (a failed "if"; reading (a)) |
| `s 171ZZ6(2) the person satisfies the conditions` (ssc7-12zd, line 94) | "A person who satisfies the conditions in subsection (2) is entitled" (a failed paragraph (b), (c), (d) or (e); reading (a)) |
| `s 171ZZ6(3) the employee is a bereaved parent` (ssc7-12zd, line 174) | "an employee is a “bereaved parent” if the employee satisfies prescribed conditions as to relationship with a child who has died" (a failed "if"; reading (a)) |
| `s 171ZZ10(2) the agreement authorising deductions is not void by virtue of subsection (1)(a)` (ssc7-12zd, line 437) | "is not void by virtue of subsection (1)(a) if the employer" is authorised, or would be (a failed "if"; reading (a)) |
| `s 171ZZ16(1) the person is entitled to statutory neonatal care pay` (ssc7-12ze, line 68) | "A person who satisfies the conditions in subsection (2) and any condition prescribed under subsection (3) is entitled" (a failed condition; reading (a)) |
| `s 171ZZ20(2) the agreement authorising deductions is not void by virtue of subsection (1)(a)` (ssc7-12ze, line 453) | "is not void by virtue of subsection (1)(a) if the employer" is authorised, or would be (a failed "if"; reading (a)) |
| `s 171A(2) the person is treated as capable of work` (ssc7-xiia, line 52) | "if a person without good cause fails to provide that information or evidence, or to do so in the manner required, he shall be treated as capable of work" (a failed "if"; reading (a)) |
| `s 171A(3) the person is treated as capable of work` (ssc7-xiia, line 84) | "if he fails without good cause to attend for or submit himself to such examination, he shall be treated as capable of work" (a failed "if"; reading (a)) |
| `s 171E(1) the person is disqualified for receiving a benefit, allowance or other advantage` (ssc7-xiia, line 454) | "if—" ... "he has become incapable of work through his own misconduct" ... "he fails without good cause to attend for or submit himself to such medical or other treatment" ... "he fails without good cause to... |
| `s 171E(1) the person is treated as capable of work` (ssc7-xiia, line 473) | "if—" ... "he has become incapable of work through his own misconduct" ... "he fails without good cause to attend for or submit himself to such medical or other treatment" ... "he fails without good cause to... |

### (b) A grant or prohibition limited by its own wording, taken as not a no

The other reading: a grant or prohibition that applies "when", "where", "if" or for a stated period says no outside its limit; each branch below would then answer `JUST FALSE` where it now answers `NOTHING`.

| function (file) | branch, with the words relied on |
| --- | --- |
| `s 171ZU(10) a payment may be made in respect of the child` (ssc7-12zc, line 350) | a payment within the prescribed period is not barred here, and whether it is payable is for the other provisions |
| `s 171ZU(11) a payment may be made to the mother` (ssc7-12zc, line 363) | after the maternity pay period the bar no longer applies, and whether the pay is payable is for the other provisions |
| `s 171ZV(10) a payment may be made in respect of the child` (ssc7-12zc, line 744) | a payment within the prescribed period is not barred here, and whether it is payable is for the other provisions |
| `s 171ZV(11) a payment may be made to the person who became entitled to statutory adoption pay` (ssc7-12zc, line 757) | after the adoption pay period the bar no longer applies, and whether the pay is payable is for the other provisions |
| `s 171ZV(18) the placement counts as a placement for adoption` (ssc7-12zc, line 868) | the reading applies to "regulations made by virtue of subsection (17)" and to a placement with an approved foster parent |
| `s 171ZY(7) the week falls within a relevant period` (ssc7-12zc, line 995) | a week counts "if it falls within a period specified in a notice", and a week outside every specified period is not covered by that "if" |
| `s 171ZY(8) the week of the relevant period containing the day` (ssc7-12zc, line 1006) | "'week', in relation to a relevant period"; a day outside the relevant period is not in one of its weeks |
| `s 171ZY(2) statutory shared parental pay is payable for the week` (ssc7-12zc, line 1026) | the grant is for "each week falling within a relevant period, up to the number of weeks determined", and it is "Subject to the following provisions of this section" |
| `s 171ZY(3) the pay is payable for the week despite the intention to care` (ssc7-12zc, line 1044) | a week with the intention to care, or outside a relevant period, is for the grant in subsection (2) |
| `s 171ZY(4) the pay is payable for the week despite work for an employer` (ssc7-12zc, line 1059) | a week without that work, or outside a relevant period, is for the grant in subsection (2) |
| `s 171ZZ(1) the agreement is void to that extent` (ssc7-12zc, line 1087) | "void to the extent that it purports" (a) or (b); an agreement that purports neither is not covered by this subsection |
| `s 171ZZ3(1) regulations may modify this Part in its application to the person` (ssc7-12zc, line 1183) | the power is for a person who is, has been or is to be in one of the three classes |
| `s 171ZZ6(7) paragraph (c) of subsection (2) is omitted` (ssc7-12zd, line 221) | the omission is for a child who "dies before the day"; a later death is for (2)(c) itself |
| `s 171ZZ9(2) the pay payable for the weeks chosen in pounds` (ssc7-12zd, line 306) | the grant covers weeks "within the qualifying period" and a number "not exceeding the prescribed number of weeks" |
| `s 171ZZ9(6) the person is liable to pay for the statutory pay week` (ssc7-12zd, line 340) | liability for a week the other does not work is for s 171ZZ8, not this subsection |
| `s 171ZZ9(8) the pay is payable for the statutory pay week` (ssc7-12zd, line 366) | a week without that work is for the grant in subsection (2) |
| `s 171ZZ10(1) the agreement is void to that extent` (ssc7-12zd, line 420) | "void to the extent that it purports" (a) or (b); an agreement that purports neither is not covered by this subsection |
| `s 171ZZ13(1) regulations may modify this Part in its application to the person` (ssc7-12zd, line 516) | the power is for a person who is, has been or is to be in one of the three classes |
| `s 171ZZ16(7) paragraph (c) of subsection (2) is omitted` (ssc7-12ze, line 237) | the omission is for care that "starts before the day"; later care is for (2)(c) itself |
| `s 171ZZ19(2) the pay payable for the weeks chosen in pounds` (ssc7-12ze, line 322) | the grant covers weeks "within the qualifying period" and a number "not exceeding the prescribed number of weeks" |
| `s 171ZZ19(6) the person is liable to pay for the statutory pay week` (ssc7-12ze, line 356) | liability for a week the other does not work is for s 171ZZ18, not this subsection |
| `s 171ZZ19(8) the pay is payable for the statutory pay week` (ssc7-12ze, line 382) | a week without that work is for the grant in subsection (2) |
| `s 171ZZ20(1) the agreement is void to that extent` (ssc7-12ze, line 436) | "void to the extent that it purports" (a) or (b); an agreement that purports neither is not covered by this subsection |
| `s 171ZZ23(1) regulations may modify this Part in its application to the person` (ssc7-12ze, line 532) | the power is for a person who is, has been or is to be in one of the three classes |
| `s 171A(1) this Part determines whether the person is capable or incapable of work` (ssc7-xiia, line 31) | "save as otherwise expressly provided"; the provision that so provides answers |
| `s 171A(5) the information is information relating to social security` (ssc7-xiia, line 97) | the subsection speaks of "information supplied in pursuance of this section" |
| `s 171B(1) the own occupation test is applicable` (ssc7-xiia, line 112) | the subsection says when the test "is applicable" ("more than 8 weeks") and is not an "only where": s 171B(3) makes the test "remain applicable" for a person with 8 weeks or fewer who has a carried-forward d... |
| `s 171B(5) the provision is disregarded for the purposes of section 171B` (ssc7-xiia, line 316) | the subsection speaks only of provisions that treat a day as, or not as, a day of incapacity for work |
| `s 171C(3) the person is treated as incapable of work in accordance with a personal capability assessment` (ssc7-xiia, line 372) | the treatment lasts "until" an assessment has been carried out or the person falls to be treated as capable, and the subsection says nothing for a person outside the prescribed circumstances or conditions |
| `s 171C(5) the Secretary of State may require the question to be determined afresh` (ssc7-xiia, line 399) | the power is "in the case of a person who ... has been determined to be incapable of work in accordance with a personal capability assessment" |
| `s 171F(1) the work is disregarded in determining whether the person is capable or incapable of work` (ssc7-xiia, line 499) | the subsection disregards "work which that person has undertaken as a councillor" and says nothing of other work |
| `s 171F(4) the person is treated as having been incapable of work on the day` (ssc7-xiia, line 597) | the treatment is for "any day which falls in the pre-commencement period" meeting both (a) and (b) |
| `s 171G(1) this Part applies for the purpose` (ssc7-xiia, line 618) | any other purpose is for s 171A(1) |
| `s 171A(1) the person is incapable of work` (ssc7-xiia, line 669) | s 171A(1), "save as otherwise expressly provided" |

That is 19 branches under (a) and 34 under (b).

### Reading a result: FALSE and NOTHING (ssc7)

This is the rule of 2026-10-29 (assumed, not ruled by a lawyer), put in the terms of this row's subject.

**`JUST TRUE` and `JUST FALSE` are the text's own answers.**
In these Parts a "no" is one of four things, and each `FALSE-kind` comment quotes the words:

- a flat negative the text states: "statutory shared parental pay is not payable to a person in respect of a week falling within a relevant period if it is not the person's intention at the beginning of the week to care for the child" (s 171ZY(3)); "A person is not liable to pay ... in respect of any statutory pay week during any part of which the other works under a contract of service with the person" (ss 171ZZ9(6), 171ZZ19(6));
- a closed definition: "\"employee\" means ...", "\"neonatal care\" means care ...", "\"councillor\" means ...", "\"prescribed\" means prescribed by regulations", "\"week\" means any period of 7 days";
- a floor or ceiling the text puts in its own words: "not less than two" and "not less than 12" prescribed weeks, "at least 56 days" and "at least 68 weeks" for the qualifying period, "for such period not exceeding 6 weeks";
- a failed "if" or "where" or "who satisfies" inside the provision that holds it (reading (a), flagged in the next section): for example, when the conditions of s 171ZU(2) are not all met, s 171ZU(1) answers `JUST FALSE`; and for s 171ZZ6(1) and s 171ZZ16(1), when a condition fails.

So `JUST FALSE` on "am I entitled to statutory parental bereavement pay?" means: the Act's own conditions are not all met on the facts stated.

**`NOTHING` (or a named "text does not say" constructor) is "not covered", never "no".**
The reasons used in this row, each marked `NOTHING-kind (<why>)` on the branch:

- *points outside the text*: the weekly rate, the prescribed number of weeks, the prescribed conditions of relationship, the powers to modify or disapply conditions (ss 171ZW(1)(a), 171ZZ7(4), 171ZZ17(4)), and the "Regulations may provide that" of the entitlement itself (fork F1). An unanswered `NOTHING` here means: regulations decide, and the Act does not say what they decide.
- *silent*: the Act does not say which treatment prevails when regulations treat a person as both capable and incapable of work (s 171D(1)), nor which relevant week governs a person entitled under two of ss 164, 171ZA, 171ZB and 171ZL (s 171ZZ16(6)), nor what follows when a reduction exceeds the weeks of the period (s 171ZU(6)).
- *undefined term*: whether the 197th day is inside "until the 197th day" (s 171B(3)); an average over a relevant period of no weeks (s 171ZZ4(6)).
- *includes* and *list not closed*: a child stillborn at 24 weeks or fewer is not said to be a child, because s 171ZZ15(a) says "include"; "modifications" "includes additions, omissions and amendments"; the liability of s 171ZX(1) is "a liability of any person of whom" the claimant has been an employee, and s 171ZX(3) lets regulations add the Commissioners.
- *limited by its own wording*: a grant or prohibition that applies only where its own words say so; for example s 171B(1) says when the own occupation test is applicable (more than 8 weeks in the 21) and is silent for 8 weeks or fewer, s 171ZY(7) says when a week falls within a relevant period ("if it falls within a period specified in a notice"), and the bars of ss 171ZU(10), 171ZU(11), 171ZY(3), 171ZY(4), 171ZZ9(6) and 171ZZ9(8) (and their counterparts) say when pay is not payable and are silent about every other case. These are listed in the marginal-readings section as reading (b).

**A caller must never turn `NOTHING` into `FALSE`.**
In the seat layer, `NOTHING` is passed through: "the text alone does not answer" is never rendered as "you are not entitled".
Typed results carry the same split in their constructors, each asserted: `s 171B(3) the text does not say whether the test applies`, `s 171C(1) the text does not say which test decides`, `s 171D(1) regulations give both treatments` and `s 171D(1) no treatment under this subsection applies`.
`REFUSE` does not exist on the stable binary, so every "not covered" is a `NOTHING` or such a constructor, with an `#ASSERT` that it is returned.

## Seams (ssc7)

Each row is an input another part answers (or, for S35, an answer this part gives), named as `inputs/PLAN.md` names it where PLAN names it.
An input is a `GIVEN` of the function that needs it.
PLAN's seam register is section 5 (table at lines 293-330); the `ssc7` entry is lines 259-266.

| seam | input, as named in the modules | type | where used | taken from PLAN? |
| --- | --- | --- | --- | --- |
| S24 | `s 35(2) the maternity allowance period` | `Period` | s 171ZU(6) and the definition `s 171ZZ4(1) maternity allowance period` | yes |
| S25 | `s 120(2) the employment is in connection with continental shelf operations` | `BOOLEAN` | ss 171ZZ3(1)(c), 171ZZ13(1)(c), and 171ZZ23(1)(c) | S25 yes for ss 171ZZ3 and 171ZZ13; **s 171ZZ23 is not in PLAN's row** (line 4216 has the same words) |
| S26 | `s 5(1)(a) the lower earnings limit in force at the time in pounds` | `NUMBER` | the earnings condition of ss 171ZU, 171ZV, 171ZZ6(2)(d), 171ZZ16(2)(d) | **no: PLAN lists S26 for ss 164 and 171ZA, not for `ssc7`**; a seam PLAN lacks for this part |
| S27 | `s 35(3A) the number of weeks to which the maternity allowance period is reduced`; `s 165(3A) the number of weeks to which the maternity pay period is reduced` | `NUMBER` each | s 171ZU(6)(b) | yes (the week conventions of s 122(1) and s 165(8) are the core's, not inputs) |
| S28 | `s 171ZN(2A) the number of weeks to which the adoption pay period has been reduced` | `NUMBER` | s 171ZV(6)(b) | yes (s 171ZN(8)'s week is the core's) |
| S29 | `s 171ZN(2) the adoption pay period`; `s 165(1) the maternity pay period`; `s 35(2) the maternity allowance period` | `Period` each | the definitions in s 171ZZ4(1), and the "reduced by" arithmetic | yes |
| S30 | `s 171ZA(2) the relevant week`; `s 171ZB(2) the relevant week`; `s 171ZL(2) the relevant week` (and `the expected week of confinement` in place of `s 164 the relevant week`) | `Period` each | s 171ZZ16(6) | yes for three of the four; **not `s 164 the relevant week`** (PLAN difference 4 above) |
| S35 (answered here) | `s 171A(1) the person is incapable of work` | `MAYBE BOOLEAN` | s 171A(1), composed in the last section of `ssc7-xiia.l4` | yes, with a difference: PLAN names the seam as one `MAYBE BOOLEAN`; the answer here is a function that returns `MAYBE BOOLEAN` from nine arguments (the Part applies for the purpose; the Part determines the question; the three "treated as capable" results; the typed treatment of s 171D(1); the typed test of s 171C(1); the own occupation test result; the personal capability assessment result), each argument itself computed by a function of this module |

S36 is `ssc4`'s `s 94(6)`, not mine; s 171G(1)(a) is where this Part says it does not apply for Part V purposes.

**Seams `ssc7` took that PLAN's seam table does not list.**

| input | what it stands for | where used |
| --- | --- | --- |
| `s 6 the person is liable to pay secondary Class 1 contributions in relation to earnings of the employee`; `s 6 the person would be liable but for the condition in section 6(1)(b)`; `s 6 the person would be liable but for the employee being under 16` | s 6, the liability that defines "employer" | the `employer` definitions of ss 171ZZ4(1), 171ZZ14(1), 171ZZ24(1) |
| `s 173(a) the person is under 18`; `s 173(a) the person is under 16` | the keel's age answer (PLAN, lines 18, 48, 112 and the K2 row at line 158: ss 172, 173, 174, 177(2) "arrive as inputs") | "child" in s 171ZZ14(1) (under 18), "employee being under the age of 16" in the employer definitions |
| `WRA 2012 s 63(3) the day on which it comes fully into force` | the date of a commencement in another Act | ss 171ZZ6(7) and 171ZZ16(7) |
| `the person has general earnings as defined by section 7 of the Income Tax (Earnings and Pensions) Act 2003`; `the person has earnings within the meaning of Parts 1 to 5` | the earnings limb of "employee" | ss 171ZZ4(2); 171ZZ14(2) and 171ZZ24(2) |
| `(o) the person is an employee within the meaning of the Employment Rights Act 1996` and its `(p)` twin | a borrowed term | the conditions of ss 171ZU(2), 171ZU(4), 171ZV(2), 171ZV(4) |
| `the body is a local authority within the meaning of section 105(1) of the Children Act 1989`; `the person is a local authority foster parent within the meaning of section 105(1) of the Children Act 1989`; `placed under section 22C of the Children Act 1989` | borrowed terms | s 171ZZ4(1), s 171ZV(18) |

**What changes if a regulation or an order changes.**
The seat asks every figure that regulations supply as a number the person states, and says so in the question: the weekly rate, the prescribed number of weeks, the prescribed length of continuous employment, the lower earnings limit, and the number of weeks prescribed under s 171ZU(6)(a)(ii) and s 171ZV(6)(a)(ii).
A change in those figures changes the answers the seat gives only through the number the person types; no figure is built into any module.
The numbers in the Act's own words (26 weeks, 8 weeks, 28 days, 7 days, 24 weeks, 56 days, 68 weeks, 6 weeks, 4 days, 197 days, 21 weeks) are built in, and a Minister's power to change one of them (s 171B(8) for the 4 days and 8 weeks of s 171B(3)) is a gate: the answer is `NOTHING` when the gate is true.

## The seat layer (ssc7)

**The seat** is a person who works, is self-employed, or claims a benefit or statutory pay in Great Britain.
`ssc7-seat.l4` imports the four layer-1 modules and asks 30 questions (below), each named "Under section N, ..." with the Act's own numbering, each with `@export` and `@desc`, plain inputs (yes/no, numbers, dates, or a module's short list of choices), and `§` groups by Part.
A question builds the module's records in a `WHERE` from the plain inputs and calls the module's rule; it restates no rule.
`ssc7-cases-seat.l4` asks each question with the facts a person in the seat would state (141 assertions written, 141 satisfied).

Provisions that address only an official, or only the maker of regulations, have no question; they are in layer 1 for what they decide.
Parts of the text that mean something to the person only through a rule already asked are not asked twice (the condition sets of ss 171ZU(2) and (4) are inputs to the questions on s 171ZU(1) and (3)).

**Defaults the seat takes, each a departure to know about.**

1. A fact the person states as a yes/no stands for a "prescribed" condition: the question says so in its `@desc`, and the person answers for the regulations that apply to them.
2. Regulations that supply a figure (weekly rate, prescribed number of weeks, prescribed length of continuous employment, the lower earnings limit, the number of weeks of s 171ZU(6)(a)(ii) and s 171ZV(6)(a)(ii)) are asked as numbers the person states.
3. Whether regulations exist that give the shared parental pay entitlement (fork F1) is asked as a yes/no.
   If the person answers that they do not, the question answers `NOTHING` ("the text alone does not answer"), not "no".
4. A record field that the rule called never reads is given a fixed placeholder, with a comment where it is built (the person's date of birth, sex, marital status and pensionable age, and the employment's kind and place, in the bereavement and neonatal questions).
5. For s 171B(3) the seat models **one unbroken series** of days of incapacity, from the day the own occupation test was determined to apply to the day in question.
   Breaks of up to 8 weeks between spells need the module's list rule, which takes a list of dates; the seat does not ask for such a list.
6. Every answer that is `MAYBE` in the module is `MAYBE` in the question; a caller must not turn `NOTHING` into "no".

**What the seat cases caught.**
The first draft of the composition for s 171A(1) took s 171D(1) as one `MAYBE BOOLEAN`.
A seat case in which regulations treated the same person as both capable and incapable of work returned the test's answer instead of "not covered", because both treatments had collapsed to `NOTHING` and fallen through.
The fix is the typed `s 171D(1) treatment of the person` (treated as capable / treated as incapable / no treatment under this subsection applies / regulations give both treatments), used by the composition, the XIIA tests, the seat and the cases.
It is in the module's tests now (finding 9).

**The questions.**

1. Under section 171ZU(1), am I entitled to statutory shared parental pay as the mother of the child?
2. Under section 171ZU(3), am I entitled to statutory shared parental pay as the mother's partner or the child's other parent?
3. Under section 171ZU(6), what is the greatest number of weeks of statutory shared parental pay I can claim after maternity pay or allowance?
4. Under section 171ZV(6), what is the greatest number of weeks of statutory shared parental pay I can claim after adoption pay?
5. Under section 171ZV(1), am I entitled to statutory shared parental pay as the first adopter of the child?
6. Under section 171ZV(3), am I entitled to statutory shared parental pay as the second adopter of the child?
7. Under section 171ZU(11), may a payment of shared parental pay be made to me before my maternity pay period has ended?
8. Under section 171ZV(11), may a payment of shared parental pay be made to me before my adoption pay period has ended?
9. Under section 171ZU(12), may I vary the period or periods in which I intend to claim shared parental pay?
10. Under section 171ZU(14), may I vary the number of weeks for which I intend to claim shared parental pay?
11. Under section 171ZX(1), is my employer liable to pay me shared parental pay?
12. Under section 171ZY(2), is shared parental pay payable to me for a given week?
13. Under section 171ZY(3), is shared parental pay payable to me for a week if I do not intend to care for the child?
14. Under section 171ZY(4), is shared parental pay payable to me for a week in which I work for an employer?
15. Under section 171ZZ(1), is my agreement void to the extent that it limits my shared parental pay or makes me pay my employer's costs?
16. Under section 171ZZ6(1), am I entitled to statutory parental bereavement pay?
17. Under section 171ZZ9(2), how much parental bereavement pay is payable to me for the weeks I choose?
18. Under section 171ZZ9(8), is parental bereavement pay payable to me for a week in which I work for another employer?
19. Under section 171ZZ15(a), does my stillborn child count as a child for parental bereavement pay?
20. Under section 171ZZ16(1), am I entitled to statutory neonatal care pay?
21. Under section 171ZZ19(2), how much neonatal care pay is payable to me for the weeks I choose?
22. Under section 171ZZ19(8), is neonatal care pay payable to me for a week in which I work for another employer?
23. Under section 171ZZ16(4), is my child's care neonatal care?
24. Under section 171A(1), am I incapable of work on a given day?
25. Under section 171B(1), does the own occupation test apply to me?
26. Under section 171B(3), does the own occupation test still apply to me on a given day?
27. Under section 171B(4), is a given day a day of incapacity for work for me?
28. Under section 171E(2), may my disqualification or treatment as capable of work last a given number of days?
29. Under section 171F(2), am I a councillor whose work as a councillor is disregarded?
30. Under section 171G(1), does the Part on incapacity for work apply for my purpose?

## What the text turns out to say (ssc7)

Numbered findings from reading and encoding lines 3718-4330.
Each says what the text says, what that did to the encoding, and where it is tested.

1. **Part 12ZC's entitlement does not exist in the Act itself.**
   Ss 171ZU(1), 171ZU(3), 171ZV(1) and 171ZV(3) each begin "Regulations may provide that, where all the conditions in subsection (2) [or (4)] are satisfied ..., the claimant ... is to be entitled".
   The Act sets out the conditions and leaves the grant to regulations; so the answer "am I entitled to shared parental pay?" cannot be `TRUE` from the Act alone.
   Part 12ZD's s 171ZZ6(1) and Part 12ZE's s 171ZZ16(1), by contrast, say "A person who satisfies the conditions ... is entitled".
   (Fork F1; tests in `ssc7-tests-12zc.l4`.)
2. **Regulations can switch off or reshape the conditions in all three Parts.**
   S 171ZW(1)(a) lists every paragraph of ss 171ZU(2), 171ZU(4), 171ZU(13), 171ZU(15) and the same of s 171ZV that "do not have effect, or have effect subject to prescribed modifications, in such cases as may be prescribed"; s 171ZZ7(4)(a) and (b) and s 171ZZ17(4)(c) and (d) do the same for Parts 12ZD and 12ZE.
   Each entitlement function therefore has a gate input, and the answer is `NOTHING` when it is true.
3. **No amount is in the ranges.**
   The weekly rate is "such fixed or earnings-related weekly rate as may be prescribed by regulations" in ss 171ZY(1), 171ZZ9(1) and 171ZZ19(1); the daily rate is one seventh of it (ss 171ZY(6), 171ZZ9(10), 171ZZ19(10)).
   The rate is an input of type `MAYBE NUMBER`; with none given the answer is `NOTHING`.
   What the Act does compute from the figures it is given: the number of weeks of shared parental pay (s 171ZU(6)), the pay for the weeks chosen (the rate times the weeks, ss 171ZZ9(2) and 171ZZ19(2)), the daily rate, and a person's normal weekly earnings (s 171ZZ4(6)).
4. **The numbers that are in the Act's own words** (built in, each tested on both sides): 26 weeks of employment and 8 weeks of earnings for the conditions of ss 171ZZ6(2) and 171ZZ16(2); "not less than two" prescribed weeks for bereavement pay (s 171ZZ9(3)) and "not less than 12" for neonatal care pay (s 171ZZ19(3)); a qualifying period of at least 56 days from the date of the child's death (s 171ZZ9(5)) and at least 68 weeks from the date of the child's birth (s 171ZZ19(5)); neonatal care that starts before the end of a period of 28 days beginning with the day after the birth (s 171ZZ16(4)) and lasts at least seven days (s 171ZZ16(2)(a)(ii)); a stillbirth after twenty-four weeks (s 171ZZ15(a)); a disqualification of no more than 6 weeks (s 171E(2)); and, in Part XIIA, more than 8 of the 21 weeks (s 171B(1)), a spell of 4 or more consecutive days, a gap of no more than 8 weeks, and the 197th day (s 171B(3)).
5. **Parts 12ZD and 12ZE are twins, and Part 12ZC's tail is a third copy.**
   Compared line by line with the quotation marks, pay names and section numbers normalised: Part 12ZD ss 171ZZ7-171ZZ13 and Part 12ZE ss 171ZZ17-171ZZ23 differ only in s 171ZZ17(4) (Part 12ZE has two extra powers, on more than one child and on care on separate occasions, so the lettering shifts), s 171ZZ18(1) ("subsection (2)(b) and (e)" against "subsections (2)(b) and (3)"), s 171ZZ18(3) ("Her Majesty's" against "His Majesty's"), s 171ZZ19(3) ("two" against "12") and s 171ZZ19(5) (56 days from death against 68 weeks from birth); the opening words of ss 171ZZ9(1) and (2) differ only in the name of the pay.
   Part 12ZC's ss 171ZZ-171ZZ3 and Part 12ZD's ss 171ZZ10-171ZZ13 differ only in s 171ZZ(2) ("For the avoidance of doubt," opens it in Part 12ZC) and s 171ZZ1(1) ("is not to affect" against "does not affect").
   Part 12ZD's s 171ZZ14 and Part 12ZE's s 171ZZ24 differ in that only the first defines "child" and in "Her" against "His" Majesty's in subsection (12).
   The modules of Parts 12ZE and the tail of Part 12ZC were generated from Part 12ZD's with the differences re-written by hand (`work/tr_ze.py`, `work/tr_zc_tail.py`), so the tests are parallel.
6. **"Employee" does not mean the same earnings in every Part.**
   S 171ZZ4(2) says "with general earnings (as defined by section 7 of the Income Tax (Earnings and Pensions) Act 2003)"; ss 171ZZ14(2) and 171ZZ24(2) say "with earnings (within the meaning of Parts 1 to 5)".
   Each Part asks the borrowed fact in its own words (fork F4).
7. **Part XIIA is silent on the 197th day itself** (fork F5).
   "Until the 197th day of incapacity for work in that spell" does not say whether the test applies on that day; s 171A(1) (seam S35) therefore answers `NOTHING` for a person on the own occupation test on exactly that day.
8. **Section 171B(1) is silent for 8 weeks or fewer, and s 171C(1) takes it up.**
   S 171B(1) says the test "is applicable" when the weeks exceed 8; it does not say it is not otherwise.
   S 171C(1) then speaks of a test that "is not applicable, or has ceased to apply", so the rule that decides which test applies reads s 171B(3)'s carry-forward as well (fork F8).
9. **Section 171D(1) can leave two treatments standing.**
   "Regulations may provide that a person shall be treated as capable of work, or as incapable of work, in such cases or circumstances as may be prescribed": the text does not say which prevails when both are prescribed for the same person, nor against ss 171A(2), 171A(3) and 171E(1).
   Both cases are `NOTHING` (silent), asserted.
   The seat cases found that the first composition lost this; see the seat section.
10. **A person entitled under more than one of ss 164, 171ZA, 171ZB and 171ZL has no stated relevant week.**
    S 171ZZ16(6) gives a relevant week for each entitlement and for "any other case"; it does not say which governs when the weeks differ.
    The function answers `NOTHING` (silent), asserted.
11. **"Councillor" in s 171F(2) names "a district council" in both countries.**
    Limb (a) (England and Wales) and limb (b) (Scotland) each include "district council".
    The definition is encoded by country, so a district council counts in the country whose limb names it and is `JUST FALSE` under the other.
12. **The rendering has slips, which the quotations carry.**
    "separate con-tracts of service" (line 4169, a hyphenation break); "remunerative work\"" with an opening curly and a closing straight quote (line 4281); a straight apostrophe in "child's death" (line 4061) and a curly one in "child’s birth" (line 4188); "Her Majesty's" in some sections and "His Majesty's" in others ("Her" at lines 3933, 4010, 4052 and 4125; "His", with a curly apostrophe, at lines 4179 and 4251); and the sub-paragraph markers of the `employer` definitions are missing, so "under section 6 is liable ..., or" and "would be liable ... but for—" and its two limbs appear as bare lines (lines 3976-3980 for s 171ZZ4(1)).
    None changes an answer; they are the reason a quotation may not match the official wording.
13. **The dates the Act leaves to another Act are inputs.**
    Ss 171ZZ6(7) and 171ZZ16(7) switch off a paragraph for events "before the day on which section 63(3) of the Welfare Reform Act 2012 comes fully into force"; the day is an input of type `DATE`.

## What the stable binary does not accept (ssc7)

Binary: `l4-stable-98`, version 1.6.98 (main, 7689b0d, 2026-10-19).
Each row below was reproduced with a one-file probe on 2026-11-04, and the message is the binary's own.

| construct | what the binary says | what I did |
| --- | --- | --- |
| `REFUSE` | "I could not find a definition for the identifier REFUSE" | every "not covered" is a `NOTHING` or a named constructor, asserted |
| `YMD` | "I could not find a definition for the identifier YMD" | `Date d m y` from `IMPORT daydate`, and no `YMD` shim of my own |
| `length` on a list (with `IMPORT prelude`) | "I could not find a definition for the identifier length" | recursion over a list (`WHEN EMPTY` / `WHEN x FOLLOWED BY rest`), and the prelude's `sort`, `nub`, `map` and `filter` |
| `sort`, `map`, `filter`, `nub`, `count`, `sum`, `any` and `all` without `IMPORT prelude` | each is "not found" without the import (and `sort` and `map` check with it) | every module starts `IMPORT prelude` |
| `TYPICALLY` on a record field | a parse error on the token after `TYPICALLY` | not used |
| a lambda as the first argument of `map` or `filter`, unparenthesised: `map GIVEN x YIELD x xs` | "unexpected GIVEN" | `map (GIVEN x YIELD x) xs` |
| a chained `ELSE IF` whose `THEN` is on its own line at the column of the `ELSE` | "incorrect indentation (got 10, should be greater than 10)" at the `THEN` | an `ELSE` followed by an indented block, or a parenthesised `ELSE (IF ...)` |
| a record literal as an argument, unparenthesised: `` `s 1 g` Rec 3 `` | "expects 1 argument, but you are applying it to 2 arguments" | `` `s 1 g` (Rec 3) `` |
| `Day` applied to a genitive without brackets: ``Day `a period`'s `the last day` `` | "There are multiple definitions for the identifier Day" | `Day (p's `the last day`)` |
| asserting the outcome of a `#TRACE` | no count in `check.sh`: the run prints `FULFILLED` and `check.sh` counts only `#ASSERT`s | the same duty is also a decision function (`s 171ZX(1) the person is liable to make payments ...`, `s 171ZZ8(1) ...`, `s 171ZZ18(1) ...`) that carries the assertions; the three `#TRACE`s were compared by hand on both binaries |

Two things I noted earlier in the run and could not reproduce in a final one-file probe, so I do not list them as limits of the binary: a genitive after a backticked name (`` `s 165(1) the maternity pay period`'s `the last day` ``) and a `CONSIDER` on a function application (`CONSIDER sort (map (GIVEN x YIELD x) xs)`) both checked cleanly when written alone.
The modules bind such a value in a `WHERE` first and `CONSIDER` the bound name; that form compiles in every context I used it in.

The brief's own list (no `BECAUSE` outside `LEST BREACH`, no `#ASSERT REFUSED`, sets and section-level `GIVEN` absent, a continuation line of an `#ASSERT` rejected, a leading `NOT` parsing as `NOT (a AND b)`) I took as given and did not test; I used none of those forms, parenthesised every `NOT`, and kept each `#ASSERT` on one line.
One probe did suggest the continuation rule may be narrower than stated: an `#ASSERT` whose right-hand side sat on an indented second line checked and was satisfied.

`MUST` with no `WITHIN` parses, and `#TRACE` of such a duty followed by the party's action prints `FULFILLED`; the three regulative rules in this range carry no deadline because the text gives none.

## What `check.sh` prints (ssc7)

Run from this folder on 2026-11-04 with `L4=.../bin/l4-stable-98 L4_MAIN=.../bin/l4-main-108 ./check.sh`; exit 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc7-12zc.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-12zd.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-12ze.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-cases-seat.l4                             0       141       0        0         0 |      0       141       0        0  same
ssc7-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-tests-12zc.l4                             0       353       0        0         0 |      0       353       0        0  same
ssc7-tests-12zd.l4                             0       164       0        0         0 |      0       164       0        0  same
ssc7-tests-12ze.l4                             0       147       0        0         0 |      0       147       0        0  same
ssc7-tests-xiia.l4                             0       173       0        0         0 |      0       173       0        0  same
ssc7-xiia.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (11 modules)                             0       978       0        0           |      0       978       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**The baseline numbers it replaced.**
The first full run of this session, before Part XIIA's composition was changed (finding 9), before the seat and its cases existed, and before the three added assertions on s 171ZZ6(2)(a), covered 9 modules with 824 satisfied assertions (12zc 353, 12zd 161, 12ze 147, xiia 163) and 0 failed, refused or errored; the run above covers 11 modules with 978 satisfied (12zd 164, xiia 173, the seat cases 141 more) and the same zeros.
The first run's output, for the record:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ssc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ssc7-12zc.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-12zd.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-12ze.l4                                   0         0       0        0         0 |      0         0       0        0  same
ssc7-tests-12zc.l4                             0       353       0        0         0 |      0       353       0        0  same
ssc7-tests-12zd.l4                             0       161       0        0         0 |      0       161       0        0  same
ssc7-tests-12ze.l4                             0       147       0        0         0 |      0       147       0        0  same
ssc7-tests-xiia.l4                             0       163       0        0         0 |      0       163       0        0  same
ssc7-xiia.l4                                   0         0       0        0         0 |      0         0       0        0  same
TOTAL (9 modules)                              0       824       0        0           |      0       824       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Files, and how to rebuild (ssc7)

Layer 1 (the law): `ssc7-12zc.l4` (ss 171ZU-171ZZ5), `ssc7-12zd.l4` (ss 171ZZ6-171ZZ15), `ssc7-12ze.l4` (ss 171ZZ16-171ZZ24), `ssc7-xiia.l4` (ss 171A-171G).
Tests: `ssc7-tests-12zc.l4` (353 assertions and a `#TRACE`), `ssc7-tests-12zd.l4` (164 and a `#TRACE`), `ssc7-tests-12ze.l4` (147 and a `#TRACE`), `ssc7-tests-xiia.l4` (173).
Layer 2 (the seat): `ssc7-seat.l4` (30 questions), `ssc7-cases-seat.l4` (141 assertions).
Notes: `NOTES.md`, `PROGRESS.md`.
Supplied and unchanged: `ssc-core.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh`.
There is no `NEEDS-CORE.md`: no type or constructor the core lacks was needed (every "not covered" type is declared under the `s N` label of its own provision).

**Generated files.**
The `ssc7-*.l4` files are built by `work/build.py` from `work/src/*.l4.in`, which are written by hand with `@@Q a b` placeholders that the builder expands into `-- src:N | text` lines copied mechanically from the raw text (each run of white space is collapsed to one space and the text is NFC-normalised; nothing else is changed).
Parts of Parts 12ZC and 12ZE are generated by scripts in `work/` (`gen_zc.py` for the condition sets of ss 171ZU and 171ZV, `tr_zc_tail.py` and `tr_ze.py` for the parallel sections, `gen_seat.py` and `gen_seat_cases.py` for the seat).
`work/` is scratch, not shipped; the `.l4` files in this folder are the deliverable.

**Rebuild and re-check** (from this folder, with `L4` and `L4_MAIN` set to the two binaries):

```
python3 -I ../../../work/build.py                      # writes the ssc7-*.l4 files
L4=<l4-stable-98> L4_MAIN=<l4-main-108> ./check.sh
python3 -I srcrefs.py check --refs   ../../../inputs/ukpga-1992-4.txt ssc7-*.l4
python3 -I srcrefs.py check --strict ../../../inputs/ukpga-1992-4.txt ssc7-*.l4
```
