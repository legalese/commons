# Specs of ss 372-377B for gen_offences.py (pass of 2026-11-04).  Raw line numbers are PC1871.txt's.
# Where a section needs a hand-written function (a definition, a presumption, a closed list) it is
# written by hand in pc-body-b-deferred.l4 around the generated block, not here.

D = "Did the accused do this? "

SECTIONS = []

# ----------------------------------------------------------------------------------------------- 372
SECTIONS.append(dict(
    sec="372", title="selling minor for purposes of prostitution, etc.", quote=(8071, 8083),
    notes=["The Explanation's presumption is a function of its own, below: it is a rebuttable presumption of intent,",
           "not an element, so the ladder reads the intent and the knowledge as the caller states them (FORK DEF-B1)."],
    record="Selling Minor Facts",
    victim="The name of the person sold, let to hire or disposed of, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by selling the said minor to the keeper of a brothel\"",
    leaves=[
        ("the accused sells, lets to hire, or otherwise disposes of a person", "Did the accused sell, let to hire, or otherwise dispose of a person?"),
        ("the person is below 21 years of age", "Was the person below 21 years of age? Set from the helper `below 21 years of age` on the person's age"),
        ("the accused intends that the person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose", "Did the accused intend that the person should, at any age, be employed or used for prostitution, for illicit intercourse with any person, or for any unlawful and immoral purpose? The Explanation presumes this intent for a female below 21 disposed of to a prostitute or brothel-keeper: see `s 372 Explanation the intent that she shall be used for prostitution`"),
        ("the accused knows it to be likely that the person will at any age be employed or used for any such purpose", "Did the accused know it to be likely that the person would, at any age, be employed or used for any such purpose?"),
    ],
    defs=[dict(
        name="sells a person below 21 years of age within section 372", lines=(8073, 8078),
        export="Whether the accused commits the offence in section 372 of the Penal Code 1871 (selling a person below 21 years of age for prostitution or another unlawful and immoral purpose)",
        conj=[
            ("Whoever sells, lets to hire, or otherwise disposes of any person below 21 years of age", "[the accused sells, lets to hire, or otherwise disposes of a person] AND [the person is below 21 years of age]", "the accused sells, lets to hire, or otherwise disposes of a person below 21 years of age"),
            ("with intent that such person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose, or knowing it to be likely that such person will at any age be employed or used for any such purpose", "[the accused intends that the person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose] OR [the accused knows it to be likely that the person will at any age be employed or used for any such purpose]", "the accused intends that the person be employed or used for prostitution, illicit intercourse or an unlawful and immoral purpose, or knows it to be likely"),
        ])],
    offences=[dict(
        label="372", lines=(8073, 8078), punish=["372"],
        export_offence="Whether the accused has committed an offence punishable under section 372 of the Penal Code 1871 (selling minor for purposes of prostitution, etc.)",
        export_charge="Frame a charge under section 372 of the Penal Code 1871 (selling minor for purposes of prostitution, etc.), or say why none can be framed",
        offence_quote="shall be punished with imprisonment for a term which may extend to 10 years, and shall also be liable to fine",
        defn="`sells a person below 21 years of age within section 372` f",
        punish_expr="`punishment prescribed by s 372`'s words", charge_name="selling minor for purposes of prostitution, etc.",
        miss_from=['sells a person below 21 years of age within section 372'],
        charge_body='CONCAT "did sell, let to hire or otherwise dispose of ", {v}, ", a person below 21 years of age, ", (IF [the accused intends that the person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose] THEN "with intent that the said person should be employed or used for the purpose of prostitution or illicit intercourse or for an unlawful and immoral purpose" ELSE "knowing it to be likely that the said person would be employed or used for such a purpose"), ", to wit, ", {m}',
    )],
))

# ----------------------------------------------------------------------------------------------- 373
SECTIONS.append(dict(
    sec="373", title="buying minor for purposes of prostitution, etc.", quote=(8085, 8097),
    notes=["The Explanation's presumption is a function of its own, below (FORK DEF-B1)."],
    record="Buying Minor Facts",
    victim="The name of the person bought, hired or obtained, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by buying the said minor from her guardian\"",
    leaves=[
        ("the accused buys, hires or otherwise obtains possession of a person", "Did the accused buy, hire or otherwise obtain possession of a person?"),
        ("the person is below 21 years of age", "Was the person below 21 years of age? Set from the helper `below 21 years of age` on the person's age"),
        ("the accused intends that the person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose", "Did the accused intend that the person should, at any age, be employed or used for prostitution, for illicit intercourse with any person, or for any unlawful and immoral purpose? The Explanation presumes this intent for a prostitute or brothel-keeper who obtains a female below 21: see `s 373 Explanation the intent that she shall be used for prostitution`"),
        ("the accused knows it to be likely that the person will at any age be employed or used for any such purpose", "Did the accused know it to be likely that the person would, at any age, be employed or used for any such purpose?"),
    ],
    defs=[dict(
        name="buys a person below 21 years of age within section 373", lines=(8087, 8092),
        export="Whether the accused commits the offence in section 373 of the Penal Code 1871 (buying a person below 21 years of age for prostitution or another unlawful and immoral purpose)",
        conj=[
            ("Whoever buys, hires or otherwise obtains possession of any person below 21 years of age", "[the accused buys, hires or otherwise obtains possession of a person] AND [the person is below 21 years of age]", "the accused buys, hires or otherwise obtains possession of a person below 21 years of age"),
            ("with intent that such person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose, or knowing it to be likely that such person will at any age be employed or used for any such purpose", "[the accused intends that the person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose] OR [the accused knows it to be likely that the person will at any age be employed or used for any such purpose]", "the accused intends that the person be employed or used for prostitution, illicit intercourse or an unlawful and immoral purpose, or knows it to be likely"),
        ])],
    offences=[dict(
        label="373", lines=(8087, 8092), punish=["373"],
        export_offence="Whether the accused has committed an offence punishable under section 373 of the Penal Code 1871 (buying minor for purposes of prostitution, etc.)",
        export_charge="Frame a charge under section 373 of the Penal Code 1871 (buying minor for purposes of prostitution, etc.), or say why none can be framed",
        offence_quote="shall be punished with imprisonment for a term which may extend to 10 years, and shall also be liable to fine",
        defn="`buys a person below 21 years of age within section 373` f",
        punish_expr="`punishment prescribed by s 373`'s words", charge_name="buying minor for purposes of prostitution, etc.",
        miss_from=['buys a person below 21 years of age within section 373'],
        charge_body='CONCAT "did buy, hire or otherwise obtain possession of ", {v}, ", a person below 21 years of age, ", (IF [the accused intends that the person shall at any age be employed or used for the purpose of prostitution or illicit intercourse with any person or for any unlawful and immoral purpose] THEN "with intent that the said person should be employed or used for the purpose of prostitution or illicit intercourse or for an unlawful and immoral purpose" ELSE "knowing it to be likely that the said person would be employed or used for such a purpose"), ", to wit, ", {m}',
    )],
))

