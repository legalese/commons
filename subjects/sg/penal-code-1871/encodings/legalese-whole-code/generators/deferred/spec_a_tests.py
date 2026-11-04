# Test-only spec of the offences of pc-body-a-deferred.l4, for gen_struct_tests.py (pass of 2026-11-04).
#
# pc-body-a-deferred.l4 was written by hand, not generated.  This file restates each offence's elements as a
# boolean formula over the facts record's leaves, written from the Code's words (the raw line numbers are
# PC1871.txt's), so that the structural tests are derived from the text and not from the module under test.
# Nothing here is emitted into the module: it only feeds gen_struct_tests.py.
#
# `record` and the leaf names must be exactly the module's; gen_tests.py rejects a misspelt leaf.

SECTIONS = []

# ---------------------------------------------------------------------------------------------- 310, 311
INF = dict(
    woman="the accused is a woman",
    act="by an intentional act or omission causes the death of her child",
    young="the child is below 12 months of age",
    birth="the balance of her mind was disturbed by reason of her not having fully recovered from the effect of giving birth to the child",
    lact="the balance of her mind was disturbed by reason of the effect of lactation consequent upon the birth of the child",
)
SECTIONS.append(dict(
    sec="310-311", record="Infanticide Facts",
    leaves=[(v, "") for v in INF.values()],
    defs=[dict(name="ladder of s 310", conj=[
        ("7181-7187", "[%s]" % INF["woman"], ""),
        ("7181-7187", "[%s]" % INF["act"], ""),
        ("7181-7187", "[%s]" % INF["young"], ""),
        ("7181-7187", "[%s] OR [%s]" % (INF["birth"], INF["lact"]), ""),
    ])],
    offences=[dict(label="311", punish=["311"], punish_expr="`punishment prescribed by s 311`'s words", charge_name="infanticide",
                   defn="`ladder of s 310` f")],
))

# --------------------------------------------------------------------------------------------------- 304B
SA = dict(
    child="the victim is a child below 14 years of age",
    dw="the victim is a domestic worker",
    vp="the victim is a vulnerable person",
    custody="the accused has custody, charge or care of the victim",
    emp="the accused is the employer of the domestic worker, a member of the employer's household or the employment agent of the domestic worker",
    hurt="the conduct consists of voluntarily causing hurt",
    neg="the conduct consists of knowingly causing neglect",
    two="the conduct took place on 2 or more occasions",
    single="the conduct took place on a single occasion and was protracted",
    death="causes the death of the victim by the course of conduct",
)
SECTIONS.append(dict(
    sec="304B", record="Sustained Abuse Facts",
    leaves=[(v, "") for v in SA.values()],
    defs=[dict(name="ladder of s 304B(1)", conj=[
        ("6862-6863", "[%s] OR [%s] OR [%s]" % (SA["child"], SA["dw"], SA["vp"]), ""),
        ("6887-6897", "([%s] AND [%s]) OR ([%s] AND [%s]) OR ([%s] AND [%s])" % (SA["child"], SA["custody"], SA["dw"], SA["emp"], SA["vp"], SA["custody"]), ""),
        ("6899-6905", "([%s] OR [%s]) AND ([%s] OR [%s])" % (SA["hurt"], SA["neg"], SA["two"], SA["single"]), ""),
        ("6862-6863", "[%s]" % SA["death"], ""),
    ])],
    offences=[dict(label="304B(1)", punish=["304B(1)"], punish_expr="`punishment prescribed by s 304B(1)`'s words",
                   charge_name="causing death of child below 14 years of age, domestic worker or vulnerable person by sustained abuse",
                   defn="`ladder of s 304B(1)` f")],
))

