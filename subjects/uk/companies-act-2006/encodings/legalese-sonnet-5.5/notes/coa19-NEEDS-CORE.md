# NEEDS-CORE (coa19: ss 859A to 894)

Constructors this part wanted in the core's `Party` and did not find.
It could not extend the core type from another module, so it declared small types of its own under its `s ...` prefix and used those; the lead may hoist the constructors and delete the local types.

Core `Party` (`coa-core.l4`, lines 85-101) has: `Company`, `Director`, `Shadow director`, `Company secretary`, `Member`, `Subscriber to the memorandum`, `Officer in default`, `Auditor`, `Creditor`, `Debenture holder`, `Person with significant control`, `Registrar`, `Secretary of State`, `Court`, `Takeover Panel`, `Competent authority`.

| wanted in `Party` | where the text uses it | the local type that stands in for it |
| --- | --- | --- |
| a liquidator of a company | s 859H(3)(a), s 874(1), s 889(1): a charge is void against "a liquidator" | `s 859H(3) party against whom the charge may be void`, `s 874(1) party against whom the charge may be void`, `s 889(1) party against whom the charge may be void` (in `coa19-a1-after.l4`, `coa19-ch1-registrar.l4`, `coa19-ch2-scotland.l4`) |
| an administrator of a company | the same three provisions | the same three types |
| the person who obtains an order for the appointment of a receiver or manager, or appoints one under an instrument | s 859K(2), s 871(1): the person who must give notice to the registrar within 7 days | `s 859K party` in `coa19-regulative.l4` (it also carries the company and the registrar, so that one DEONTIC type serves every rule in that module) |
| a person interested in a charge | ss 859A(2), 859F(3), 859J(1), 860(2), 878(2): "the company or a person interested in the charge" | plain BOOLEAN inputs ("I am the company or a person interested") |
| the Registrar of Titles and the Registrar of Deeds (Northern Ireland) | s 868(1), (2), (4): the officials who must cause copies to be delivered to the registrar | not modelled as parties; the duties are encoded for what reaches the company (`s 868(1) ...`, `s 868(2) ...`, `s 868(4) ...`) |

No new `Fine limit`, `Mode of conviction`, `Penalty` or `Place of registration` constructor was needed: every penalty in this range is a `Penalty OF ...` built from the core's constructors, and Chapters 1 and 2 use the core `Place of registration`.
