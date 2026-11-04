#!/usr/bin/env bash
# Run srcrefs.py --strict on every module that quotes a source, against the texts deposited in this repository.
# An Act module quotes TA1999.txt by line number; an instrument module quotes its own deposited texts as src:ID:N,
# where ID is the stem of a file in the same registers/source-bundle/ directory as the RAW file named here.
set -u
here="$(cd "$(dirname "$0")" && pwd)"
subj="$here/../../.."
act="$subj/telecommunications-act-1999/registers/source-bundle/TA1999.txt"
inst() { echo "$subj/$1/registers/source-bundle/$2.txt"; }
fail=0
run() { raw="$1"; shift; for m in "$@"; do python3 -I "$here/srcrefs.py" check --strict "$raw" "$here/$m" || fail=1; done; }
run "$act" sgta-s2-definitions.l4 sgta-s3-5-privilege-licensing.l4 sgta-s11-approval.l4 sgta-part6-offences.l4 sgta-part8-penalties.l4 sgta-part9-general.l4 $(cd "$here" && ls sgta-*.l4 | grep -vE '^sgta-(tests|tv|i-|nouns|ta-vintage)' | grep -vE '^sgta-(s2-definitions|s3-5-privilege-licensing|s11-approval|part6-offences|part8-penalties|part9-general)\.l4$')
run "$(inst telecommunications-exemption-notification-2001 TA1999-N1)" $(cd "$here" && ls sgta-i-n1-*.l4)
run "$(inst telecommunications-radio-communication-regulations-2001 TA1999-RG5)" $(cd "$here" && ls sgta-i-rg5-*.l4)
run "$(inst telecommunications-dealers-regulations-2003 TA1999-RG6)" $(cd "$here" && ls sgta-i-rg6-*.l4)
run "$(inst telecommunications-class-licences-regulations-2000 TA1999-RG3)" $(cd "$here" && ls sgta-i-rg3-*.l4 | grep -v -- -1999)
run "$(inst telecommunications-designated-telecommunication-licensees-notifications TA1999-DTL-S23-2011)" sgta-i-dtl-notifications.l4
run "$(inst telecommunications-composition-of-offences-regulations-2005 TA1999-COMP-S706-2005)" sgta-i-comp.l4
run "$(inst telecommunications-ship-station-operators-regulations TA1999-RG1)" sgta-i-rg1-ship.l4
run "$(inst telecommunications-cable-detection-workers-regulations TA1999-RG4)" sgta-i-rg4-cable.l4
run "$(inst telecommunications-internal-wiring-regulations-2005 TA1999-IW-S479-2005)" sgta-i-iw-wiring.l4
run "$(inst telecommunications-resellers-coinafons-notification-2007 TA1999-RESELL-S77-2007)" sgta-i-resell.l4
run "$(inst telecommunications-prescribed-trusts-regulations-2017 TA1999-TRUSTS-S403-2017)" sgta-i-trusts.l4
# Added 2026-11-04 (follow-up list): the TAS-era Order and the 1999 Revised Editions, the 2024 instruments and the Acts after Act 15 of 2017.
run "$(inst telecommunications-tas-exemption-specified-equipment-order-1998 TA1999-O3)" sgta-i-o3-1998.l4
run "$(inst telecommunications-dealers-regulations-1999 TA1999-DEAL99)" sgta-i-rg7-1999.l4
run "$(inst telecommunications-radio-communication-regulations-1999 TA1999-RADIO99)" sgta-i-rg3-1999.l4
run "$(inst telecommunications-in-vehicle-unit-exemption-notification-2024 TA1999-ERP-S381-2024)" sgta-i-erp-s381-2024.l4
run "$(inst telecommunications-wiring-work-regulations-2024 TA1999-WW-S559-2024)" sgta-i-ww-2024.l4
run "$act" sgta-i-acts-after-2017.l4
run "$(inst telecommunications-cancellation-notification-2011 TA1999-CANC-S22-2011)" sgta-i-canc-s22-2011.l4
# The quarantined sgta-tv-* modules (the seat, its cases and the Broadcasting Act table) were left out of the runs above by the first grep -v.
# They carry no `src:` quote lines or @ref locators, so srcrefs.py finds 0 lines in them (printed here with a "tv " prefix so that the totals above stay the Act's and instruments'); the
# check that does bear on them is check-tv-citations.py (every FILE.txt:N locator in them and in TV-QUESTION.md must exist; every quoted fragment of the Rg 1 table must be in the deposits).
for m in $(cd "$here" && ls sgta-tv-*.l4); do python3 -I "$here/srcrefs.py" check --strict "$act" "$here/$m" 2>&1 | sed 's/^srcrefs check:/tv srcrefs check ('"$m"'):/' || fail=1; done
python3 -I "$here/check-tv-citations.py" || fail=1
exit $fail
