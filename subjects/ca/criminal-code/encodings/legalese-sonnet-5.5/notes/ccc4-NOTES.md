# NOTES -- ccc4: the Criminal Code of Canada, lines 1904-2381 (sections 84 to 110.3, Part III first half)

Status of this file, 2026-11-16: written after the modules, the tests and the seat layer were finished and checked; the counts below were measured against the files of this folder on that date (by the scripts named, or by `grep` on the files), and no `.l4` file was edited after the `check.sh` run quoted at the end.
It describes what is on disk (`check.sh` output at the end); nothing in it is a plan.

**About the text.**
The source is a plain-text rendering, made by a converter script, of the English text of the Criminal Code from the Justice Laws Website consolidation, under the Reproduction Order and the Open Government Licence - Canada (`inputs/STUB-SOURCE-LICENSE.md`).
It is not the official text, the French version (equally authoritative) is not among the sources, and nothing here is claimed verified against the official text.
Every quotation in the `.l4` files is copied from the raw text mechanically (`-- src:N | ...` lines, checked by `srcrefs.py` in both modes: 0 problems).
The consolidation date is the one in `inputs/R.S.C.-1985-c.-C-46.meta.json` ("Act current to 2026-09-30 and last amended on 2026-07-18", fetched 2026-10-21).

**Where the brief and PLAN.md differ.**
The brief governs, as it says it does (brief, line 3).
(1) PLAN section 1 says a part receives `ccc-core.l4` only, and not `ccc-definitions.l4`; the brief (file layout) lists `ccc-core.l4` and `ccc-definitions.l4` as the keel's read-only files, and `ccc-interpretation.l4` is in the folder too, so the seat layer imports all three and calls the keel's `s 2 ...` terms, `s 3.01(1)` and `s 3.01(2)`; layer 1 still takes each answer of section 2 and section 3.01 as an input (PLAN R4), so the merge stays mechanical.
(2) The ruling of 2026-11-12 on a function named for a grant or a power, and the name-test sweep, are in the brief and not in PLAN.md.
(3) The brief's rules for naming seat questions ("Under section N,") and for their direction (a question's name asks what its body answers, in the same direction) are not in PLAN.md.

**Files.**
Layer 1: `ccc4-s84-definitions.l4`, `ccc4-s85-98-use-possession.l4`, `ccc4-s99-108-trafficking-and-others.l4`, `ccc4-s109-110-3-prohibition-orders.l4`; tests: `ccc4-tests-s84.l4`, `ccc4-tests-s85-98.l4`, `ccc4-tests-s99-108.l4`, `ccc4-tests-s109-110-3.l4`.
Layer 2: `ccc4-seat.l4` (121 questions), `ccc4-cases-seat.l4` (660 assertions, every question has at least one) and `ccc4-cases-seat-expected-red.l4` (6 assertions meant to fail, findings 12 and 13).
Also `NOTES.md`, `NEEDS-CORE.md`, `PROGRESS.md`.
The scripts that build them are in `../../../work/` (not shipped): `build.py`, `gen_*.py`, `gentests.py`, `gen_seat.py`, `gen_seat_cases.py`, `lint-kinds.py`, `cmp-traces.py`, `units.py`, `cover.py`, `notes_*.py`.

## Coverage (ccc4)

One row per text unit of lines 1904-2381 (334 units: every section, subsection, paragraph, sub-paragraph and defined term; a heading line belongs to the unit it introduces).
`work/units.py` builds the unit list from the raw text and checks that every one of the 468 non-blank lines of the range falls in exactly one unit.
The L4 name is the narrowest rule or type of layer 1 whose `@ref` source lines cover the unit (`work/cover.py`); the table is built by `work/notes_cov.py`, and the script fails if a name it prints is not defined in a module.
A unit with a `fork` disposition points at the register below; the other rows that a fork touches without changing their disposition are named in the register.

