# NOTES: the keel of the Securities and Futures Act 2001 (Singapore), Part 1 (ss 1, 2, 3, 4, 4A, 4B)

Every sentence below that states a count was produced by a script run on the files in this folder (`work/gen/verify.py`, `work/gen/docs_notes.py`; the scratch generators are not part of the deposit), or is marked as an observation of one run.

## Edition encoded

The Securities and Futures Act 2001, 2020 Revised Edition, in the Singapore Statutes Online (SSO) informal consolidation "version in force from 29/6/2026 to 20/10/2026", retrieved 2026-10-09 (`inputs/SOURCES.md` has its hashes), carrying the amendments its amendment marks show.
That file is a plain-text rendering of a PDF: it is **not the official text**, and nothing here is verified against the official text.
A later consolidation may exist and was not read; the encoding is of that text only.
Line numbers (`src:N`) are lines of that file as it is: lines 1 to 4224 are this keel's range (the front matter and arrangement of sections, lines 1 to 1667, are inert; the body starts at line 1668).
Amendment marks (`[4/2017]`, `[Act 12 of 2024 wef 30/08/2024]`) and page furniture are not quoted and are not rules.
The text is quoted only where it is encoded, mechanically (`srcrefs.py` checks every quote line and every `@ref` locator).
Nothing in this folder says or suggests that the Singapore Government or the Attorney-General's Chambers endorses, checks or is associated with this work.

## Coverage (keel)

One row per section, subsection, paragraph and defined term of lines 1 to 4224: 209 rows, of which 199 `encoded`, 3 `fork`, 7 `inert` and 0 `repealed or blank in this text`.
Check by script (`verify.py` (a)): all 3113 non-blank lines of `SFA2001.txt` 1 to 4224 fall in exactly one row, and all 209 rows are used; the `Lines` column gives each row's inclusive range (blank lines, page furniture and amendment marks inside a range belong to its row).
There is no `repealed or blank in this text` row: the body (line 1668 on) of this range shows no `[Repealed` or `[Deleted` marker (grep over lines 1668 to 4224 finds none); the many `[Repealed]` entries are in the arrangement of sections at the head, which is front matter.
A row names the L4 functions that encode it (all in the module shown; tests are in the module of the same name with `-tests`, or in `sfa-cases-seat-keel.l4`).

