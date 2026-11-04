# Specs of ss 377BB-377BO for gen_offences.py (pass of 2026-11-04).  Raw line numbers are PC1871.txt's.
SECTIONS = []
FALSE_KIND = 'FALSE-kind (the text says no in its own words): '

# ---------------------------------------------------------------------------------------- 377C
SECTIONS.append(dict(
    sec="377C", title="interpretation of sections 375 to 377BO (sexual offences)", quote=(9907, 10062),
    notes=["Definitions and rules of reading, as functions: MAYBE BOOLEAN, JUST FALSE only where the text says no in its own words",
           "(\"means\", \"if\", flat negatives), NOTHING where it says \"includes\", \"may include\", or is limited by its own wording."]))

# ---------------------------------------------------------------------------------------- 377BB
OBS1 = "A intentionally observes B doing a private act without B's consent"
KN1 = "A knows or has reason to believe that B does not consent to being observed"
EQ2 = "A operates equipment with the intention of enabling A or another person to observe a third person (B) doing a private act without B's consent"
KN2 = "A knows or has reason to believe that B (whether B's private act was recorded or not) does not consent to A operating equipment with that intention"
REC3 = "A intentionally or knowingly records B doing a private act without B's consent"
KN3 = "A knows or has reason to believe that B does not consent to A recording the act"
EQ4 = "A operates equipment without B's consent with the intention of enabling A or another person (C) to observe B's genital region, breasts if B is female, or buttocks (whether exposed or covered) in circumstances where the genital region, breasts, buttocks or underwear would not otherwise be visible"
KN4 = "A knows or has reason to believe that B (whether B's image was recorded or not) does not consent to A operating the equipment with that intention"
REC5 = "A intentionally or knowingly records without B's consent an image of B's genital region, breasts if B is female, or buttocks (whether exposed or covered), in circumstances where the genital region, breasts, buttocks or underwear would not otherwise be visible"
KN5 = "A knows or has reason to believe that B does not consent to A recording the image"
INS6 = "A installs equipment, or constructs or adapts a structure or part of a structure, with the intention of enabling A or another person to commit an offence under section 377BB(1), (2), (3), (4) or (5)"
B14 = "B is below 14 years of age"
SECTIONS.append(dict(
    sec="377BB", title="voyeurism", quote=(9062, 9152),
    notes=["Six ways to commit the offence, subsections (1) to (6), one punishment, (7) and (8). \"Private act\" is `s 377C(3)(f) the person is doing a private act`;",
           "the presumption of subsection (9) is `s 377BB(9) the effect of the recording` below."],
    record="Voyeurism Facts",
    victim="The name of the person observed or recorded (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by recording B showering through a hole in the wall with a mobile phone\"",
    leaves=[
        (OBS1, "Did A intentionally observe B doing a private act (see `s 377C(3)(f) the person is doing a private act`; observation is read with `s 377C(3)(e)`), without B's consent? (s 377BB(1)(a))"), (KN1, "Did A know or have reason to believe that B did not consent to being observed? (s 377BB(1)(b))"),
        (EQ2, "Did A operate equipment with the intention of enabling A or another person to observe a third person (B) doing a private act without B's consent? (s 377BB(2)(a))"), (KN2, "Did A know or have reason to believe that B (whether B's private act was recorded or not) did not consent to A operating equipment with that intention? (s 377BB(2)(b))"),
        (REC3, "Did A intentionally or knowingly record B doing a private act without B's consent? (s 377BB(3)(a))"), (KN3, "Did A know or have reason to believe that B did not consent to A recording the act? (s 377BB(3)(b))"),
        (EQ4, "Did A operate equipment without B's consent with the intention of enabling A or another person (C) to observe B's genital region, breasts if B is female, or buttocks (whether exposed or covered) in circumstances where they or the underwear would not otherwise be visible? (s 377BB(4)(a))"), (KN4, "Did A know or have reason to believe that B (whether B's image was recorded or not) did not consent to A operating the equipment with that intention? (s 377BB(4)(b))"),
        (REC5, "Did A intentionally or knowingly record, without B's consent, an image of B's genital region, breasts if B is female, or buttocks (whether exposed or covered), in circumstances where they or the underwear would not otherwise be visible? (s 377BB(5)(a))"), (KN5, "Did A know or have reason to believe that B did not consent to A recording the image? (s 377BB(5)(b))"),
        (INS6, "Did A install equipment, or construct or adapt a structure or part of a structure (see `s 377C(1) the thing is a structure`), with the intention of enabling A or another person to commit an offence under s 377BB(1), (2), (3), (4) or (5)? (s 377BB(6))"),
        (B14, "Is the person against whom the offence is committed below 14 years of age? NOT an element: it chooses which punishment s 377BB states (s 377BB(7), (8))"),
    ],
    defs=[dict(name="commits voyeurism within section 377BB", lines=(9064, 9129),
               export="Whether the accused commits an offence under section 377BB of the Penal Code 1871 (voyeurism: observing, operating equipment to observe, recording, installing equipment)",
               conj=[("(1) intentionally observes another person (B) doing a private act without B's consent and knows or has reason to believe that B does not consent; (2) operates equipment with the intention of enabling A or another person to observe a third person (B) doing a private act without B's consent ...; (3) intentionally or knowingly records another person (B) doing a private act without B's consent ...; (4) operates equipment without another person's (B) consent with the intention of enabling A or another person (C) to observe B's genital region, breasts if B is female, or buttocks ...; (5) intentionally or knowingly records without another person's (B) consent an image of B's genital region, breasts if B is female, or buttocks ...; (6) installs equipment, or constructs or adapts a structure or part of a structure, with the intention of enabling A or another person to commit an offence under subsection (1), (2), (3), (4) or (5)",
                      "([%s] AND [%s]) OR ([%s] AND [%s]) OR ([%s] AND [%s]) OR ([%s] AND [%s]) OR ([%s] AND [%s]) OR [%s]" % (OBS1, KN1, EQ2, KN2, REC3, KN3, EQ4, KN4, REC5, KN5, INS6),
                      "one of the six ways in section 377BB(1) to (6): observing, operating equipment to observe, recording, operating equipment to observe the genital region, breasts or buttocks, recording an image of them, or installing equipment or a structure - each with the knowledge or reason to believe that B does not consent, except installing")])],
    offences=[dict(label="377BB(7)", lines=(9133, 9141), punish=["377BB(7)", "377BB(8)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BB(7) of the Penal Code 1871 (voyeurism)",
                   export_charge="Frame a charge under section 377BB(7) of the Penal Code 1871 (voyeurism), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under this section shall on conviction be punished",
                   defn="`commits voyeurism within section 377BB` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 377BB(8)`'s words ELSE `punishment prescribed by s 377BB(7)`'s words" % B14,
                   charge_name="voyeurism",
                   miss_from=["commits voyeurism within section 377BB"],
                   charge_body='CONCAT (IF [%s] THEN "did intentionally observe " ELSE (IF [%s] THEN "did operate equipment with the intention of enabling the observation of " ELSE (IF [%s] THEN "did record " ELSE (IF [%s] THEN "did operate equipment with the intention of enabling the observation of the genital region, breasts or buttocks of " ELSE (IF [%s] THEN "did record an image of the genital region, breasts or buttocks of " ELSE "did install equipment, or construct or adapt a structure, with the intention of enabling the commission of an offence against "))))), {v}, " without the consent of the said person, to wit, ", {m}' % (OBS1, EQ2, REC3, EQ4, REC5))],
))

# ---------------------------------------------------------------------------------------- 377BC
DIST = "A intentionally or knowingly distributes an image or recording of B without B's consent to the distribution"
POSS = "A intentionally or knowingly has in A's possession an image or recording of B for the purpose of distribution without B's consent to the distribution"
OBT = "A knows or has reason to believe that the image or recording was obtained through the commission of an offence under section 377BB"
KNC = "A knows or has reason to believe that B does not consent to the distribution"
IMG14 = "the image or recording is of a person below 14 years of age"
SECTIONS.append(dict(
    sec="377BC", title="distribution of voyeuristic image or recording", quote=(9154, 9195),
    notes=["\"Distribute\" is `s 377C(1) the conduct is distributing`; \"image\" is `s 377C(1) the thing is an image`."],
    record="Distribution of Voyeuristic Image Facts",
    victim="The name of the person in the image or recording (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by posting a video of B showering to a messaging group\"",
    leaves=[(DIST, "Did A intentionally or knowingly distribute an image or recording of B without B's consent to the distribution? (s 377BC(1)(a))"),
            (POSS, "Did A intentionally or knowingly have in A's possession an image or recording of B for the purpose of distribution without B's consent to the distribution? (s 377BC(2)(a))"),
            (OBT, "Did A know or have reason to believe that the image or recording was obtained through the commission of an offence under s 377BB? (s 377BC(1)(b), (2)(b))"),
            (KNC, "Did A know or have reason to believe that B does not consent to the distribution? (s 377BC(1)(c), (2)(c))"),
            (IMG14, "Is the image or recording of a person below 14 years of age? NOT an element: it chooses which punishment s 377BC states (s 377BC(3), (4))")],
    defs=[dict(name="distributes a voyeuristic image or recording within section 377BC", lines=(9156, 9177),
               export="Whether the accused commits an offence under section 377BC(1) or (2) of the Penal Code 1871 (distributing, or possessing for distribution, a voyeuristic image or recording)",
               conj=[("(1)(a) intentionally or knowingly distributes an image or recording of another person (B) without B's consent to the distribution; or (2)(a) intentionally or knowingly has in his possession an image or recording of another person (B) for the purpose of distribution without B's consent to the distribution", "[%s] OR [%s]" % (DIST, POSS), "A intentionally or knowingly distributes, or has in his possession for distribution, an image or recording of B without B's consent to the distribution"),
                     ("(b) knowing or having reason to believe that the image or recording was obtained through the commission of an offence under section 377BB", "[%s]" % OBT, "A knows or has reason to believe that the image or recording was obtained through an offence under section 377BB"),
                     ("(c) knows or has reason to believe that B does not consent to the distribution", "[%s]" % KNC, "A knows or has reason to believe that B does not consent to the distribution")])],
    offences=[dict(label="377BC(3)", lines=(9181, 9193), punish=["377BC(3)", "377BC(4)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BC(3) of the Penal Code 1871 (distribution of voyeuristic image or recording)",
                   export_charge="Frame a charge under section 377BC(3) of the Penal Code 1871 (distribution of voyeuristic image or recording), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) or (2) shall on conviction be punished",
                   defn="`distributes a voyeuristic image or recording within section 377BC` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 377BC(4)`'s words ELSE `punishment prescribed by s 377BC(3)`'s words" % IMG14,
                   charge_name="distribution of voyeuristic image or recording",
                   miss_from=["distributes a voyeuristic image or recording within section 377BC"],
                   charge_body='CONCAT (IF [%s] THEN "did distribute " ELSE "did have in your possession for distribution "), "an image or recording of ", {v}, " without the consent of the said person to the distribution, knowing or having reason to believe that it was obtained through the commission of an offence under section 377BB of the Penal Code 1871, to wit, ", {m}' % DIST)],
))

# ---------------------------------------------------------------------------------------- 377BD
PS1 = "A has in A's possession or has gained access to an image or recording of another person"
OB1 = "A knows or has reason to believe that the image or recording was obtained through the commission of an offence under section 377BB"
IN1 = "A knows or has reason to believe that the image or recording is an intimate image or recording as defined in section 377BE(5)"
NC1 = "A knows or has reason to believe that the possession of or access to the image or recording was without the consent of the person depicted"
HM1 = "A knows or has reason to believe that the possession of or access to the image or recording will or is likely to cause humiliation, alarm or distress to the person depicted"
PR5 = "A intentionally produces an intimate image or recording (as defined in section 377BE(5)) of another person (B)"
NC5 = "A produces it without the consent of B"
HM5 = "A knows or has reason to believe that the production of the image or recording will or is likely to cause humiliation, alarm or distress to B"
SECTIONS.append(dict(
    sec="377BD", title="possession of or gaining access to voyeuristic or intimate image or recording and production of intimate image or recording", quote=(9197, 9287),
    notes=["Two offences, (1) possession or access and (5) production; each has its own punishment, (2)-(3) and (6)-(7).",
           "\"Intimate image or recording\" is `s 377BE(5) the image or recording is an intimate image or recording`, in the 377BE block below."],
    record="Possession of Voyeuristic Image Facts",
    victim="The name of the person depicted (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by storing in a cloud account a video of B showering\"",
    leaves=[(PS1, "Did A have in A's possession (see `s 377BD(4)(a) the person has the electronic image in his possession`) or gain access to (see `s 377BD(4)(b)`) an image or recording of another person? (s 377BD(1))"),
            (OB1, "Did A know or have reason to believe that the image or recording was obtained through the commission of an offence under s 377BB? (s 377BD(1)(a))"),
            (IN1, "Did A know or have reason to believe that the image or recording is an intimate image or recording as defined in s 377BE(5)? (s 377BD(1)(b)(i))"),
            (NC1, "Did A know or have reason to believe that the possession of or access to it was without the consent of the person depicted? (s 377BD(1)(b)(ii))"),
            (HM1, "Did A know or have reason to believe that the possession of or access to it will or is likely to cause humiliation, alarm or distress to the person depicted? (s 377BD(1)(b)(iii))"),
            (PR5, "Did A intentionally produce an intimate image or recording (s 377BE(5)) of another person (B)? Ways of producing are read with `s 377BD(8) the way is a way of producing material` (s 377BD(5))"),
            (NC5, "Did A produce it without the consent of B? (s 377BD(5)(a))"),
            (HM5, "Did A know or have reason to believe that the production will or is likely to cause humiliation, alarm or distress to B? (s 377BD(5)(b))"),
            (IMG14, "Is the image or recording of a person below 14 years of age? NOT an element: it chooses which punishment s 377BD states (s 377BD(3), (7))")],
    defs=[dict(name="possesses or gains access to a voyeuristic or intimate image or recording within section 377BD(1)", lines=(9200, 9216),
               export="Whether the accused commits the offence in section 377BD(1) of the Penal Code 1871 (possession of or access to an image or recording obtained through voyeurism, or an intimate image or recording)",
               conj=[("Any person shall be guilty of an offence who has in his possession or has gained access to an image or recording of another person", "[%s]" % PS1, "A has in A's possession or has gained access to an image or recording of another person"),
                     ("and (a) knows or has reason to believe that the image or recording was obtained through the commission of an offence under section 377BB; or (b) knows or has reason to believe that (i) the image or recording is an intimate image or recording as defined in section 377BE(5); (ii) the possession of or access to the image or recording was without the consent of the person depicted; and (iii) the possession of or access to the image or recording will or is likely to cause humiliation, alarm or distress to the person depicted", "[%s] OR ([%s] AND [%s] AND [%s])" % (OB1, IN1, NC1, HM1), "A knows or has reason to believe that the image or recording was obtained through an offence under section 377BB; or that it is an intimate image or recording, that the possession or access is without the consent of the person depicted, and that it will or is likely to cause them humiliation, alarm or distress")]),
          dict(name="produces an intimate image or recording within section 377BD(5)", lines=(9251, 9259),
               export="Whether the accused commits the offence in section 377BD(5) of the Penal Code 1871 (intentionally producing an intimate image or recording of another person without consent)",
               conj=[("Any person who intentionally produces an intimate image or recording (as defined in section 377BE(5)) of another person (B) (a) without the consent of B; and (b) knowing or having reason to believe that the production of the image or recording will or is likely to cause humiliation, alarm or distress to B, shall be guilty of an offence", "[%s] AND [%s] AND [%s]" % (PR5, NC5, HM5), "A intentionally produces an intimate image or recording of B without B's consent, knowing or having reason to believe it will or is likely to cause B humiliation, alarm or distress")])],
    offences=[dict(label="377BD(2)", lines=(9220, 9230), punish=["377BD(2)", "377BD(3)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BD(2) of the Penal Code 1871 (possession of or access to a voyeuristic or intimate image or recording)",
                   export_charge="Frame a charge under section 377BD(2) of the Penal Code 1871 (possession of or access to a voyeuristic or intimate image or recording), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) shall on conviction be punished",
                   defn="`possesses or gains access to a voyeuristic or intimate image or recording within section 377BD(1)` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 377BD(3)`'s words ELSE `punishment prescribed by s 377BD(2)`'s words" % IMG14,
                   charge_name="possession of or gaining access to voyeuristic or intimate image or recording",
                   miss_from=["possesses or gains access to a voyeuristic or intimate image or recording within section 377BD(1)"],
                   charge_body='CONCAT "did have in your possession, or gain access to, an image or recording of ", {v}, ", knowing or having reason to believe that it was obtained through an offence under section 377BB of the Penal Code 1871 or that it is an intimate image or recording, to wit, ", {m}'),
              dict(label="377BD(6)", lines=(9263, 9272), punish=["377BD(6)", "377BD(7)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BD(6) of the Penal Code 1871 (production of an intimate image or recording)",
                   export_charge="Frame a charge under section 377BD(6) of the Penal Code 1871 (production of an intimate image or recording), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (5) shall on conviction be punished",
                   defn="`produces an intimate image or recording within section 377BD(5)` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 377BD(7)`'s words ELSE `punishment prescribed by s 377BD(6)`'s words" % IMG14,
                   charge_name="production of intimate image or recording",
                   miss_from=["produces an intimate image or recording within section 377BD(5)"],
                   charge_body='CONCAT "did intentionally produce an intimate image or recording of ", {v}, " without the consent of the said person, knowing or having reason to believe that the production would or was likely to cause the said person humiliation, alarm or distress, to wit, ", {m}')],
))

# ---------------------------------------------------------------------------------------- 377BE
DI1 = "A intentionally or knowingly distributes an intimate image or recording of B"
TH2 = "A knowingly threatens the distribution of an intimate image or recording of B"
WO = "the distribution (or threatened distribution) is without B's consent to the distribution"
H1 = "A knows or has reason to believe that the distribution will or is likely to cause B humiliation, alarm or distress"
H2 = "A knows or has reason to believe that the threat will or is likely to cause B humiliation, alarm or distress"
BB14 = "B is below 14 years of age"
SECTIONS.append(dict(
    sec="377BE", title="distributing or threatening to distribute intimate image or recording", quote=(9290, 9368),
    notes=["Subsection (5) defines \"intimate image or recording\": `s 377BE(5) the image or recording is an intimate image or recording`, below, with its two Illustrations.",
           "Subsection (6), that the prosecution need not prove the threatened image exists or is intimate, is two functions below."],
    record="Intimate Image Facts",
    victim="The name of the person depicted (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by posting a nude photograph of B to a social media account\"",
    leaves=[(DI1, "Did A intentionally or knowingly distribute an intimate image or recording of B? (s 377BE(1)(a); see `s 377C(1) the conduct is distributing`)"),
            (TH2, "Did A knowingly threaten the distribution of an intimate image or recording of B? (s 377BE(2)(a))"),
            (WO, "Was it without B's consent to the distribution? (s 377BE(1)(b), (2)(b))"),
            (H1, "Did A know or have reason to believe that the distribution will or is likely to cause B humiliation, alarm or distress? (s 377BE(1)(c))"),
            (H2, "Did A know or have reason to believe that the threat will or is likely to cause B humiliation, alarm or distress? (s 377BE(2)(c))"),
            (BB14, "Is B below 14 years of age? NOT an element: it chooses which punishment s 377BE states (s 377BE(3), (4))")],
    defs=[dict(name="distributes or threatens to distribute an intimate image or recording within section 377BE", lines=(9292, 9312),
               export="Whether the accused commits an offence under section 377BE(1) or (2) of the Penal Code 1871 (distributing, or threatening to distribute, an intimate image or recording)",
               conj=[("(1) intentionally or knowingly distributes an intimate image or recording of another person (B); (b) without B's consent to the distribution; and (c) knows or has reason to believe that the distribution will or is likely to cause B humiliation, alarm or distress; or (2) knowingly threatens the distribution of an intimate image or recording of another person (B); without B's consent to the distribution; and knows or has reason to believe that the threat will or is likely to cause B humiliation, alarm or distress", "([%s] AND [%s] AND [%s]) OR ([%s] AND [%s] AND [%s])" % (DI1, WO, H1, TH2, WO, H2), "A intentionally or knowingly distributes, or knowingly threatens to distribute, an intimate image or recording of B without B's consent to the distribution, knowing or having reason to believe that it will or is likely to cause B humiliation, alarm or distress")])],
    offences=[dict(label="377BE(3)", lines=(9316, 9325), punish=["377BE(3)", "377BE(4)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BE(3) of the Penal Code 1871 (distributing or threatening to distribute an intimate image or recording)",
                   export_charge="Frame a charge under section 377BE(3) of the Penal Code 1871 (distributing or threatening to distribute an intimate image or recording), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) or (2) shall on conviction be punished",
                   defn="`distributes or threatens to distribute an intimate image or recording within section 377BE` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 377BE(4)`'s words ELSE `punishment prescribed by s 377BE(3)`'s words" % BB14,
                   charge_name="distributing or threatening to distribute intimate image or recording",
                   miss_from=["distributes or threatens to distribute an intimate image or recording within section 377BE"],
                   charge_body='CONCAT (IF [%s] THEN "did distribute an intimate image or recording of " ELSE "did threaten the distribution of an intimate image or recording of "), {v}, " without the consent of the said person to the distribution, knowing or having reason to believe that it would or was likely to cause the said person humiliation, alarm or distress, to wit, ", {m}' % DI1)],
))

# ---------------------------------------------------------------------------------------- 377BF
EXP = "A intentionally exposes A's genitals"
DST = "A intentionally distributes to B an image of A's or any other person's genitals"
PG = "A did so for the purpose of obtaining sexual gratification"
PH = "A did so for the purpose of causing B humiliation, alarm or distress"
INT = "A intends that B will see the genitals"
WOC = "A does so without B's consent"
SECTIONS.append(dict(
    sec="377BF", title="sexual exposure", quote=(9370, 9407),
    record="Sexual Exposure Facts",
    victim="The name of the person (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by exposing your genitals to B on a train\"",
    leaves=[(EXP, "Did A intentionally expose A's genitals? (s 377BF(1)(a))"), (DST, "Did A intentionally distribute to B an image of A's or any other person's genitals? (s 377BF(2)(a))"),
            (PG, "Was it for the purpose of obtaining sexual gratification? (s 377BF(1)(a), (2)(a))"), (PH, "Was it for the purpose of causing B humiliation, alarm or distress? (s 377BF(1)(a), (2)(a))"),
            (INT, "Did A intend that B will see A's genitals (or, in s 377BF(2), A's or the other person's genitals)? (s 377BF(1)(b), (2)(b))"), (WOC, "Did A do so without B's consent? (s 377BF(1)(c), (2)(c))"),
            (BB14, "Is B below 14 years of age? NOT an element: it chooses which punishment s 377BF states (s 377BF(3), (4))")],
    defs=[dict(name="commits sexual exposure within section 377BF", lines=(9372, 9392),
               export="Whether the accused commits an offence under section 377BF(1) or (2) of the Penal Code 1871 (sexual exposure: exposing genitals, or distributing an image of genitals, to B without B's consent)",
               conj=[("(a) for the purpose of obtaining sexual gratification or of causing another person (B) humiliation, alarm or distress, intentionally exposes A's genitals, or intentionally distributes to B an image of A's or any other person's genitals", "([%s] OR [%s]) AND ([%s] OR [%s])" % (EXP, DST, PG, PH), "for the purpose of obtaining sexual gratification or of causing B humiliation, alarm or distress, A intentionally exposes A's genitals or distributes to B an image of A's or another person's genitals"),
                     ("(b) intends that B will see A's genitals (or the other person's genitals); and (c) does so without B's consent", "[%s] AND [%s]" % (INT, WOC), "A intends that B will see the genitals and does so without B's consent")])],
    offences=[dict(label="377BF(3)", lines=(9397, 9405), punish=["377BF(3)", "377BF(4)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BF(3) of the Penal Code 1871 (sexual exposure)",
                   export_charge="Frame a charge under section 377BF(3) of the Penal Code 1871 (sexual exposure), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) or (2) shall on conviction be punished",
                   defn="`commits sexual exposure within section 377BF` f",
                   punish_expr="IF [%s] THEN `punishment prescribed by s 377BF(4)`'s words ELSE `punishment prescribed by s 377BF(3)`'s words" % BB14,
                   charge_name="sexual exposure",
                   miss_from=["commits sexual exposure within section 377BF"],
                   charge_body='CONCAT "for the purpose of obtaining sexual gratification or of causing humiliation, alarm or distress to ", {v}, ", did intentionally ", (IF [%s] THEN "expose your genitals" ELSE "distribute to the said person an image of genitals"), ", intending that the said person would see them, without the consent of the said person, to wit, ", {m}' % EXP)],
))

# ---------------------------------------------------------------------------------------- 377BG-377BK
CAM = "A knows or has reason to believe that the material is child abuse material"
SECTIONS.append(dict(
    sec="377BG", title="using or involving child in production of child abuse material", quote=(9409, 9446),
    notes=["\"Child abuse material\" is `s 377C(1) the material is child abuse material`; the leaf below is set from it."],
    record="Child Abuse Material Use Facts",
    victim="The name of the person below 16 years of age used in the production, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by filming the said child in a sexual pose\"",
    leaves=[("A uses a person who is below 16 years of age for the production of material", "Did A use a person below 16 years of age for the production of material? (s 377BG(1)(a)) Ways of using are read with `s 377BG(3)(c)`; ways of producing with `s 377BG(3)(b)`"),
            ("A causes or procures a person below 16 years of age to be so used", "Did A cause or procure a person below 16 years of age to be so used? (s 377BG(1)(b))"),
            ("A, having the care or custody of a person below 16 years of age, consents to the person being so used or allows the person to be so used", "Did A, having the care (see `s 377BG(3)(a) A has the care of the person below 16 years of age`) or custody of a person below 16 years of age, consent to the person being so used or allow the person to be so used? (s 377BG(1)(c))"),
            (CAM, "Did A know or have reason to believe that the material is child abuse material, as `s 377C(1) the material is child abuse material` says? (s 377BG(1)(a))")],
    defs=[dict(name="uses a person below 16 years of age to produce child abuse material within section 377BG(1)", lines=(9411, 9419),
               export="Whether the accused commits the offence in section 377BG(1) of the Penal Code 1871 (using, or causing or allowing the use of, a person below 16 years of age in the production of child abuse material)",
               conj=[("(a) uses a person who is below 16 years of age for the production of material; (b) causes or procures a person of that age to be so used; or (c) having the care or custody of a person of that age, consents to the person being so used or allows the person to be so used", "[A uses a person who is below 16 years of age for the production of material] OR [A causes or procures a person below 16 years of age to be so used] OR [A, having the care or custody of a person below 16 years of age, consents to the person being so used or allows the person to be so used]", "A uses a person below 16 years of age for the production of material, or causes or procures it, or, having the care or custody, consents or allows it"),
                     ("which he knows or has reason to believe is child abuse material", "[%s]" % CAM, "A knows or has reason to believe that the material is child abuse material")])],
    offences=[dict(label="377BG(2)", lines=(9423, 9425), punish=["377BG(2)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BG(2) of the Penal Code 1871 (using or involving a child in the production of child abuse material)",
                   export_charge="Frame a charge under section 377BG(2) of the Penal Code 1871 (using or involving a child in the production of child abuse material), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) shall on conviction be punished with imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning",
                   defn="`uses a person below 16 years of age to produce child abuse material within section 377BG(1)` f",
                   punish_expr="`punishment prescribed by s 377BG(2)`'s words", charge_name="using or involving child in production of child abuse material",
                   miss_from=["uses a person below 16 years of age to produce child abuse material within section 377BG(1)"],
                   charge_body='CONCAT "did use, or cause or procure the use of, or, having the care or custody of, consent to or allow the use of, ", {v}, ", a person below 16 years of age, for the production of material which you knew or had reason to believe was child abuse material, to wit, ", {m}')],
))

SECTIONS.append(dict(
    sec="377BH", title="producing child abuse material", quote=(9448, 9473),
    record="Child Abuse Material Production Facts",
    victim="A description of the material produced, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by drawing images of children in sexual poses\"",
    leaves=[("A intentionally produces material", "Did A intentionally produce material? Ways of producing are read with `s 377BH(3) the way is a way of producing material`"), (CAM, "Did A know or have reason to believe that the material is child abuse material, as `s 377C(1) the material is child abuse material` says? (s 377BH(1))")],
    defs=[dict(name="produces child abuse material within section 377BH(1)", lines=(9451, 9453),
               export="Whether the accused commits the offence in section 377BH(1) of the Penal Code 1871 (intentionally producing child abuse material)",
               conj=[("Any person who intentionally produces child abuse material knowing or having reason to believe that the material is child abuse material shall be guilty of an offence", "[A intentionally produces material] AND [%s]" % CAM, "A intentionally produces material, knowing or having reason to believe that it is child abuse material")])],
    offences=[dict(label="377BH(2)", lines=(9457, 9459), punish=["377BH(2)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BH(2) of the Penal Code 1871 (producing child abuse material)",
                   export_charge="Frame a charge under section 377BH(2) of the Penal Code 1871 (producing child abuse material), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) shall on conviction be punished with imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning",
                   defn="`produces child abuse material within section 377BH(1)` f",
                   punish_expr="`punishment prescribed by s 377BH(2)`'s words", charge_name="producing child abuse material",
                   miss_from=["produces child abuse material within section 377BH(1)"],
                   charge_body='CONCAT "did intentionally produce child abuse material, namely ", (f\'s victim), ", knowing or having reason to believe that it was child abuse material, to wit, ", {m}')],
))

SECTIONS.append(dict(
    sec="377BI", title="distributing or selling child abuse material", quote=(9475, 9491),
    record="Child Abuse Material Distribution Facts",
    victim="A description of the material, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by sending the said video to a group chat\"",
    leaves=[("A distributes or sells or offers for sale child abuse material, or has in A's possession child abuse material for the purpose of such distribution, sale or offer for sale", "Did A distribute (see `s 377C(1) the conduct is distributing`) or sell or offer for sale child abuse material, or have child abuse material in A's possession for the purpose of such distribution, sale or offer for sale? (s 377BI(1)(a))"), (CAM, "Did A know or have reason to believe that the material is child abuse material? (s 377BI(1)(b))")],
    defs=[dict(name="distributes or sells child abuse material within section 377BI(1)", lines=(9477, 9483),
               export="Whether the accused commits the offence in section 377BI(1) of the Penal Code 1871 (distributing or selling child abuse material, or possessing it for that purpose)",
               conj=[("(a) distributes or sells or offers for sale child abuse material or has in the person's possession child abuse material for the purpose of such distribution, sale or offer for sale; and (b) knows or has reason to believe that the material is child abuse material", "[A distributes or sells or offers for sale child abuse material, or has in A's possession child abuse material for the purpose of such distribution, sale or offer for sale] AND [%s]" % CAM, "A distributes or sells or offers for sale child abuse material, or has it for that purpose, knowing or having reason to believe that it is child abuse material")])],
    offences=[dict(label="377BI(2)", lines=(9487, 9489), punish=["377BI(2)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BI(2) of the Penal Code 1871 (distributing or selling child abuse material)",
                   export_charge="Frame a charge under section 377BI(2) of the Penal Code 1871 (distributing or selling child abuse material), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) shall on conviction be punished with imprisonment for a term which may extend to 7 years, and shall also be liable to fine or to caning",
                   defn="`distributes or sells child abuse material within section 377BI(1)` f",
                   punish_expr="`punishment prescribed by s 377BI(2)`'s words", charge_name="distributing or selling child abuse material",
                   miss_from=["distributes or sells child abuse material within section 377BI(1)"],
                   charge_body='CONCAT "did distribute, or sell, or offer for sale, or have in your possession for such distribution, sale or offer for sale, child abuse material, namely ", (f\'s victim), ", knowing or having reason to believe that it was child abuse material, to wit, ", {m}')],
))

SECTIONS.append(dict(
    sec="377BJ", title="advertising or seeking child abuse material", quote=(9493, 9528),
    record="Child Abuse Material Advertising Facts",
    victim="A description of the material, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by posting an advertisement on an online forum\"",
    leaves=[("A, for the purposes of distributing or selling or offering for sale any child abuse material, advertises the material", "Did A, for the purposes of distributing or selling or offering for sale any child abuse material, advertise the material? \"Advertise\" is read with `s 377BJ(4) the conduct is advertising` (s 377BJ(1)(a))"),
            ("A announces or otherwise makes known by any means any offer or purported offer to acquire, buy or gain access to any child abuse material", "Did A announce or otherwise make known by any means any offer or purported offer to acquire, buy or gain access to any child abuse material? (s 377BJ(2)(a))"),
            (CAM, "Did A know or have reason to believe that the material is child abuse material? (s 377BJ(1)(b), (2)(b))")],
    defs=[dict(name="advertises or seeks child abuse material within section 377BJ", lines=(9495, 9509),
               export="Whether the accused commits an offence under section 377BJ(1) or (2) of the Penal Code 1871 (advertising child abuse material for distribution or sale, or announcing an offer to acquire or gain access to it)",
               conj=[("(1)(a) for the purposes of distributing or selling or offering for sale any child abuse material advertises the material; or (2)(a) announces or otherwise makes known by any means any offer or purported offer to acquire, buy or gain access to any child abuse material", "[A, for the purposes of distributing or selling or offering for sale any child abuse material, advertises the material] OR [A announces or otherwise makes known by any means any offer or purported offer to acquire, buy or gain access to any child abuse material]", "A advertises child abuse material for distribution or sale, or announces an offer to acquire, buy or gain access to it"),
                     ("and knows or has reason to believe that the material is child abuse material", "[%s]" % CAM, "A knows or has reason to believe that the material is child abuse material")])],
    offences=[dict(label="377BJ(3)", lines=(9513, 9515), punish=["377BJ(3)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BJ(3) of the Penal Code 1871 (advertising or seeking child abuse material)",
                   export_charge="Frame a charge under section 377BJ(3) of the Penal Code 1871 (advertising or seeking child abuse material), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) or (2) shall on conviction be punished with imprisonment for a term which may extend to 5 years, and shall also be liable to fine or to caning",
                   defn="`advertises or seeks child abuse material within section 377BJ` f",
                   punish_expr="`punishment prescribed by s 377BJ(3)`'s words", charge_name="advertising or seeking child abuse material",
                   miss_from=["advertises or seeks child abuse material within section 377BJ"],
                   charge_body='CONCAT (IF [A, for the purposes of distributing or selling or offering for sale any child abuse material, advertises the material] THEN "did advertise child abuse material for the purpose of distributing or selling or offering it for sale, namely " ELSE "did announce or make known an offer to acquire, buy or gain access to child abuse material, namely "), (f\'s victim), ", knowing or having reason to believe that it was child abuse material, to wit, ", {m}')],
))

SECTIONS.append(dict(
    sec="377BK", title="possession of or gaining access to child abuse material", quote=(9530, 9567),
    record="Child Abuse Material Possession Facts",
    victim="A description of the material, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by storing the said video in a cloud account\"",
    leaves=[("A has in A's possession or has gained access to child abuse material", "Did A have in A's possession (see `s 377BK(3)(a) the person has the electronic child abuse material in his possession`) or gain access to (see `s 377BK(3)(b)`) child abuse material? (s 377BK(1)(a))"), (CAM, "Did A know or have reason to believe that the material is child abuse material? (s 377BK(1)(b))")],
    defs=[dict(name="possesses or gains access to child abuse material within section 377BK(1)", lines=(9532, 9537),
               export="Whether the accused commits the offence in section 377BK(1) of the Penal Code 1871 (possession of or access to child abuse material)",
               conj=[("(a) has in the person's possession or has gained access to child abuse material; and (b) knows or has reason to believe that the material is child abuse material", "[A has in A's possession or has gained access to child abuse material] AND [%s]" % CAM, "A has in A's possession or has gained access to child abuse material, knowing or having reason to believe that it is child abuse material")])],
    offences=[dict(label="377BK(2)", lines=(9541, 9543), punish=["377BK(2)"],
                   export_offence="Whether the accused has committed an offence punishable under section 377BK(2) of the Penal Code 1871 (possession of or gaining access to child abuse material)",
                   export_charge="Frame a charge under section 377BK(2) of the Penal Code 1871 (possession of or gaining access to child abuse material), or say why none can be framed",
                   offence_quote="a person who is guilty of an offence under subsection (1) shall on conviction be punished with imprisonment for a term which may extend to 5 years, and shall also be liable to fine or to caning",
                   defn="`possesses or gains access to child abuse material within section 377BK(1)` f",
                   punish_expr="`punishment prescribed by s 377BK(2)`'s words", charge_name="possession of or gaining access to child abuse material",
                   miss_from=["possesses or gains access to child abuse material within section 377BK(1)"],
                   charge_body='CONCAT "did have in your possession, or gain access to, child abuse material, namely ", (f\'s victim), ", knowing or having reason to believe that it was child abuse material, to wit, ", {m}')],
))

# ---------------------------------------------------------------------------------------- 377BL
REL = "A is in a relationship with B that is exploitative of B"
B1618 = "B is of or above 16 but below 18 years of age"
U2 = "A uses B for the production of material which A knows or has reason to believe is abusive material, or causes or procures B to be so used"
P3 = "A intentionally produces abusive material of B"
D4 = "A distributes or sells or offers for sale abusive material of B, or has in A's possession abusive material of B for the purpose of such distribution, sale or offer for sale, knowing or having reason to believe that the material is abusive material of B"
SECTIONS.append(dict(
    sec="377BL", title="exploitation by abusive material of minor of or above 16 but below 18 years of age", quote=(9569, 9641),
    notes=["Subsection (1): the section applies only where the relationship is exploitative; the first two leaves are part of every offence below.",
           "\"Abusive material\" is `s 377BL(6) the material is abusive material`; ways of producing and using are `s 377BL(5)(a)` and `(b)`."],
    record="Exploitative Abusive Material Facts",
    victim="The name of the person of or above 16 but below 18 years of age (B), as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by filming B in a sexual pose\"",
    leaves=[(REL, "Is A in a relationship with B that is exploitative of B, as the court determines under s 377CA? (s 377BL(1))"),
            (B1618, "Is B of or above 16 but below 18 years of age? Set from the helper `of or above 16 years of age but below 18 years of age` on B's age (s 377BL(1))"),
            (U2, "Did A use B for the production of material which A knows or has reason to believe is abusive material, or cause or procure B to be so used? (s 377BL(2))"),
            (P3, "Did A intentionally produce abusive material of B? (s 377BL(3))"),
            (D4, "Did A distribute or sell or offer for sale abusive material of B, or have it in A's possession for that purpose, knowing or having reason to believe that the material is abusive material of B? (s 377BL(4))")],
    defs=[
        dict(name="uses an exploitatively related minor to produce abusive material within section 377BL(2)", lines=(9571, 9580),
             export="Whether the accused commits the offence in section 377BL(2) of the Penal Code 1871 (using a minor of or above 16 but below 18 years of age in an exploitative relationship to produce abusive material)",
             conj=[("(1) This section applies only where a person (A) is in a relationship with another person (B) who is of or above 16 but below 18 years of age, that is exploitative of B", "[%s] AND [%s]" % (REL, B1618), "A is in a relationship with B, who is of or above 16 but below 18 years of age, that is exploitative of B"),
                   ("(2) A person (A) who uses B for the production of material which A knows or has reason to believe is abusive material or causes or procures B to be so used shall be guilty of an offence", "[%s]" % U2, "A uses B for the production of abusive material, or causes or procures B to be so used")]),
        dict(name="produces abusive material of an exploitatively related minor within section 377BL(3)", lines=(9571, 9586),
             export="Whether the accused commits the offence in section 377BL(3) of the Penal Code 1871 (intentionally producing abusive material of a minor of or above 16 but below 18 years of age in an exploitative relationship)",
             conj=[("(1) This section applies only where a person (A) is in a relationship with another person (B) who is of or above 16 but below 18 years of age, that is exploitative of B", "[%s] AND [%s]" % (REL, B1618), "A is in a relationship with B, who is of or above 16 but below 18 years of age, that is exploitative of B"),
                   ("(3) A person (A) who intentionally produces abusive material of B shall be guilty of an offence", "[%s]" % P3, "A intentionally produces abusive material of B")]),
        dict(name="distributes abusive material of an exploitatively related minor within section 377BL(4)", lines=(9571, 9594),
             export="Whether the accused commits the offence in section 377BL(4) of the Penal Code 1871 (distributing or selling abusive material of a minor of or above 16 but below 18 years of age in an exploitative relationship)",
             conj=[("(1) This section applies only where a person (A) is in a relationship with another person (B) who is of or above 16 but below 18 years of age, that is exploitative of B", "[%s] AND [%s]" % (REL, B1618), "A is in a relationship with B, who is of or above 16 but below 18 years of age, that is exploitative of B"),
                   ("(4) A person (A) who distributes or sells or offers for sale abusive material of B or has in A's possession abusive material of B for the purpose of such distribution, sale or offer for sale; and knowing or having reason to believe that the material is abusive material of B shall be guilty of an offence", "[%s]" % D4, "A distributes or sells or offers for sale abusive material of B, or has it for that purpose, knowing or having reason to believe it is abusive material of B")]),
    ],
    offences=[
        dict(label="377BL(2)", lines=(9577, 9580), punish=["377BL(2)"],
             export_offence="Whether the accused has committed an offence punishable under section 377BL(2) of the Penal Code 1871 (using an exploitatively related minor to produce abusive material)",
             export_charge="Frame a charge under section 377BL(2) of the Penal Code 1871 (using an exploitatively related minor to produce abusive material), or say why none can be framed",
             offence_quote="shall be guilty of an offence and shall on conviction be punished with imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning",
             defn="`uses an exploitatively related minor to produce abusive material within section 377BL(2)` f",
             punish_expr="`punishment prescribed by s 377BL(2)`'s words", charge_name="using exploitatively related minor to produce abusive material",
             miss_from=["uses an exploitatively related minor to produce abusive material within section 377BL(2)"],
             charge_body='CONCAT "being in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, did use, or cause or procure the use of, the said person for the production of material which you knew or had reason to believe was abusive material, to wit, ", {m}'),
        dict(label="377BL(3)", lines=(9584, 9586), punish=["377BL(3)"],
             export_offence="Whether the accused has committed an offence punishable under section 377BL(3) of the Penal Code 1871 (producing abusive material of an exploitatively related minor)",
             export_charge="Frame a charge under section 377BL(3) of the Penal Code 1871 (producing abusive material of an exploitatively related minor), or say why none can be framed",
             offence_quote="shall be guilty of an offence and shall on conviction be punished with imprisonment for a term which may extend to 10 years, and shall also be liable to fine or to caning",
             defn="`produces abusive material of an exploitatively related minor within section 377BL(3)` f",
             punish_expr="`punishment prescribed by s 377BL(3)`'s words", charge_name="producing abusive material of exploitatively related minor",
             miss_from=["produces abusive material of an exploitatively related minor within section 377BL(3)"],
             charge_body='CONCAT "being in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, did intentionally produce abusive material of the said person, to wit, ", {m}'),
        dict(label="377BL(4)", lines=(9590, 9594), punish=["377BL(4)"],
             export_offence="Whether the accused has committed an offence punishable under section 377BL(4) of the Penal Code 1871 (distributing abusive material of an exploitatively related minor)",
             export_charge="Frame a charge under section 377BL(4) of the Penal Code 1871 (distributing abusive material of an exploitatively related minor), or say why none can be framed",
             offence_quote="shall be guilty of an offence and shall on conviction be punished with imprisonment for a term which may extend to 7 years, and shall also be liable to fine or to caning",
             defn="`distributes abusive material of an exploitatively related minor within section 377BL(4)` f",
             punish_expr="`punishment prescribed by s 377BL(4)`'s words", charge_name="distributing abusive material of exploitatively related minor",
             miss_from=["distributes abusive material of an exploitatively related minor within section 377BL(4)"],
             charge_body='CONCAT "being in a relationship that is exploitative of ", {v}, ", a person of or above 16 but below 18 years of age, did distribute or sell or offer for sale abusive material of the said person, or have it in your possession for that purpose, knowing or having reason to believe that it was abusive material, to wit, ", {m}'),
    ],
))

# ---------------------------------------------------------------------------------------- 377BM-377BO (quotation only; the rest by hand)
SECTIONS.append(dict(sec="377BM", title="defences to offences relating to intimate image or recording and voyeurism", quote=(9643, 9706)))
SECTIONS.append(dict(sec="377BN", title="defences to child abuse material offences", quote=(9708, 9833)))
SECTIONS.append(dict(sec="377BO", title="child abuse material offences outside or partially outside Singapore", quote=(9835, 9905)))