| unit | lines | kind | disposition | L4 name |
| --- | --- | --- | --- | --- |
| s 84(1) | 1904-1908 | subsection | inert (1) | (the lead-in words "In this Part," and the headings: they scope the definitions and create no rule) |
| s 84(1) "ammunition" | 1909 | defined term | encoded | `s 84(1) ammunition kind`; `s 84(1) ammunition` |
| s 84(1) "antique firearm" | 1910 | defined term | encoded | `s 84(1) antique firearm` |
| s 84(1) "antique firearm"(a) | 1911 | paragraph | encoded | `s 84(1) antique firearm` |
| s 84(1) "antique firearm"(b) | 1912 | paragraph | encoded | `s 84(1) antique firearm` |
| s 84(1) "authorization" | 1913 | defined term | encoded | `s 84(1) authorization` |
| s 84(1) "automatic firearm" | 1914 | defined term | encoded | `s 84(1) automatic firearm` |
| s 84(1) "cartridge magazine" | 1915 | defined term | encoded | `s 84(1) cartridge magazine` |
| s 84(1) "chief firearms officer" | 1916 | defined term | encoded | `s 84(1) chief firearms officer` |
| s 84(1) "Commissioner of Firearms" | 1917 | defined term | encoded | `s 84(1) Commissioner of Firearms` |
| s 84(1) "cross-bow" | 1918 | defined term | encoded | `s 84(1) cross-bow` |
| s 84(1) "export" | 1919 | defined term | encoded | `s 84(1) export` |
| s 84(1) "firearm part" | 1920 | defined term | encoded | `s 84(1) firearm part` |
| s 84(1) "firearms officer" | 1921 | defined term | encoded | `s 84(1) firearms officer` |
| s 84(1) "handgun" | 1922 | defined term | encoded | `s 84(1) handgun` |
| s 84(1) "imitation firearm" | 1923 | defined term | fork (F2) | `s 84(1) imitation firearm` |
| s 84(1) "import" | 1924 | defined term | encoded | `s 84(1) import` |
| s 84(1) "licence" | 1925 | defined term | encoded | `s 84(1) licence` |
| s 84(1) "non-restricted firearm" | 1926 | defined term | encoded | `s 84(1) non-restricted firearm`; `s 84(1) class of firearm` (+2) |
| s 84(1) "prescribed" | 1927 | defined term | encoded | `s 84(1) prescribed` |
| s 84(1) "prohibited ammunition" | 1928 | defined term | encoded | `s 84(1) prohibited ammunition`; `s 84(1) the kind of thing is ammunition or prohibited ammunition` |
| s 84(1) "prohibited device" | 1929 | defined term | encoded | `s 84(1) prohibited device`; `s 84(1) kind of thing` (+1) |
| s 84(1) "prohibited device"(a) | 1930 | paragraph | encoded | `s 84(1) prohibited device`; `s 84(1) kind of thing` (+1) |
| s 84(1) "prohibited device"(b) | 1931 | paragraph | encoded | `s 84(1) prohibited device`; `s 84(1) kind of thing` (+1) |
| s 84(1) "prohibited device"(c) | 1932 | paragraph | encoded | `s 84(1) prohibited device`; `s 84(1) kind of thing` (+1) |
| s 84(1) "prohibited device"(d) | 1933 | paragraph | encoded | `s 84(1) prohibited device`; `s 84(1) kind of thing` (+1) |
| s 84(1) "prohibited device"(e) | 1934 | paragraph | encoded | `s 84(1) prohibited device`; `s 84(1) kind of thing` (+1) |
| s 84(1) "prohibited firearm" | 1935 | defined term | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(a) | 1936 | paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(a)(i) | 1937 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(a)(ii) | 1938-1939 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(b) | 1940 | paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(b)(i) | 1941 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(b)(ii) | 1942 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(c) | 1943 | paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(d) | 1944 | paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(e) | 1945 | paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(e)#2 | 1946 | paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(e)#2(i) | 1947 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(e)#2(ii) | 1948 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited firearm"(e)#2(iii) | 1949 | sub-paragraph | encoded | `s 84(1) prohibited firearm` |
| s 84(1) "prohibited weapon" | 1950 | defined term | encoded | `s 84(1) prohibited weapon` |
| s 84(1) "prohibited weapon"(a) | 1951 | paragraph | encoded | `s 84(1) prohibited weapon` |
| s 84(1) "prohibited weapon"(b) | 1952 | paragraph | encoded | `s 84(1) prohibited weapon` |
| s 84(1) "prohibition order" | 1953 | defined term | encoded | `s 84(1) prohibition order` |
| s 84(1) "Registrar" | 1954 | defined term | encoded | `s 84(1) Registrar` |
| s 84(1) "registration certificate" | 1955 | defined term | encoded | `s 84(1) registration certificate` |
| s 84(1) "replica firearm" | 1956 | defined term | encoded | `s 84(1) replica firearm` |
| s 84(1) "restricted firearm" | 1957 | defined term | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(a) | 1958 | paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(b) | 1959 | paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(b)(i) | 1960 | sub-paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(b)(ii) | 1961 | sub-paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(b)(iii) | 1962 | sub-paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(c) | 1963 | paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted firearm"(d) | 1964 | paragraph | encoded | `s 84(1) restricted firearm` |
| s 84(1) "restricted weapon" | 1965-1966 | defined term | encoded | `s 84(1) restricted weapon`; `s 84(1) semi-automatic` |
| s 84(1) "superior court" | 1967 | defined term | encoded | `s 84(1) superior court`; `s 84(1) the superior court in the place` |
| s 84(1) "superior court"(a) | 1968 | paragraph | encoded | `s 84(1) superior court`; `s 84(1) the superior court in the place` |
| s 84(1) "superior court"(b) | 1969 | paragraph | encoded | `s 84(1) superior court`; `s 84(1) the superior court in the place` |
| s 84(1) "superior court"(c) | 1970 | paragraph | encoded | `s 84(1) superior court`; `s 84(1) the superior court in the place` |
| s 84(1) "superior court"(d) | 1971 | paragraph | fork (F-Nunavut) | `s 84(1) superior court`; `s 84(1) the superior court in the place` |
| s 84(1) "superior court"(e) | 1972 | paragraph | repealed or blank in this text | (the text shows (e) [Repealed, 2026, c. 11, s. 3]) |
| s 84(1) "transfer" | 1973 | defined term | encoded | `s 84(1) transfer act`; `s 84(1) transfer` |
| s 84(2) | 1974-1975 | subsection | encoded | `s 84(2) the length of the barrel of a firearm in millimetres` |
| s 84(2)(a) | 1976 | paragraph | encoded | `s 84(2) the length of the barrel of a firearm in millimetres` |
| s 84(2)(b) | 1977-1978 | paragraph | encoded | `s 84(2) the length of the barrel of a firearm in millimetres` |
| s 84(3) | 1979-1980 | subsection | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(a) | 1981 | paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(b) | 1982 | paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(b)(i) | 1983 | sub-paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(b)(ii) | 1984 | sub-paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(c) | 1985 | paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(c)(i) | 1986 | sub-paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(c)(ii) | 1987 | sub-paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(d) | 1988 | paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(d)(i) | 1989 | sub-paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3)(d)(ii) | 1990 | sub-paragraph | encoded | `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` |
| s 84(3.1) | 1991-1992 | subsection | encoded | `s 84(3.1) the antique firearm is a firearm for the purpose` |
| s 84(4) | 1993-1994 | subsection | encoded | `s 84(4)(a) the person is the holder of an authorization or a licence` |
| s 84(4)(a) | 1995 | paragraph | encoded | `s 84(4)(a) the person is the holder of an authorization or a licence` |
| s 84(4)(b) | 1996 | paragraph | encoded | `s 84(4)(b) the person is the holder of a registration certificate for a firearm` |
| s 84(4)(b)(i) | 1997 | sub-paragraph | encoded | `s 84(4)(b) the person is the holder of a registration certificate for a firearm` |
| s 84(4)(b)(ii) | 1998 | sub-paragraph | encoded | `s 84(4)(b) the person is the holder of a registration certificate for a firearm` |
| s 84(5) | 1999-2000 | subsection | encoded | `s 84(5) the earlier offence is to be considered as an earlier offence` |
| s 84(5)(a) | 2001 | paragraph | encoded | `s 84(5) the earlier offence is to be considered as an earlier offence` |
| s 84(5)(b) | 2002 | paragraph | encoded | `s 84(5) the earlier offence is to be considered as an earlier offence` |
| s 84(5)(c) | 2003-2004 | paragraph | fork (F-ten-years) | `s 84(5) the earlier offence is to be considered as an earlier offence` |
| s 84(6) | 2005-2006 | subsection | encoded | `s 84(6) offence`; `s 84(6) offence one is the earlier offence for the purposes of subsection (5)` |
| s 85(1) | 2008-2010 | subsection | fork (F-OF) | `s 85(1) the person commits an offence by using a firearm in the commission of an offence` |
| s 85(1)(a) | 2011 | paragraph | encoded | `s 85(1) the person commits an offence by using a firearm in the commission of an offence` |
| s 85(1)(b) | 2012 | paragraph | encoded | `s 85(1) the person commits an offence by using a firearm in the commission of an offence` |
| s 85(1)(c) | 2013 | paragraph | encoded | `s 85(1) the person commits an offence by using a firearm in the commission of an offence` |
| s 85(2) | 2014-2015 | subsection | fork (F-OF) | `s 85(2) the person commits an offence by using an imitation firearm in the commission of an offence` |
| s 85(2)(a) | 2016 | paragraph | encoded | `s 85(2) the person commits an offence by using an imitation firearm in the commission of an offence` |
| s 85(2)(b) | 2017 | paragraph | encoded | `s 85(2) the person commits an offence by using an imitation firearm in the commission of an offence` |
| s 85(2)(c) | 2018-2019 | paragraph | encoded | `s 85(2) the person commits an offence by using an imitation firearm in the commission of an offence` |
| s 85(3) | 2020-2021 | subsection | encoded | `s 85(3) the class of the offence`; `s 85(3) the punishment on indictment` |
| s 85(4) | 2022-2024 | subsection | encoded | `s 85(4) the sentence must be served consecutively to the other punishment or sentence` |
| s 86(1) | 2025-2026 | subsection | fork (F-OF) | `s 86(1) the person commits an offence of careless use of a firearm, etc.` |
| s 86(2) | 2027 | subsection | fork (F-OF) | `s 86(2) the person commits an offence by contravening a storage regulation, etc.` |
| s 86(3) | 2028-2029 | subsection | encoded | `s 86(3) the class of the offence`; `s 86(3)(a) the punishment on indictment` |
| s 86(3)(a) | 2030 | paragraph | encoded | `s 86(3)(a) the punishment on indictment` |
| s 86(3)(a)(i) | 2031 | sub-paragraph | encoded | `s 86(3)(a) the punishment on indictment` |
| s 86(3)(a)(ii) | 2032 | sub-paragraph | encoded | `s 86(3)(a) the punishment on indictment` |
| s 86(3)(b) | 2033 | paragraph | encoded | `s 86(3)(b) the punishment on summary conviction` |
| s 87(1) | 2034-2035 | subsection | fork (F-OF) | `s 87(1) the person commits the offence of pointing a firearm` |
| s 87(2) | 2036-2037 | subsection | encoded | `s 87(2) the class of the offence`; `s 87(2)(a) the punishment on indictment` |
| s 87(2)(a) | 2038 | paragraph | encoded | `s 87(2)(a) the punishment on indictment` |
| s 87(2)(b) | 2039 | paragraph | encoded | `s 87(2)(b) the punishment on summary conviction` |
| s 88(1) | 2041-2043 | subsection | fork (F-OF, F-weapon) | `s 88(1) the person commits an offence of possession of a weapon for a dangerous purpose` |
| s 88(2) | 2044-2045 | subsection | encoded | `s 88(2) the class of the offence`; `s 88(2)(a) the punishment on indictment` |
| s 88(2)(a) | 2046 | paragraph | encoded | `s 88(2)(a) the punishment on indictment` |
| s 88(2)(b) | 2047 | paragraph | encoded | `s 88(2)(b) the punishment on summary conviction` |
| s 89(1) | 2048-2049 | subsection | fork (F-OF, F-weapon) | `s 89(1) the person commits an offence of carrying a weapon while attending a public meeting` |
| s 89(2) | 2050-2051 | subsection | encoded | `s 89(2) the class of the offence`; `s 89(2) the punishment on summary conviction` |
| s 90(1) | 2052-2053 | subsection | fork (F-OF, F-weapon) | `s 90(1) the person commits an offence of carrying a concealed weapon` |
| s 90(2) | 2054-2055 | subsection | encoded | `s 90(2) the class of the offence`; `s 90(2)(a) the punishment on indictment` |
| s 90(2)(a) | 2056 | paragraph | encoded | `s 90(2)(a) the punishment on indictment` |
| s 90(2)(b) | 2057 | paragraph | encoded | `s 90(2)(b) the punishment on summary conviction` |
| s 91(1) | 2058-2059 | subsection | fork (F-OF) | `s 91(1) the person commits an offence of unauthorized possession of a firearm` |
| s 91(1)(a) | 2060 | paragraph | encoded | `s 91(1) the person commits an offence of unauthorized possession of a firearm` |
| s 91(1)(b) | 2061 | paragraph | encoded | `s 91(1) the person commits an offence of unauthorized possession of a firearm` |
| s 91(2) | 2062-2063 | subsection | fork (F-OF) | `s 91(2) the person commits an offence of unauthorized possession of a prohibited weapon or restricted weapon` |
| s 91(3) | 2064-2065 | subsection | encoded | `s 91(3) the class of the offence`; `s 91(3)(a) the punishment on indictment` |
| s 91(3)(a) | 2066 | paragraph | encoded | `s 91(3)(a) the punishment on indictment` |
| s 91(3)(b) | 2067 | paragraph | encoded | `s 91(3)(b) the punishment on summary conviction` |
| s 91(4) | 2068-2069 | subsection | encoded | `s 91(4) subsections (1) and (2) do not apply to the person` |
| s 91(4)(a) | 2070 | paragraph | encoded | `s 91(4) subsections (1) and (2) do not apply to the person` |
| s 91(4)(b) | 2071 | paragraph | encoded | `s 91(4) subsections (1) and (2) do not apply to the person` |
| s 91(4)(b)(i) | 2072 | sub-paragraph | encoded | `s 91(4) subsections (1) and (2) do not apply to the person` |
| s 91(4)(b)(ii) | 2073 | sub-paragraph | encoded | `s 91(4) subsections (1) and (2) do not apply to the person` |
| s 91(5) | 2074 | subsection | repealed or blank in this text | (the text shows (5) [Repealed, 2012, c. 6, s. 2]) |
| s 92(1) | 2075-2076 | subsection | fork (F-OF) | `s 92(1) the person commits an offence of possession of a firearm knowing its possession is unauthorized` |
| s 92(1)(a) | 2077 | paragraph | encoded | `s 92(1) the person commits an offence of possession of a firearm knowing its possession is unauthorized` |
| s 92(1)(b) | 2078-2079 | paragraph | encoded | `s 92(1) the person commits an offence of possession of a firearm knowing its possession is unauthorized` |
| s 92(2) | 2080 | subsection | fork (F-OF) | `s 92(2) the person commits an offence of possession of a prohibited weapon, device or ammunition knowing its possession is unauthorized` |
| s 92(3) | 2081-2082 | subsection | encoded | `s 92(3) the class of the offence`; `s 92(3) the punishment on indictment` |
| s 92(4) | 2083-2084 | subsection | encoded | `s 92(4) subsections (1) and (2) do not apply to the person` |
| s 92(4)(a) | 2085 | paragraph | encoded | `s 92(4) subsections (1) and (2) do not apply to the person` |
| s 92(4)(b) | 2086 | paragraph | encoded | `s 92(4) subsections (1) and (2) do not apply to the person` |
| s 92(4)(b)(i) | 2087 | sub-paragraph | encoded | `s 92(4) subsections (1) and (2) do not apply to the person` |
| s 92(4)(b)(ii) | 2088 | sub-paragraph | encoded | `s 92(4) subsections (1) and (2) do not apply to the person` |
| s 92(5) | 2089 | subsection | repealed or blank in this text | (the text shows (5) and (6) [Repealed, 2012, c. 6, s. 3]) |
| s 93(1) | 2090-2091 | subsection | fork (F-OF) | `s 93(1) the person commits an offence of possession at an unauthorized place` |
| s 93(1)(a) | 2092 | paragraph | encoded | `s 93(1) the person commits an offence of possession at an unauthorized place` |
| s 93(1)(b) | 2093 | paragraph | encoded | `s 93(1) the person commits an offence of possession at an unauthorized place` |
| s 93(1)(c) | 2094 | paragraph | encoded | `s 93(1) the person commits an offence of possession at an unauthorized place` |
| s 93(2) | 2095-2096 | subsection | encoded | `s 93(2) the class of the offence`; `s 93(2)(a) the punishment on indictment` |
| s 93(2)(a) | 2097 | paragraph | encoded | `s 93(2)(a) the punishment on indictment` |
| s 93(2)(b) | 2098 | paragraph | encoded | `s 93(2)(b) the punishment on summary conviction` |
| s 93(3) | 2099-2100 | subsection | encoded | `s 93(3) subsection (1) does not apply to a person who possesses a replica firearm` |
| s 94(1) | 2101-2102 | subsection | fork (F-OF) | `s 94(1) the person commits an offence of unauthorized possession in a motor vehicle` |
| s 94(1)(a) | 2103 | paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(i) | 2104 | sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(i)(A) | 2105 | sub-sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(i)(B) | 2106 | sub-sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(ii) | 2107 | sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(ii)(A) | 2108 | sub-sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(ii)(B) | 2109 | sub-sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(a)(iii) | 2110 | sub-paragraph | encoded | `s 94(1)(a) the occupant is within the exception for a firearm` |
| s 94(1)(b) | 2111 | paragraph | encoded | `s 94(1)(b) the occupant is within the exception for a weapon, device or ammunition` |
| s 94(1)(b)(i) | 2112 | sub-paragraph | encoded | `s 94(1)(b) the occupant is within the exception for a weapon, device or ammunition` |
| s 94(1)(b)(ii) | 2113 | sub-paragraph | encoded | `s 94(1)(b) the occupant is within the exception for a weapon, device or ammunition` |
| s 94(1)(b)(ii)(A) | 2114 | sub-sub-paragraph | encoded | `s 94(1)(b) the occupant is within the exception for a weapon, device or ammunition` |
| s 94(1)(b)(ii)(B) | 2115 | sub-sub-paragraph | encoded | `s 94(1)(b) the occupant is within the exception for a weapon, device or ammunition` |
| s 94(2) | 2116-2117 | subsection | encoded | `s 94(2) the class of the offence`; `s 94(2)(a) the punishment on indictment` |
| s 94(2)(a) | 2118 | paragraph | encoded | `s 94(2)(a) the punishment on indictment` |
| s 94(2)(b) | 2119 | paragraph | encoded | `s 94(2)(b) the punishment on summary conviction` |
| s 94(3) | 2120-2121 | subsection | encoded | `s 94(3) subsection (1) does not apply to an occupant who attempted to leave or left the motor vehicle` |
| s 94(4) | 2122-2123 | subsection | encoded | `s 94(4) subsection (1) does not apply when an occupant came into possession by the operation of law` |
| s 94(5) | 2124 | subsection | repealed or blank in this text | (the text shows (5) [Repealed, 2012, c. 6, s. 4]) |
| s 95(1) | 2125-2126 | subsection | fork (F-OF) | `s 95(1) the person commits an offence of possession of a prohibited or restricted firearm with ammunition` |
| s 95(1)(a) | 2127 | paragraph | encoded | `s 95(1) the person commits an offence of possession of a prohibited or restricted firearm with ammunition` |
| s 95(1)(b) | 2128 | paragraph | encoded | `s 95(1) the person commits an offence of possession of a prohibited or restricted firearm with ammunition` |
| s 95(2) | 2129-2130 | subsection | encoded | `s 95(2) the class of the offence`; `s 95(2)(a) the punishment on indictment` |
| s 95(2)(a) | 2131 | paragraph | encoded | `s 95(2)(a) the punishment on indictment` |
| s 95(2)(b) | 2132 | paragraph | encoded | `s 95(2)(b) the punishment on summary conviction` |
| s 95(3) | 2133-2134 | subsection | encoded | `s 95(3) subsection (1) does not apply to the person` |
| s 96(1) | 2135-2136 | subsection | fork (F-OF) | `s 96(1) the person commits an offence of possession of a weapon obtained by the commission of an offence` |
| s 96(2) | 2137-2138 | subsection | encoded | `s 96(2) the class of the offence`; `s 96(2)(a) the punishment on indictment` |
| s 96(2)(a) | 2139 | paragraph | encoded | `s 96(2)(a) the punishment on indictment` |
| s 96(2)(b) | 2140 | paragraph | encoded | `s 96(2)(b) the punishment on summary conviction` |
| s 96(3) | 2141-2142 | subsection | encoded | `s 96(3) subsection (1) does not apply to the person` |
| s 97 | 2143 | section | repealed or blank in this text | (the text shows 97 [Repealed before coming into force, 2008, c. 20, s. 3]) |
| s 98(1) | 2144-2145 | subsection | fork (F-OF) | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98(1)(a) | 2146 | paragraph | encoded | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98(1)(b) | 2147 | paragraph | encoded | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98(1)(c) | 2148 | paragraph | encoded | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98(1)(c)(i) | 2149 | sub-paragraph | encoded | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98(1)(c)(ii) | 2150 | sub-paragraph | encoded | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98(2) | 2151-2152 | subsection | encoded | `s 98(2) place`; `s 98(2) break` |
| s 98(3) | 2153-2154 | subsection | encoded | `s 98(3)(a) the person enters` |
| s 98(3)(a) | 2155 | paragraph | encoded | `s 98(3)(a) the person enters` |
| s 98(3)(b) | 2156 | paragraph | encoded | `s 98(3)(b) the person is deemed to have broken and entered` |
| s 98(3)(b)(i) | 2157 | sub-paragraph | encoded | `s 98(3)(b) the person is deemed to have broken and entered` |
| s 98(3)(b)(ii) | 2158 | sub-paragraph | encoded | `s 98(3)(b) the person is deemed to have broken and entered` |
| s 98(4) | 2159-2160 | subsection | encoded | `s 98(4) the class of the offence`; `s 98(4) the punishment on indictment` |
| s 98.1 | 2161-2162 | section | fork (F-OF) | `s 98.1 the person commits an offence of robbery to steal a firearm`; `s 98.1 the class of the offence` (+1) |
| s 99(1) | 2164-2166 | subsection | fork (F-OF) | `s 99(1) the person commits an offence of weapons trafficking` |
| s 99(1)(a) | 2167 | paragraph | encoded | `s 99(1) the person commits an offence of weapons trafficking` |
| s 99(1)(b) | 2168-2169 | paragraph | encoded | `s 99(1) the person commits an offence of weapons trafficking` |
| s 99(2) | 2170-2171 | subsection | encoded | `s 99(2) the class of the offence`; `s 99(2) the punishment when the object in question is a firearm, device, part or ammunition` |
| s 99(2)(a) | 2172 | paragraph | encoded | `s 99(2) three years` |
| s 99(2)(b) | 2173 | paragraph | encoded | `s 99(2) three years` |
| s 99(3) | 2174-2175 | subsection | encoded | `s 99(3) the class of the offence`; `s 99(3) the punishment in any other case` |
| s 100(1) | 2176-2177 | subsection | fork (F-OF) | `s 100(1) the person commits an offence of possession for the purpose of weapons trafficking` |
| s 100(1)(a) | 2178 | paragraph | encoded | `s 100(1) the person commits an offence of possession for the purpose of weapons trafficking` |
| s 100(1)(b) | 2179-2180 | paragraph | encoded | `s 100(1) the person commits an offence of possession for the purpose of weapons trafficking` |
| s 100(2) | 2181-2182 | subsection | encoded | `s 100(2) the class of the offence`; `s 100(2) the punishment when the object in question is a firearm, device, part or ammunition` |
| s 100(2)(a) | 2183 | paragraph | encoded | `s 100(2) the class of the offence`; `s 100(2) the punishment when the object in question is a firearm, device, part or ammunition` |
| s 100(2)(b) | 2184 | paragraph | encoded | `s 100(2) the class of the offence`; `s 100(2) the punishment when the object in question is a firearm, device, part or ammunition` |
| s 100(3) | 2185-2186 | subsection | encoded | `s 100(3) the class of the offence`; `s 100(3) the punishment in any other case` |
| s 101(1) | 2187-2188 | subsection | fork (F-OF) | `s 101(1) the person commits an offence of transfer without authority` |
| s 101(2) | 2189-2190 | subsection | encoded | `s 101(2) the class of the offence`; `s 101(2)(a) the punishment on indictment` |
| s 101(2)(a) | 2191 | paragraph | encoded | `s 101(2)(a) the punishment on indictment` |
| s 101(2)(b) | 2192 | paragraph | encoded | `s 101(2)(b) the punishment on summary conviction` |
| s 102(1) | 2194-2196 | subsection | fork (F-OF) | `s 102(1) the person commits an offence of making an automatic firearm` |
| s 102(2) | 2197-2198 | subsection | encoded | `s 102(2) the class of the offence`; `s 102(2)(a) the punishment on indictment` |
| s 102(2)(a) | 2199 | paragraph | encoded | `s 102(2)(a) the punishment on indictment` |
| s 102(2)(b) | 2200 | paragraph | encoded | `s 102(2)(b) the punishment on summary conviction` |
| s 102.1(1) | 2202-2204 | subsection | fork (F-OF) | `s 102.1(1) the person commits an offence of possession of computer data` |
| s 102.1(2) | 2205-2206 | subsection | fork (F-OF) | `s 102.1(2) the person commits an offence of distribution of computer data` |
| s 102.1(3) | 2207-2208 | subsection | encoded | `s 102.1(3) the class of the offence`; `s 102.1(3)(a) the punishment on indictment` |
| s 102.1(3)(a) | 2209 | paragraph | encoded | `s 102.1(3)(a) the punishment on indictment` |
| s 102.1(3)(b) | 2210 | paragraph | encoded | `s 102.1(3)(b) the punishment on summary conviction` |
| s 102.1(4) | 2211-2212 | subsection | encoded | `s 102.1(4) computer data`; `s 102.1(4) computer system` |
| s 103(1) | 2214-2216 | subsection | fork (F-OF) | `s 103(1) the person commits an offence of importing or exporting knowing it is unauthorized` |
| s 103(1)(a) | 2217 | paragraph | encoded | `s 103(1) the person commits an offence of importing or exporting knowing it is unauthorized` |
| s 103(1)(b) | 2218-2219 | paragraph | encoded | `s 103(1) the person commits an offence of importing or exporting knowing it is unauthorized` |
| s 103(2) | 2220-2221 | subsection | encoded | `s 103(2) the class of the offence`; `s 103(2) the punishment when the object in question is a firearm, device, part or prohibited ammunition` |
| s 103(2)(a) | 2222 | paragraph | encoded | `s 103(2) the class of the offence`; `s 103(2) the punishment when the object in question is a firearm, device, part or prohibited ammunition` |
| s 103(2)(b) | 2223 | paragraph | encoded | `s 103(2) the class of the offence`; `s 103(2) the punishment when the object in question is a firearm, device, part or prohibited ammunition` |
| s 103(2.1) | 2224-2225 | subsection | encoded | `s 103(2.1) the class of the offence`; `s 103(2.1) the punishment in any other case` |
| s 103(3) | 2226 | subsection | repealed or blank in this text | (the text shows (3) [Repealed, 2019, c. 25, s. 28]) |
| s 104(1) | 2227-2228 | subsection | fork (F-OF) | `s 104(1) the person commits an offence of unauthorized importing or exporting` |
| s 104(1)(a) | 2229 | paragraph | encoded | `s 104(1) the person commits an offence of unauthorized importing or exporting` |
| s 104(1)(b) | 2230-2231 | paragraph | encoded | `s 104(1) the person commits an offence of unauthorized importing or exporting` |
| s 104(2) | 2232-2233 | subsection | encoded | `s 104(2) the class of the offence`; `s 104(2)(a) the punishment on indictment` |
| s 104(2)(a) | 2234 | paragraph | encoded | `s 104(2)(a) the punishment on indictment` |
| s 104(2)(b) | 2235 | paragraph | encoded | `s 104(2)(b) the punishment on summary conviction` |
| s 104(3) | 2236 | subsection | repealed or blank in this text | (the text shows (3) [Repealed, 2019, c. 25, s. 29]) |
| s 104.1(1) | 2238-2240 | subsection | fork (F-OF) | `s 104.1(1) the person commits an offence of altering a cartridge magazine` |
| s 104.1(2) | 2241-2242 | subsection | encoded | `s 104.1(2) the class of the offence`; `s 104.1(2)(a) the punishment on indictment` |
| s 104.1(2)(a) | 2243 | paragraph | encoded | `s 104.1(2)(a) the punishment on indictment` |
| s 104.1(2)(b) | 2244-2246 | paragraph | encoded | `s 104.1(2)(b) the punishment on summary conviction` |
| s 105(1) | 2247-2248 | subsection | fork (F-OF, F-despatch) | `s 105(1)(a) the person commits an offence by not reporting a loss`; `s 105(1)(a) the duty to report a loss` |
| s 105(1)(a) | 2249 | paragraph | encoded | `s 105(1)(a) the person commits an offence by not reporting a loss`; `s 105(1)(a) the duty to report a loss` |
| s 105(1)(b) | 2250 | paragraph | encoded | `s 105(1)(b) the person commits an offence by not delivering or reporting a find`; `s 105(1)(b) the duty to deliver or report a find` |
| s 105(2) | 2251-2252 | subsection | encoded | `s 105(2) the class of the offence`; `s 105(2)(a) the punishment on indictment` |
| s 105(2)(a) | 2253 | paragraph | encoded | `s 105(2)(a) the punishment on indictment` |
| s 105(2)(b) | 2254 | paragraph | encoded | `s 105(2)(b) the punishment on summary conviction` |
| s 106(1) | 2255-2256 | subsection | fork (F-OF, F-despatch) | `s 106(1) the person commits an offence by not reporting a destruction`; `s 106(1) the duty to report a destruction` |
| s 106(1)(a) | 2257 | paragraph | encoded | `s 106(1) the person commits an offence by not reporting a destruction`; `s 106(1) the duty to report a destruction` |
| s 106(1)(b) | 2258-2259 | paragraph | encoded | `s 106(1) the person commits an offence by not reporting a destruction`; `s 106(1) the duty to report a destruction` |
| s 106(2) | 2260-2261 | subsection | encoded | `s 106(2) the class of the offence`; `s 106(2)(a) the punishment on indictment` |
| s 106(2)(a) | 2262 | paragraph | encoded | `s 106(2)(a) the punishment on indictment` |
| s 106(2)(b) | 2263 | paragraph | encoded | `s 106(2)(b) the punishment on summary conviction` |
| s 107(1) | 2264-2265 | subsection | fork (F-OF) | `s 107(1) the person commits an offence by making a false report or statement` |
| s 107(2) | 2266-2267 | subsection | encoded | `s 107(2) the class of the offence`; `s 107(2)(a) the punishment on indictment` |
| s 107(2)(a) | 2268 | paragraph | encoded | `s 107(2)(a) the punishment on indictment` |
| s 107(2)(b) | 2269 | paragraph | encoded | `s 107(2)(b) the punishment on summary conviction` |
| s 107(3) | 2270-2271 | subsection | encoded | `s 107(3) assertion`; `s 107(3) report or statement` |
| s 108(1) | 2272-2273 | subsection | fork (F-OF) | `s 108(1) the person commits an offence of tampering with a serial number` |
| s 108(1)(a) | 2274 | paragraph | encoded | `s 108(1) the person commits an offence of tampering with a serial number` |
| s 108(1)(b) | 2275 | paragraph | encoded | `s 108(1) the person commits an offence of tampering with a serial number` |
| s 108(2) | 2276-2277 | subsection | encoded | `s 108(2) the class of the offence`; `s 108(2)(a) the punishment on indictment` |
| s 108(2)(a) | 2278 | paragraph | encoded | `s 108(2)(a) the punishment on indictment` |
| s 108(2)(b) | 2279 | paragraph | encoded | `s 108(2)(b) the punishment on summary conviction` |
| s 108(3) | 2280-2281 | subsection | encoded | `s 108(3) no person is guilty of an offence under paragraph (1)(b) by reason only of possessing the firearm` |
| s 108(4) | 2282-2283 | subsection | encoded | `s 108(4) the evidence is proof that the person possesses the firearm knowing that the serial number on it has been altered, defaced or removed` |
| s 109(1) | 2285-2287 | subsection | encoded | `s 109(1) the offence is an indictable offence`; `s 109(1)(a) the maximum imprisonment is ten years or more` (+2) |
| s 109(1)(a) | 2288 | paragraph | fork (F-hybrid, F-3.01) | `s 109(1)(a) the maximum imprisonment is ten years or more`; `s 109(1)(a) the offence is one in which violence was used and for which the person may be sentenced to imprisonment for ten years or more` |
| s 109(1)(a.1) | 2289 | paragraph | encoded | `s 109(1)(a.1) the offence is one in which violence was used against an intimate partner, a child or parent, or a person who resides with them` |
| s 109(1)(a.1)(i) | 2290 | sub-paragraph | encoded | `s 109(1)(a.1) the offence is one in which violence was used against an intimate partner, a child or parent, or a person who resides with them` |
| s 109(1)(a.1)(ii) | 2291 | sub-paragraph | encoded | `s 109(1)(a.1) the offence is one in which violence was used against an intimate partner, a child or parent, or a person who resides with them` |
| s 109(1)(a.1)(iii) | 2292 | sub-paragraph | encoded | `s 109(1)(a.1) the offence is one in which violence was used against an intimate partner, a child or parent, or a person who resides with them` |
| s 109(1)(b) | 2293 | paragraph | encoded | `s 109(1)(b) the offence is one of those the paragraph names` |
| s 109(1)(c) | 2294 | paragraph | encoded | `s 109(1)(c) the offence relates to the contravention of a subsection of the Controlled Drugs and Substances Act that the paragraph names` |
| s 109(1)(c.1) | 2295 | paragraph | encoded | `s 109(1)(c.1) the offence relates to the contravention of a subsection of the Cannabis Act that the paragraph names` |
| s 109(1)(d) | 2296-2297 | paragraph | encoded | `s 109(1)(d) the offence involves a thing the person was prohibited from possessing` |
| s 109(2) | 2298-2299 | subsection | encoded | `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` |
| s 109(2)(a) | 2300 | paragraph | fork (F-109-ammo) | `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` |
| s 109(2)(a)(i) | 2301 | sub-paragraph | encoded | `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` |
| s 109(2)(a)(ii) | 2302 | sub-paragraph | encoded | `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` |
| s 109(2)(b) | 2303 | paragraph | fork (F-109-ammo) | `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` |
| s 109(3) | 2304-2305 | subsection | encoded | `s 109(3) the period for which the order prohibits the thing, in any other case` |
| s 109(4) | 2306-2307 | subsection | encoded | `s 109(4) release from confinement`; `s 109(4) release from imprisonment` |
| s 109(5) | 2308-2309 | subsection | encoded | `s 109(5) the section applies in respect of every order made under subsection (1)` |
| s 110(1) | 2310-2311 | subsection | encoded | `s 110(1) the court must consider whether it is desirable to make a prohibition order`; `s 110(1) the court must make a prohibition order` (+1) |
| s 110(1)(a) | 2312 | paragraph | fork (F-3.01) | `s 110(1) the court must consider whether it is desirable to make a prohibition order`; `s 110(1) the court must make a prohibition order` (+1) |
| s 110(1)(b) | 2313-2314 | paragraph | encoded | `s 110(1) the court must consider whether it is desirable to make a prohibition order`; `s 110(1) the court must make a prohibition order` (+1) |
| s 110(2) | 2315-2316 | subsection | encoded | `s 110(2) the latest day on which the order may end` |
| s 110(2.1) | 2317-2318 | subsection | fork (F-110(2.1), F-3.01) | `s 110(2.1) the order may be imposed for life or for any shorter duration` |
| s 110(2.1)(a) | 2319 | paragraph | encoded | `s 110(2.1) the order may be imposed for life or for any shorter duration` |
| s 110(2.1)(b) | 2320 | paragraph | encoded | `s 110(2.1) the order may be imposed for life or for any shorter duration` |
| s 110(2.1)(c) | 2321 | paragraph | encoded | `s 110(2.1) the order may be imposed for life or for any shorter duration` |
| s 110(3) | 2322-2323 | subsection | encoded | `s 110(3) the court must include in the record a statement of its reasons`; `s 110(3) the duty of the court to include its reasons in the record` |
| s 110(4) | 2324-2325 | subsection | encoded | `s 110(4) release from confinement`; `s 110(4) release from imprisonment` |
| s 110(5) | 2326-2327 | subsection | encoded | `s 110(5) the section applies in respect of every order made under subsection (1)` |
| s 110.1(1) | 2328-2329 | subsection | fork (F-110.1(1)) | `s 110.1(1) any person may make an ex parte application to a provincial court judge for an order` |
| s 110.1(2) | 2330-2331 | subsection | fork (F-110.1(2)) | `s 110.1(2) the provincial court judge may hold the hearing in private` |
| s 110.1(3) | 2332-2333 | subsection | fork (F-110.1(3), F-30-days) | `s 110.1(3) the provincial court judge must make an emergency prohibition order`; `s 110.1(3) the period specified in the order is within the limit of thirty days` (+1) |
| s 110.1(4) | 2334-2335 | subsection | encoded | `s 110.1(4) a copy of the order must be served on the person to whom it is addressed` |
| s 110.1(5) | 2336-2337 | subsection | fork (F-110.1(5)) | `s 110.1(5) the provincial court judge may issue a warrant to search and seize` |
| s 110.1(6) | 2338-2339 | subsection | fork (F-110.1(6)) | `s 110.1(6) the peace officer may search for and seize without a warrant` |
| s 110.1(7) | 2340-2341 | subsection | fork (F-immediately) | `s 110.1(7) the peace officer must make a report to a justice`; `s 110.1(7) item of the report` (+1) |
| s 110.1(7)(a) | 2342 | paragraph | encoded | `s 110.1(7) what the report must show` |
| s 110.1(7)(b) | 2343 | paragraph | encoded | `s 110.1(7) what the report must show` |
| s 110.1(8) | 2344-2345 | subsection | encoded | `s 110.1(8) the occasion on which the things and documents must be returned to the person` |
| s 110.1(8)(a) | 2346 | paragraph | encoded | `s 110.1(8) the occasion on which the things and documents must be returned to the person` |
| s 110.1(8)(b) | 2347 | paragraph | encoded | `s 110.1(8) the occasion on which the things and documents must be returned to the person` |
| s 110.1(8)(c) | 2348 | paragraph | encoded | `s 110.1(8) the occasion on which the things and documents must be returned to the person` |
| s 110.1(9) | 2349-2350 | subsection | encoded | `s 110.1(9) the section applies in respect of every order made under subsection (3)` |
| s 110.1(10) | 2351-2352 | subsection | encoded | `s 110.1(10) provincial court judge` |
| s 110.2(1) | 2353-2354 | subsection | fork (F-110.2(1)) | `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information`; `s 110.2(1) information` |
| s 110.2(1)(a) | 2355 | paragraph | encoded | `s 110.2(1) the information is within the order that may be made` |
| s 110.2(1)(b) | 2356 | paragraph | encoded | `s 110.2(1) the information is within the order that may be made` |
| s 110.2(1)(c) | 2357 | paragraph | encoded | `s 110.2(1) the information is within the order that may be made` |
| s 110.2(1)(d) | 2358 | paragraph | encoded | `s 110.2(1) the information is within the order that may be made` |
| s 110.2(2) | 2359-2360 | subsection | encoded | `s 110.2(2) the day on which the order made under subsection (1) expires` |
| s 110.2(3) | 2361-2362 | subsection | encoded | `s 110.2(3) the day on which an order made under subsection (1) ceases to have effect` |
| s 110.2(3)(a) | 2363 | paragraph | encoded | `s 110.2(3) the day on which an order made under subsection (1) ceases to have effect` |
| s 110.2(3)(b) | 2364 | paragraph | encoded | `s 110.2(3) the day on which an order made under subsection (1) ceases to have effect` |
| s 110.2(4) | 2365-2366 | subsection | fork (F-immediately) | `s 110.2(4) the documents must be placed in a packet and sealed by the judge`; `s 110.2(4) the duty of the provincial court judge to place the documents in a packet and seal it` |
| s 110.2(5) | 2367-2368 | subsection | encoded | `s 110.2(5) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` |
| s 110.3(1) | 2369-2370 | subsection | fork (F-110.3(1)) | `s 110.3(1) a provincial court judge may make an order to delete identifying information`; `s 110.3(1) direction` |
| s 110.3(1)(a) | 2371 | paragraph | encoded | `s 110.3(1) what the order directs` |
| s 110.3(1)(b) | 2372 | paragraph | encoded | `s 110.3(1) what the order directs` |
| s 110.3(1)(c) | 2373 | paragraph | encoded | `s 110.3(1) what the order directs` |
| s 110.3(2) | 2374-2375 | subsection | encoded | `s 110.3(2) the order may be for the period, whether definite or indefinite` |
| s 110.3(3) | 2376-2377 | subsection | fork (F-immediately) | `s 110.3(3) the originals must be placed in a packet and sealed by the judge`; `s 110.3(3) the duty of the provincial court judge to place the originals in a packet and seal it` |
| s 110.3(4) | 2378-2379 | subsection | encoded | `s 110.3(4) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` |
| s 110.3(5) | 2380-2381 | subsection | encoded | `s 110.3(5) the order made under this section applies in respect of that hearing` |