| Provision | Lines | Disposition | Module | L4 name(s) or reason |
| --- | --- | --- | --- | --- |
| s 2(1) "capital markets products" | src:1862-1867 | encoded | sfa-definitions-products | `s 2(1) "capital markets products" the product is capital markets products` |
| s 2(1) "securities" | src:3097-3124 | encoded | sfa-definitions-products | `s 2(1) "securities" the instrument is securities` |
| s 2(1) "securities-based derivatives contract" | src:3125-3131 | encoded | sfa-definitions-products | `s 2(1) "securities-based derivatives contract" the contract is a securities-based derivatives contract` |
| s 2(1) "specified products" | src:3138-3141 | encoded | sfa-definitions-products | `s 2(1) "specified products" the product is a specified product` |
| s 2(1) "specified securities-based derivatives contract" | src:3142-3145 | encoded | sfa-definitions-products | `s 2(1) "specified securities-based derivatives contract" the contract is a specified securities-based derivatives contract` |
| s 2(1) "spot contract" | src:3146-3153 | encoded | sfa-definitions-products | `s 2(1) "spot contract" the contract or arrangement is a spot contract` |
| s 2(1) "spot foreign exchange contract" | src:3154-3159 | encoded | sfa-definitions-products | `s 2(1) "spot foreign exchange contract" the contract is a spot foreign exchange contract` |
| s 2(1) "underlying thing" | src:3337-3400 | encoded | sfa-definitions-products | `s 2(1) "underlying thing" (a) the thing is an underlying thing in relation to a derivatives contract or a spot contract` and `s 2(1) "underlying thing" (b) ...` |
| s 2(1) "commodity" | src:2194-2222 | encoded | sfa-definitions-products | `s 2(1) "commodity" the thing is a commodity` |
| s 2(1) "financial instrument" | src:2545-2551 | encoded | sfa-definitions-products | `s 2(1) "financial instrument" the thing is a financial instrument` |
| s 2(1) "derivatives contract" | src:2354-2407 | encoded | sfa-definitions-products | `s 2(1) "derivatives contract" the contract or arrangement is a derivatives contract` |
| s 2(1) "exchange-traded derivatives contract" | src:2423-2457 | encoded | sfa-definitions-products | `s 2(1) "exchange-traded derivatives contract" the derivatives contract is an exchange-traded derivatives contract` |
| s 2(1) "futures contract" | src:2611-2636 | encoded | sfa-definitions-products | `s 2(1) "futures contract" the contract is a futures contract` |
| s 2(1) "debenture" | src:2312-2347 | encoded | sfa-definitions-products | `s 2(1) "debenture" the instrument is a debenture` |
| s 2(1) "share" | src:3135-3137 | encoded | sfa-definitions-products | `s 2(1) "share" the interest is a share` |
| s 2(1) "voting share" | src:3460-3462 | encoded | sfa-definitions-products | `s 2(1) "voting share" the share is a voting share` |
| s 2(1) "derivative" | src:2351-2353 | encoded | sfa-definitions-products | `s 2(1) "derivative" the thing is a derivative of a unit in a business trust` |
| s 2(1) "treasury share" | src:3305-3313 | encoded | sfa-definitions-products | `s 2(1) "treasury share" (a) the share of a company is a treasury share`, `s 2(1) "treasury share" (b) the share of a corporation other than a company is a treasury share` |
| s 2(1) "collective investment scheme" | src:1979-2193 | encoded | sfa-definitions-schemes | `s 2(1) "collective investment scheme" (a) the arrangement has the characteristics in paragraph (a)`, `s 2(1) "collective investment scheme" the arrangement is a collective investment scheme` |
| s 2(1) "closed-end fund" | src:1897-1974 | encoded | sfa-definitions-schemes | `s 2(1) "closed-end fund" the arrangement is a closed-end fund`, `s 2(1) "closed-end fund" the day 1 July 2013` |
| s 2(1) "Code on Collective Investment Schemes" | src:1975-1978 | encoded | sfa-definitions-schemes | `s 2(1) "Code on Collective Investment Schemes" the document is the Code on Collective Investment Schemes` |
| s 2(1) "custodian" | src:2260-2263 | encoded | sfa-definitions-schemes | `s 2(1) "custodian" the entity is a custodian of the scheme` |
| s 2(1) "manager" | src:2690-2694 | encoded | sfa-definitions-schemes | `s 2(1) "manager" the person is the manager of the collective investment scheme` |
| s 2(1) "participant" | src:2724-2751 | encoded | sfa-definitions-schemes | `s 2(1) "participant" the person is a participant` |
| s 2(1) "responsible person" | src:3047-3061 | encoded | sfa-definitions-schemes | `s 2(1) "responsible person" who is the responsible person of the scheme` |
| s 2(1) "real estate investment trust" | src:2881-2895 | encoded | sfa-definitions-schemes | `s 2(1) "real estate investment trust" the scheme is a real estate investment trust` |
| s 2(1) "real estate investment trust management" | src:2896-2898 | encoded | sfa-definitions-schemes | `s 2(1) "real estate investment trust management" the activity is real estate investment trust management` |
| s 2(1) "unit" | src:3401-3412 | encoded | sfa-definitions-schemes | `s 2(1) "unit" (a) the right or interest is a unit in a collective investment scheme`, `s 2(1) "unit" (b) the thing is a unit in a business trust` |
| s 2(1) "unitholder" | src:3413-3420 | encoded | sfa-definitions-schemes | `s 2(1) "unitholder" (a) the person is a unitholder of a collective investment scheme`, `s 2(1) "unitholder" (b) the person is a unitholder of a business trust` |
| s 2(1) "voting unit" | src:3463-3528 | encoded | sfa-definitions-schemes | `s 2(1) "voting unit" (a) the unit is a voting unit in a business trust`, `s 2(1) "voting unit" (b) the unit is a voting unit in a collective investment scheme`, `s 2(1) "voting unit" the unit carries a vote in some circumstance the definition does not list` |
| s 2(1) "substantial unitholder" | src:3166-3181 | encoded | sfa-definitions-schemes | `s 2(1) "substantial unitholder" (a) the participant is a substantial unitholder of a collective investment scheme`, `s 2(1) "substantial unitholder" (b) the person is a substantial unitholder of a business trust` |
| s 2(1) "business trust" | src:1856-1861 | encoded | sfa-definitions-schemes | `s 2(1) "business trust" the trust is a business trust` |
| s 2(1) "registered business trust" | src:2915-2920 | encoded | sfa-definitions-schemes | `s 2(1) "registered business trust" the trust is a registered business trust` |
| s 2(1) "recognised business trust" | src:2899-2901 | encoded | sfa-definitions-schemes | `s 2(1) "recognised business trust" the trust is a recognised business trust` |
| s 2(1) "trustee-manager" | src:3314-3336 | encoded | sfa-definitions-schemes | `s 2(1) "trustee-manager" the person is the trustee-manager of the business trust` |
| s 2(1) "VCC" | src:3457-3459 | encoded | sfa-definitions-schemes | `s 2(1) "VCC" the company is a VCC` |
| s 2(1) "sub-fund" | src:3160-3162 | encoded | sfa-definitions-schemes | `s 2(1) "sub-fund" the arrangement is a sub-fund` |
| s 2(1) "advocate and solicitor" | src:1758-1761 | encoded | sfa-definitions-persons | `s 2(1) "advocate and solicitor" the person is an advocate and solicitor` |
| s 2(1) "auditor" | src:1782-1809 | encoded | sfa-definitions-persons | `s 2(1) "auditor" the person is an auditor` |
| s 2(1) "chairperson" | src:1872-1873 | encoded | sfa-definitions-persons | `s 2(1) "chairperson" the person is a chairperson` |
| s 2(1) "chief executive officer" | src:1874-1890 | encoded | sfa-definitions-persons | `s 2(1) "chief executive officer" the person is a chief executive officer of the relevant person` |
| s 2(1) "executive officer" | src:2458-2473 | encoded | sfa-definitions-persons | `s 2(1) "executive officer" the person is an executive officer of the relevant person` |
| s 2(1) "company" | src:2223-2225 | encoded | sfa-definitions-persons | `s 2(1) "company" the body is a company` |
| s 2(1) "corporation" | src:2257-2259 | encoded | sfa-definitions-persons | `s 2(1) "corporation" the body is a corporation` |
| s 2(1) "director" | src:2416-2418 | encoded | sfa-definitions-persons | `s 2(1) "director" the person is a director` |
| s 2(1) "officer" | src:2711-2713 | encoded | sfa-definitions-persons | `s 2(1) "officer" the person is an officer` |
| s 2(1) "financial year" | src:2552-2554 | encoded | sfa-definitions-persons | `s 2(1) "financial year" the period is a financial year` |
| s 2(1) "foreign company" | src:2558-2560 | encoded | sfa-definitions-persons | `s 2(1) "foreign company" the body is a foreign company` |
| s 2(1) "holding company" | src:2637-2639 | encoded | sfa-definitions-persons | `s 2(1) "holding company" the corporation is a holding company` |
| s 2(1) "public company" | src:2859-2861 | encoded | sfa-definitions-persons | `s 2(1) "public company" the body is a public company` |
| s 2(1) "related corporation" | src:2974-2976 | encoded | sfa-definitions-persons | `s 2(1) "related corporation" the corporation is a related corporation` |
| s 2(1) "subsidiary" | src:3163-3165 | encoded | sfa-definitions-persons | `s 2(1) "subsidiary" the corporation is a subsidiary` |
| s 2(1) "office copy" | src:2708-2710 | encoded | sfa-definitions-persons | `s 2(1) "office copy" the document is an office copy` |
| s 2(1) "firm" | src:2555-2557 | encoded | sfa-definitions-persons | `s 2(1) "firm" the body is a firm` |
| s 2(1) "limited liability partnership" | src:2651-2653 | encoded | sfa-definitions-persons | `s 2(1) "limited liability partnership" the body is a limited liability partnership` |
| s 2(1) "newspaper" | src:2705-2707 | encoded | sfa-definitions-persons | `s 2(1) "newspaper" the publication is a newspaper` |
| s 2(1) "partner" | src:2752-2755 | encoded | sfa-definitions-persons | `s 2(1) "partner" the person is a partner of the limited liability partnership`, `s 2(1) "manager" (limited liability partnership) the person is a manager of the limited liability partnership` |
| s 2(1) "advising on corporate finance" | src:1755-1757 | encoded | sfa-definitions-persons | `s 2(1) "advising on corporate finance" the activity is advising on corporate finance` |
| s 2(1) "dealing in capital markets products" | src:2309-2311 | encoded | sfa-definitions-persons | `s 2(1) "dealing in capital markets products" the activity is dealing in capital markets products` |
| s 2(1) "fund management" | src:2608-2610 | encoded | sfa-definitions-persons | `s 2(1) "fund management" the activity is fund management` |
| s 2(1) "leveraged foreign exchange trading" | src:2640-2642 | encoded | sfa-definitions-persons | `s 2(1) "leveraged foreign exchange trading" the activity is leveraged foreign exchange trading` |
| s 2(1) "product financing" | src:2825-2827 | encoded | sfa-definitions-persons | `s 2(1) "product financing" the activity is product financing` |
| s 2(1) "providing credit rating services" | src:2828-2830 | encoded | sfa-definitions-persons | `s 2(1) "providing credit rating services" the activity is providing credit rating services` |
| s 2(1) "providing custodial services" | src:2831-2833 | encoded | sfa-definitions-persons | `s 2(1) "providing custodial services" the activity is providing custodial services` |
| s 2(1) "regulated activity" | src:2921-2923 | encoded | sfa-definitions-persons | `s 2(1) "regulated activity" the activity is a regulated activity` |
| s 2(1) "entity" | src:2419-2422 | encoded | sfa-definitions-persons | `s 2(1) "entity" the body is an entity` |
| s 2(1) "connected person" | src:2226-2256 | encoded | sfa-definitions-persons | `s 2(1) "connected person" (a) the person is connected to the individual`, `s 2(1) "connected person" (b) the body is connected to the firm, limited liability partnership or corporation` |
| s 2(1) "customer" | src:2264-2308 | encoded | sfa-definitions-persons | `s 2(1) "customer" the person is a customer` |
| s 2(1) "franchise" | src:2561-2601 | encoded | sfa-definitions-persons | `s 2(1) "franchise" the agreement or arrangement is a franchise` |
| s 2(1) "principal" | src:2816-2824 | encoded | sfa-definitions-persons | `s 2(1) "principal" the person is the principal of the representative` |
| s 2(1) "representative" | src:2977-3046 | encoded | sfa-definitions-persons | `s 2(1) "representative" the person is a representative of the principal` |
| s 2(1) "appointed representative" | src:1762-1770 | encoded | sfa-definitions-persons | `s 2(1) "appointed representative" (a) the person is an appointed representative in respect of a type of regulated activity`, `s 2(1) "appointed representative" (b) the person is an appointed representative` |
| s 2(1) "provisional representative" | src:2853-2858 | encoded | sfa-definitions-persons | `s 2(1) "provisional representative" (a) the person is a provisional representative in respect of a type of regulated activity`, `s 2(1) "provisional representative" (b) the person is a provisional representative` |
| s 2(1) "temporary representative" | src:3283-3288 | encoded | sfa-definitions-persons | `s 2(1) "temporary representative" (a) the person is a temporary representative in respect of a type of regulated activity`, `s 2(1) "temporary representative" (b) the person is a temporary representative` |
| s 2(1) "public register of representatives" | src:2862-2864 | encoded | sfa-definitions-persons | `s 2(1) "public register of representatives" the register is the public register of representatives` |
| s 2(1) "regulated financial institution" | src:2924-2930 | encoded | sfa-definitions-persons | `s 2(1) "regulated financial institution" the person is a regulated financial institution` |
| s 2(1) "regulatory authority" | src:2931-2939 | encoded | sfa-definitions-persons | `s 2(1) "regulatory authority" the authority is a regulatory authority of the foreign country or jurisdiction` |
| s 2(1) "capital markets services licence" | src:1868-1871 | encoded | sfa-definitions-persons | `s 2(1) "capital markets services licence" the licence is a capital markets services licence` |
| s 2(1) "exempt person" | src:2482-2487 | encoded | sfa-definitions-persons | `s 2(1) "exempt person" the person is an exempt person` |
| s 2(1) "approved clearing house" | src:1771-1774 | encoded | sfa-definitions-markets | `s 2(1) "approved clearing house" the corporation is approved clearing house` |
| s 2(1) "approved exchange" | src:1775-1777 | encoded | sfa-definitions-markets | `s 2(1) "approved exchange" the corporation is approved exchange` |
| s 2(1) "approved holding company" | src:1778-1781 | encoded | sfa-definitions-markets | `s 2(1) "approved holding company" the corporation is approved holding company` |
| s 2(1) "recognised clearing house" | src:2902-2905 | encoded | sfa-definitions-markets | `s 2(1) "recognised clearing house" the corporation is recognised clearing house` |
| s 2(1) "recognised market operator" | src:2906-2909 | encoded | sfa-definitions-markets | `s 2(1) "recognised market operator" the corporation is recognised market operator` |
| s 2(1) "licensed trade repository" | src:2647-2650 | encoded | sfa-definitions-markets | `s 2(1) "licensed trade repository" the corporation is a licensed trade repository` |
| s 2(1) "licensed foreign trade repository" | src:2643-2646 | encoded | sfa-definitions-markets | `s 2(1) "licensed foreign trade repository" the corporation is a licensed foreign trade repository` |
| s 2(1) "Authority" | src:1821-1824 | encoded | sfa-definitions-markets | `s 2(1) "Authority" the body is the Authority` |
| s 2(1) "Securities Industry Council" | src:3132-3134 | encoded | sfa-definitions-markets | `s 2(1) "Securities Industry Council" the body is the Securities Industry Council` |
| s 2(1) "Take-over Code" | src:3182-3185 | encoded | sfa-definitions-markets | `s 2(1) "Take-over Code" the document is the Take-over Code` |
| s 2(1) "organised market" | src:2714-2715 | encoded | sfa-definitions-markets | `s 2(1) "organised market" the market is an organised market` |
| s 2(1) "clearing facility" | src:1891-1893 | encoded | sfa-definitions-markets | `s 2(1) "clearing facility" the facility is a clearing facility` |
| s 2(1) "clearing or settlement" | src:1894-1896 | encoded | sfa-definitions-markets | `s 2(1) "clearing or settlement" the activity is clearing or settlement` |
| s 2(1) "business rules" | src:1831-1855 | encoded | sfa-definitions-markets | `s 2(1) "business rules" the statements are the business rules of the body` |
| s 2(1) "listing rules" | src:2654-2689 | encoded | sfa-definitions-markets | `s 2(1) "listing rules" the rules are the listing rules of the corporation` |
| s 2(1) "overseas exchange" | src:2716-2723 | encoded | sfa-definitions-markets | `s 2(1) "overseas exchange" the person is an overseas exchange` |
| s 2(1) "quote" | src:2865-2880 | encoded | sfa-definitions-markets | `s 2(1) "quote" the display or provision of information is to quote` |
| s 2(1) "member" | src:2695-2704 | encoded | sfa-definitions-markets | `s 2(1) "member" the person is a member of the body` |
| s 2(1) "user" | src:3421-3448 | encoded | sfa-definitions-markets | `s 2(1) "user" the person is a user` |
| s 2(1) "transaction information" | src:3289-3304 | encoded | sfa-definitions-markets | `s 2(1) "transaction information" the information is transaction information` |
| s 2(1) "user information" | src:3449-3456 | encoded | sfa-definitions-markets | `s 2(1) "user information" the information is user information` |
| s 2(1) "book" | src:1825-1830 | encoded | sfa-definitions-markets | `s 2(1) "book" the thing is a book` |
| s 2(1) "record" | src:2910-2914 | encoded | sfa-definitions-markets | `s 2(1) "record" the information is a record` |
| s 2(1) "defalcation" | src:2348-2350 | encoded | sfa-definitions-markets | `s 2(1) "defalcation" the act is a defalcation` |
| s 2(1) "FSMA prohibition order" | src:2602-2607 | encoded | sfa-definitions-markets | `s 2(1) "FSMA prohibition order" the order is an FSMA prohibition order` |
| s 2(1) "related Acts prohibition order" | src:2940-2973 | encoded | sfa-definitions-markets | `s 2(1) "related Acts prohibition order" the order is a related Acts prohibition order` |
| s 2(1) "section 101A prohibition order" | src:3062-3078 | encoded | sfa-definitions-markets | `s 2(1) "section 101A prohibition order" the order is a section 101A prohibition order` |
| s 2(1) "section 123ZZC prohibition order" | src:3079-3096 | encoded | sfa-definitions-markets | `s 2(1) "section 123ZZC prohibition order" the order is a section 123ZZC prohibition order` |
| s 2(1) "prescribed written law" | src:2756-2815 | encoded | sfa-definitions-markets | `s 2(1) "prescribed written law" the written law is a prescribed written law` |
| s 2(1) "take-over offer" | src:3186-3282 | encoded | sfa-definitions-markets | `s 2(1) "take-over offer" (a) the offer is a take-over offer by acquisition`, `s 2(1) "take-over offer" (b) the proposal is a take-over offer by compromise or arrangement`, `s 2(1) "take-over offer" the proposal is a take-over offer` |
| s 2(1) "administering a designated benchmark" | src:1680-1718 | encoded | sfa-definitions-benchmarks | `s 2(1) "administering a designated benchmark" the act is administering a designated benchmark` |
| s 2(1) "administering a financial benchmark" | src:1719-1754 | encoded | sfa-definitions-benchmarks | `s 2(1) "administering a financial benchmark" the act is administering a financial benchmark` |
| s 2(1) "authorised benchmark administrator" | src:1810-1816 | encoded | sfa-definitions-benchmarks | `s 2(1) "authorised benchmark administrator" the corporation is an authorised benchmark administrator` |
| s 2(1) "authorised benchmark submitter" | src:1817-1820 | encoded | sfa-definitions-benchmarks | `s 2(1) "authorised benchmark submitter" the corporation is an authorised benchmark submitter` |
| s 2(1) "designated benchmark submitter" | src:2412-2415 | encoded | sfa-definitions-benchmarks | `s 2(1) "designated benchmark submitter" the corporation is a designated benchmark submitter` |
| s 2(1) "exempt benchmark administrator" | src:2474-2477 | encoded | sfa-definitions-benchmarks | `s 2(1) "exempt benchmark administrator" the person is an exempt benchmark administrator` |
| s 2(1) "exempt benchmark submitter" | src:2478-2481 | encoded | sfa-definitions-benchmarks | `s 2(1) "exempt benchmark submitter" the person is an exempt benchmark submitter` |
| s 2(1) "financial benchmark" | src:2488-2544 | encoded | sfa-definitions-benchmarks | `s 2(1) "financial benchmark" the price, rate, index or value is a financial benchmark` |
| s 2(1) "designated benchmark" | src:2408-2411 | encoded | sfa-definitions-benchmarks | `s 2(1) "designated benchmark" the benchmark is a designated benchmark` |
| s 2(1) "providing information in relation to a designated benchmark" | src:2834-2843 | encoded | sfa-definitions-benchmarks | `s 2(1) "providing information in relation to a designated benchmark" the act is providing information in relation to a designated benchmark` |
| s 2(1) "providing information in relation to a financial benchmark" | src:2844-2852 | encoded | sfa-definitions-benchmarks | `s 2(1) "providing information in relation to a financial benchmark" the act is providing information in relation to a financial benchmark` |
| front matter and arrangement of sections | src:1-1667 | inert | sfa-definitions-rest | reason 1 (not operative): the cover page, the arrangement of sections and the like; the arrangement is garbled in this rendering and out of step with the body (it prints some titles against the wrong numbers), so section numbers and headings are read from the body from line 1668 |
| Part 1 heading and the heading "Short title" | src:1668-1671 | inert | sfa-definitions-rest | reason 1 (not operative): "PART 1 PRELIMINARY" and the marginal heading "Short title" |
| s 1 | src:1672-1675 | inert | sfa-definitions-rest | reason 2 (machinery): s 1 gives the short title, "This Act is the Securities and Futures Act 2001" |
| s 3 marginal heading | src:3660-3661 | inert | sfa-definitions-rest | reason 1 (not operative): the marginal heading "Associated person" |
| s 4 marginal heading | src:3780-3782 | inert | sfa-definitions-rest | reason 1 (not operative): the marginal heading of s 4 ("Interest in securities, securities-based derivatives contracts or units in collective investment scheme") |
| s 4A marginal heading | src:3998-3999 | inert | sfa-definitions-rest | reason 1 (not operative): the marginal heading "Specific classes of investors" |
| s 4B marginal heading | src:4212-4213 | inert | sfa-definitions-rest | reason 1 (not operative): the marginal heading "Application" |
| s 2(1) (chapeau) | src:1676-1679 | encoded | sfa-definitions-rest | `s 2(1) the definitions apply unless the context otherwise requires`, `s 2(1) the answer under a definition, allowing for the context` |
| s 2(2) | src:3529-3618 | fork | sfa-definitions-rest | `s 2(2) the matter is within the affairs of a corporation` (fork F1 in NOTES.md) |
| s 2(3) | src:3619-3624 | encoded | sfa-definitions-rest | `s 2(3) the change of the corporation's name does not affect its identity or the application of the law to it` |
| s 2(4) | src:3625-3639 | encoded | sfa-definitions-rest | `s 2(4) the person has a substantial shareholding in the corporation` |
| s 2(5) | src:3640-3653 | encoded | sfa-definitions-rest | `s 2(5) the person has a substantial shareholding in the corporation whose share capital has 2 or more classes` |
| s 2(6) | src:3654-3659 | encoded | sfa-definitions-rest | `s 2(6) the person is a substantial shareholder in the corporation` |
| s 3(1) (chapeau) | src:3662-3664 | encoded | sfa-associates | `s 3(1) the person is associated with the other person` |
| s 3(1)(a) | src:3665-3672 | encoded | sfa-associates | `s 3(1)(a) the person is a director, secretary or related corporation of the corporation` |
| s 3(1)(b) | src:3673-3703 | encoded | sfa-associates | `s 3(1)(b) the person has an agreement about voting power with the other person` |
| s 3(1)(c) | src:3704-3707 | encoded | sfa-associates | `s 3(1)(c) the person is acting in concert with the other person` |
| s 3(2) | src:3743-3750 | encoded | sfa-associates | `s 3(2) the director is considered associated with the other person in the proceedings` |
| s 3(1)(d) | src:3708-3722 | encoded | sfa-associates | `s 3(1)(d) the person is a fellow director or a trustee connected with the other person` |
| s 3(1)(e) | src:3723-3727 | encoded | sfa-associates | `s 3(1)(e) subsidiary legislation regards the person as associated with the other person` |
| s 3(1)(f) | src:3728-3736 | encoded | sfa-associates | `s 3(1)(f) the person is associated with the other person in another way` |
| s 3(1)(g) | src:3737-3742 | encoded | sfa-associates | `s 3(1)(g) the other person has acted with a view to becoming associated with the person` |
| s 3(3)(a) | src:3755-3759 | encoded | sfa-associates | `s 3(3)(a) the circumstance is that one of the persons provides advice to, or acts for, the other in a professional or business capacity` |
| s 3(3)(b) | src:3760-3764 | encoded | sfa-associates | `s 3(3)(b) the circumstance is that a customer gives specific instructions to a dealer to acquire shares` |
| s 3(3)(c) | src:3765-3769 | encoded | sfa-associates | `s 3(3)(c) the circumstance is that one of the persons has sent or proposes to send the other a take-over offer` |
| s 3(3)(d) | src:3770-3779 | encoded | sfa-associates | `s 3(3)(d) the circumstance is that one of the persons has appointed the other as proxy or representative` |
| s 3(3) (chapeau) | src:3751-3754 | encoded | sfa-associates | `s 3(3) the person is taken to be associated by virtue of subsection (1)(b), (c), (e) or (f)` |
| s 4(1) | src:3783-3792 | encoded | sfa-interests | `s 4(1) the person has authority over the disposal of the thing` |
| s 4(2) | src:3793-3801 | encoded | sfa-interests | `s 4(2) it is immaterial that the authority is subject to restraint or restriction` |
| s 4(3) | src:3802-3811 | encoded | sfa-interests | `s 4(3) the person is treated as having an interest through a trust` |
| s 4(4) | src:3812-3832 | encoded | sfa-interests | `s 4(4) the person is treated as having an interest through a corporation the person directs or controls` |
| s 4(5) | src:3833-3848 | encoded | sfa-interests | `s 4(5) the person is treated as having an interest through a corporation in which the person and associates hold 20% of the votes` |
| s 4(6) | src:3849-3869 | encoded | sfa-interests | `s 4(6) the person is an associate of the other person for the purposes of subsection (5)` |
| s 4(7) (chapeau) | src:3870-3877 | encoded | sfa-interests | `s 4(7) the person is treated as having an interest in one of the circumstances` |
| s 4(7)(a) | src:3878-3881 | encoded | sfa-interests | `s 4(7)(a) the person has entered into a contract to purchase the thing` |
| s 4(7)(b) | src:3882-3889 | encoded | sfa-interests | `s 4(7)(b) the person has a right to have the thing transferred to the person or to the person's order` |
| s 4(7)(c) | src:3890-3902 | encoded | sfa-interests | `s 4(7)(c) the person has the right to acquire the thing, or an interest in it, under an option` |
| s 4(7)(d) | src:3903-3919 | encoded | sfa-interests | `s 4(7)(d) the person is entitled to exercise or control the exercise of a right attached to the thing` |
| s 4(8) | src:3920-3931 | encoded | sfa-interests | `s 4(8) the thing is held jointly by the person with another person` |
| s 4(9) | src:3932-3939 | encoded | sfa-interests | `s 4(9) it is immaterial that the interest cannot be related to a particular thing` |
| s 4(10) (chapeau) | src:3940-3941 | encoded | sfa-interests | `s 4(10) the interest is to be disregarded` |
| s 4(10)(a) | src:3942-3948 | encoded | sfa-interests | `s 4(10)(a) the interest is that of a bare trustee` |
| s 4(10)(b) | src:3949-3959 | encoded | sfa-interests | `s 4(10)(b) the interest is that of a lender holding it only as security` |
| s 4(10)(c) | src:3960-3964 | encoded | sfa-interests | `s 4(10)(c) the interest is held by reason of holding a prescribed office` |
| s 4(10)(d) | src:3965-3968 | encoded | sfa-interests | `s 4(10)(d) the interest is a company's interest in its own securities bought under the Companies Act` |
| s 4(10)(e) | src:3969-3976 | encoded | sfa-interests | `s 4(10)(e) the interest is a prescribed interest` |
| s 4(10)(f) | src:3977-3983 | encoded | sfa-interests | `s 4(10)(f) for Part 7, the interest is in a cash-settled securities-based derivatives contract` |
| s 4(11) | src:3984-3997 | encoded | sfa-interests | `s 4(11) the interest is to be disregarded by reason only of its remoteness, how it arose, or restraint` |
| s 4A(1) (chapeau) | src:4000-4002 | encoded | sfa-investors | `s 4A(1) the person is in the class of investor` |
| s 4A(1)(a) (chapeau) | src:4003-4004 | encoded | sfa-investors | `s 4A(1)(a) the person is an accredited investor` |
| s 4A(1)(a)(i) (chapeau) | src:4005-4006 | encoded | sfa-investors | `s 4A(1)(a) the person is an accredited investor` |
| s 4A(1)(a)(i)(A) | src:4007-4012 | encoded | sfa-investors | `s 4A(1)(a)(i)(A) the first amount of net personal assets, in Singapore dollars`, `s 4A(1)(a)(i)(A) the individual's net personal assets exceed the amount` |
| s 4A(1)(a)(i)(B) | src:4013-4032 | encoded | sfa-investors | `s 4A(1)(a)(i)(B) the first amount of financial assets, in Singapore dollars`, `s 4A(1)(a)(i)(B) the individual's financial assets, net of related liabilities, exceed the amount` |
| s 4A(1)(a)(i)(C) | src:4033-4038 | encoded | sfa-investors | `s 4A(1)(a)(i)(C) the first amount of income, in Singapore dollars`, `s 4A(1)(a)(i)(C) the individual's income in the preceding 12 months is not less than the amount` |
| s 4A(1)(a)(ii) | src:4039-4054 | fork | sfa-investors | `s 4A(1)(a)(ii) the first amount of net assets, in Singapore dollars`, `s 4A(1)(a)(ii) the corporation's net assets exceed the amount` (fork F3 in NOTES.md) |
| s 4A(1)(a)(iii) | src:4055-4057 | encoded | sfa-investors | `s 4A(1)(a)(iii) the person is the trustee of a prescribed trust, when acting in that capacity` |
| s 4A(1)(a)(iv) | src:4058-4059 | encoded | sfa-investors | `s 4A(1)(a)(iv) the person is a person the Authority has prescribed as an accredited investor` |
| s 4A(1)(b) | src:4060-4073 | encoded | sfa-investors | `s 4A(1)(b) the person is an expert investor` |
| s 4A(1)(c) (chapeau) | src:4074-4075 | encoded | sfa-investors | `s 4A(1)(c) the person is an institutional investor` |
| s 4A(1)(c)(i) | src:4076-4077 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(ii) | src:4078-4080 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(iii) | src:4081-4099 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(iv) | src:4100-4108 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(v) | src:4109-4110 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(vi) | src:4111-4113 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(vii) | src:4114-4120 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(viii) | src:4121-4124 | encoded | sfa-investors | `s 4A(1)(c)(i) to (viii) the person is the Government, a government body or a central-government entity` |
| s 4A(1)(c)(ix) | src:4125-4126 | encoded | sfa-investors | `s 4A(1)(c)(ix) to (xiv) the person is a licensed financial institution` |
| s 4A(1)(c)(x) | src:4127-4129 | encoded | sfa-investors | `s 4A(1)(c)(ix) to (xiv) the person is a licensed financial institution` |
| s 4A(1)(c)(xi) | src:4130-4132 | encoded | sfa-investors | `s 4A(1)(c)(ix) to (xiv) the person is a licensed financial institution` |
| s 4A(1)(c)(xii) | src:4133-4136 | encoded | sfa-investors | `s 4A(1)(c)(ix) to (xiv) the person is a licensed financial institution` |
| s 4A(1)(c)(xiii) | src:4137-4139 | encoded | sfa-investors | `s 4A(1)(c)(ix) to (xiv) the person is a licensed financial institution` |
| s 4A(1)(c)(xiv) | src:4140-4141 | encoded | sfa-investors | `s 4A(1)(c)(ix) to (xiv) the person is a licensed financial institution` |
| s 4A(1)(c)(xv) | src:4142-4143 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xvi) | src:4144-4145 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xvii) | src:4146-4147 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xviii) | src:4148-4149 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xix) | src:4150-4151 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xx) | src:4152-4153 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xxi) | src:4154-4155 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xxii) | src:4156-4157 | encoded | sfa-investors | `s 4A(1)(c)(xv) to (xxii) the person is an approved or recognised market institution` |
| s 4A(1)(c)(xxiii) | src:4158-4176 | encoded | sfa-investors | `s 4A(1)(c)(xxiii) to (xxvii) the person is a foreign regulated entity, a pension fund or scheme, a bond dealer or a prescribed person` |
| s 4A(1)(c)(xxiv) | src:4177-4179 | encoded | sfa-investors | `s 4A(1)(c)(xxiii) to (xxvii) the person is a foreign regulated entity, a pension fund or scheme, a bond dealer or a prescribed person` |
| s 4A(1)(c)(xxv) | src:4180-4183 | encoded | sfa-investors | `s 4A(1)(c)(xxiii) to (xxvii) the person is a foreign regulated entity, a pension fund or scheme, a bond dealer or a prescribed person` |
| s 4A(1)(c)(xxvi) | src:4184-4186 | encoded | sfa-investors | `s 4A(1)(c)(xxiii) to (xxvii) the person is a foreign regulated entity, a pension fund or scheme, a bond dealer or a prescribed person` |
| s 4A(1)(c)(xxvii) | src:4187-4190 | encoded | sfa-investors | `s 4A(1)(c)(xxiii) to (xxvii) the person is a foreign regulated entity, a pension fund or scheme, a bond dealer or a prescribed person` |
| s 4A(1A) | src:4191-4207 | fork | sfa-investors | `s 4A(1A)(b)(ii) the most the primary residence counts for, in Singapore dollars`, `s 4A(1A) the value of the individual's primary residence counted in net personal assets` (fork F2 in NOTES.md) |
| s 4A(2) | src:4208-4211 | encoded | sfa-investors | `s 4A(2) the Authority has prescribed a modification of the definitions for the provision` |
| s 4B | src:4214-4224 | encoded | sfa-application | `s 4B this Act applies to the person in respect of the activities` |

