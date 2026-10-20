# Banking Act 1959 — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the
design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no
independent test pass, no human gate. Not for public use as advice.

One module, `ba-depositor.l4`, holds the rules and the exported questions (each with
`@export` and `@desc`). One case file, `ba-cases-depositor.l4`, is built by the
scratchpad generator `gen_banking-act-1959_baseline.py`. Its expected values were
written by hand from the text.

There was no first-pass encoding of this Act to replace.

## Edition

Banking Act 1959, compilation register id C2026C00104, retrieved 13 October 2026, as
deposited at `../../registers/source-bundle/C1959A00006.txt`.

The **Banking Regulation 2016 is not deposited**. It sets:

- the s 16AG limit per account-holder per ADI;
- the s 16AF clearance adjustment;
- the accounts prescribed for ss 5(4)(a), 5(7) and 16AH(5);
- the s 69 variations (a longer inactivity period, accounts in or out, the reporting
  threshold, and the interest on repayment).

Each of these is an input. The lives use a limit of **$250,000**. That figure is an
input value taken from the encoding plan, not from any deposited text.

## Checks

- `ba-cases-depositor.l4`: 69 assertions written, 69 satisfied, 0 errors, 0 warnings.
- `ba-depositor.l4`: checks with no errors or warnings.
- Both were run with the stable `l4` from VS Code extension 1.6.98.
- Spot check: two expected values altered on a scratch copy, and both failed.

## Seat

**The depositor.** That is the account-holder of a deposit account with an ADI. In the
lives it is Chloe, aged seven, with a children's savings account. Division 2AA is
written about what the Minister may declare and what APRA must pay. The depositor is
the person the scheme exists for, and the one who asks "is my money safe?". So the
encoding asks:

- `Am I an account-holder`
- `Is my account protected`
- `Can the scheme be switched on for my bank`
- `Is my bank a declared ADI`
- `Can the declaration be revoked`
- `My share of this account before the limit`
- `What is the most I can be paid at this bank`
- `How much does APRA pay me`
- `Is all my protected money covered`
- `How much can I still claim from the bank`
- `How may I be paid`
- `Can APRA open an account for me without my consent`
- `Must APRA open an account of the same kind for me`
- `Must APRA send me a statement`
- `Is my account a children's account`
- `Is my money unclaimed`
- `Will my money go to the Commonwealth`
- `How much do I get back`

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The
  instrument, the Banking Regulation 2016, is not deposited, so its numbers are
  inputs.
- **The actors the text names.** Followed: the account-holder, joint account-holders,
  the ADI, the Minister, APRA, a Banking Act statutory manager, the Treasurer.
- **A judgment handed to someone else, answered conditionally.**
  - The Minister's choice to declare an ADI is asked as a fact.
  - The Treasurer's satisfaction under s 69(7) is asked as a fact.
  - APRA's s 16AG(3) split of the limit between accounts is not guessed. The residual
    claim is worked out across all of the depositor's accounts at the bank together.
- **The Act's own definitions worked out from facts; borrowed terms asked as facts.**
  - Worked out from facts: account-holder, declared ADI, protected account,
    children's account, unclaimed moneys.
  - Asked as facts: whether the bank is an ADI or a foreign ADI (a matter of record
    under s 9), the net credit balance, and the 30 June end of the financial year.
- **One case is the text's natural unit.** The unit is one account-holder with one
  ADI, because the s 16AG limit applies per account-holder per ADI. The accounts are
  given as a list.
- **The Act's own terms, each glossed.** Followed.
- **Operative sections in; machinery out.** Followed. The rest of the Act
  (authorisation, prudential supervision, statutory management, directions) addresses
  ADIs and APRA and gives a depositor nothing to claim.

## The lives

| Event | Decision it asks | Answer here |
|---|---|---|
| chloe c012 (2010-03-20), a children's savings account with her mother as signatory: "Are her deposits protected?" | `Is my account protected`, `How much does APRA pay me`, `Am I an account-holder`, `Is my money unclaimed` | Yes, protected. If her bank failed and were declared, APRA would pay her the balance plus accrued interest: $502 on the assumed figures, well under the $250,000 input limit, so nothing is left to claim from the bank. Chloe is the account-holder. Her mother, a signatory whose name the account is not in, is not. Her account is a children's account, so it never becomes unclaimed moneys, even after eight years untouched. |