Counts per disposition (334 rows): encoded 277; fork 49; inert 1 (reason 1: 1; reasons 2 and 3: 0); repealed or blank in this text 7.

## Fork register (ccc4)

Every ambiguity found in lines 1904-2381, the readings seen, the one taken, and the text that licenses each.
The ids are the ones the `.l4` comments cite (`fork F2`, `fork F-OF`, ...); a unit whose disposition is `fork` in the coverage table names its ids.
Quotations are copied from the raw text by line number (`work/notes_forks.py`); the rulings are copied from `BRIEF.md` by line number.

### The rulings these forks rest on, word for word

The rule of 2026-10-29 and its two readings left for a lawyer are in the brief (lines 56-64), and are restated in "Reading a result: FALSE and NOTHING (ccc4)" below.
The rulings below carry the `NOTHING-kind` tags of this part; each is recorded here word for word, as `BRIEF.md` line 111 requires.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

The ruling of 2026-11-12 on a function named for a grant or a power is in `BRIEF.md` line 24; the three limits it sets are applied in "Name-test sweep of 2026-11-12".

### Forks taken

- **F-OF** -- the 31 offence subsections (ss 85(1), 85(2), 86(1), 86(2), 87(1), 88(1), 89(1), 90(1), 91(1), 91(2), 92(1), 92(2), 93(1), 94(1), 95(1), 96(1), 98(1), 98.1, 99(1), 100(1), 101(1), 102(1), 102.1(1), 102.1(2), 103(1), 104(1), 104.1(1), 105(1), 106(1), 107(1), 108(1)).
  Rule: each `s N(k) the person commits an offence ...`.
  Readings seen: A: "Every person commits an offence who ..." defines the offence by its elements, so an unmet bare element answers JUST FALSE (the section says in its own words who commits the offence); B: the section prohibits what it names and says nothing of anything else, so an unmet element answers NOTHING.
  Taken: A, with this limit: a case inside a limb the text writes with "without lawful excuse", "without being the holder of" or "otherwise than under the authority of" answers NOTHING (a prohibition limited by its own wording: reading (b)); "do not apply to", "unless" and "No person is guilty" answer JUST FALSE.
  Licensing text: e.g. "85 (1) Every person commits an offence who uses a firearm, whether or not the person causes or means to cause bodily harm to any person as a result of using the firearm," (line 2010)

- **F2** -- s 84(1) "imitation firearm".
  Rule: `s 84(1) imitation firearm`.
  Readings seen: A: "means ... and includes a replica firearm" is closed by "means", so a thing that neither imitates a firearm nor is a replica firearm answers JUST FALSE; B: "includes" leaves the list open, so it answers NOTHING.
  Taken: A, as the keel reads "means ... and includes" in its own definitions.
  Licensing text: "imitation firearm means any thing that imitates a firearm, and includes a replica firearm; (fausse arme à feu)" (line 1923)

- **F-Nunavut** -- s 84(1) "superior court"(d).
  Rule: `s 84(1) superior court` over `Province or territory`.
  Readings seen: A: "a territory, the Supreme Court" names the Supreme Court for Nunavut too; B: s 2 "superior court of criminal jurisdiction" (f) names the Nunavut Court of Justice, so Nunavut belongs elsewhere.
  Taken: A, as this text has it.
  Licensing text: "(d) in Nova Scotia, British Columbia, Prince Edward Island, Newfoundland and Labrador and a territory, the Supreme Court; (cour supérieure)" (line 1971)

- **F-ten-years** -- s 84(5), the sentence "However, an earlier offence shall not be taken into account if 10 years have elapsed".
  Rule: `s 84(5) the earlier offence is to be considered as an earlier offence`.
  Readings seen: A: ten years have elapsed on the tenth anniversary itself (the later conviction is on or after the earlier conviction plus ten years plus the days in custody); B: only after the tenth anniversary.
  Taken: A.
  Licensing text: "However, an earlier offence shall not be taken into account if 10 years have elapsed between the day on which the person was convicted of the earlier offence and the day on which the person was convicted of the offence for which sentence is being imposed, not taking into account any time in custody." (line 2004)

- **F-hybrid** -- s 109(1)(a).
  Rule: `s 109(1) the offence is an indictable offence`.
  Readings seen: A: an offence that the section makes both indictable and punishable on summary conviction is an indictable offence when the proceeding is by indictment, and NOTHING otherwise; B: it is always an indictable offence until the proceeding is chosen; C: never, because the text calls it neither.
  Taken: A. The words "hybrid" and "dual procedure" occur nowhere in the text.
  Licensing text: "(a) an indictable offence in the commission of which violence against a person was used, threatened or attempted and for which the person may be sentenced to imprisonment for ten years or more," (line 2288)