## Fork register (keel)

Each entry: the provision, the function, the answer taken, the other reading and the text that licenses each.
F1 to F3 are `fork` rows of the coverage table; P1 to P10 are the counting conventions of `sfa-periods.l4`, which Part 1 does not settle (they are assumed, not ruled by a lawyer; the family takes them once so that the Acts agree).
Every fork is also marked `-- FORK F<n>` (F1 to F3) in the code, in the function that carries it.

**F1. s 2(2), "unless the contrary intention appears" (`s 2(2) the matter is within the affairs of a corporation`, sfa-definitions-rest.l4).**
Text: "Any reference in this Act to the affairs of a corporation, unless the contrary intention appears, is to be construed as including a reference to --" (src:3529-3531).
Answer taken: when a contrary intention appears the function answers `NOTHING` (the extended construction falls away; whether the matter is within the affairs of the corporation in its ordinary sense is left to the provision, which is not in this function's facts).
Other reading: `JUST FALSE`, taking "unless" as the text's no.
The two readings differ only for a caller who has said a contrary intention appears.

**F2. s 4A(1A)(b), the primary residence "is taken to be the lower of" two values (`s 4A(1A) the value of the individual's primary residence counted in net personal assets`, sfa-investors.l4).**
Text: "(a) is to be calculated by deducting any outstanding amounts in respect of any credit facility that is secured by the residence from the estimated fair market value of the residence; and (b) is taken to be the lower of the following: (i) the value calculated under paragraph (a); (ii) $1 million." (src:4195-4204).
Answer taken: the lower of the two, literally, so secured credit larger than the residence's value gives a negative figure that reduces net personal assets (tested: value $1,000,000, secured credit $1,500,000 gives minus $500,000).
Other reading: the figure is never below nought.
The earlier pass (inputs/NAIVE-EVIDENCE) also does not floor it.

**F3. s 4A(1)(a)(ii)(A) and (B), which corporations may use which balance sheet (`s 4A(1)(a)(ii) the corporation's net assets exceed the amount`, sfa-investors.l4).**
Text: "as determined by (A) the most recent audited balance sheet of the corporation; or (B) where the corporation is not required to prepare audited accounts regularly, a balance sheet of the corporation certified by the corporation as giving a true and fair view ..., which date must be within the preceding 12 months" (src:4042-4053).
Answer taken: (A) is open to any corporation that has an audited balance sheet; (B) only to one not required to prepare audited accounts regularly, and then only with a certified balance sheet dated within the preceding 12 months of the date asked.
Other reading: (A) is confined to a corporation that is required to prepare audited accounts regularly (because (B) is introduced with "where the corporation is not required to ..."), so a corporation not required to audit that nonetheless has an audited balance sheet is tested only under (B).
The two readings differ for a corporation that is not required to prepare audited accounts regularly, has an audited balance sheet showing more than the amount, and has no certified one: `JUST TRUE` here, `JUST FALSE` on the other reading.


**P1. the day of the event is not counted** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the last day of a period after` in sfa-periods.l4.
Answer taken: day 1 of "N days after X" is the day after X, so the last day is X plus N.
Other reading: the day of the event is day 1, so the last day is X plus N minus 1.

**P2.
"within N days after X" is a window that opens the day after X** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the date is within a period after`, `period: the date is not later than the end of a period after` in sfa-periods.l4.
Answer taken: an act on X itself is not "within" the window; "not later than" the last day includes the last day.
Other reading: an act on X itself is within the window.

**P3. a period of weeks** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the last day of a period after` (unit Weeks) in sfa-periods.l4.
Answer taken: a week is 7 days.
Other reading: a calendar week (Sunday to Saturday).

**P4. a period of months or years ends on the corresponding date of the last month** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the last day of a period after` (units Months, Years) in sfa-periods.l4.
Answer taken: where that month has no such date it ends on the month's last day (31 August plus 6 months is 28 February in a non-leap year); daydate's `add months` clamps this way.
Other reading: the period rolls over into the next month, or ends the day before the corresponding date.

**P5.
"not less than N days before X"** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the latest day for an act a period before`, `period: the date is at least a period before` in sfa-periods.l4.
Answer taken: the last day on which the act may be done is X minus N (X not counted, the day of the act counted).
Other reading: clear days (P7).

**P6.
"within N months before X"** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the date is within a period before` in sfa-periods.l4.
Answer taken: from the corresponding date N months earlier up to the day before X.
Other reading: the period includes X, or opens the day after the corresponding date.

**P7.
"N clear days"** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the latest day for an act at least a number of clear days before`, `period: the earliest day for an act after a number of clear days from` in sfa-periods.l4.
Answer taken: offered, never defaulted: both the day of the event and the day of the act are excluded.
Other reading: P1 and P5 (a clear-days reading is the alternative they stand against).

**P8. business days** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the date is a business day`, `period: the day reached counting business days`, `period: the last day of a number of business days after`, `period: the date is within a number of business days after` in sfa-periods.l4.
Answer taken: "business day" is not defined in this Act (finding 1), so days are counted from the day after the event, skipping weekends and the supplied public holidays.
Other reading: a business day is a day on which the Authority or an approved exchange is open (not coded).

**P10.
"N units beginning with D" and "N units ending with D"** (provision: none; Part 1 has no counting rule, see finding 1) function(s) `period: the last day of a period beginning with`, `period: the first day of a period ending with` in sfa-periods.l4.
Answer taken: D counts as day 1, so the period ends the day before the same date N units on (where stepping D forward clamped to a short month's last day under P4, the period ends on that clamped date); "ending with D" counts D as the last day.
Other reading: D is not counted (as P1).

P9 of the header of `sfa-periods.l4` is not a fork: a count that is not a whole non-negative number is not checked there (the caller supplies N from the Act's own words).
The text of this Act that counts days in its own words is outside this range: "within 2 days (excluding any Saturday, Sunday or public holiday) from the date of lodgment" (src:39267, 39317, 39409, in sfac's range); `period: the last day of a number of business days after` counts exactly that.

## Jural relations (keel)

Hohfeld's correlatives (a right is the other party's duty; a privilege is the other party's no-right; a power is the other party's liability; an immunity is the other party's disability).
Part 1 creates no duty, so there is no claim-right row.
Each rule is stated once, as a relation between two parties, from the side of the holder.


| Provision | Holds the right, privilege, power or immunity | Bears the correlative | Kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 4B | a person in respect of whom a transitional approval or transitional licence mentioned in section 66 of the Commodity Trading Act 1992 is in force | whoever would apply this Act to those activities (the Authority, a court, a counterparty) | immunity / disability | `s 4B this Act applies to the person in respect of the activities` |
| s 4A(2) | the Authority (power to prescribe modifications of the definitions for any specified provision) | persons whose class of investor changes for that provision (liability) | power / liability | `s 4A(2) the Authority has prescribed a modification of the definitions for the provision`; `s 4A(1) the person is in the class of investor` answers `NOTHING` when one is prescribed |
| s 4A(1)(a)(i)(A), (B), (C), (ii) "such other amount as the Authority may prescribe in place of the first amount" | the Authority (power to prescribe another amount) | individuals and corporations tested against the amount (liability) | power / liability | the inputs `the Authority has prescribed another amount in place of the first amount` and `the other amount the Authority has prescribed, in Singapore dollars` of `s 4A(1)(a)(i)(A)`, `(B)`, `(C)`, `s 4A(1)(a)(ii)` |
| s 4A(1)(a)(iii), (iv), (b)(ii), (iii), (c)(ii), (viii), (xxvi), (xxvii), (xxiii) "such other Act as may be prescribed" | the Authority, or the Minister by regulations under section 341 (power to prescribe a trust, person, statutory board, agency or Act) | the trustee, person, board or agency prescribed (liability) | power / liability | the prescribed-fact inputs of `s 4A(1)(a)(iii)`, `s 4A(1)(a)(iv)`, `s 4A(1)(b)`, `s 4A(1)(c)(i) to (viii)`, `s 4A(1)(c)(xxiii) to (xxvii)` |
| s 3(1)(e) | the Authority or Minister (power, by subsidiary legislation made under this Act, to treat a person as associated) | the person so treated (liability) | power / liability | `s 3(1)(e) subsidiary legislation regards the person as associated with the other person` |
| s 3(2) | a person alleged in proceedings to be associated as a fellow director | the person alleging the association (disability: cannot rely on the association without proving knowledge) | immunity / disability | `s 3(2) the director is considered associated with the other person in the proceedings` |
| s 3(3) | a person whose only link is advice or agency in a professional or business capacity, a customer's instruction, a take-over offer or an unpaid proxy appointment | whoever would treat that person as associated under s 3(1)(b), (c), (e) or (f) (disability) | immunity / disability | `s 3(3) the person is taken to be associated by virtue of subsection (1)(b), (c), (e) or (f)` and `s 3(3)(a)` to `(d)` |
| s 4(10) and (11) | a person whose interest is that of a bare trustee, a lender holding only as security, the holder of a prescribed office, a company in its own securities or the holder of a cash-settled contract for Part 7 (immunity from the interest being counted); s 4(11) denies a disregard for remoteness, manner of arising or restraint | whoever would count the interest (disability) | immunity / disability | `s 4(10) the interest is to be disregarded` and `s 4(10)(a)` to `(f)`; `s 4(11) the interest is to be disregarded by reason only of its remoteness, how it arose, or restraint` |
| s 1; s 2(1) (every defined term and the chapeau); s 2(2), (3), (4), (5), (6); s 3(1); s 4(1), (2), (3), (4), (5), (6), (7), (8), (9); s 4A(1) (each limb), (1A) | none | none | none: a definition, a deeming rule or a counting rule that creates no relation between two parties (the duties these definitions feed are in Parts 7, 8, 12 and 13) | the functions of the coverage table |

## Marginal readings for a lawyer (keel)

The brief's two readings "for a lawyer, not for you to decide": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (and flat negatives count as the text saying no); (b) a prohibition or grant limited by its own wording does not (the answer is `NOTHING`).
Every branch below rests on one of them; the other reading is a one-branch change (swap `JUST FALSE` and `NOTHING` on the named branch).
The branches are listed by script from the code: reading (a) from the `-- MARGINAL-READING (a)` comments, reading (b) from the `-- NOTHING-kind (limited by its own wording)` comments.

### Reading (a): a failed "if" answers `JUST FALSE`; the other reading answers `NOTHING`

| Function | File:line of the branch |
| --- | --- |
| s 2(4) the person has a substantial shareholding in the corporation | sfa-definitions-rest.l4:171 |
| s 2(5) the person has a substantial shareholding in the corporation whose share capital has 2 or more classes | sfa-definitions-rest.l4:193 |
| ? | sfa-interests.l4:14 |
| s 4(1) the person has authority over the disposal of the thing | sfa-interests.l4:48 |
| s 4 the person has an interest in the securities, securities-based derivatives contracts or units | sfa-interests.l4:72 |
| s 4(4) the person is treated as having an interest through a corporation the person directs or controls | sfa-interests.l4:128 |
| s 4(5) the person is treated as having an interest through a corporation in which the person and associates hold 20% of the votes | sfa-interests.l4:151 |
| s 4(6) the person is an associate of the other person for the purposes of subsection (5) | sfa-interests.l4:179 |
| s 4(7) the person is treated as having an interest in one of the circumstances | sfa-interests.l4:199 |
| s 4(8) the thing is held jointly by the person with another person | sfa-interests.l4:289 |
| s 4(10) the interest is to be disregarded | sfa-interests.l4:322 |
| s 4(10)(a) the interest is that of a bare trustee | sfa-interests.l4:338 |
| s 4(10)(b) the interest is that of a lender holding it only as security | sfa-interests.l4:357 |
| s 4(10)(c) the interest is held by reason of holding a prescribed office | sfa-interests.l4:371 |
| s 4(10)(d) the interest is a company's interest in its own securities bought under the Companies Act | sfa-interests.l4:385 |
| s 4(10)(e) the interest is a prescribed interest | sfa-interests.l4:399 |
| s 4(10)(f) for Part 7, the interest is in a cash-settled securities-based derivatives contract | sfa-interests.l4:414 |

Not marginal, though a condition is involved: the sites where the text says "where" are decided by the Guide's periods ruling of 2026-11-05, rule (b) ("a 'where ...' condition: when it fails the answer is `JUST FALSE`"): `s 4(3)`, `s 4(7)(a)` to `(d)` (each carries a comment naming the ruling).
A branch under a definition that says "means" (the great majority of the s 2(1) functions) rests on "means", which the brief names as the text's own no; a branch under a flat negative (`s 3(2)`, `s 3(3)`, `s 4(11)`, `s 4B`) rests on the flat-negative reading of the Guide's N2 ruling (2026-11-04: "flat negatives count as a no").

### Reading (b): a rule limited by its own wording answers `NOTHING` outside its limit; the other reading answers `JUST FALSE`

| Function | File:line of the branch |
| --- | --- |
| s 4B this Act applies to the person in respect of the activities | sfa-application.l4:38 |
| s 3(1) the person is associated with the other person | sfa-associates.l4:46 |
| s 3(1)(b) a corporation may be an associate in a matter relating to shares | sfa-associates.l4:115 |
| s 3(2) the director is considered associated with the other person in the proceedings | sfa-associates.l4:147 |
| s 3(3) the person is taken to be associated by virtue of subsection (1)(b), (c), (e) or (f) | sfa-associates.l4:288 |
| s 2(1) "business rules" the statements are the business rules of the body | sfa-definitions-markets.l4:219 |
| s 2(1) "listing rules" the rules are the listing rules of the corporation | sfa-definitions-markets.l4:264 |
| s 2(1) "member" the person is a member of the body | sfa-definitions-markets.l4:324 |
| s 2(1) "chief executive officer" the person is a chief executive officer of the relevant person | sfa-definitions-persons.l4:115 |
| s 2(1) "executive officer" the person is an executive officer of the relevant person | sfa-definitions-persons.l4:142 |
| s 2(1) "representative" the person is a representative of the principal | sfa-definitions-persons.l4:681 |
| s 2(2) the matter is within the affairs of a corporation | sfa-definitions-rest.l4:135 |
| s 2(3) the change of the corporation's name does not affect its identity or the application of the law to it | sfa-definitions-rest.l4:152 |
| s 2(5) the person has a substantial shareholding in the corporation whose share capital has 2 or more classes | sfa-definitions-rest.l4:194 |
| s 2(1) "custodian" the entity is a custodian of the scheme | sfa-definitions-schemes.l4:342 |
| s 2(1) "real estate investment trust" the scheme is a real estate investment trust | sfa-definitions-schemes.l4:468 |
| s 4 the person has an interest in the securities, securities-based derivatives contracts or units | sfa-interests.l4:64 |
| s 4(11) the interest is to be disregarded by reason only of its remoteness, how it arose, or restraint | sfa-interests.l4:434 |
| s 4A(2) the Authority has prescribed a modification of the definitions for the provision | sfa-investors.l4:423 |

### Reading a result: FALSE and NOTHING (keel)

This is how to read an answer from this keel, in the terms of Part 1.
A function answers `JUST TRUE` when the facts put to it fit the definition, deeming rule or limb it encodes.
It answers `JUST FALSE` ("a no") only where the text itself says no to the case in its own words: a definition that says "means" and no limb fits; an express exclusion ("but does not include", "is not taken to be associated", "is not considered ... unless", "does not apply"); or a condition the text introduces with "if" or "where" that is not met.
It answers `NOTHING` ("not covered") where the text lists without closing the list ("includes", "is to be construed as including"), leaves a word undefined ("controlling interest", "business day", "acting in concert"), is silent, hands the answer to a power or another Act that is not among the sources ("as the Authority may prescribe", "section 66 of the Commodity Trading Act 1992"), or limits its own grant or rule ("in relation to a matter relating to shares", "by reason only of", "to the extent that") and the case falls outside the limit.
A caller must never turn `NOTHING` into `FALSE`: the combining functions of this keel take the answers of their limbs as `MAYBE BOOLEAN` inputs so that a limb the caller could not answer stays `NOTHING` and is never read as a no.
In this keel a `JUST FALSE` from a limb is not yet a no for the whole term: only the combining function ("is a reference to", "means", "in any one or more of the following circumstances") says no, and only when every limb says no.

## Split sites (keel)

The two questions the brief leaves to each encoder, recorded site by site and counted here.
A search for `SPLIT-SITE` over this folder finds the one branch below (`sfa-associates.l4`) and the mentions in this file.

- (i), an unmet element of an offence or a contravention: **0 sites.** Part 1 creates no offence and states no contravention, so no function answers an unmet element of one.
- (ii), a "may" gated by "where", "when", "upon", "on application", "with the consent of" and the like: **1 site, S1, answered `NOTHING`.**

**S1. s 3(1)(b), the closing words "except that, in relation to a matter relating to shares in a corporation, a person may be an associate of the corporation and the corporation may be an associate of a person" (src:3699-3702); function `s 3(1)(b) a corporation may be an associate in a matter relating to shares`, sfa-associates.l4.**
Answer taken: `JUST TRUE` where the matter relates to shares in a corporation; `NOTHING` where it does not.
Other reading: `JUST FALSE` where it does not (the "may" is a permission whose gate, "in relation to a matter relating to shares in a corporation", has failed, read as a bar).
Relies on `inputs/ENCODING-GUIDE.md` line 87 (section 5, "Everywhere else it answers `NOTHING`: ... or limits a grant or prohibition in its own wording and the case falls outside the limit") and line 93, the periods ruling of 2026-11-05, rule (c): "a scope limit with no 'only' ...: outside the scope the answer is `NOTHING`".
The gate is a scope limit ("in relation to ...") with no "only", and the function is named for a permission, so the Guide's NOTHING line is the one that fits; the site is also listed under reading (b) above.
Tests on both inputs: `shares` TRUE (`JUST TRUE`) and FALSE (`NOTHING`), in sfa-associates-tests.l4.
The "where" conditions that gate a deeming rule, not a "may" ("Where any property held in trust ...", s 4(3); "where the person has entered into a contract ...", s 4(7)(a) to (d)), are not split sites: they follow the periods ruling of 2026-11-05, rule (b), and are marked in the code.
The other "may"s in the range are not grants gated by a condition: they are the Authority's power to prescribe ("as the Authority may prescribe"), the case-by-case "as the case may be", and the capacity "either of those persons may exercise" inside a definition.

## Rules with no breach path (keel)

None: Part 1 states no duty, prohibition or time-limited obligation, so this keel contains no regulative rule (`PARTY ... MUST`, `SHANT`) and no `#TRACE`.
Every function here is a decision function over facts.
The provisions that feed the duties of Parts 7, 8, 12 and 13 are the definitions, the deemed interests of s 4 and the investor classes of s 4A; the duties and their breach paths are those parts' to encode.

## Compared with the earlier pass

The earlier pass (`inputs/NAIVE-EVIDENCE`) covers one thing in this range: the accredited-investor tests of s 4A(1)(a) and (1A) (module `sfa-offers-exemptions.l4`, cases in `sfa-cases-offers-exemptions.l4`).
Its facts are reused in `sfa-cases-earlier-pass.l4` (15 assertions through the question `Under section 4A(1)(a), is this person an accredited investor`, and `Under section 4A(1A)`), with each expected value decided here from the text of s 4A.
Its code and names were not copied; its answers are BOOLEAN where these are `MAYBE BOOLEAN` (its TRUE is `JUST TRUE` here, its FALSE is `JUST FALSE`).

**Answers that agree** (the earlier pass's own case file, 12 accredited-investor assertions and one residence value): the savings angel (others 650,000; home 1,200,000 with 900,000 secured; financial 600,000; income 180,000) is not accredited; the angel with 3,000,000 of listed shares is; others 1,500,000 with a 3,000,000 home and 1,000,000 secured is accredited (home counted at 1,000,000); others 900,000 with a 2,000,000 home is not; exactly 2,000,000 is not; financial assets of exactly 1,000,000 are not and 1,000,001 are; income of 300,000 is and 299,999 is not; a corporation shown to have exactly 10,000,000 is not and 10,000,001 is (here: on an audited balance sheet); the residence value for a 1,600,000 home with 800,000 secured is 800,000.

**Cases whose answer differs between the earlier pass and this encoding** (both are cases of the earlier pass's function for a corporation, "a corporation with these net assets is an accredited investor", which takes the net assets alone):

| Facts | Earlier pass | This encoding | Why |
| --- | --- | --- | --- |
| A corporation with net assets of 10,000,001 and no audited balance sheet and no certified balance sheet | TRUE | `JUST FALSE` | s 4A(1)(a)(ii) says net assets "as determined by" (A) the most recent audited balance sheet or (B) a certified balance sheet; with neither, neither limb is met |
| A corporation not required to prepare audited accounts regularly, with a certified balance sheet showing 10,000,001 but dated more than 12 months before the date asked | TRUE | `JUST FALSE` | limb (B) requires the date to be "within the preceding 12 months" |

**Differences of structure, not of answer on its cases:** this encoding also tests that the person is an individual for limbs (A) to (C) and a corporation for limb (ii); takes the Authority's "such other amount" as inputs; encodes limbs (a)(iii) and (iv) (prescribed trustees and persons), expert investors and institutional investors; and answers `NOTHING` for a limb the caller could not answer.
Both encodings read s 4A(1A)(b) literally, with no floor at nought (F2); the earlier pass's note that the Authority's power to modify the definitions (s 4A(2)) is left out is met here by `s 4A(2)` and the class function.

## What the text turns out to say (numbered findings)

Each finding was checked against the text or the generated files when written (the check is named).

1. **"business day" is not defined in Part 1.** A search of lines 1668 to 4224 finds no "business day"; the first uses are at lines 21211 and 28203 (Part 7).
   The periods module counts business days under convention P8, an assumption (fork register).
2. **"relevant person" is not a term of s 4A.** It is defined at line 44338 (s 275(2), in sfad's range) and again later (lines 50589, 51081, 52728, 53115); lines 1881 and 2465 use "(called in this definition a relevant person)" as a local label inside two s 2(1) definitions.
   This keel encodes no "relevant person"; sfad takes the investor classes of s 4A as inputs.
3. **"listed corporation", "issuer", "prospectus" and "offer" are not s 2(1) terms.** There is no definition of "listed corporation" anywhere in the text (a search for the defined form finds none); "issuer" and "prospectus" are defined in Part 13 (lines 37576 and 37626, sfac's range) and "offer" later (line 45244).
   The parts take them from their own provisions or as inputs.
4. **"controlling interest" (s 4(4)(b), line 3827) is not defined anywhere in the text** (its only occurrence).
   It is asked as an input (`the person has a controlling interest in the corporation`).
5. **`inputs/XREFS.md` lists s 200, s 204 and s 209 as sections of sfab that this range cites; they are sections of the Financial Services and Markets Act 2022.** Lines 2945 to 2963 and 3066 to 3089 read "section 200(1)(b) and (2) to (7) of the Financial Services and Markets Act 2022", "section 204(1) to (4) of the ...", "section 209(1)(a), (c) and (d), (4) to (14), (17) and (18) of the ...".
   The script matched section numbers only.
   This keel cites no section of sfab.
6. **The rendering repeats a paragraph label on continuation text.** s 2(2) has a second "(d)" at line 3577 ("(d) and without limiting sub-paragraphs (i) to (iv), any conduct of such a receiver ...") and s 3(1)(b) has a second "(b)" at line 3699 ("(b) except that, in relation to a matter relating to shares ...").
   The structure of a provision comes from its labels, so each is encoded as the continuation it reads as (an input `dd` of s 2(2); the separate function for the "except that" words), not as a new paragraph.
7. **s 4A's amounts say "(or its equivalent in a foreign currency)" and give no conversion rule** (lines 4008, 4015, 4034 to 4035, 4040).
   Money inputs are therefore Singapore dollars, converted by the caller.
8. **The lower-of rule for the primary residence has no floor (s 4A(1A)(b))**: fork F2.
9. **s 2(4) and s 2(5) give the same answer for s 2(6) whether they are cumulative or the second displaces the first.** This is derived, not stated in the text: the share of all votes a person holds is a weighted average of the shares held in each class, so a person holding 5% or more of all the votes holds 5% or more of at least one class, and s 2(5) is then met.
   `s 2(6)` is therefore `s 2(4) OR s 2(5)` either way; the test cases in sfa-definitions-rest-tests.l4 include a person with 1% of the whole and 5% of one class.
10. **"associate" in s 4(5) and (6) is a different thing from "associated person" in s 3.** s 4(6) says "For the purposes of subsection (5), a person is an associate of another person if ...", with its own three limbs, and s 3 defines a person "associated" with another by seven limbs.
    They are separate functions (`s 4(6) ...`, `s 3(1) ...`) and must not be mixed.
11. **s 4(10)(f) disregards an interest only "for the purposes of Part 7".** A caller outside Part 7 gets `JUST FALSE` from the limb and the interest counts.
12. **About a third of the 120 defined terms point at another Act or section** ("has the meaning given by ...").
    A rough script count over the first lines of each definition finds 38; the count is a heuristic, not a coverage claim.
    Each such term is a function over the fact that the other Act's test is met, asked as an input named for the fact.
13. **Several terms mean different things for different Parts.** "participant", "customer", "user", "representative", "responsible person", "prescribed written law" and "voting unit" each carry an enumerated input for the provision read or the circumstance; a caller must say which.
14. **Five terms of s 2(1) are open lists, wholly or in part** (the text says "includes"): "auditor" (for Division 1 of Part 13, for an entity that is not a company), "book", "debenture", "entity" and "financial instrument"; s 2(2) is a sixth open list ("is to be construed as including").
    Each answers `NOTHING` beyond its listed limbs.
15. **Several limbs of s 4A(1)(c) name other Acts and sections not among the sources** (the Banking Act 1970, the Finance Companies Act 1967, the Insurance Act 1966, the Trust Companies Act 2005, section 81SF of this Act, which is in a later wave); each is a yes/no input.
16. **s 4B turns on section 66 of the Commodity Trading Act 1992, which is not a source**; both its facts are inputs.
17. **s 4(2), s 4(9) and s 4(11) say that something is immaterial or is not a ground, and change no outcome in the combining function.** They are encoded as functions (answering `JUST TRUE`, `JUST TRUE` and `JUST FALSE` respectively, `NOTHING` outside their words) so that no non-blank line is skipped.
18. **The amendment mark `[Act 12 of 2024 wef 30/08/2024]` (line 3831) sits after s 4(4) and is not part of the provision**; marks are neither quoted nor encoded.

## What the stable binary does not accept

Observed in this run on the stable build 1.6.110 (and the second build 1.6.109 reads every module the same: the `check.sh` table below).

- An `ELSE IF ... THEN ...` after an `ELSE` gave a parse error in the layout used (the continuation after `ELSE` is read as a new expression); `BRANCH` with `IF ... THEN ...` lines and `OTHERWISE` is used throughout.
- `rel NOT EQUALS x` gave "unexpected NOT": write `(NOT (rel EQUALS x))`.
  Every `NOT` in this folder is bracketed (`verify.py` (d)).
- `f WITH a IS FALSE EQUALS JUST TRUE` gave a type error: bracket the call, `(f WITH ...) EQUALS x`.
  The generated tests do.
- A field read written `<long backticked field> OF c` inside `any (GIVEN c YIELD ...)` gave "There are multiple definitions for the identifier" and argument-type errors; the possessive `c's <field>` works.
  (The cause was not investigated.)
- A name in two imported modules cannot be used: every name here begins with its provision label (`verify.py` (b) finds two exceptions, both test constants copied from the house `sg-periods-tests.l4`: `the supplied public holidays` and `no public holidays`).
- Not used, so nothing is claimed about them: `TYPICALLY`, `REFUSE`, `BECAUSE`, sets and opaque `DECLARE`.
- Worked on both builds: the `%` literal in arithmetic (`... AT LEAST (`the total voting power in the other body` TIMES 20%)`, `sfa-definitions-persons.l4` line 472; `TIMES 5%` in `sfa-definitions-schemes.l4`), each tested on both sides of the boundary; `@export` and `@desc` on `MEANS` functions; `LIST OF` inputs and `EMPTY`; `any (GIVEN c YIELD ...) list`; a function applied to function results as arguments; `IF ... THEN ... ELSE ...` inside brackets as an argument; `CONSIDER` is not needed.

## What `check.sh` prints

Run from this folder as `L4=<l4 1.6.110> L4_MAIN=<l4 1.6.109> ./check.sh` on 2026-11-19, after the last regeneration of the modules.
Exit code 0.
Every module compiles with no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning` (counted separately by a scratch script over all files: 0 and 0), every assertion is satisfied on both builds, and the four counts of each module are the same on both.
Output, verbatim:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sfa-application-tests.l4                       0         4       0        0         0 |      0         4       0        0  same
sfa-application.l4                             0         0       0        0         0 |      0         0       0        0  same
sfa-associates-tests.l4                        0        72       0        0         0 |      0        72       0        0  same
sfa-associates.l4                              0         0       0        0         0 |      0         0       0        0  same
sfa-cases-earlier-pass.l4                      0        15       0        0         0 |      0        15       0        0  same
sfa-cases-seat-keel.l4                         0       113       0        0         0 |      0       113       0        0  same
sfa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-benchmarks-tests.l4            0        61       0        0         0 |      0        61       0        0  same
sfa-definitions-benchmarks.l4                  0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-markets-tests.l4               0       116       0        0         0 |      0       116       0        0  same
sfa-definitions-markets.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-persons-tests.l4               0       144       0        0         0 |      0       144       0        0  same
sfa-definitions-persons.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-products-tests.l4              0       107       0        0         0 |      0       107       0        0  same
sfa-definitions-products.l4                    0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-rest-tests.l4                  0        41       0        0         0 |      0        41       0        0  same
sfa-definitions-rest.l4                        0         0       0        0         0 |      0         0       0        0  same
sfa-definitions-schemes-tests.l4               0       110       0        0         0 |      0       110       0        0  same
sfa-definitions-schemes.l4                     0         0       0        0         0 |      0         0       0        0  same
sfa-interests-tests.l4                         0        86       0        0         0 |      0        86       0        0  same
sfa-interests.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-investors-tests.l4                         0       118       0        0         0 |      0       118       0        0  same
sfa-investors.l4                               0         0       0        0         0 |      0         0       0        0  same
sfa-periods-tests.l4                           0        82       0        0         0 |      0        82       0        0  same
sfa-periods.l4                                 0         0       0        0         0 |      0         0       0        0  same
sfa-seat-keel.l4                               0         0       0        0         0 |      0         0       0        0  same
TOTAL (26 modules)                             0      1069       0        0           |      0      1069       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`srcrefs.py` over the same modules (`python3 -I srcrefs.py check --refs ../../../inputs/SFA2001.txt sfa-*.l4`, then the same with `--strict`):

```
srcrefs check: 1731 src: lines, 178 runs, 184 locators, 0 problems
srcrefs check: 1731 src: lines, 178 runs, 184 locators, 0 problems
```

A scratch script (`verify.py`, in the generator folder outside this deposit) checks what `check.sh` does not.
Its output on the final run:

```
(a) non-blank lines 3113, each in exactly one row: YES; rows used 209 of 209
    rows by disposition: {'encoded': 199, 'inert': 7, 'fork': 3}
(b) top-level names not beginning with a provision label: 2
     ('sfa-periods-tests.l4', 'the supplied public holidays')
     ('sfa-periods-tests.l4', 'no public holidays')
(c) quoted passages 236, fragments 380, not found in the text: 0
(d) unbracketed NOT in code: 0
(e) #ASSERT continuation lines: 0
(f) forbidden words in code: 0
(g) files with an emoji: 0
(h) every file under 1200 lines: True ; core lines 127
```

(b) lists two names that do not begin with a provision label: the test constants `the supplied public holidays` and `no public holidays` in `sfa-periods-tests.l4`, copied from the house `sg-periods-tests.l4` so that the period tests read the same way across the family.
(c) checks that every fragment in a `-- FALSE-kind (...)` or `-- NOTHING-kind (...)` comment that is quoted from the text occurs in the text.
(d) checks that no `NOT` in code is unbracketed, so no rule reads `NOT x OR y`; there is none, so there is no boundary input to test for it.
A search for `SPLIT-SITE` in the `.l4` files finds one line, `sfa-associates.l4` line 115.

