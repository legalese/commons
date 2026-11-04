# Specs of ss 376F-377B for gen_offences.py (pass of 2026-11-04).  Raw line numbers are PC1871.txt's.
SECTIONS = []
FALSE_KIND = 'FALSE-kind (the text says no in its own words): '

# --------------------------------------------------------------------------------------------- 376F
TOUCH = "A intentionally touches B"
INCITE = "A intentionally incites B to touch A or B or another person"
SEXT = "the touching is sexual"
CONS = "B consents to the touching"
NSP = "B is not A's spouse"
SPS = "B is A's spouse"
IND = "A obtains B's consent by means of an inducement offered or given by A for that purpose"
THR = "A obtains B's consent by means of a threat made by A for that purpose"
DEC = "A obtains B's consent by means of a deception practised by A for that purpose"
MD = "B has a mental disability within section 376F(5)"
KN = "A knows or could reasonably be expected to know that B has a mental disability"
PEN = "the touching involved penetration of the vagina or anus with a part of the body or anything else, or penetration of the mouth with the penis"
SECTIONS.append(dict(
    sec="376F", title="procurement of sexual activity with person with mental disability", quote=(8800, 8848),
    notes=["\"Mental disability\" (subsection (5), \"means\") is `s 376F(5) the impairment is a mental disability`, below.",
           "Subsection (2) is \"subject to subsection (3)\": the offence under (2) is the one whose touching involved no such penetration (FORK DEF-B5)."],
    record="Mental Disability Procurement Facts",
    victim="The name of the person touched (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by threatening to withhold the said person's allowance unless the said person agreed to be touched\"",
    leaves=[
        (TOUCH, "Did A intentionally touch B? (s 376F(1)(a))"),
        (INCITE, "Did A intentionally incite B to touch A or B or another person? (s 376F(1)(a))"),
        (SEXT, "Is the touching sexual - as s 377C(3)(d) says? (s 376F(1)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (CONS, "Did B consent to the touching? (s 376F(1)(b))"),
        (NSP, "Is B NOT A's spouse? (s 376F(1)(c)(i))"),
        (SPS, "Is B A's spouse? (s 376F(1)(c)(ii))"),
        (IND, "Did A obtain B's consent by means of an inducement offered or given by A for that purpose? Counts only where B is not A's spouse (s 376F(1)(c)(i))"),
        (THR, "Did A obtain B's consent by means of a threat made by A for that purpose? (s 376F(1)(c)(i), (ii))"),
        (DEC, "Did A obtain B's consent by means of a deception practised by A for that purpose? (s 376F(1)(c)(i), (ii))"),
        (MD, "Does B have a mental disability as s 376F(5) gives the meaning - an impairment of or disturbance in the functioning of the mind or brain, resulting from a disability or disorder of the mind or brain, which impairs the ability to make a proper judgement in giving consent to sexual touching? Set from `s 376F(5) the impairment is a mental disability` (s 376F(1)(ca))"),
        (KN, "Did A know, or could A reasonably be expected to know, that B has a mental disability? (s 376F(1)(d))"),
        (PEN, "Did the touching involve penetration of the vagina or anus with a part of the body or anything else, or penetration of the mouth with the penis? NOT an element: it chooses between s 376F(2) (5 years) and s 376F(3) (20 years)"),
    ],
    defs=[dict(name="procures sexual touching from a person with a mental disability within section 376F(1)", lines=(8801, 8818),
               export="Whether the accused commits the offence in section 376F(1) of the Penal Code 1871 (procuring a sexual touching, to which a person with a mental disability consents, by inducement, threat or deception)",
               conj=[("(a) A intentionally touches another person (B) or intentionally incites B to touch A or B or another person", "[%s] OR [%s]" % (TOUCH, INCITE), "A intentionally touches B or intentionally incites B to touch A or B or another person"),
                     ("(b) the touching is sexual and B consents to the touching", "[%s] AND [%s]" % (SEXT, CONS), "the touching is sexual and B consents to it"),
                     ("(c) A obtains B's consent (i) where B is not A's spouse, by means of an inducement offered or given, a threat made or a deception practised by A for that purpose; or (ii) where B is A's spouse, by means of a threat made or a deception practised by A for that purpose", "([%s] AND ([%s] OR [%s] OR [%s])) OR ([%s] AND ([%s] OR [%s]))" % (NSP, IND, THR, DEC, SPS, THR, DEC), "A obtains B's consent by inducement, threat or deception where B is not A's spouse, or by threat or deception where B is A's spouse"),
                     ("(ca) B has a mental disability; and (d) A knows or could reasonably be expected to know that B has a mental disability", "[%s] AND [%s]" % (MD, KN), "B has a mental disability and A knows or could reasonably be expected to know it")])],
    offences=[
        dict(label="376F(2)", lines=(8822, 8824), punish=["376F(2)"],
             export_offence="Whether the accused has committed an offence punishable under section 376F(2) of the Penal Code 1871 (procuring sexual activity with a person with a mental disability, no penetration)",
             export_charge="Frame a charge under section 376F(2) of the Penal Code 1871 (procuring sexual activity with a person with a mental disability, no penetration), or say why none can be framed",
             offence_quote="Subject to subsection (3), a person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 5 years, or with fine, or with caning, or with any combination of such punishments",
             defn="`procures sexual touching from a person with a mental disability within section 376F(1)` f AND NOT [%s]" % PEN,
             punish_expr="`punishment prescribed by s 376F(2)`'s words", charge_name="procurement of sexual activity with person with mental disability",
             miss_from=["procures sexual touching from a person with a mental disability within section 376F(1)"],
             miss_extra=[("NOT [%s]" % PEN, "the touching did not involve penetration (otherwise section 376F(3) applies)")],
             charge_body='CONCAT "did intentionally touch, or incite to touch, ", {v}, ", a person with a mental disability, in a sexual touching to which the said person consented because you obtained the consent by inducement, threat or deception, knowing or being reasonably expected to know that the said person had a mental disability, to wit, ", {m}'),
        dict(label="376F(3)", lines=(8835, 8837), punish=["376F(3)"],
             export_offence="Whether the accused has committed an offence punishable under section 376F(3) of the Penal Code 1871 (procuring sexual activity with a person with a mental disability, with penetration)",
             export_charge="Frame a charge under section 376F(3) of the Penal Code 1871 (procuring sexual activity with a person with a mental disability, with penetration), or say why none can be framed",
             offence_quote="a person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 20 years, and shall also be liable to a fine or to caning",
             defn="`procures sexual touching from a person with a mental disability within section 376F(1)` f AND [%s]" % PEN,
             punish_expr="`punishment prescribed by s 376F(3)`'s words", charge_name="procurement of sexual activity with person with mental disability involving penetration",
             miss_from=["procures sexual touching from a person with a mental disability within section 376F(1)"],
             miss_extra=[("[%s]" % PEN, "the touching involved penetration of the vagina or anus with a part of the body or anything else, or penetration of the mouth with the penis")],
             charge_body='CONCAT "did intentionally touch, or incite to touch, ", {v}, ", a person with a mental disability, in a sexual touching involving penetration to which the said person consented because you obtained the consent by inducement, threat or deception, knowing or being reasonably expected to know that the said person had a mental disability, to wit, ", {m}'),
    ],
))

# --------------------------------------------------------------------------------------------- 376G
A16 = "A is of or above 16 years of age"
GA = "A penetrates, with A's penis, the vagina, anus or mouth of B"
GB = "A sexually penetrates, with a part of A's body (other than A's penis, if A is a man) or anything else, the vagina or anus of B"
GC = "A causes or permits B, a man, to penetrate, with B's penis, the vagina, anus or mouth of A"
GD = "A causes or permits B to sexually penetrate, with a part of B's body (other than B's penis, if B is a man) or anything else, the vagina or anus of A"
B16P = "B is of or above 16 years of age"
CFR = "B is a close family relative of A within section 376G(2)"
KNR = "A knows that B is a close family relative"
NEST = "the act of penetration, as the facts of an offence under sections 375, 376 or 376AA"
V6 = "A is below 18 years of age and is a victim of an offence under section 376AA in respect of the same acts"
SECTIONS.append(dict(
    sec="376G", title="incest", quote=(8850, 8907),
    notes=["Subsection (2) defines \"close family relative\" (\"B is a close family relative of A if ...\"): `s 376G(2) B is a close family relative of A`, below.",
           "Subsection (4): \"an act of penetration ... which would constitute an offence under section 375(1)(a), 375(1A)(a), 376(2) or 376AA(1)\" is read over a nested",
           "`Sexual Penetration Facts` for the same act, which the caller supplies (FORK DEF-B6). Subsection (5), consent immaterial, is `s 376G(5)` below.",
           "Subsection (6) is read as a flat negative applying to the whole offence (marginal reading a)."],
    record="Incest Facts",
    victim="The name of the close family relative (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by having sexual intercourse with the said B, A's sister\"",
    leaves=[
        (A16, "Is the accused (A) of or above 16 years of age? Set from NOT `below 16 years of age` on A's age"),
        (GA, "Did A penetrate, with A's penis, the vagina, anus or mouth of B? (s 376G(1)(a))"),
        (GB, "Did A sexually penetrate, with a part of A's body (other than A's penis, if A is a man) or anything else, the vagina or anus of B? (s 376G(1)(b))"),
        (GC, "Did A cause or permit B, a man, to penetrate, with B's penis, the vagina, anus or mouth of A? (s 376G(1)(c))"),
        (GD, "Did A cause or permit B to sexually penetrate, with a part of B's body (other than B's penis, if B is a man) or anything else, the vagina or anus of A? (s 376G(1)(d))"),
        (B16P, "Is B of or above 16 years of age? Set from NOT `below 16 years of age` on B's age (s 376G(1)(a)-(d))"),
        (CFR, "Is B a close family relative of A - A's grandchild, child, sibling, half-sibling, parent or grandparent, whether or not the relationship is traced through lawful wedlock (s 376G(2))? Set from `s 376G(2) B is a close family relative of A`"),
        (KNR, "Did A know that B is a close family relative? (s 376G(1))"),
        (NEST, "The facts of the same act of penetration, read under ss 375, 376 and 376AA. If they make out an offence under s 375(1)(a), 375(1A)(a), 376(2) or 376AA(1), s 376G does not apply (s 376G(4))", "Sexual Penetration Facts"),
        (V6, "Is A below 18 years of age and a victim of an offence under s 376AA in respect of the same acts? (s 376G(6): then A is not guilty under this section)"),
    ],
    defs=[dict(name="has sexual penetration with a close family relative within section 376G(1)", lines=(8852, 8872),
               export="Whether the accused commits the offence in section 376G(1) of the Penal Code 1871 (incest: sexual penetration with a close family relative of or above 16 years of age)",
               conj=[(None, "[%s]" % A16, "A is of or above 16 years of age"),
                     ("(a)-(d) penetrates, sexually penetrates, causes or permits penetration of or by a person of or above 16 years of age who is a close family relative (B)", "([%s] OR [%s] OR [%s] OR [%s]) AND [%s] AND [%s]" % (GA, GB, GC, GD, B16P, CFR), "A penetrates, or causes or permits penetration with, a close family relative B of or above 16 years of age"),
                     ("knowing that B is a close family relative", "[%s]" % KNR, "A knows that B is a close family relative"),
                     ("(4) This section does not apply to an act of penetration mentioned in subsection (1) which would constitute an offence under section 375(1)(a), 375(1A)(a), 376(2) or 376AA(1)", "NOT (`an act of penetration excluded from section 376G by section 376G(4)` ([%s]))" % NEST, "the act would not constitute an offence under section 375(1)(a), 375(1A)(a), 376(2) or 376AA(1) (section 376G(4))", FALSE_KIND + '"This section does not apply to an act of penetration mentioned in subsection (1) which would constitute an offence under section 375(1)(a), 375(1A)(a), 376(2) or 376AA(1)"'),
                     ("(6) A person below 18 years of age who is a victim of an offence under section 376AA is not guilty of an offence under this section in respect of the same acts constituting the offence under that section", "NOT [%s]" % V6, "A is not a person below 18 years of age who is a victim of an offence under section 376AA in respect of the same acts (section 376G(6))", FALSE_KIND + '"is not guilty of an offence under this section in respect of the same acts constituting the offence under that section"')])],
    offences=[dict(label="376G(3)", lines=(8882, 8883), punish=["376G(3)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376G(3) of the Penal Code 1871 (incest)",
                   export_charge="Frame a charge under section 376G(3) of the Penal Code 1871 (incest), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under this section shall be punished with imprisonment for a term which may extend to 5 years",
                   defn="`has sexual penetration with a close family relative within section 376G(1)` f",
                   punish_expr="`punishment prescribed by s 376G(3)`'s words", charge_name="incest",
                   miss_from=["has sexual penetration with a close family relative within section 376G(1)"],
                   charge_body='CONCAT "being of or above 16 years of age, did have sexual penetration with ", {v}, ", a close family relative of or above 16 years of age, knowing that the said person was a close family relative, to wit, ", {m}')],
))

# --------------------------------------------------------------------------------------------- 376H
HT = "A intentionally touches B"
HI = "A intentionally incites B to touch A or the bodily fluids of A, to touch B, to touch another person (C) or the bodily fluids of C, or to be touched by C"
HF = "A fraudulently obtains B's consent by means of deception or false representation practised or made by A for that purpose"
HR1 = "the deception or false representation relates to the use or manner of use of any sexually protective measure"
HR2 = "the deception or false representation relates to the risk of B contracting a sexually transmitted disease from the touching"
HK = "A knows or has reason to believe that the consent was given in consequence of such deception or false representation"
SECTIONS.append(dict(
    sec="376H", title="procurement of sexual activity by deception or false representation", quote=(8909, 8976),
    notes=["Subsection (3) gives three rules of reading - a false representation, express or implied, \"sexually protective measure\" - each a function below."],
    record="Deceptive Procurement Facts",
    victim="The name of the person touched (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by falsely telling the said person that a condom was being worn\"",
    leaves=[
        (HT, "Did A intentionally touch B? (s 376H(1)(a))"),
        (HI, "Did A intentionally incite B to touch A or the bodily fluids of A, to touch B, to touch another person (C) or the bodily fluids of C, or to be touched by C? (s 376H(1)(a)(i)-(iv))"),
        (SEXT, "Is the touching sexual - as s 377C(3)(d) says? (s 376H(1)(b)) See `s 377C(3)(d) the conduct is sexual`"),
        (CONS, "Did B consent to the touching? (s 376H(1)(b))"),
        (HF, "Did A fraudulently obtain B's consent by means of a deception or false representation practised or made by A for that purpose? A false representation is read with `s 376H(3)(a) the representation is false` and `s 376H(3)(b) the representation is express or implied` (s 376H(1)(c))"),
        (HR1, "Does the deception or false representation relate to the use or manner of use of any sexually protective measure? (s 376H(1)(d)(i)) See `s 376H(3)(c) the thing is a sexually protective measure`"),
        (HR2, "Does the deception or false representation relate to the risk of B contracting a sexually transmitted disease from the touching? (s 376H(1)(d)(ii))"),
        (HK, "Did A know, or have reason to believe, that the consent was given in consequence of such deception or false representation? (s 376H(1)(e))"),
        (PEN, "Did the sexual touching involve penetration of the vagina or anus with a part of the body or anything else, or penetration of the mouth with the penis? NOT an element: it chooses which punishment s 376H(2) states (10 years, or 2 years)"),
    ],
    defs=[dict(name="procures sexual touching by deception or false representation within section 376H(1)", lines=(8910, 8938),
               export="Whether the accused commits the offence in section 376H(1) of the Penal Code 1871 (procuring a sexual touching by deception or false representation about a sexually protective measure or the risk of a sexually transmitted disease)",
               conj=[("(a) A intentionally touches another person (B) or intentionally incites B to (i) touch A or the bodily fluids of A; (ii) touch B; (iii) touch another person (C) or the bodily fluids of C; or (iv) be touched by C", "[%s] OR [%s]" % (HT, HI), "A intentionally touches B or intentionally incites B to touch or be touched"),
                     ("(b) the touching is sexual and B consents to the touching", "[%s] AND [%s]" % (SEXT, CONS), "the touching is sexual and B consents to it"),
                     ("(c) A fraudulently obtains B's consent by means of deception or false representation practised or made by A for that purpose", "[%s]" % HF, "A fraudulently obtains B's consent by deception or false representation"),
                     ("(d) the deception or false representation relates to (i) the use or manner of use of any sexually protective measure; or (ii) the risk of B contracting a sexually transmitted disease from the touching", "[%s] OR [%s]" % (HR1, HR2), "the deception or false representation relates to the use or manner of use of a sexually protective measure, or to the risk of B contracting a sexually transmitted disease"),
                     ("(e) A knows or has reason to believe that the consent was given in consequence of such deception or false representation", "[%s]" % HK, "A knows or has reason to believe that the consent was given in consequence of the deception or false representation")])],
    offences=[dict(label="376H(2)", lines=(8942, 8956), punish=["376H(2)(a)", "376H(2)(b)"],
                   export_offence="Whether the accused has committed an offence punishable under section 376H(2) of the Penal Code 1871 (procuring sexual activity by deception or false representation)",
                   export_charge="Frame a charge under section 376H(2) of the Penal Code 1871 (procuring sexual activity by deception or false representation), or say why none can be framed",
                   offence_quote="A person who is guilty of an offence under subsection (1) shall be punished",
                   defn="`procures sexual touching by deception or false representation within section 376H(1)` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 376H(2)(a)`'s words ELSE `punishment prescribed by s 376H(2)(b)`'s words" % PEN,
                   charge_name="procurement of sexual activity by deception or false representation",
                   miss_from=["procures sexual touching by deception or false representation within section 376H(1)"],
                   charge_body='CONCAT "did intentionally touch, or incite to touch, ", {v}, " in a sexual touching to which the said person consented, having fraudulently obtained the consent by a deception or false representation relating to a sexually protective measure or to the risk of contracting a sexually transmitted disease, knowing or having reason to believe that the consent was given in consequence of it, to wit, ", {m}')],
))

# ---------------------------------------------------------------------------------------------- 377
CRa = "A penetrates, with A's penis, the vagina, anus or mouth of a human corpse"
CRb = "A sexually penetrates, with a part of A's body (other than A's penis, if A is a man) or anything else, the vagina or anus of a human corpse"
CRc = "A causes A's vagina, anus or mouth to be penetrated by the penis of a human corpse"
CRd = "A causes A's vagina or anus to be sexually penetrated by a part of a human corpse (other than the penis, if the human corpse is that of a deceased man)"
CRe = "A causes a person (B) to penetrate, with B's penis (if B is a man), the vagina, anus or mouth of a human corpse, without B's consent"
CRf = "A causes B to sexually penetrate, with a part of B's body (other than B's penis, if B is a man) or anything else, the vagina or anus of a human corpse, without B's consent"
CRg = "A causes B's vagina, anus or mouth to be penetrated by the penis of a human corpse, without B's consent"
CRh = "A causes B's vagina or anus to be sexually penetrated by a part of a human corpse (other than the penis, if the human corpse is that of a deceased man), without B's consent"
SECTIONS.append(dict(
    sec="377", title="sexual penetration, etc., of a corpse", quote=(8978, 9020),
    record="Corpse Penetration Facts",
    victim="A description of the corpse, or the name of the person (B) caused to penetrate or be penetrated, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by penetrating the vagina of the body of the late Tan Mei Ling with your penis\"",
    leaves=[
        (CRa, "Did A do this? (s 377(1)(a))"), (CRb, "Did A do this? (s 377(1)(b))"), (CRc, "Did A do this? (s 377(1)(c))"), (CRd, "Did A do this? (s 377(1)(d))"),
        (CRe, "Did A do this, B not consenting? (s 377(1)(e))"), (CRf, "Did A do this, B not consenting? (s 377(1)(f))"),
        (CRg, "Did A do this, B not consenting? (s 377(1)(g))"), (CRh, "Did A do this, B not consenting? (s 377(1)(h))"),
    ],
    defs=[
        dict(name="penetrates a human corpse within section 377(1)(a) to (d)", lines=(8980, 8992),
             export="Whether the accused commits an offence under section 377(1)(a), (b), (c) or (d) of the Penal Code 1871 (sexual penetration of a human corpse, or causing one's own penetration by a human corpse)",
             conj=[("A person (A) who (a) penetrates, with A's penis, the vagina, anus or mouth of a human corpse; (b) sexually penetrates, with a part of A's body (other than A's penis, if A is a man) or anything else, the vagina or anus of a human corpse; (c) causes A's vagina, anus or mouth to be penetrated by the penis of a human corpse; (d) causes A's vagina or anus to be sexually penetrated by a part of a human corpse (other than the penis, if the human corpse is that of a deceased man)",
                    "[%s] OR [%s] OR [%s] OR [%s]" % (CRa, CRb, CRc, CRd), "A does one of the acts in section 377(1)(a), (b), (c) or (d)")]),
        dict(name="causes a person to penetrate or be penetrated by a human corpse within section 377(1)(e) to (h)", lines=(8994, 9006),
             export="Whether the accused commits an offence under section 377(1)(e), (f), (g) or (h) of the Penal Code 1871 (causing another person, without that person's consent, to penetrate or be penetrated by a human corpse)",
             conj=[("A person (A) who (e) causes a person (B) to penetrate ... the vagina, anus or mouth of a human corpse, without B's consent; (f) causes B to sexually penetrate ... the vagina or anus of a human corpse, without B's consent; (g) causes B's vagina, anus or mouth to be penetrated by the penis of a human corpse, without B's consent; or (h) causes B's vagina or anus to be sexually penetrated by a part of a human corpse ..., without B's consent",
                    "[%s] OR [%s] OR [%s] OR [%s]" % (CRe, CRf, CRg, CRh), "A does one of the acts in section 377(1)(e), (f), (g) or (h), without B's consent")]),
    ],
    offences=[
        dict(label="377(2)", lines=(9010, 9012), punish=["377(2)"],
             export_offence="Whether the accused has committed an offence punishable under section 377(2) of the Penal Code 1871 (sexual penetration of a corpse)",
             export_charge="Frame a charge under section 377(2) of the Penal Code 1871 (sexual penetration of a corpse), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under subsection (1)(a), (b), (c) or (d) shall be punished with imprisonment for a term that may extend to 5 years, or with fine, or with both",
             defn="`penetrates a human corpse within section 377(1)(a) to (d)` f",
             punish_expr="`punishment prescribed by s 377(2)`'s words", charge_name="sexual penetration of a corpse",
             miss_from=["penetrates a human corpse within section 377(1)(a) to (d)"],
             charge_body='CONCAT "did an act of sexual penetration of, or by, a human corpse, namely ", {v}, ", to wit, ", {m}'),
        dict(label="377(3)", lines=(9014, 9018), punish=["377(3)"],
             export_offence="Whether the accused has committed an offence punishable under section 377(3) of the Penal Code 1871 (causing another person, without consent, to penetrate or be penetrated by a corpse)",
             export_charge="Frame a charge under section 377(3) of the Penal Code 1871 (causing another person, without consent, to penetrate or be penetrated by a corpse), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under subsection (1)(e), (f), (g) or (h) shall be punished with imprisonment for a term that may extend to 20 years, and shall also be liable to fine or to caning",
             defn="`causes a person to penetrate or be penetrated by a human corpse within section 377(1)(e) to (h)` f",
             punish_expr="`punishment prescribed by s 377(3)`'s words", charge_name="causing a person without consent to penetrate or be penetrated by a corpse",
             miss_from=["causes a person to penetrate or be penetrated by a human corpse within section 377(1)(e) to (h)"],
             charge_body='CONCAT "did cause ", {v}, " without the consent of the said person to penetrate, or to be penetrated by, a human corpse, to wit, ", {m}'),
    ],
))

# --------------------------------------------------------------------------------------------- 377B
AN = "the creature is an animal within section 47"
BA = "A penetrates, with A's penis, the vagina, anus or any orifice of an animal"
BB = "A causes or permits A's vagina, anus or mouth to be penetrated by the penis of an animal"
BC = "A causes any man (B) to penetrate, with B's penis, the vagina, anus or any orifice of an animal"
BD = "A causes the vagina, anus or mouth of another person (B) to be penetrated with the penis of an animal"
NC = "B did not consent to the penetration"
SECTIONS.append(dict(
    sec="377B", title="sexual penetration with living animal", quote=(9024, 9050),
    record="Animal Penetration Facts",
    victim="A description of the animal, or the name of the person (B) caused to penetrate or be penetrated, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by penetrating the vagina of a dog with your penis\"",
    leaves=[
        (AN, "Is the creature an \"animal\" - any living creature other than a human being (s 47)? See `s 47 the creature is an animal`"),
        (BA, "Did A do this? (s 377B(1)(a))"), (BB, "Did A do this? (s 377B(1)(b))"),
        (BC, "Did A do this? (s 377B(3)(a))"), (BD, "Did A do this? (s 377B(3)(b))"),
        (NC, "Did B NOT consent to the penetration? (s 377B(3))"),
    ],
    defs=[
        dict(name="penetrates or is penetrated by a living animal within section 377B(1)", lines=(9026, 9033),
             export="Whether the accused commits the offence in section 377B(1) of the Penal Code 1871 (penetrating an animal, or causing or permitting one's own penetration by an animal)",
             conj=[(None, "[%s]" % AN, "the creature is an animal"),
                   ("(a) penetrates, with A's penis, the vagina, anus or any orifice of an animal; or (b) causes or permits A's vagina, anus or mouth, as the case may be, to be penetrated by the penis of an animal", "[%s] OR [%s]" % (BA, BB), "A penetrates an animal with A's penis, or causes or permits A's own penetration by the penis of an animal")]),
        dict(name="causes another person to penetrate or be penetrated by a living animal within section 377B(3)", lines=(9038, 9046),
             export="Whether the accused commits the offence in section 377B(3) of the Penal Code 1871 (causing another person, without that person's consent, to penetrate or be penetrated by an animal)",
             conj=[(None, "[%s]" % AN, "the creature is an animal"),
                   ("(a) causes any man (B) to penetrate, with B's penis, the vagina, anus or any orifice of an animal; or (b) causes the vagina, anus or mouth of another person (B) to be penetrated with the penis of an animal", "[%s] OR [%s]" % (BC, BD), "A causes a man to penetrate an animal, or causes another person to be penetrated by the penis of an animal"),
                   ("shall be guilty of an offence if B did not consent to the penetration", "[%s]" % NC, "B did not consent to the penetration")]),
    ],
    offences=[
        dict(label="377B(2)", lines=(9035, 9036), punish=["377B(2)"],
             export_offence="Whether the accused has committed an offence punishable under section 377B(2) of the Penal Code 1871 (sexual penetration with a living animal)",
             export_charge="Frame a charge under section 377B(2) of the Penal Code 1871 (sexual penetration with a living animal), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under subsection (1) shall be punished with imprisonment for a term which may extend to 2 years, or with fine, or with both",
             defn="`penetrates or is penetrated by a living animal within section 377B(1)` f",
             punish_expr="`punishment prescribed by s 377B(2)`'s words", charge_name="sexual penetration with living animal",
             miss_from=["penetrates or is penetrated by a living animal within section 377B(1)"],
             charge_body='CONCAT "did an act of sexual penetration with a living animal, namely ", {v}, ", to wit, ", {m}'),
        dict(label="377B(4)", lines=(9048, 9050), punish=["377B(4)"],
             export_offence="Whether the accused has committed an offence punishable under section 377B(4) of the Penal Code 1871 (causing another person, without consent, to have sexual penetration with a living animal)",
             export_charge="Frame a charge under section 377B(4) of the Penal Code 1871 (causing another person, without consent, to have sexual penetration with a living animal), or say why none can be framed",
             offence_quote="A person who is guilty of an offence under subsection (3) shall be punished with imprisonment for a term which may extend to 20 years, and shall also be liable to fine or to caning",
             defn="`causes another person to penetrate or be penetrated by a living animal within section 377B(3)` f",
             punish_expr="`punishment prescribed by s 377B(4)`'s words", charge_name="causing a person without consent to have sexual penetration with living animal",
             miss_from=["causes another person to penetrate or be penetrated by a living animal within section 377B(3)"],
             charge_body='CONCAT "did cause ", {v}, " without the consent of the said person to penetrate, or to be penetrated by, a living animal, to wit, ", {m}'),
    ],
))