- **F-109-ammo** -- s 109(2)(a) and (b).
  Rule: `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge`.
  Readings seen: A: prohibited ammunition is ammunition (s 84(1)), so it is named in both (a) (ends not earlier than ten years after) and (b) (for life), and the order forbids it for life, which satisfies the floor of (a); B: (a) governs and the period is ten years.
  Taken: A.
  Licensing text: "(2) An order made under subsection (1) shall, in the case of a first conviction for or discharge from the offence to which the order relates, prohibit the ..." (line 2299) and "(b) any prohibited firearm, restricted firearm, prohibited weapon, prohibited device and prohibited ammunition for life." (line 2303)

- **F-110.1(3)** -- s 110.1(3), "the judge shall make an order".
  Rule: `s 110.1(3) the provincial court judge must make an emergency prohibition order`.
  Readings seen: A: a failed "if" in a duty counts as the text's no (reading (a)), so the answer is JUST FALSE; B: NOTHING, because "if A then B" does not itself say "if not A then not B".
  Taken: A. It is a duty, not a power, so the ruling of 2026-11-12 does not reach it (limit 2 of the three).
  Licensing text: "(3) If, at the conclusion of a hearing of an application made under subsection (1), the provincial court judge is satisfied that the circumstances referred to in that subsection exist and that an order should be made without delay to ..." (line 2333)

- **F-30-days** -- s 110.1(3), "for a period not exceeding 30 days".
  Rule: `s 110.1(3) the period specified in the order is within the limit of thirty days`.
  Readings seen: A: a period the text states: outside it the answer is JUST FALSE (ruling (a) of 2026-11-05); B: NOTHING, a stated period being among the limits of a grant (rule of 2026-10-29).
  Taken: A.
  Licensing text: "... ibited device, firearm part, ammunition, prohibited ammunition or explosive substance, or all such things, for a period not exceeding 30 days, as is specified in the order, beginning on the day on which the order is made." (line 2333)

- **F-immediately** -- ss 110.1(7), 110.2(4) and 110.3(3), "immediately".
  Rule: the regulative rules `s 110.1(7) the duty of the peace officer to make a report to a justice`, `s 110.2(4) the duty of the provincial court judge to place the documents in a packet and seal it`, `s 110.3(3) the duty of the provincial court judge to place the originals in a packet and seal it` (their actions are `s 110.1 make a report to a justice`, `s 110.2 place the documents in a packet and seal it`, `s 110.3 place the originals in a packet and seal it`).
  Readings seen: A: the text gives no number, so the rule has no WITHIN; B: "immediately" is WITHIN 0 days.
  Taken: A. A deadline the text does not state is not invented; a trace that does not contain the act leaves the duty standing.
  Licensing text: "(7) A peace officer who executes a warrant referred to in subsection (5) or who conducts a search without a warrant under subsection (6) shall immediately make a report to a justice having ..." (line 2341)

- **F-despatch** -- ss 105(1) and 106(1), "with reasonable despatch".
  Rule: the regulative rules `s 105(1)(a) the duty to report a loss`, `s 105(1)(b) the duty to deliver or report a find`, `s 106(1) the duty to report a destruction` (their actions begin `s 105 report the loss ...`, `s 105 deliver the found thing ...`, `s 106 report the destruction ...`).
  Readings seen: A: the text fixes no period, so the rule has no WITHIN; B: a WITHIN of some number of days, which the text does not give.
  Taken: A.
  Licensing text: "... n, an authorization, a licence or a registration certificate, or having had it stolen from the person’s possession, does not with reasonable despatch report the loss to a peace officer, to a firearms officer or a chief firearms officer; or" (line 2249) and "does not with reasonable despatch report the destruction to a peace officer, firearms officer or chief firearms officer." (line 2259)

- **F-110(2.1)** -- s 110(2.1), "may be imposed for life or for any shorter duration if, in the commission of the offence, violence was used".
  Rule: `s 110(2.1) the order may be imposed for life or for any shorter duration`.
  Readings seen: A: a function named for a power, with an "if" gate that fails, answers NOTHING (ruling of 2026-11-12, "limits a grant ... in its own wording"); B: JUST FALSE, a failed "if" read as the text's own no (reading (a)).
  Taken: A.
  Licensing text: "(2.1) Despite subsection (2), an order made under subsection (1) may be imposed for life or for any shorter duration if, in the commission of the offence, violence was used, threatened or attempted ..." (line 2318)

- **F-110.1(1)** -- s 110.1(1), "Any person may make an ex parte application ... if the person believes on reasonable grounds".
  Rule: `s 110.1(1) any person may make an ex parte application to a provincial court judge for an order`.
  Readings seen: A: NOTHING when the "if" gate fails (ruling of 2026-11-12); B: JUST FALSE (reading (a)).
  Taken: A.
  Licensing text: "110.1 (1) Any person may make an ex parte application to a provincial court judge for an order prohibiting another person from possessing any firearm, cross-bow, prohibited weapon, restricted weapon, prohibited device, firearm part, ammunition, prohibited ..." (line 2329)

- **F-110.1(2)** -- s 110.1(2), "may hold the hearing ... in private if the judge considers that it is necessary".
  Rule: `s 110.1(2) the provincial court judge may hold the hearing in private`.
  Readings seen: A: NOTHING when the "if" gate fails; B: JUST FALSE.
  Taken: A.
  Licensing text: "(2) The provincial court judge may hold the hearing of an application made under subsection (1) in private if the judge considers that it is necessary to protect the security of the applicant or of anyone known to the applicant." (line 2331)

- **F-110.1(5)** -- s 110.1(5), "If a provincial court judge is satisfied by information on oath ... the judge may issue a warrant".
  Rule: `s 110.1(5) the provincial court judge may issue a warrant to search and seize`.
  Readings seen: A: NOTHING when the "if" gate fails; B: JUST FALSE.
  Taken: A.
  Licensing text: "(5) If a provincial court judge is satisfied by information on oath that there are reasonable grounds to believe that a person who is subject to an order made under subsection (3) possesses, in a building, receptacle or place, any thing ..." (line 2337)

- **F-110.1(6)** -- s 110.1(6), "If ... a peace officer is satisfied ... the peace officer may -- if the grounds for obtaining a warrant ... exist but ... it would not be practicable to obtain a warrant -- search for and seize".
  Rule: `s 110.1(6) the peace officer may search for and seize without a warrant`.
  Readings seen: A: NOTHING when an "if" gate fails; B: JUST FALSE.
  Taken: A.
  Licensing text: "(6) If, in respect of a person who is subject to an order made under subsection (3), a peace officer is satisfied that there are reasonable grounds to believe that it is not desirable, in the interests of the safety of the person, or of ..." (line 2339)

- **F-110.2(1)** -- s 110.2(1), "If an order is made under subsection 110.1(3), a provincial court judge may, on application by the person who applied for the order or on the judge's own motion, if the judge considers that it is necessary".
  Rule: `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information`.
  Readings seen: A: the two "if" gates answer NOTHING when they fail (ruling of 2026-11-12), and the "on application ... or on the judge's own motion" gate, of the kind of "when" and "upon", answers JUST FALSE when it alone fails (rulings (b) and (c) of 2026-11-05); the gates are read in the text's order and the first that fails decides; B: all three answer NOTHING (a power limited by its own wording); C: all three answer JUST FALSE.
  Taken: A. That an "on application" gate goes with the listed group is assumed, not ruled.
  Licensing text: "110.2 (1) If an order is made under subsection 110.1(3), a provincial court judge may, on application by the person who applied for the order or on the judge’s own motion, if the judge considers that it is necessary to protect the security of the person or of anyone known to the person, make an ..." (line 2354)

- **F-110.3(1)** -- s 110.3(1), the same three gates as s 110.2(1).
  Rule: `s 110.3(1) a provincial court judge may make an order to delete identifying information`.
  Readings seen: As for F-110.2(1).
  Taken: A, as for F-110.2(1).
  Licensing text: "110.3 (1) If an order is made under subsection 110.1(3) or 110.2(1), a provincial court judge may, on application by the person who applied for the order referred to in subsection 110.1(3) or on the judge’s own motion, if the judge considers that it is necessary to protect the security of the ..." (line 2370)