# ---------------------------------------------------------------------------------------------- 373A
SECTIONS.append(dict(
    sec="373A", title="importing woman for purposes of prostitution, etc.", quote=(8099, 8113),
    record="Importing Woman Facts",
    victim="The name of the woman brought into Singapore, sold or bought, as it is to appear in the charge",
    manner="What the accused did, as it is to read after \"to wit,\" - for example \"by bringing the said woman from Jakarta on a promise of work as a cook\"",
    leaves=[
        ("the accused by any false pretence, false representation, or fraudulent or deceitful means brings, or assists in bringing, into Singapore a woman", "Did the accused, by any false pretence, false representation, or fraudulent or deceitful means, bring a woman into Singapore, or assist in bringing her? (s 373A(a))"),
        ("the accused intends that the woman may be employed or used for the purpose of prostitution", "Did the accused intend that the woman might be employed or used for the purpose of prostitution? (s 373A(a))"),
        ("the accused brings, or assists in bringing, into Singapore a woman", "Did the accused bring a woman into Singapore, or assist in bringing her, by whatever means? (s 373A(b))"),
        ("the accused intends that the woman may be sold or bought for the purpose of prostitution", "Did the accused intend that the woman might be sold or bought for the purpose of prostitution? (s 373A(b))"),
        ("the accused sells or buys a woman for the purpose of prostitution", "Did the accused sell or buy a woman for the purpose of prostitution? (s 373A(c))"),
    ],
    defs=[dict(
        name="imports, sells or buys a woman for prostitution within section 373A", lines=(8101, 8110),
        export="Whether the accused commits the offence in section 373A of the Penal Code 1871 (bringing a woman into Singapore for prostitution by deceit, bringing her for sale or purchase for prostitution, or selling or buying her for prostitution)",
        conj=[
            ("Whoever (a) by any false pretence, false representation, or fraudulent or deceitful means, brings, or assists in bringing, into Singapore any woman with intent that such woman may be employed or used for the purpose of prostitution; (b) brings, or assists in bringing, into Singapore any woman with intent that such woman may be sold or bought for the purpose of prostitution; or (c) sells or buys any woman for the purpose of prostitution",
             "([the accused by any false pretence, false representation, or fraudulent or deceitful means brings, or assists in bringing, into Singapore a woman] AND [the accused intends that the woman may be employed or used for the purpose of prostitution]) OR ([the accused brings, or assists in bringing, into Singapore a woman] AND [the accused intends that the woman may be sold or bought for the purpose of prostitution]) OR [the accused sells or buys a woman for the purpose of prostitution]",
             "the accused, by deceit, brings a woman into Singapore for prostitution; or brings her into Singapore for sale or purchase for prostitution; or sells or buys her for prostitution"),
        ])],
    offences=[dict(
        label="373A", lines=(8101, 8113), punish=["373A"],
        export_offence="Whether the accused has committed an offence punishable under section 373A of the Penal Code 1871 (importing woman for purposes of prostitution, etc.)",
        export_charge="Frame a charge under section 373A of the Penal Code 1871 (importing woman for purposes of prostitution, etc.), or say why none can be framed",
        offence_quote="shall be punished with imprisonment for a term not exceeding 10 years, and shall also be liable to fine",
        defn="`imports, sells or buys a woman for prostitution within section 373A` f",
        punish_expr="`punishment prescribed by s 373A`'s words", charge_name="importing woman for purposes of prostitution, etc.",
        miss_from=['imports, sells or buys a woman for prostitution within section 373A'],
        charge_body='CONCAT (IF [the accused sells or buys a woman for the purpose of prostitution] THEN "did sell or buy " ELSE "did bring, or assist in bringing, into Singapore "), {v}, (IF [the accused sells or buys a woman for the purpose of prostitution] THEN ", a woman, for the purpose of prostitution" ELSE (IF [the accused by any false pretence, false representation, or fraudulent or deceitful means brings, or assists in bringing, into Singapore a woman] THEN ", a woman, by false pretence, false representation or fraudulent or deceitful means, with intent that she be employed or used for the purpose of prostitution" ELSE ", a woman, with intent that she be sold or bought for the purpose of prostitution")), ", to wit, ", {m}',
    )],
))
