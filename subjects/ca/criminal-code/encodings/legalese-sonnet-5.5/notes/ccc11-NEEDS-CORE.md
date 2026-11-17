# NEEDS-CORE.md -- ccc11 (Part VIII.1)

Constructors of the core's `Party` that this part wanted and the core lacks. A constructor cannot be added to a core type from another module, so this part declared a small type of its own under its prefix for each and uses it in its regulative rules; the lead may hoist them into `Party` at the merge and replace the part's types.

| wanted in `Party` | used by (the text) | declared here as |
| --- | --- | --- |
| `a person` (an unnamed person: "No person shall ...") | `s 320.36(1)` and `s 320.36(2)` (the prohibitions on using a bodily substance or its results otherwise than as the section allows; lines 6478, 6480) | `s 320.36 party` with the constructor `s 320.36 any person` (`ccc11-general.l4`) |
| `a person who takes samples of blood` (a qualified medical practitioner or a qualified technician, by 320.28(6)) | `s 320.28(8)` ("A person who takes samples of blood under this section shall cause one of the samples to be retained"; line 6389) | `s 320.28 party` with the constructor `s 320.28 a person who takes samples of blood under section 320.28` (`ccc11-investigation.l4`) |

Not needed: a type or constructor for any other part of the range. `Provision of the Code`, `Imprisonment`, `Fine`, `Punishment`, `Length of time`, `Mode of proceeding` and `Class of offence` carry everything the punishments and the offences name; the occasion (first, second, subsequent) is this part's own enumeration (`s 320.19 occasion`), because the core has no such type and only this part and the sentencing parts (ccc26) turn on it. The lead may hoist it.