# --------------------------------------------------------------------------------------------------- 304C
HD = dict(
    child="B is below 14 years of age",
    dw="B is a domestic worker",
    vp="B is a vulnerable person",
    unl="B dies as a result of an unlawful act",
    mem="the person who did that act was a member of the same household as B",
    cont="the person who did that act had frequent contact with B",
    amem="A was a member of the same household as B",
    acont="A had frequent contact with B at the time of that act",
    risk="at that time there was a significant risk of grievous hurt being caused to B by the unlawful act of such a person",
    own="A was the person whose act caused B's death",
    aware="A was, or ought to have been, aware of the significant risk",
    failed="A failed to take such steps as A could reasonably have been expected to take to protect B from the significant risk",
    fore="the unlawful act occurred in circumstances of the kind that A foresaw or ought to have foreseen",
    cannot="A could not have been expected in A's circumstances to take any such step",
)
SECTIONS.append(dict(
    sec="304C", record="Household Death Facts",
    leaves=[(v, "") for v in HD.values()],
    defs=[dict(name="ladder of s 304C(1)", conj=[
        ("6914-6917", "[%s] OR [%s] OR [%s]" % (HD["child"], HD["dw"], HD["vp"]), ""),
        ("6916-6921", "[%s] AND [%s] AND [%s]" % (HD["unl"], HD["mem"], HD["cont"]), ""),
        ("6922-6923", "[%s] AND [%s]" % (HD["amem"], HD["acont"]), ""),
        ("6925-6928", "[%s]" % HD["risk"], ""),
        ("6930-6938", "[%s] OR ([%s] AND [%s] AND [%s])" % (HD["own"], HD["aware"], HD["failed"], HD["fore"]), ""),
        ("6948-6949", "NOT [%s]" % HD["cannot"], ""),
    ])],
    offences=[dict(label="304C(4)", punish=["304C(4)"], punish_expr="`punishment prescribed by s 304C(4)`'s words",
                   charge_name="causing or allowing death of child below 14 years of age, domestic worker or vulnerable person in same household",
                   defn="`ladder of s 304C(1)` f")],
))

# --------------------------------------------------------------------------------------------------- 308A
GO = dict(
    member="the accused is or acts as a member of a group",
    obj="the accused knows that the common object of the members of the group is to commit an offence under this Code or any written law",
    likely="the accused knows that death or grievous hurt is likely to be caused in furtherance of the group's common object",
    weapon="the accused knows that a deadly weapon, or anything which, used as a weapon of offence, is likely to cause death, is to be used in any manner against another person in the furtherance of that common object",
    death="the death of a person was caused in furtherance of the group's common object",
)
SECTIONS.append(dict(
    sec="308A", record="Group Object Death Facts",
    leaves=[(v, "") for v in GO.values()],
    defs=[dict(name="ladder of s 308A(1)", conj=[
        ("7107-7109", "[%s]" % GO["member"], ""),
        ("7110-7111", "[%s]" % GO["obj"], ""),
        ("7113-7121", "[%s] OR [%s]" % (GO["likely"], GO["weapon"]), ""),
        ("7123-7125", "[%s]" % GO["death"], ""),
    ])],
    offences=[dict(label="308A(2)", punish=["308A(2)"], punish_expr="`punishment prescribed by s 308A(2)`'s words",
                   charge_name="causing death in furtherance of a group's object",
                   defn="`ladder of s 308A(1)` f")],
))

# ---------------------------------------------------------------------------------------------------- 314
MC = dict(
    top="not an act authorised by the Termination of Pregnancy Act 1974",
    child="the woman is with child",
    intent="the accused does an act with intent to cause the miscarriage of the woman",
    death="the act causes the death of the woman",
    noconsent="the act is done without the consent of the woman",
    knows="the offender knows that the act is likely to cause death",
)
SECTIONS.append(dict(
    sec="314", record="Miscarriage Death Facts",
    leaves=[(v, "") for v in MC.values()],
    defs=[dict(name="ladder of s 314", conj=[
        ("7233-7234", "[%s]" % MC["top"], ""),
        ("7233-7235", "[%s]" % MC["child"], ""),
        ("7233-7235", "[%s]" % MC["intent"], ""),
        ("7233-7235", "[%s]" % MC["death"], ""),
    ])],
    offences=[dict(label="314", punish=["314", "314, without consent"],
                   punish_expr="IF [%s] THEN `punishment prescribed by s 314, without consent`'s words ELSE `punishment prescribed by s 314`'s words" % MC["noconsent"],
                   charge_name="death caused by act done with intent to cause miscarriage",
                   defn="`ladder of s 314` f")],
))