- **F-3.01** -- ss 109(1)(a), 110(1)(a), 110(2.1), through s 3.01(1) "includes a reference to any of the following offences".
  Rule: `s 3.01(1) the offence counts as an offence in the commission of which violence is used, threatened or attempted against any person or class of persons` (the keel's), called by `s 109(1)(a) ...`, `s 110(1) the court must consider whether it is desirable to make a prohibition order`, `s 110(2.1) ...`.
  Readings seen: A: "includes" leaves open what else counts, so a person with no violence in fact whose offence is none of those s 3.01(1) lists gets NOTHING on limb (a); B: the list only adds to the plain meaning ("violence ... was used"), so with no violence in fact and none of the listed offences the limb is JUST FALSE.
  Taken: A, as the keel's `s 3.01(1)` answers NOTHING outside its list. This is the commonest case: an ordinary offence with no violence and no weapon answers NOTHING on "must the court consider ...", not "no". See finding 13.
  Licensing text: "3.01 (1) In a provision listed in subsection (2), a reference to an offence in the commission of which violence is used, threatened or attempted against any person or class of persons includes a reference to any of the following offences:" (line 258)

- **F-weapon** -- ss 88(1), 89(1), 90(1) and the seat questions that ask whether a thing is a "weapon", through s 2 "weapon".
  Rule: `s 2 weapon` (the keel's), taken as an input in layer 1 and called by the seat.
  Readings seen: A (the keel's): "without restricting the generality of the foregoing, includes a firearm" leaves the definition open, so a thing that neither injures nor threatens nor is a firearm answers NOTHING; B: "means any thing used, designed to be used or intended for use (a) ... or (b) ..." is closed by "means", so it answers JUST FALSE (the reading taken for F2).
  Taken: A, in the seat only: layer 2 calls the keel's `s 2 weapon` and does not restate it; layer 1 takes the answer of s 2 "weapon" as a plain input. See finding 12.
  Licensing text: "weapon means any thing used, designed to be used or intended for use" (line 220) ... "and, without restricting the generality of the foregoing, includes a firearm and, for the purposes of sections 88, 267 and 272, any thing used, designed to be used or intended for use in binding or ..." (line 223)

### Listed under the name-test sweep of 2026-11-12 (assumed, not ruled; for a lawyer or the maintainer)

Limit 3 of the ruling of 2026-11-12 says not to decide two groups by sweep, and to list them with a count.
- **"may" functions whose gate is "where", "when" or "upon" (count: 2).**
  `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information` and `s 110.3(1) a provincial court judge may make an order to delete identifying information`: each has an "on application ... or on the judge's own motion" gate (the kind of "on such an application") together with two "if" gates; they are the whole of this group, and are forked as F-110.2(1) and F-110.3(1).
  The guide's rulings (b) and (c) of 2026-11-05 say JUST FALSE when that gate fails and the line on grants points to NOTHING; these two functions answer JUST FALSE when that gate alone fails and NOTHING when an "if" gate fails first, and a lawyer should say whether a grant's "on application" gate is a bar or a limit.
  That these equivalents go with the listed group is assumed, not ruled.
- **"entitled"-named functions (count: 0).** No function or type of this part has "entitled" in its name; the text uses the word once, in s 110.1(7)(b): "the peace officer was entitled to conduct the search" (line 2343), which is a ground to be reported, not a claim encoded here.

## Jural relations (ccc4)

One row per provision that creates a relation (Hohfeld: claim and duty, privilege and no-right, power and liability, immunity and disability); the row names the party that holds the right, privilege, power or immunity, the party that bears the correlative duty, no-right, liability or disability, and the L4 rule.
A rule is stated once in layer 1, as a relation between two parties, never once from each side.
The text names the bearer of nearly every duty here (the court, the judge, the peace officer) and the holder of almost none; where it names no holder the row says "not named in the text", and only an offence is given the Crown as holder and a punishment the convicting court as holder of the power to impose it, which is implied and not stated.

| section | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 85(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 85(1) the person commits an offence by using a firearm in the commission of an offence` |
| s 85(2) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 85(2) the person commits an offence by using an imitation firearm in the commission of an offence` |
| s 86(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 86(1) the person commits an offence of careless use of a firearm, etc.` |
| s 86(2) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 86(2) the person commits an offence by contravening a storage regulation, etc.` |
| s 87(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 87(1) the person commits the offence of pointing a firearm` |
| s 88(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 88(1) the person commits an offence of possession of a weapon for a dangerous purpose` |
| s 89(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 89(1) the person commits an offence of carrying a weapon while attending a public meeting` |
| s 90(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 90(1) the person commits an offence of carrying a concealed weapon` |
| s 91(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 91(1) the person commits an offence of unauthorized possession of a firearm` |
| s 91(2) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 91(2) the person commits an offence of unauthorized possession of a prohibited weapon or restricted weapon` |
| s 92(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 92(1) the person commits an offence of possession of a firearm knowing its possession is unauthorized` |
| s 92(2) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 92(2) the person commits an offence of possession of a prohibited weapon, device or ammunition knowing its possession is unauthorized` |
| s 93(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 93(1) the person commits an offence of possession at an unauthorized place` |
| s 94(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 94(1) the person commits an offence of unauthorized possession in a motor vehicle` |
| s 95(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 95(1) the person commits an offence of possession of a prohibited or restricted firearm with ammunition` |
| s 96(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 96(1) the person commits an offence of possession of a weapon obtained by the commission of an offence` |
| s 98(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 98(1) the person commits an offence of breaking and entering to steal a firearm` |
| s 98.1 | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 98.1 the person commits an offence of robbery to steal a firearm` |
| s 99(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 99(1) the person commits an offence of weapons trafficking` |
| s 100(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 100(1) the person commits an offence of possession for the purpose of weapons trafficking` |
| s 101(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 101(1) the person commits an offence of transfer without authority` |
| s 102(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 102(1) the person commits an offence of making an automatic firearm` |
| s 102.1(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 102.1(1) the person commits an offence of possession of computer data` |
| s 102.1(2) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 102.1(2) the person commits an offence of distribution of computer data` |
| s 103(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 103(1) the person commits an offence of importing or exporting knowing it is unauthorized` |
| s 104(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 104(1) the person commits an offence of unauthorized importing or exporting` |
| s 104.1(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 104.1(1) the person commits an offence of altering a cartridge magazine` |
| s 107(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 107(1) the person commits an offence by making a false report or statement` |
| s 108(1) | the Crown (the state, on behalf of the public) | the person (the accused) | claim / duty (the duty not to do what the section names) | `s 108(1) the person commits an offence of tampering with a serial number` |
| s 105(1) | the Crown (the state, on behalf of the public), through the peace officer, firearms officer or chief firearms officer who must be told | the person (the accused), who lost, found or destroyed the thing | claim / duty (the duty to report or deliver) | `s 105(1)(a) the person commits an offence by not reporting a loss`; `s 105(1)(b) the person commits an offence by not delivering or reporting a find` |
| s 106(1) | the Crown (the state, on behalf of the public), through the peace officer, firearms officer or chief firearms officer who must be told | the person (the accused), who lost, found or destroyed the thing | claim / duty (the duty to report or deliver) | `s 106(1) the person commits an offence by not reporting a destruction` |
| s 85(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 85(3) the punishment on indictment` |
| s 86(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 86(3)(a) the punishment on indictment` |
| s 87(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 87(2)(a) the punishment on indictment` |
| s 88(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 88(2)(a) the punishment on indictment` |
| s 89(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 89(2) the punishment on summary conviction` |
| s 90(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 90(2)(a) the punishment on indictment` |
| s 91(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 91(3)(a) the punishment on indictment` |
| s 92(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 92(3) the punishment on indictment` |
| s 93(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 93(2)(a) the punishment on indictment` |
| s 94(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 94(2)(a) the punishment on indictment` |
| s 95(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 95(2)(a) the punishment on indictment` |
| s 96(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 96(2)(a) the punishment on indictment` |
| s 98(4) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 98(4) the punishment on indictment` |
| s 99(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 99(2) the punishment when the object in question is a firearm, device, part or ammunition` |
| s 99(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 99(3) the punishment in any other case` |
| s 100(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 100(2) the punishment when the object in question is a firearm, device, part or ammunition` |
| s 100(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 100(3) the punishment in any other case` |
| s 101(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 101(2)(a) the punishment on indictment` |
| s 102(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 102(2)(a) the punishment on indictment` |
| s 102.1(3) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 102.1(3)(a) the punishment on indictment` |
| s 103(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 103(2) the punishment when the object in question is a firearm, device, part or prohibited ammunition` |
| s 103(2.1) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 103(2.1) the punishment in any other case` |
| s 104(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 104(2)(a) the punishment on indictment` |
| s 104.1(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 104.1(2)(a) the punishment on indictment` |
| s 105(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 105(2)(a) the punishment on indictment` |
| s 106(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 106(2)(a) the punishment on indictment` |
| s 107(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 107(2)(a) the punishment on indictment` |
| s 108(2) | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 108(2)(a) the punishment on indictment` |
| s 98.1 | the court that convicts the person | the person (the accused), once convicted | power / liability (the power to impose the stated punishment) | `s 98.1 the punishment on indictment` |
| s 85(4) | the Crown (the state, on behalf of the public) | the person (the accused), sentenced under s 85(1) or (2) | claim / duty (the sentence is served consecutively to any other punishment from the same event or any sentence the person is then subject to) | `s 85(4) the sentence must be served consecutively to the other punishment or sentence` |
| s 91(4) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 91(1) and (2)) | `s 91(4) subsections (1) and (2) do not apply to the person` |
| s 92(4) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 92(1) and (2)) | `s 92(4) subsections (1) and (2) do not apply to the person` |
| s 93(3) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 93(1)) | `s 93(3) subsection (1) does not apply to a person who possesses a replica firearm` |
| s 94(3) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 94(1)) | `s 94(3) subsection (1) does not apply to an occupant who attempted to leave or left the motor vehicle` |
| s 94(4) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 94(1)) | `s 94(4) subsection (1) does not apply when an occupant came into possession by the operation of law` |
| s 95(3) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 95(1)) | `s 95(3) subsection (1) does not apply to the person` |
| s 96(3) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 96(1)) | `s 96(3) subsection (1) does not apply to the person` |
| s 108(3) | the person (the accused), within the exception | the Crown (the state, on behalf of the public) | immunity / disability (the Crown cannot treat the person as guilty under s 108(1)(b)) | `s 108(3) no person is guilty of an offence under paragraph (1)(b) by reason only of possessing the firearm` |
| s 108(4) | the Crown (the state, on behalf of the public) | the person (the accused), who possesses a firearm with an obliterated serial number | power / liability (the evidence is proof of knowledge in the absence of evidence to the contrary) | `s 108(4) the evidence is proof that the person possesses the firearm knowing that the serial number on it has been altered, defaced or removed` |
| s 109(1) | not named in the text | the court that sentences the person or discharges them | duty (the duty to make a prohibition order) (the person is under the correlative liability to the order) | `s 109(1) the court must make a prohibition order` |
| s 109(1) | the court | the person (the accused) | power / liability (the order binds the person for the period of s 109(2) or (3)) | `s 109(2) and (3) the period for which the order prohibits the thing` |
| s 109(2) | not named in the text | the court that makes the order | duty (to prohibit the things of paragraph (a) for a period ending not earlier than ten years after the person's release or conviction, and those of paragraph (b) for life); the person is under the correlative liability | `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` |
| s 109(3) | not named in the text | the court that makes the order | duty (to prohibit the things the subsection lists for life); the person is under the correlative liability | `s 109(3) the period for which the order prohibits the thing, in any other case` |
| s 110(1) | not named in the text | the court that sentences the person or discharges them | duty (the duty to consider whether an order is desirable, and to make it if it so decides) | `s 110(1) the court must consider whether it is desirable to make a prohibition order`; `s 110(1) the court must make a prohibition order` |
| s 110(2.1) | the court | the person (the accused) | power / liability (the power to impose the order for life or any shorter duration, where violence was used against the persons named) | `s 110(2.1) the order may be imposed for life or for any shorter duration` |
| s 110(3) | not named in the text | the court | duty (the duty to put reasons for not making an order, or for not forbidding everything, in the record) | `s 110(3) the court must include in the record a statement of its reasons` |
| s 110.1(1) | any person who believes on reasonable grounds | the person (the accused) (the person against whom the order is sought) | power / liability (the power to apply ex parte to a provincial court judge) | `s 110.1(1) any person may make an ex parte application to a provincial court judge for an order` |
| s 110.1(2) | the provincial court judge | the applicant and the public | power / liability (the power to hold the hearing in private) | `s 110.1(2) the provincial court judge may hold the hearing in private` |
| s 110.1(3) | not named in the text | the provincial court judge | duty (the duty to make an emergency order of not more than 30 days) (the person against whom the order is sought is under the correlative liability) | `s 110.1(3) the provincial court judge must make an emergency prohibition order` |
| s 110.1(4) | the person to whom the order is addressed | the party that the judge directs or the rules of court name (the text does not name who serves) | claim / duty (the duty to serve a copy of the order) | `s 110.1(4) a copy of the order must be served on the person to whom it is addressed` |
| s 110.1(5) | the provincial court judge | the person (the accused) (the person subject to the order) | power / liability (the power to issue a warrant to search and seize) | `s 110.1(5) the provincial court judge may issue a warrant to search and seize` |
| s 110.1(6) | the peace officer | the person (the accused) (the person subject to the order) | power / liability (the power to search and seize without a warrant) | `s 110.1(6) the peace officer may search for and seize without a warrant` |
| s 110.1(7) | a justice having jurisdiction in respect of the matter (the report is made to the justice) | the peace officer who executes a warrant or searches without one | duty (the duty to report) | `s 110.1(7) the peace officer must make a report to a justice` |
| s 110.1(8) | the person (the accused) (the person against whom the order was made) | the party holding the things seized or surrendered (the text does not name a party) | claim / duty (the duty to return the things and documents) | `s 110.1(8) the occasion on which the things and documents must be returned to the person` |
| s 110.2(1) | the provincial court judge | the public and anyone who would seek access to the information | power / liability (the power to prohibit access to, and disclosure of, information) | `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information` |
| s 110.2(4) | not named in the text | the provincial court judge | duty (the duty to place the documents in a packet and seal it) | `s 110.2(4) the documents must be placed in a packet and sealed by the judge` |
| s 110.2(5) | a person applying to revoke or vary the order (the text does not say who may apply) | the provincial court judge who made the order or another one | privilege / no-right (the application may be made to either judge) | `s 110.2(5) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` |
| s 110.3(1) | the provincial court judge | the public and any person served with the documents | power / liability (the power to order that identifying information be deleted from copies) | `s 110.3(1) a provincial court judge may make an order to delete identifying information` |
| s 110.3(2) | the provincial court judge | the same persons | power / liability (the power to fix any period, definite or indefinite, that the judge considers necessary) | `s 110.3(2) the order may be for the period, whether definite or indefinite` |
| s 110.3(3) | not named in the text | the provincial court judge | duty (the duty to seal the originals in a packet) | `s 110.3(3) the originals must be placed in a packet and sealed by the judge` |
| s 110.3(4) | a person applying to revoke or vary the order (the text does not say who may apply) | the provincial court judge who made the order or another one | privilege / no-right (the application may be made to either judge) | `s 110.3(4) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` |
| s 84(1), 84(2), 84(3), 84(3.1), 84(4), 84(5), 84(6) | none | none | none: the definitions of s 84(1) (the defined terms and their paragraphs), the barrel length of s 84(2), the deeming of s 84(3), the holders of s 84(4), and the counting rules of s 84(5) and (6) create no relation of their own | `s 84(1) the thing is within the meaning the term has in subsection 84(1)`, `s 84(2) the length of the barrel of a firearm in millimetres`, `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision`, `s 84(3.1) the antique firearm is a firearm for the purpose`, `s 84(4)(a) the person is the holder of an authorization or a licence`, `s 84(5) the earlier offence is to be considered as an earlier offence` |
| s 98(2), 98(3), 102.1(4), 107(3), 109(4), 109(5), 110(2), 110(4), 110(5), 110.1(9), 110.1(10), 110.2(2), 110.2(3), 110.3(5) | none | none | none: a definition, a deeming rule, a period, or an application clause; each is a function that other rules call | `s 98(2) place`, `s 98(3)(a) the person enters`, `s 98(3)(b) the person is deemed to have broken and entered`, `s 102.1(4) computer data`, `s 107(3) report or statement`, `s 109(4) release from imprisonment`, `s 109(5) the section applies in respect of every order made under subsection (1)`, `s 110(2) the latest day on which the order may end`, `s 110.1(9) the section applies in respect of every order made under subsection (3)`, `s 110.1(10) provincial court judge`, `s 110.2(2) and (3) the day on which an order made under subsection (1) ends`, `s 110.3(5) the order made under this section applies in respect of that hearing` |

| s 91(5), 92(5), 94(5), 97, 103(3), 104(3) | none | none | none: repealed or blank in this text | (no rule: the text shows "[Repealed ...]") |

## Marginal readings for a lawyer (ccc4)

Two readings are left for a lawyer (brief, line 63), and this part takes the status quo on both:
- **(a)** a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no;
- **(b)** a prohibition or grant limited by its own wording does not.
The table lists every branch of layer 1 that rests on one of them, one row per function, with the other reading.
Reconciliation of every JUST FALSE branch of the four layer-1 modules (113 in all): 36 rest on (a) and are in the table; the others are not, for these reasons: a closed definition or an offence section (forks F2, F-OF) 66; a closed list of provisions the text names 3; passes an answer on ("propagates") 3; an "on application" gate (forks F-110.2(1), F-110.3(1)) 2; a definition delegated to s 342.1(2) (the other part answers) 2; a stated period (fork F-30-days) 1.
A branch counts as (a) when it is a failed "where", "if", "who" or "as soon as" gate of a duty or rule, an exclusion ("does not include", "no consideration shall be given to"), or a flat negative; the branches that are not are listed by reason above, and their forks are in the fork register.
NOTHING branches resting on (b): 54, in 52 functions; JUST FALSE branches resting on (a): 36, in 31 functions.

| function | file:line | answer | reading | text relied on | the other reading |
| --- | --- | --- | --- | --- | --- |
| `s 109(1) the offence is an indictable offence` | s109-110-3-prohibition-orders:32 | JUST FALSE | (a) | "an indictable offence in the commission of which violence against a person was used" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 109(1)(a) the maximum imprisonment is ten years or more` | s109-110-3-prohibition-orders:54 | JUST FALSE | (a) | "for which the person may be sentenced to imprisonment for ten years or more" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 109(1)(d) the offence involves a thing the person was prohibited from possessing` | s109-110-3-prohibition-orders:184 | JUST FALSE | (a) | "an offence that involves, or the subject-matter of which is, a firearm" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 109(1) the court must make a prohibition order` | s109-110-3-prohibition-orders:240, s109-110-3-prohibition-orders:243 | JUST FALSE | (a) | "Where a person is convicted, or discharged under section 730, of" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 109(2) the period for which the order prohibits the thing, in the case of a first conviction or discharge` | s109-110-3-prohibition-orders:305 | NOTHING | (b) | "in the case of a first conviction for or discharge from the offence to which the order relates" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 109(3) the period for which the order prohibits the thing, in any other case` | s109-110-3-prohibition-orders:341 | NOTHING | (b) | "in any case other than a case described in subsection (2)" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 109(5) the section applies in respect of every order made under subsection (1)` | s109-110-3-prohibition-orders:402 | NOTHING | (b) | "Sections 113 to 117 apply in respect of every order made under subsection (1)" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110(1) the court must consider whether it is desirable to make a prohibition order` | s109-110-3-prohibition-orders:424, s109-110-3-prohibition-orders:428 | JUST FALSE | (a) | "Where a person is convicted, or discharged under section 730, of" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110(1) the court must make a prohibition order` | s109-110-3-prohibition-orders:461 | JUST FALSE | (a) | "if the court decides that it is so desirable, the court shall so order" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110(2.1) the order may be imposed for life or for any shorter duration` | s109-110-3-prohibition-orders:517 | NOTHING | (b) | "may be imposed for life or for any shorter duration if, in the commission of the offence, violence was used, t ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110(3) the court must include in the record a statement of its reasons` | s109-110-3-prohibition-orders:550 | JUST FALSE | (a) | "Where the court does not make an order under subsection (1), or where the court does make such an order but do ..." | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110(5) the section applies in respect of every order made under subsection (1)` | s109-110-3-prohibition-orders:588 | NOTHING | (b) | "Sections 113 to 117 apply in respect of every order made under subsection (1)" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.1(1) any person may make an ex parte application to a provincial court judge for an order` | s109-110-3-prohibition-orders:601 | NOTHING | (b) | "if the person believes on reasonable grounds that it is not desirable in the interests of the safety" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.1(2) the provincial court judge may hold the hearing in private` | s109-110-3-prohibition-orders:612 | NOTHING | (b) | "if the judge considers that it is necessary to protect the security of the applicant" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.1(3) the provincial court judge must make an emergency prohibition order` | s109-110-3-prohibition-orders:625 | JUST FALSE | (a) | "If, at the conclusion of a hearing of an application made under subsection (1), the provincial court judge is  ..." | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110.1(5) the provincial court judge may issue a warrant to search and seize` | s109-110-3-prohibition-orders:675 | NOTHING | (b) | "If a provincial court judge is satisfied by information on oath that there are reasonable grounds to believe" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.1(6) the peace officer may search for and seize without a warrant` | s109-110-3-prohibition-orders:692 | NOTHING | (b) | "if the grounds for obtaining a warrant under subsection (5) exist but, by reason of a possible danger to the s ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.1(7) the peace officer must make a report to a justice` | s109-110-3-prohibition-orders:705 | JUST FALSE | (a) | "A peace officer who executes a warrant referred to in subsection (5) or who conducts a search without a warran ..." | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110.1(9) the section applies in respect of every order made under subsection (3)` | s109-110-3-prohibition-orders:773 | NOTHING | (b) | "Sections 113, 114 and 116 apply in respect of every order made under subsection (3)" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.1(10) provincial court judge` | s109-110-3-prohibition-orders:784 | NOTHING | (b) | "In this section and sections 110.4, 111, 112, 117.0101, 117.0104, 117.011 and 117.012" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information` | s109-110-3-prohibition-orders:810, s109-110-3-prohibition-orders:812 | NOTHING | (b) | "If an order is made under subsection 110.1(3), a provincial court judge may"; "if the judge considers that it is necessary to protect the security of the person or of anyone known to the pe ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.2(2) the day on which the order made under subsection (1) expires` | s109-110-3-prohibition-orders:844 | NOTHING | (b) | "Unless an order made under subsection (1) is revoked earlier" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.2(3) the day on which an order made under subsection (1) ceases to have effect` | s109-110-3-prohibition-orders:860 | NOTHING | (b) | "if, before the order made under subsection 110.1(3) expires or is revoked, a date is fixed under subsection 11 ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.2(4) the documents must be placed in a packet and sealed by the judge` | s109-110-3-prohibition-orders:893 | JUST FALSE | (a) | "If an order is made under subsection (1), all documents relating to" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110.2(5) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` | s109-110-3-prohibition-orders:915 | NOTHING | (b) | "may be made to the provincial court judge who made the order or to another provincial court judge" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.3(1) a provincial court judge may make an order to delete identifying information` | s109-110-3-prohibition-orders:929, s109-110-3-prohibition-orders:931 | NOTHING | (b) | "If an order is made under subsection 110.1(3) or 110.2(1), a provincial court judge may"; "if the judge considers that it is necessary to protect the security of the person or of anyone known to the pe ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.3(2) the order may be for the period, whether definite or indefinite` | s109-110-3-prohibition-orders:960 | NOTHING | (b) | "any period — definite or indefinite — that the provincial court judge considers necessary" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.3(3) the originals must be placed in a packet and sealed by the judge` | s109-110-3-prohibition-orders:971 | JUST FALSE | (a) | "If an order is made under subsection (1), the originals of all documents" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 110.3(4) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` | s109-110-3-prohibition-orders:993 | NOTHING | (b) | "may be made to the provincial court judge who made the order or to another provincial court judge" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 110.3(5) the order made under this section applies in respect of that hearing` | s109-110-3-prohibition-orders:1006 | NOTHING | (b) | "if a date is fixed under subsection 110.4(1) for the hearing of an application made under subsection 111(1), a ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 84(1) firearm part` | s84-definitions:175 | JUST FALSE | (a) | "but does not include, unless otherwise prescribed, a barrel for a firearm or a slide for a handgun" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 84(1) replica firearm` | s84-definitions:415 | JUST FALSE | (a) | "but does not include any such device that is designed or intended to exactly resemble, or to resemble with nea ..." | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 84(1) semi-automatic` | s84-definitions:478 | NOTHING | (b) | "in respect of a firearm" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 84(3) the weapon is deemed not to be a firearm for the purposes of the provision` | s84-definitions:797 | NOTHING | (b) | "For the purposes of sections 91 to 95, 99 to 101, 103 to 107 and 117.03 of this Act and the provisions of the  ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 84(3.1) the antique firearm is a firearm for the purpose` | s84-definitions:833 | NOTHING | (b) | "an antique firearm is a firearm for the purposes of regulations made under paragraph 117(h) of the Firearms Ac ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 84(4)(a) the person is the holder of an authorization or a licence` | s84-definitions:848 | JUST FALSE | (a) | "if the authorization or licence has been issued to the person and the person continues to hold it" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 84(4)(b) the person is the holder of a registration certificate for a firearm` | s84-definitions:862 | JUST FALSE | (a) | "a registration certificate for a firearm if" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 84(5) the earlier offence is to be considered as an earlier offence` | s84-definitions:882 | NOTHING | (b) | "for the purpose of subsection 99(2), 100(2) or 103(2)" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 84(5) the earlier offence is to be considered as an earlier offence` | s84-definitions:883, s84-definitions:884 | JUST FALSE | (a) | "if the person was earlier convicted of any of the following offences"; "an earlier offence shall not be taken into account if 10 years have elapsed" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 84(6) offence one is the earlier offence for the purposes of subsection (5)` | s84-definitions:938 | JUST FALSE | (a) | "the only question to be considered is the sequence of convictions" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 85(4) the sentence must be served consecutively to the other punishment or sentence` | s85-98-use-possession:110 | NOTHING | (b) | "to any other punishment imposed on the person for an offence arising out of the same event or series of events ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 86(1) the person commits an offence of careless use of a firearm, etc.` | s85-98-use-possession:126 | NOTHING | (b) | "without lawful excuse" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 87(1) the person commits the offence of pointing a firearm` | s85-98-use-possession:193 | NOTHING | (b) | "without lawful excuse" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 89(1) the person commits an offence of carrying a weapon while attending a public meeting` | s85-98-use-possession:281 | NOTHING | (b) | "without lawful excuse" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 90(1) the person commits an offence of carrying a concealed weapon` | s85-98-use-possession:309 | JUST FALSE | (a) | "unless the person is authorized under the Firearms Act to carry it concealed" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 91(1) the person commits an offence of unauthorized possession of a firearm` | s85-98-use-possession:354 | JUST FALSE | (a) | "Subsections (1) and (2) do not apply to" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 91(1) the person commits an offence of unauthorized possession of a firearm` | s85-98-use-possession:356 | NOTHING | (b) | "without being the holder of" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 91(2) the person commits an offence of unauthorized possession of a prohibited weapon or restricted weapon` | s85-98-use-possession:374 | JUST FALSE | (a) | "Subsections (1) and (2) do not apply to" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 91(2) the person commits an offence of unauthorized possession of a prohibited weapon or restricted weapon` | s85-98-use-possession:376 | NOTHING | (b) | "without being the holder of a licence under which the person may possess it" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 91(4) subsections (1) and (2) do not apply to the person` | s85-98-use-possession:426 | NOTHING | (b) | "do not apply to" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 92(1) the person commits an offence of possession of a firearm knowing its possession is unauthorized` | s85-98-use-possession:461 | JUST FALSE | (a) | "Subsections (1) and (2) do not apply to" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 92(2) the person commits an offence of possession of a prohibited weapon, device or ammunition knowing its possession is unauthorized` | s85-98-use-possession:481 | JUST FALSE | (a) | "Subsections (1) and (2) do not apply to" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 92(4) subsections (1) and (2) do not apply to the person` | s85-98-use-possession:525 | NOTHING | (b) | "do not apply to" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 93(1) the person commits an offence of possession at an unauthorized place` | s85-98-use-possession:560 | JUST FALSE | (a) | "Subsection (1) does not apply to a person who possesses a replica firearm" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 93(3) subsection (1) does not apply to a person who possesses a replica firearm` | s85-98-use-possession:602 | NOTHING | (b) | "does not apply to a person who possesses a replica firearm" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 94(1)(a) the occupant is within the exception for a firearm` | s85-98-use-possession:630 | JUST FALSE | (a) | "unless" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 94(1)(b) the occupant is within the exception for a weapon, device or ammunition` | s85-98-use-possession:656 | JUST FALSE | (a) | "unless" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 94(3) subsection (1) does not apply to an occupant who attempted to leave or left the motor vehicle` | s85-98-use-possession:668 | NOTHING | (b) | "does not apply to an occupant of a motor vehicle who" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 94(4) subsection (1) does not apply when an occupant came into possession by the operation of law` | s85-98-use-possession:678 | NOTHING | (b) | "does not apply to an occupant of a motor vehicle when the occupant or any other occupant ... is a person who c ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 94(1) the person commits an offence of unauthorized possession in a motor vehicle` | s85-98-use-possession:694, s85-98-use-possession:695, s85-98-use-possession:697 | JUST FALSE | (a) | "Subsection (1) does not apply to an occupant of a motor vehicle who"; "Subsection (1) does not apply to an occupant of a motor vehicle when" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 95(1) the person commits an offence of possession of a prohibited or restricted firearm with ammunition` | s85-98-use-possession:757 | JUST FALSE | (a) | "Subsection (1) does not apply to a person who is using the firearm under the direct and immediate supervision" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 95(1) the person commits an offence of possession of a prohibited or restricted firearm with ammunition` | s85-98-use-possession:759 | NOTHING | (b) | "without being the holder of" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 95(3) subsection (1) does not apply to the person` | s85-98-use-possession:799 | NOTHING | (b) | "does not apply to a person who is using the firearm under the direct and immediate supervision of another pers ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 96(1) the person commits an offence of possession of a weapon obtained by the commission of an offence` | s85-98-use-possession:814 | JUST FALSE | (a) | "Subsection (1) does not apply to a person who comes into possession" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 96(3) subsection (1) does not apply to the person` | s85-98-use-possession:858 | NOTHING | (b) | "does not apply to a person who comes into possession of anything referred to in that subsection by the operati ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 98(3)(a) the person enters` | s85-98-use-possession:934 | JUST FALSE | (a) | "a person enters as soon as any part of his or her body or any part of an instrument that he or she uses is wit ..." | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 98(3)(b) the person is deemed to have broken and entered` | s85-98-use-possession:950 | JUST FALSE | (a) | "a person is deemed to have broken and entered if he or she" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |
| `s 99(2) the punishment when the object in question is a firearm, device, part or ammunition` | s99-108-trafficking-and-others:71 | NOTHING | (b) | "when the object in question is" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 99(3) the punishment in any other case` | s99-108-trafficking-and-others:93 | NOTHING | (b) | "In any other case" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 100(2) the punishment when the object in question is a firearm, device, part or ammunition` | s99-108-trafficking-and-others:146 | NOTHING | (b) | "when the object in question is" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 100(3) the punishment in any other case` | s99-108-trafficking-and-others:168 | NOTHING | (b) | "In any other case" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 101(1) the person commits an offence of transfer without authority` | s99-108-trafficking-and-others:189 | NOTHING | (b) | "otherwise than under the authority of" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 102(1) the person commits an offence of making an automatic firearm` | s99-108-trafficking-and-others:237 | NOTHING | (b) | "without lawful excuse" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 102.1(1) the person commits an offence of possession of computer data` | s99-108-trafficking-and-others:295 | NOTHING | (b) | "otherwise than under the authority of" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 102.1(2) the person commits an offence of distribution of computer data` | s99-108-trafficking-and-others:313 | NOTHING | (b) | "otherwise than under the authority of" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 103(2) the punishment when the object in question is a firearm, device, part or prohibited ammunition` | s99-108-trafficking-and-others:385 | NOTHING | (b) | "when the object in question is" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 103(2.1) the punishment in any other case` | s99-108-trafficking-and-others:408 | NOTHING | (b) | "In any other case" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 104(1) the person commits an offence of unauthorized importing or exporting` | s99-108-trafficking-and-others:438 | NOTHING | (b) | "otherwise than under the authority of" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 104.1(1) the person commits an offence of altering a cartridge magazine` | s99-108-trafficking-and-others:495 | NOTHING | (b) | "without lawful excuse" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 108(1) the person commits an offence of tampering with a serial number` | s99-108-trafficking-and-others:735 | NOTHING | (b) | "without lawful excuse" | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 108(3) no person is guilty of an offence under paragraph (1)(b) by reason only of possessing the firearm` | s99-108-trafficking-and-others:772 | NOTHING | (b) | "No person is guilty of an offence under paragraph (1)(b) by reason only of possessing a prohibited firearm or  ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 108(4) the evidence is proof that the person possesses the firearm knowing that the serial number on it has been altered, defaced or removed` | s99-108-trafficking-and-others:783 | NOTHING | (b) | "evidence that a person possesses a firearm the serial number on which has been wholly or partially obliterated ..." | JUST FALSE: a prohibition or grant limited by its own wording does say no outside the limit |
| `s 108(4) the evidence is proof that the person possesses the firearm knowing that the serial number on it has been altered, defaced or removed` | s99-108-trafficking-and-others:784 | JUST FALSE | (a) | "in the absence of evidence to the contrary" | NOTHING: "if A then B" does not itself say "if not A then not B"; a flat negative is not the text's no |

### Fork lines of the ruling of 2026-11-12 (one per function; the readings are in the fork register)

- **F-110(2.1)**: `s 110(2.1) the order may be imposed for life or for any shorter duration`; the other reading: JUST FALSE for a case where the violence gate fails (reading (a)).
- **F-110.1(1)**: `s 110.1(1) any person may make an ex parte application to a provincial court judge for an order`; the other reading: JUST FALSE for a case where the belief gate fails (reading (a)).
- **F-110.1(2)**: `s 110.1(2) the provincial court judge may hold the hearing in private`; the other reading: JUST FALSE for a case where the judge does not consider it necessary (reading (a)).
- **F-110.1(5)**: `s 110.1(5) the provincial court judge may issue a warrant to search and seize`; the other reading: JUST FALSE for a case where the judge is not satisfied (reading (a)).
- **F-110.1(6)**: `s 110.1(6) the peace officer may search for and seize without a warrant`; the other reading: JUST FALSE for a case where an "if" gate fails (reading (a)).
- **F-110.2(1)**: `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information`; the other reading: all three gates NOTHING (a power limited by its own wording), or all three JUST FALSE.
- **F-110.3(1)**: `s 110.3(1) a provincial court judge may make an order to delete identifying information`; the other reading: all three gates NOTHING, or all three JUST FALSE.

### Reading a result: FALSE and NOTHING (ccc4)

A function of this part answers `JUST TRUE`, `JUST FALSE` or `NOTHING` (the rule of 2026-10-29, assumed, not ruled by a lawyer, with the rulings recorded word for word in the fork register above (E1 and N2 of the bench `commons-negation-1030`, and those of 2026-11-05) and the ruling of 2026-11-12 on powers).
**A "no" (`JUST FALSE`) in this part is one of these, and each branch quotes the words:**
- an unmet element of an offence section ("Every person commits an offence who uses a firearm ..." and the element is absent), on reading A of fork F-OF;
- a closed definition ("handgun means ...", "semi-automatic, in respect of a firearm, means ...") and the thing is outside it;
- an exception that applies ("Subsections (1) and (2) do not apply to ...", "unless ...", "No person is guilty ... by reason only of ...");
- a duty whose "if" gate fails (s 110.1(3)), a stated period that is missed (the 30 days of s 110.1(3)), and an "on application" gate that fails (s 110.2(1), s 110.3(1)).
**"Not covered" (`NOTHING`) is one of these, and each branch carries its kind:**
- the text is silent or lists without closing the list ("includes", "without restricting the generality of the foregoing");
- a term is undefined here or answered by another part or by the regulations ("prescribed", s 2 "firearm", s 787(1));
- a prohibition or grant is limited by its own wording and the case is inside or outside the limit: "without lawful excuse" with an excuse, "without being the holder of" with a licence held, "otherwise than under the authority of", and a power with an "if" gate that fails (the ruling of 2026-11-12: s 110(2.1), s 110.1(1), (2), (5), (6), s 110.2(1), s 110.3(1)).
`NOTHING` is never "no": a person for whom a question answers `NOTHING` has not been told that what they did is lawful, only that the text does not say.
A caller of these functions must never turn `NOTHING` into `FALSE`; the seat layer passes it through unchanged, and "not known" is passed on as `NOTHING`.
The seat's own `"no"` is the person's answer to a question about a fact, not the text's no (two branches of `ccc4-seat.l4`, marked "an input value").

## Seams (ccc4)

Each seam input this part took (each read from the modules; the functions that take it are listed), and where it differs from PLAN.md.

| seam | taken as | taken by | against PLAN |
| --- | --- | --- | --- |
| s 2 terms | inputs `s 2 firearm: ...`, `s 2 weapon: ...`, `s 2 motor vehicle: ...`, `s 2 intimate partner: ...`, each `MAYBE BOOLEAN` (the seat calls the keel's `s 2 <term>` instead) | `s 84(1)` (firearm, weapon), `s 88(1)`, `s 89(1)`, `s 90(1)` (weapon), `s 94(1)` (motor vehicle), `s 109(1)(a.1)` and `s 110(2.1)` (intimate partner) | as PLAN R4 |
| s 3.01(1) (keel) | input `s 3.01(1) the offence counts as an offence in the commission of which violence is used, threatened or attempted against any person or class of persons`, `MAYBE BOOLEAN`; the seat calls the keel's `s 3.01(1)` and `s 3.01(2)` (with the provision 109(1)) | `s 109(1)(a)`, `s 109(1)(a.1)`, `s 110(1)`, `s 110(2.1)` | **differs in name:** PLAN names it `s 3.01 the offence counts as one in which violence is used, threatened or attempted`; this part uses the keel's own function name, so the merge deletes the input and nothing else; see fork F-3.01 and finding 13 |
| s 787(1) (ccc29) | input `s 787(1) the general penalty for an offence punishable on summary conviction`, a `Punishment` | the summary limb of 19 functions: `s 86(3)(b)`, `s 87(2)(b)`, `s 88(2)(b)`, `s 89(2)`, `s 90(2)(b)`, `s 91(3)(b)`, `s 93(2)(b)`, `s 94(2)(b)`, `s 95(2)(b)`, `s 96(2)(b)`, `s 101(2)(b)`, `s 102(2)(b)`, `s 102.1(3)(b)`, `s 104(2)(b)`, `s 104.1(2)(b)`, `s 105(2)(b)`, `s 106(2)(b)`, `s 107(2)(b)`, `s 108(2)(b)` | as PLAN |
| s 321 (ccc12) | input `s 321 the person breaks`, `MAYBE BOOLEAN` | `s 98(2)` | as PLAN |
| s 342.1(2) (ccc12) | inputs `s 342.1(2) the thing is computer data` and `s 342.1(2) the thing is a computer system`, both `MAYBE BOOLEAN` | `s 102.1(4)` | as PLAN |
| s 343 | input `s 343 the person commits a robbery within the meaning of section 343`, `MAYBE BOOLEAN` | `s 98.1` | **not in PLAN:** PLAN lists ss 98 and 102.1 against ccc12 (ss 321, 342.1(2)) and does not list s 98.1, which says "robbery within the meaning of section 343"; the lead should join this input to the part that encodes s 343 |
| s 117.07 to 117.1 (ccc5) | not taken | `s 94(1)(a)(iii)` | **differs:** PLAN lists a `MAYBE BOOLEAN` input `s 117.07 the person is exempt from the prohibition (...)` for ss 94 and 110.1; s 94(1)(a)(iii) asks whether the person "had reasonable grounds to believe" that another occupant could not be convicted under ss 117.07 to 117.1, so it is a plain fact about the person's belief (a `BOOLEAN` input), and the answer of the part that encodes ss 117.07 to 117.1 is not an element (comment at `ccc4-s85-98-use-possession.l4:607`); no function of s 110.1 takes it either: s 110.1(9) only names sections 113, 114 and 116 |

Seams that other parts ask of this part (what this part must answer):
- `s 84(1) the thing is within the meaning the term has in subsection 84(1)` (s 2.1, the keel): written, `MAYBE BOOLEAN`.
- **`s 110.1 an emergency prohibition order has been made` (ss 110.4 to 113, ccc5; PLAN: `MAYBE BOOLEAN`): not written.** The nearest functions are `s 110.1(3) the provincial court judge must make an emergency prohibition order` (answers what the judge must do) and the duty `s 110.1(3) the duty of the provincial court judge to make an emergency prohibition order`; neither answers whether an order "has been made", and the "an order is made" facts of ss 110.1(4) to 110.3(5) are plain `BOOLEAN` inputs here. The lead should join ccc5's input to such a fact at the merge, or ask this part for the function; it is a gap against PLAN, not a core item.
- The punishment of each offence section (ccc1, ccc14, ccc26): PLAN asks the offence sections for the punishment; each offence here has `s N(k) the class of the offence` and `s N(k) the punishment on indictment` (and the s 787(1) seam for the summary limb), as the seat's penalty record uses them.

## Findings: what the text turns out to say (ccc4)

1. **A territory is the Supreme Court, Nunavut included.** s 84(1) "superior court" (d) says "a territory, the Supreme Court"; s 2 "superior court of criminal jurisdiction" (f) names the Nunavut Court of Justice. Encoded as s 84(1) has it (fork F-Nunavut).
2. **A 2026 amendment is already in the text.** s 84(1) "superior court" (e) reads "[Repealed, 2026, c. 11, s. 3]"; the consolidation is current to 2026-09-30 (`inputs/R.S.C.-1985-c.-C-46.meta.json`).
3. **Seven units are repealed or blank in this text** (coverage table): the paragraph above, ss 91(5), 92(5) and (6), 94(5), 97 (repealed before coming into force), 103(3) and 104(3).
4. **s 89(2) is the only provision of the range whose whole punishment is summary conviction** ("is guilty of an offence punishable on summary conviction"); the other 18 summary limbs are paragraph (b) of a section that also has an indictable limb. It states no penalty, so its question asks only how the offence is classified (see "Second seat audit", Q32), and the penalty is s 787(1)'s.
5. **The ten-year cut-off of s 84(5) leaves out time in custody** ("not taking into account any time in custody"): `ten years have elapsed` adds the days spent in custody to the ten years, and the tenth anniversary itself counts as elapsed (fork F-ten-years). s 84(5) says it applies "for the purpose of subsection 99(2), 100(2) or 103(2)".
6. **s 84(6): only the sequence of convictions counts.** `s 84(6) offence one is the earlier offence ...` compares the days of conviction and ignores the days of commission; equal days answer NOTHING.
7. **"Ten years less a day" is not ten years.** s 109(1)(a) asks for imprisonment "for ten years or more"; a maximum written "ten years less a day" is below it, and the seat asks the "less a day" flag (test case, `ccc4-cases-seat.l4`).
8. **Prohibited ammunition is in both limbs of s 109(2).** It is ammunition (a: ten years) and prohibited ammunition (b: life); the order forbids it for life (fork F-109-ammo).
9. **The emergency order is "not exceeding 30 days"** (s 110.1(3)); the test is whole years and months zero and days at most 30 (fork F-30-days).
10. **The return of seized things has three occasions, and (c) overrides (a) and (b).** s 110.1(8)(c) says "despite paragraphs (a) and (b)", so revocation is tested first.
11. **An order under s 110.2(1) expires with the s 110.1(3) order (s 110.2(2)), or, if a hearing date is fixed under s 110.4(1), on that date or on the day the s 110.1(3) order is revoked if that is earlier (s 110.2(3)).** `s 110.2(2) the day on which the order made under subsection (1) expires` answers NOTHING when the s 110.2(1) order "is revoked earlier", because it then ends on a day the text does not give.
12. **s 2 "weapon" and the keel's reading (a seam finding).** The raw text (lines 220-223) says "weapon means any thing used, designed to be used or intended for use (a) in causing death or injury to any person, or (b) for the purpose of threatening or intimidating any person and, without restricting the generality of the foregoing, includes a firearm and, for the purposes of sections 88, 267 and 272, any thing used ... in binding or tying up a person against their will".
    On the reading of fork F2 ("means ... and includes" is closed), a thing outside (a), (b), a firearm and the binding case is not a weapon and the answer would be JUST FALSE.
    The keel's `s 2 weapon` answers NOTHING there ("list not closed": "without restricting the generality of the foregoing"), and the seat layer calls it without restating it.
    Four seat cases (`Under section 84(1), is my weapon a prohibited weapon`, and one each for ss 88(1), 89(1), 90(1)) first expected JUST FALSE, were found to answer NOTHING, and the NOTHING assertion now stands in `ccc4-cases-seat.l4` with the first expectation, JUST FALSE, asserted in the red file (end of finding 13); the other reading stays recorded here and in fork F-weapon.
    Layer 1 is unaffected: it takes the answer of s 2 "weapon" as an input, and its tests use JUST FALSE as an input value.
13. **The commonest case answers "not covered" on s 110(1)(a).** s 3.01(1) says a reference to an offence of violence "includes a reference to any of the following offences" (sexual offences, ss 264, 279.01, 279.011), and the keel's `s 3.01(1)` answers NOTHING for an offence it does not list.
    So for a person whose offence had no violence in fact and is none of those, limb (a) of s 109(1), of s 110(1) and the exception of s 110(2.1) answer NOTHING, not JUST FALSE; on reading B of fork F-3.01 they would be JUST FALSE.
    Two cases of the question about s 110(1) (Q96) first expected JUST FALSE for such facts and now expect NOTHING, each citing this finding in its comment.
    **Six seat expectations are kept failing in their own file, as the brief asks:** `ccc4-cases-seat-expected-red.l4` holds the first expectation, JUST FALSE, of each of the six cases (four of finding 12, two of this one) and is listed in `check.sh` `expected_failed` with the count 6; it fails 6 times, identically on both builds (errors 6, satisfied 0, failed 6 on each).
    The same six facts are asserted as NOTHING, what the keel answers, in `ccc4-cases-seat.l4` (its 660 assertions are unchanged), each with a comment naming the red file; those six NOTHING expectations were written after the first run, and are the keel's reading, not a reading of this range.
    The first run had seven failures: the six above and a seventh in the s 110(1) block (`work/run-seat.txt`, first-run lines 78, 269, 285, 297, 786, 787, 789); the case that failed there and whose facts were then changed (violence used, s 109(1) applying, so that the text itself says no) is not in the red file, because its original facts were not kept.
14. **"Within a reasonable period" and "with reasonable despatch" are facts, not numbers.** ss 91(4)(b), 92(4)(b) and 96(3) state no period and take it as a plain `BOOLEAN` input; the duties of ss 105(1) and 106(1) ("with reasonable despatch") carry no WITHIN (fork F-despatch).
15. **"Prescribed" is outside the sources.** Every "prescribed" in s 84(1) is an input (`MAYBE BOOLEAN` in layer 1); the seat asks the person "yes", "no" or "not known", and "not known" (or any other word) is passed on as NOTHING (`ccc4 seat: yes, no or not known`).
16. **The ISU and prescribed words share one seat input.** In the question about the class of a firearm (s 84(1)), "the handgun is prescribed and for use in International Shooting Union competitions" is one STRING that feeds both the prohibited-firearm and the restricted-firearm definitions; "not known" gives NOTHING for both.
17. **The plan lacks two seams** (s 343 and the "has been made" function): see "Seams (ccc4)".

## What the stable binary does not accept (ccc4)

Where the skills describe a construct the stable binary (1.6.110, and 1.6.109 as the second build) rejects, the binary governs.
Hit while writing this part:
- **`NOT` binds the whole rest of the group.** `NOT (x) AND y` parses as `NOT ((x) AND y)`, and `NOT (A) OR B` the same; put `NOT` last in its group or write `(NOT x)`. Found by the tests in s 92(1) and s 92(2) and fixed; every `NOT` in the modules is parenthesised.
- **A heading takes one backtick token** (`§ `Section 85 -- Using ...``); a heading with two backtick tokens is a parse error.
- **A deontic value cannot be asserted** (`#ASSERT` over a `DEONTIC` result is not available): the 10 regulative rules (3 in ss 105 and 106, 7 in ss 109 to 110.3) are run with `#TRACE` (7 traces in `ccc4-tests-s99-108.l4`, 22 in `ccc4-tests-s109-110-3.l4`, identical on both builds by `work/cmp-traces.py`), and the duties of ss 109(1), 110(1), 110(3), 110.1(3), 110.1(7), 110.2(4) and 110.3(3) are also encoded as decision functions that are asserted (for example `s 110.2(4) the documents must be placed in a packet and sealed by the judge`).
- **`REFUSE`, `#ASSERT REFUSED` and `BECAUSE`** are not used: "not covered" is `NOTHING` (or a named constructor), and asserted.
- **A multi-line `LIST` needs parentheses and commas**, and an `#ASSERT` must be on one line.
- **A name defined in two imported modules cannot be used**: every top-level name, type and constructor of this part begins with its section label, or `ccc4 seat:` in the seat layer.

## Seat questions (ccc4)

The seat is a person who is, or may be, accused of an offence under the Criminal Code.
The 121 questions of `ccc4-seat.l4`, in the text's order under their `§` headings, each named "Under section N,"; the numbers are the order in the file.
(Assumed, not ruled: Singapore's Penal Code is the model, as the maintainer instructed on 2026-11-09, but this is a plain seat layer.)

**Part III -- Interpretation (section 84): what is the thing I hold or did something with?**

1. Under section 84(1), is my firearm a prohibited firearm, a restricted firearm or a non-restricted firearm?
2. Under section 84(2), what is the length of my firearm’s barrel in millimetres?
3. Under section 84(1), is my firearm an antique firearm?
4. Under section 84(1), is my device a prohibited device?
5. Under section 84(1), is my weapon a prohibited weapon?
6. Under section 84(1), is my weapon a restricted weapon?
7. Under section 84(1), is my thing prohibited ammunition?
8. Under section 84(1), is my device a replica firearm?
9. Under section 84(1), is my device a cross-bow?
10. Under section 84(1), is my thing a firearm part?
11. Under section 84(3), does the Code deem my weapon not to be a firearm for the purposes of the section I am asking about?
12. Under section 84(4), am I the holder of an authorization or a licence?
13. Under section 84(4), am I the holder of a registration certificate for a firearm?
14. Under section 84(5), must my earlier conviction be counted as an earlier offence in deciding whether I have committed a second or subsequent offence?
15. Under section 84(6), was my first offence the earlier offence for the purposes of subsection (5)?
16. Under section 84(1), is what I did a transfer?
17. Under section 84(1), is what I did an export?
18. Under section 84(1), is what I did an import?
19. Under section 84(1), is the order I am subject to a prohibition order?
**Use Offences (sections 85 to 87): did what I did with a firearm make me guilty of an offence, and how grave is it?**

20. Under section 85(1), have I committed an offence by using a firearm in the commission of an offence?
21. Under section 85(2), have I committed an offence by using an imitation firearm in the commission of an offence?
22. Under section 85(3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
23. Under section 85(4), must my sentence for using a firearm or an imitation firearm be served consecutively to my other punishment or sentence?
24. Under section 86(1), have I committed an offence of careless use of a firearm, weapon, device or ammunition?
25. Under section 86(2), have I committed an offence by contravening a storage regulation?
26. Under section 86(3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
27. Under section 87(1), have I committed the offence of pointing a firearm?
28. Under section 87(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
**Possession Offences (sections 88 to 98.1): did what I possessed or carried make me guilty of an offence, and how grave is it?**

29. Under section 88(1), have I committed an offence by possessing a weapon for a dangerous purpose?
30. Under section 88(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
31. Under section 89(1), have I committed an offence by carrying a weapon while attending a public meeting?
32. Under section 89(2), how is the offence classified?
33. Under section 90(1), have I committed an offence by carrying a concealed weapon?
34. Under section 90(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
35. Under section 91(1), have I committed an offence by possessing a firearm without a licence and registration certificate?
36. Under section 91(2), have I committed an offence by possessing a prohibited weapon, restricted weapon, prohibited device or prohibited ammunition without a licence?
37. Under section 91(3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
38. Under section 91(4), do subsections (1) and (2) of section 91 not apply to me?
39. Under section 92(1), have I committed an offence by possessing a firearm knowing that my possession is unauthorized?
40. Under section 92(2), have I committed an offence by possessing a prohibited weapon, device or ammunition knowing that my possession is unauthorized?
41. Under section 92(3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
42. Under section 92(4), do subsections (1) and (2) of section 92 not apply to me?
43. Under section 93(1), have I committed an offence by possessing a firearm, weapon, device or ammunition at an unauthorized place?
44. Under section 93(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
45. Under section 93(3), does subsection 93(1) not apply to me because I possess a replica firearm?
46. Under section 94(1), have I committed an offence as an occupant of a motor vehicle in which I knew there was a firearm, weapon, device or ammunition?
47. Under section 94(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
48. Under section 95(1), have I committed an offence by possessing a loaded prohibited or restricted firearm, or one with readily accessible ammunition?
49. Under section 95(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
50. Under section 96(1), have I committed an offence by possessing a firearm, weapon, device or ammunition that I know was obtained by an offence?
51. Under section 96(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
52. Under section 98(1), have I committed an offence of breaking and entering to steal a firearm?
53. Under section 98(2), is the thing I broke into a place?
54. Under section 98(3), did I enter the place?
55. Under section 98(3), am I deemed to have broken and entered?
56. Under section 98(4), how is the offence classified and what is the punishment if I am prosecuted by indictment?
57. Under section 98.1, have I committed an offence of robbery to steal a firearm?
58. Under section 98.1, how is the offence classified and what is the punishment if I am prosecuted by indictment?
**Trafficking, Assembling, Computer Data, Export and Import Offences (sections 99 to 104.1): did what I made, sold, transferred, possessed, imported or exported make me guilty of an offence, and how grave is it?**

59. Under section 99(1), have I committed the offence of weapons trafficking?
60. Under section 99(2) and (3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
61. Under section 100(1), have I committed the offence of possession for the purpose of weapons trafficking?
62. Under section 100(2) and (3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
63. Under section 101(1), have I committed an offence by transferring a firearm, weapon, device, part or ammunition without authority?
64. Under section 101(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
65. Under section 102(1), have I committed the offence of making an automatic firearm?
66. Under section 102(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
67. Under section 102.1(1), have I committed an offence by possessing or accessing computer data for making a firearm?
68. Under section 102.1(2), have I committed an offence by distributing computer data for making a firearm?
69. Under section 102.1(3), how is the offence classified and what is the punishment if I am prosecuted by indictment?
70. Under section 103(1), have I committed the offence of importing or exporting knowing it is unauthorized?
71. Under section 103(2) and (2.1), how is the offence classified and what is the punishment if I am prosecuted by indictment?
72. Under section 104(1), have I committed an offence of unauthorized importing or exporting?
73. Under section 104(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
74. Under section 104.1(1), have I committed an offence by altering a cartridge magazine so that it becomes a prohibited device?
75. Under section 104.1(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
**Lost, Destroyed or Defaced Weapons (sections 105 to 108): did I fail to report, or report falsely, or tamper with a serial number?**

76. Under section 105(1)(a), have I committed an offence by not reporting the loss or theft of a firearm, weapon, device, ammunition or document?
77. Under section 105(1)(b), have I committed an offence by not delivering up or reporting a firearm, weapon, device or ammunition that I found?
78. Under section 105(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
79. Under section 106(1), have I committed an offence by not reporting the destruction of a firearm, weapon, device or ammunition?
80. Under section 106(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
81. Under section 107(1), have I committed an offence by knowingly making a false report or statement about a loss, theft or destruction?
82. Under section 107(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
83. Under section 107(3), is what I said a report or statement?
84. Under section 108(1), have I committed an offence of tampering with a serial number?
85. Under section 108(2), how is the offence classified and what is the punishment if I am prosecuted by indictment?
86. Under section 108(3), am I not guilty of an offence under paragraph 108(1)(b) by reason only of possessing the firearm?
87. Under section 108(4), is the evidence that I possess a firearm with an obliterated serial number proof that I knew it had been altered?
**Prohibition Orders (sections 109 to 110.3): must or may a court forbid me to possess firearms and other weapons, for how long, and what can be done to me and to the records?**

88. Under section 109(1)(a), is my offence one in which violence was used and for which I may be sentenced to imprisonment for ten years or more?
89. Under section 109(1)(b), is my offence one that paragraph (b) names?
90. Under section 109(1)(c) and (c.1), is my offence one relating to a contravention of the Controlled Drugs and Substances Act or the Cannabis Act that the paragraphs name?
91. Under section 109(1)(d), is my offence one that involves a thing I was already prohibited from possessing?
92. Under section 109(1), must the court make a prohibition order against me?
93. Under section 109(2) and (3), for how long must the order forbid me to possess the thing?
94. Under section 109(4), is what I received a release from imprisonment?
95. Under section 109(5), does the section I am asking about apply to an order made against me?
96. Under section 110(1), must the court consider whether to make a prohibition order against me?
97. Under section 110(1), must the court make a prohibition order against me?
98. Under section 110(2), what is the latest day on which a discretionary prohibition order may end?
99. Under section 110(2.1), may a discretionary prohibition order be imposed on me for life or for any shorter duration?
100. Under section 110(3), must the court give reasons for not making a prohibition order or for not forbidding everything?
101. Under section 110.1(1), may someone apply, without notice to me, for an emergency prohibition order against me?
102. Under section 110.1(2), may the provincial court judge hear the application against me in private?
103. Under section 110.1(3), must the provincial court judge make an emergency prohibition order against me?
104. Under section 110.1(3), is the period the order is for within the limit of thirty days?
105. Under section 110.1(4), must a copy of the emergency order be served on me?
106. Under section 110.1(5), may a provincial court judge issue a warrant to search for and seize the things I am forbidden to possess?
107. Under section 110.1(6), may a peace officer search for and seize the things I am forbidden to possess without a warrant?
108. Under section 110.1(7), must the peace officer who searched report to a justice?
109. Under section 110.1(8), when must the things seized from me or surrendered by me be returned to me?
110. Under section 110.1(9), does the section I am asking about apply to the emergency order made against me?
111. Under section 110.1(10), is the judge a provincial court judge within the meaning of the sections it names?
112. Under section 110.2(1), may a provincial court judge order that information about the order made against me be kept from the public?
113. Under section 110.2(2) and (3), on what day does the order keeping information from the public end?
114. Under section 110.2(4), must the documents about the order made against me be sealed?
115. Under section 110.2(5), may an application to revoke or vary the order keeping information from the public be made to the judge who made it or to another provincial court judge?
116. Under section 110.3(1), may a provincial court judge order that the documents I receive be edited to remove identifying information?
117. Under section 110.3(1), what does an order to delete identifying information direct?
118. Under section 110.3(2), may the order to delete identifying information be for any period, definite or indefinite?
119. Under section 110.3(3), must the originals of the documents be sealed?
120. Under section 110.3(4), may an application to revoke or vary the order to delete identifying information be made to the judge who made it or to another provincial court judge?
121. Under section 110.3(5), does an order to delete identifying information still apply to the hearing of the application against me?

### Second seat audit (the instruction of 2026-11-12; done 2026-11-16)

Every one of the 121 questions was read against the BODY of the layer-1 function it calls, not against its own title (`work/dumpaudit.py` prints each title with the called bodies; `work/pairs.txt` pairs a title with every function it calls).
This file recorded no direction audit before, so the direction audit is recorded here too.
- **Questions read: 121. Retitled: 11. Read and left: 110** (the doubtful ones are listed below with a reason; the rest were read and are not listed).
- **Direction: 0 mismatches.** Each question title was compared with the name of the function it calls (`work/pairs.txt`, generated by `work/pairseat.py`): "may" with "may", "must" with "must", "have I committed" with "commits", "do not apply" and "not guilty" with the same negatives; no title is a grant over a bar or the reverse (criterion 3: 0 retitles). Every retitle is for scope, limb or premise.
- **Assertions restated in place: 51 in `ccc4-cases-seat.l4`** carry `-- RECONCILED 2026-11-12: was #ASSERT ...` for the retitled questions (the cases file is generated by question key from the names in `ccc4-seat.l4`, so each carries the new name); the layer-1 tests are unaffected by a retitle.
- The criterion numbers are those of the instruction: (1) a different limb, route or scope; (2) a premise, qualifier or consequence the function does not compute or the text does not say; (3) polarity or modal; (4) the type of the answer.

| no. | old name | new name (written out exactly) | criterion and reason |
| --- | --- | --- | --- |
| 14 | Under section 84(5), must my earlier conviction be counted as an earlier offence for the minimum punishment of a second or subsequent offence | Under section 84(5), must my earlier conviction be counted as an earlier offence in deciding whether I have committed a second or subsequent offence | (2) the old title ("for the minimum punishment of a second or subsequent offence") carried a consequence the function does not compute: it answers whether the earlier offence is to be considered as an earlier offence, and s 84(5) says "In determining ... whether a convicted person has committed a second or subsequent offence" |
| 23 | Under section 85(4), must my sentence for using a firearm be served consecutively to my other sentences | Under section 85(4), must my sentence for using a firearm or an imitation firearm be served consecutively to my other punishment or sentence | (1) the old title named one limb ("using a firearm", "other sentences") where s 85(4) reaches an offence under subsection (1) or (2) (an imitation firearm is subsection (2)) and "any other punishment imposed ... for an offence arising out of the same event or series of events" as well as any other sentence |
| 32 | Under section 89(2), how is the offence classified and what is the punishment if I am prosecuted by indictment | Under section 89(2), how is the offence classified | (2) the old title asked for "the punishment if I am prosecuted by indictment" of an offence that s 89(2) makes punishable on summary conviction only; the function answers its class and no punishment |
| 86 | Under section 108(3), am I not guilty of possessing a firearm whose serial number was altered, because the number was replaced and certified | Under section 108(3), am I not guilty of an offence under paragraph 108(1)(b) by reason only of possessing the firearm | (1) the old title ("not guilty of possessing a firearm whose serial number was altered, because the number was replaced and certified") read as a general acquittal; the text frees a person only from an offence under paragraph (1)(b), "by reason only of possessing", for a prohibited or restricted firearm, and the function is scoped to that paragraph |
| 95 | Under section 109(5), do sections 113 to 117 apply to an order made against me | Under section 109(5), does the section I am asking about apply to an order made against me | (1) the old title asked about sections 113 to 117 together; s 109(5) says they apply, and the function answers for the one section the person names (NOTHING for any other) |
| 97 | Under section 110(1), must the court make a prohibition order against me because it finds it desirable | Under section 110(1), must the court make a prohibition order against me | (2) the old title built the premise "because it finds it desirable" into the question; the function takes the decision of the court as an input and answers for either value, so a premise the title asserts is not one the function holds fixed |
| 98 | Under section 110(2), what is the latest day on which a discretionary prohibition order may end, if I do not fall within subsection (2.1) | Under section 110(2), what is the latest day on which a discretionary prohibition order may end | (2) the old title carried a qualifier, "if I do not fall within subsection (2.1)", that the function does not compute; s 110(2) states none ("Despite subsection (2)" opens (2.1)) |
| 110 | Under section 110.1(9), do sections 113, 114 and 116 apply to the emergency order made against me | Under section 110.1(9), does the section I am asking about apply to the emergency order made against me | (1) as Q95: the old title asked about sections 113, 114 and 116 together; the function answers for the one section the person names |
| 115 | Under section 110.2(5), may I apply to revoke or vary the order keeping information from the public | Under section 110.2(5), may an application to revoke or vary the order keeping information from the public be made to the judge who made it or to another provincial court judge | (2) the old title made "I" the applicant; s 110.2(5) says only to whom an application "may be made" ("the provincial court judge who made the order or ... another provincial court judge") and names no applicant |
| 118 | Under section 110.3(2), may the order to delete identifying information be for an indefinite period | Under section 110.3(2), may the order to delete identifying information be for any period, definite or indefinite | (1) the old title named one limb ("an indefinite period") where s 110.3(2) says "any period -- definite or indefinite -- that the provincial court judge considers necessary" |
| 120 | Under section 110.3(4), may I apply to revoke or vary the order to delete identifying information | Under section 110.3(4), may an application to revoke or vary the order to delete identifying information be made to the judge who made it or to another provincial court judge | (2) as Q115, for s 110.3(4) |

Read and left, with the reason (doubtful ones only):
- Q1: asks which class a firearm is in ("a prohibited firearm, a restricted firearm or a non-restricted firearm") over a function that returns the class; a rephrasing of this title was tried and reverted, being wording.
- Q15: "my first offence" is the function's `offence one`; the body compares the days of conviction, as "the earlier offence" asks.
- Q35: compresses "without being the holder of (a) a licence ...; and (b) in the case of a prohibited firearm or a restricted firearm, a registration certificate" to "without a licence and registration certificate"; the body asks for the certificate only for those two kinds (`the person holds what the subsection requires`).
- Q24, 43, 46, 50, 63, 76, 77, 79: shorten the text's list of things to "a firearm, weapon, device or ammunition"; a shortened list is wording, and each function takes the kind of thing as an input (`the kind of thing`, `the kind of thing possessed`).
- Q99: "may a discretionary prohibition order be imposed on me for life or for any shorter duration" restates the name of `s 110(2.1) the order may be imposed for life or for any shorter duration`; the "if violence was used" gate is the function's inputs.
- Q100: "give reasons" for the text's "include in the record a statement of the court's reasons" (s 110(3)); the function is named for the record, the title for the giving: wording, not a different limb.
- Q108: "the peace officer who searched" is the text's "a peace officer who executes a warrant ... or who conducts a search without a warrant"; the function takes both facts as inputs.
- Q105, 112, 114, 116, 119, 121: "the order made against me" restates the text's own premise ("If an order is made under subsection ..."), which each function takes as its first input (`an order has been made under subsection (3)`, `an order is made under subsection (1)`, `an order is made under subsection 110.1(3)` and the like) and which a person answers; the title names the order the section is about and does not make the function's answer depend on anything else. **Borderline, and a judgment call:** it has the shape of the Q97 retitle (a premise in the title that a case can negate), and was left because Q97's title said "because it finds it desirable", a causal premise, while these name the referent. A lawyer may prefer to retitle the group.
- Q106, 107: "the things I am forbidden to possess" is the text's "any thing the possession of which is prohibited by the order" (s 110.1(5), (6)).

### Name-test sweep of 2026-11-12

Done 2026-11-16 on every function of the four layer-1 modules and the seat whose name contains "may", "permitted", "power", "entitled" or "authorized" / "authorised" (21 layer-1 names: 13 with "may", 8 with "unauthorized"; none with "permitted", "power", "entitled" or "authorised").

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 5 | 9 | 2 | 0 |

**Flipped to NOTHING (5), one fork line each in the fork register above and in the marginal readings (b): a function named for a power, with an "if" gate that fails.**
All five were written as `NOTHING` in the first pass under the brief's ruling, so this sweep changed no answer of them (answers changed by the sweep: 0; assertions restated for them: 0).
- `s 110(2.1) the order may be imposed for life or for any shorter duration` (fork F-110(2.1); "if, in the commission of the offence, violence was used")
- `s 110.1(1) any person may make an ex parte application to a provincial court judge for an order` (F-110.1(1); "if the person believes on reasonable grounds")
- `s 110.1(2) the provincial court judge may hold the hearing in private` (F-110.1(2); "if the judge considers that it is necessary")
- `s 110.1(5) the provincial court judge may issue a warrant to search and seize` (F-110.1(5); "If a provincial court judge is satisfied")
- `s 110.1(6) the peace officer may search for and seize without a warrant` (F-110.1(6); "If ... a peace officer is satisfied", "if the grounds ... exist")
The coverage rows of these five say `fork (F-..)`.

**Kept JUST FALSE (9), because they are not named for a grant or a power or the text closes the gate:**
- Offences whose names contain "unauthorized" (8): `s 91(1) the person commits an offence of unauthorized possession of a firearm`, `s 91(2) ... of unauthorized possession of a prohibited weapon or restricted weapon`, `s 92(1) ... knowing its possession is unauthorized`, `s 92(2) ... knowing its possession is unauthorized`, `s 93(1) ... at an unauthorized place`, `s 94(1) ... of unauthorized possession in a motor vehicle`, `s 103(1) ... knowing it is unauthorized`, `s 104(1) ... of unauthorized importing or exporting`. They are bars, not grants (limit 2): an unmet element answers JUST FALSE (fork F-OF) and "without being the holder of" with a licence held answers NOTHING.
- The provision's own question (1): `s 109(1)(a) the offence is one in which violence was used and for which the person may be sentenced to imprisonment for ten years or more` ("may be sentenced" states a maximum term, not a power).
- Gates closed by the text ("only if", "only where", "may not ... unless"): none among the "may" functions of this part.

**Listed, "may" with a where/when/upon-kind gate (2), in the fork register only (assumed, not ruled):**
- `s 110.2(1) a provincial court judge may make an order prohibiting access to, and the disclosure of, information` (F-110.2(1))
- `s 110.3(1) a provincial court judge may make an order to delete identifying information` (F-110.3(1))
Each has an "on application ... or on the judge's own motion" gate together with two "if" gates (which answer NOTHING).
The "on application" gate alone failing answers JUST FALSE (rulings (b) and (c) of 2026-11-05, which the instruction of 2026-11-12 leaves as they stand for these gates); the first pass had answered NOTHING for that case, so this is the only answer the sweep changed (two functions, one case each).
Assertions restated in place: 2 in `ccc4-tests-s109-110-3.l4` (one for each function, `-- RECONCILED 2026-11-12: was ... NOTHING`), and 2 in `ccc4-cases-seat.l4` (the questions about s 110.2(1) and s 110.3(1)); four assertions were added to `ccc4-tests-s109-110-3.l4` (333 to 337 satisfied), two for each function, to fix the order in which the gates are read (the first that fails, in the text's order, decides).

**Listed, "entitled" (0):** no function or type of this part is named with "entitled".

**Named with a word of the list but never answering JUST FALSE for a failed gate (5), not in a column:**
- `s 110(2) the latest day on which the order may end` (returns a date)
- `s 110.2(1) the information is within the order that may be made` (a classification of information; answers JUST TRUE or NOTHING)
- `s 110.2(5) an application to revoke the order or vary its terms and conditions may be made to the provincial court judge` and `s 110.3(4) ...` (a permission; no "if" gate in the text: the function answers JUST TRUE when an order was made and the application is made to the judge who made it or another provincial court judge, and NOTHING otherwise, kind "limited by its own wording", so there is no JUST FALSE to flip)
- `s 110.3(2) the order may be for the period, whether definite or indefinite` (limited by a "that the provincial court judge considers necessary" clause, not by an "if" gate: NOTHING under the guide's sentence on a grant limited in its own wording, listed under marginal readings (b))

**"It is lawful ..." functions (outside the sweep): scoped 0; unscoped and retitled 0.** No function of this part has "lawful" in its name; "lawful excuse" and "may lawfully possess" occur only in input names.

The seat questions whose names contain these words (12 with "may": Q88, Q98, Q99, Q101, Q102, Q106, Q107, Q112, Q115, Q116, Q118, Q120; 5 with "unauthorized": Q39, Q40, Q43, Q70, Q72) call the layer-1 function of that name; they are not additional functions, and none was added or changed by the sweep except Q112 and Q116, whose assertions were restated with the two functions above. The one place the seat turns a person's "no" into JUST FALSE is `ccc4 seat: yes, no or not known`, marked "an input value".

## What check.sh prints (ccc4)

Run as `env -u JL4_LIBRARY_PATH L4=<scratchpad>/bin/l4-main-110 L4_MAIN=<scratchpad>/bin/l4-main-109 ./check.sh` in this folder (`l4-main-110` is 1.6.110, `l4-main-109` is 1.6.109), after the last edit of any `.l4` file (2026-11-16).
The script printed the lines below and returned status 0 (read by the shell that ran it; the script does not print its own status).

Baseline (before the edits of this resume; 12 modules, no `ccc4-cases-seat.l4` yet): `TOTAL (12 modules) 0 1372 0 0 | 0 1372 0 0`.
After: `TOTAL (14 modules) 6 2036 6 0 | 6 2036 6 0`.
The 664 more satisfied assertions are the 660 of `ccc4-cases-seat.l4` and 4 added to `ccc4-tests-s109-110-3.l4` (333 to 337); the 6 errors and 6 failed are the six assertions of `ccc4-cases-seat-expected-red.l4`, which are meant to fail (`check.sh` `expected_failed`: 6), on both builds, and that is the only module with errors or failures.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc4-cases-seat-expected-red.l4                6         0       6        0         6 |      6         0       6        0  same
ccc4-cases-seat.l4                             0       660       0        0         0 |      0       660       0        0  same
ccc4-s109-110-3-prohibition-orders.l4          0         0       0        0         0 |      0         0       0        0  same
ccc4-s84-definitions.l4                        0         0       0        0         0 |      0         0       0        0  same
ccc4-s85-98-use-possession.l4                  0         0       0        0         0 |      0         0       0        0  same
ccc4-s99-108-trafficking-and-others.l4         0         0       0        0         0 |      0         0       0        0  same
ccc4-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
ccc4-tests-s109-110-3.l4                       0       337       0        0         0 |      0       337       0        0  same
ccc4-tests-s84.l4                              0       374       0        0         0 |      0       374       0        0  same
ccc4-tests-s85-98.l4                           0       332       0        0         0 |      0       332       0        0  same
ccc4-tests-s99-108.l4                          0       333       0        0         0 |      0       333       0        0  same
TOTAL (14 modules)                             6      2036       6        0           |      6      2036       6        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Other checks run on the same final files:
- `python3 -I srcrefs.py check --refs <raw text> ccc4-*.l4` and the same with `--strict`: `srcrefs check: 655 src: lines, 193 runs, 256 locators, 0 problems` in both modes.
- `work/lint-kinds.py`: every `JUST FALSE` carries a FALSE-kind comment whose quoted words are found in the raw text, and every `NOTHING` a NOTHING-kind comment with one of the six reasons: 262 result branches (110 JUST FALSE, 144 NOTHING, 6 passing an answer on, 2 input values of the seat), 219 quotations checked, 0 problems.
- `python3 -I work/cmp-traces.py ccc4-tests-s99-108.l4 ccc4-tests-s109-110-3.l4`: `traces 1.6.110 = 7, 1.6.109 = 7 ... identical: True` and `traces 1.6.110 = 22, 1.6.109 = 22 ... identical: True`; `check.sh` counts assertions and does not compare `#TRACE` outcomes, so they were compared separately.
- Positive control (2026-11-16): in a copy of the folder, one assertion of `ccc4-cases-seat.l4` (line 51) had `EQUALS JUST TRUE` flipped to `EQUALS JUST FALSE`; `l4 run` printed `eval/assertion-failed` at error severity and the count of satisfied lines fell from 1320 to 1318, and it still exited 0, which is why `check.sh` reads the output and not the exit code; the copy was deleted.
- Audit counts: `work/units.py` prints `# units: 334; non-blank lines: 468; covered: 468; missing: []` for lines 1904-2381; the coverage table has 334 rows after (no coverage table existed before this file was written: rows before 0).