The scenario states no balance, bank or interest. The cases assume a $500 balance,
$2 of accrued interest, and an account in Chloe's name, in Australian dollars,
repayable on demand, with an ADI. The failure is hypothetical.

## Why this scope

The seat and the one life event ask whether a child's deposits are safe. That is
Division 2AA, with s 5's definitions behind it. Section 69 is included because it is
the other provision that decides what happens to a depositor's money without the
depositor acting, and it has an exclusion for exactly Chloe's kind of account.

Left out:

- **s 16AE.** Advice to the Minister.
- **ss 16AIA-16AIB.** How APRA works out a transferred liabilities determination.
  Only its effect on the depositor (s 16AIC(3)) is encoded.
- **Subdivision D (administration) and Subdivisions F and G** (disclosure, and
  competition-law exceptions).
- **Subdivision E.** It addresses the liquidator. The residual claim is encoded from
  s 16AI instead.
- **The pooled trust rule of s 16AF(3).** The trustee is the single account-holder,
  which the encoding already gives.
- **Set-off under Corporations Act s 553C.**
- **The ADI's offences under s 69.**

## What the Act turns out to say

1. **The scheme is not automatic.** The Minister "may declare" that Subdivision C
   applies to an ADI, and only if APRA has applied for it to be wound up or a
   statutory manager is in control (s 16AD(1)). The scheme is switched on bank by bank.
   Asserted.
2. **It cannot be switched on for a foreign ADI** (s 16AD(1) note, s 11E). Asserted.
3. **It cannot be switched off.** "The Minister cannot revoke a declaration"
   (s 16AD(5)). Asserted.
4. **The payment is the balance plus interest accrued but not credited**, adjusted
   under the regulations for clearance of transactions (s 16AF(1)). Asserted.
5. **Joint accounts are split equally.** Each holder gets "an equal share" of what a
   sole holder would get (s 16AF(2)), and each share counts against that holder's own
   limit. Asserted.
6. **One limit per person per bank.** It applies across all of a person's protected
   accounts with "a particular declared ADI" (s 16AG(1)), and the amount is set by
   regulation. Asserted with the $250,000 input.
7. **Above the limit, the depositor still claims.** APRA takes over the depositor's
   claim against the bank only "to the extent of" the entitlement (s 16AI(1)). The
   rest stays the depositor's claim in the winding up. Asserted.
8. **Foreign-currency accounts are not protected** on and after 12 October 2011,
   unless the bank was already a declared ADI on that day (s 5(5)). Asserted.
   Chloe's account was opened in 2010, before that date. It is in dollars, so this
   does not touch her.
9. **APRA can open a bank account in your name without asking** (s 16AH(3)-(4)), but
   not with a declared ADI. Asserted.
10. **A statement is due within 14 days after the financial year** in which you were
    paid (s 16AHA(2)). Asserted.
11. **A children's account is never unclaimed moneys** (s 69(1A)(b)). Whether an
    account is a children's account turns on its terms and on the holder being under
    18 *when it was opened* (s 69(12)). Asserted.
    INFERENCE, not asserted: such an account stays out of s 69 after the child turns
    18 for as long as its terms still require a holder under 18. What the terms say
    then is not in the deposit.
12. **Seven years untouched makes other money unclaimed.** Fees debited and interest
    credited do not count as operating the account (s 69(1)-(2)). Asserted.
13. **The money can be kept from the Commonwealth.** It goes to the Commonwealth by the
    end of March after the year unless the depositor uses the account, or tells the
    bank to treat it as active, before the bank's statement (s 69(3)(c)-(d), (5)).
    Asserted.
14. **The money can be got back.** It is repaid through the bank, with interest from
    1 July 2013 under the regulations, if the Treasurer is satisfied (s 69(7), (7AA)).
    Asserted.
15. **A signatory is not an account-holder.** The definition turns on holding the
    account "in its name" (s 5(1)). On that reading, Chloe's mother, as signatory, is
    not an account-holder of Chloe's account. INFERENCE from the words. Asserted.

## What would need doing before this is worth anything

- Deposit the Banking Regulation 2016 and replace the inputs with its figures: the
  limit, the clearance rules, the prescribed accounts, and the s 69 settings.
- Read the law as it stood in March 2010 for c012. The deposit is the 2026
  compilation, and whether the limit or the definitions differed in 2010 cannot be
  answered from it.
- Encode Subdivision E, the liquidator's handling of the residual claim, and the
  Corporations Act set-off, if a life ever has a balance over the limit.
- An independent test pass, and the human gates.