# --------------------------------------------------------------------------------------------------- 315
CD = dict(
    top="not an act authorised by the Termination of Pregnancy Act 1974",
    intent="the accused intends to destroy the life of a child capable of being born alive",
    before="by an intentional act causes the child to die before it has an existence independent of its mother",
    after="by such act causes the child to die after its birth",
    saves="the act is immediately necessary to save the life of the mother",
)
SECTIONS.append(dict(
    sec="315", record="Child Destruction Facts",
    leaves=[(v, "") for v in CD.values()],
    defs=[dict(name="ladder of s 315(1)", conj=[
        ("7245-7246", "[%s]" % CD["top"], ""),
        ("7246-7248", "[%s]" % CD["intent"], ""),
        ("7247-7249", "[%s] OR [%s]" % (CD["before"], CD["after"]), ""),
        ("7249-7250", "NOT [%s]" % CD["saves"], ""),
    ])],
    offences=[dict(label="315(1)", punish=["315(1)"], punish_expr="`punishment prescribed by s 315(1)`'s words",
                   charge_name="child destruction before, at or immediately after birth",
                   defn="`ladder of s 315(1)` f")],
))

# --------------------------------------------------------------------------------------------------- 316
QU = dict(
    act="the accused does an act under such circumstances that if he thereby caused death he would be guilty of culpable homicide",
    death="the accused by such act causes the death of a quick unborn child",
)
SECTIONS.append(dict(
    sec="316", record="Quick Unborn Child Facts",
    leaves=[(v, "") for v in QU.values()],
    defs=[dict(name="ladder of s 316", conj=[
        ("7260-7262", "[%s]" % QU["act"], ""),
        ("7261-7262", "[%s]" % QU["death"], ""),
    ])],
    offences=[dict(label="316", punish=["316"], punish_expr="`punishment prescribed by s 316`'s words",
                   charge_name="causing death of a quick unborn child by an act amounting to culpable homicide",
                   defn="`ladder of s 316` f")],
))

# -------------------------------------------------------------------------------------------------- 335A
AN = dict(
    dw="B is a domestic worker",
    vp="B is a vulnerable person",
    suffers="B suffers neglect, hurt, grievous hurt, sexual abuse or any injury to B's mental health as a result of the unlawful act of another person (C)",
    knew="A knew or had reason to believe that B was at risk of such neglect, hurt, grievous hurt, sexual abuse or injury caused by C",
    emp="A was at the time of the risk the employer of B, a member of B's employer's household or an employment agent of B",
    care="A had, at the time of the risk, the custody, charge or care of B",
    failed="A failed to take such steps as A could reasonably have been expected to take in A's circumstances to protect B from the risk",
    fore="the act occurred in circumstances of the kind that A foresaw or ought to have foreseen",
    death="death is caused to the domestic worker or vulnerable person",
)
SECTIONS.append(dict(
    sec="335A", record="Allowing Neglect Facts",
    leaves=[(v, "") for v in AN.values()],
    defs=[
        dict(name="ladder of s 335A(1)", conj=[
            ("7529-7531", "[%s]" % AN["dw"], ""),
            ("7529-7531", "[%s]" % AN["suffers"], ""),
            ("7533-7534", "[%s]" % AN["knew"], ""),
            ("7536-7537", "[%s]" % AN["emp"], ""),
            ("7539-7541", "[%s]" % AN["failed"], ""),
            ("7543-7544", "[%s]" % AN["fore"], ""),
        ]),
        dict(name="ladder of s 335A(2)", conj=[
            ("7551-7553", "[%s]" % AN["vp"], ""),
            ("7551-7553", "[%s]" % AN["suffers"], ""),
            ("7555-7556", "[%s]" % AN["knew"], ""),
            ("7558-7559", "[%s]" % AN["care"], ""),
            ("7561-7563", "[%s]" % AN["failed"], ""),
            ("7565-7566", "[%s]" % AN["fore"], ""),
        ]),
    ],
    offences=[
        dict(label="335A(1)", punish=["335A(5)(a)", "335A(5)(b)"],
             punish_expr="IF [%s] THEN `punishment prescribed by s 335A(5)(a)`'s words ELSE `punishment prescribed by s 335A(5)(b)`'s words" % AN["death"],
             charge_name="allowing neglect, physical or sexual abuse of a domestic worker", defn="`ladder of s 335A(1)` f"),
        dict(label="335A(2)", punish=["335A(5)(a)", "335A(5)(b)"],
             punish_expr="IF [%s] THEN `punishment prescribed by s 335A(5)(a)`'s words ELSE `punishment prescribed by s 335A(5)(b)`'s words" % AN["death"],
             charge_name="allowing neglect, physical or sexual abuse of a vulnerable person", defn="`ladder of s 335A(2)` f"),
    ],
))
