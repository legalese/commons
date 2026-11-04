#!/bin/sh
# count.sh LOG: the four numbers check.sh counts, from the output of `l4 run`.
msgs=$(grep -A1 -E '^[[:space:]]*Message:' "$1")
err=$(grep -c 'DiagnosticSeverity_Error' "$1")
ok=$(printf '%s\n' "$msgs" | grep -cE 'assertion satisfied')
bad=$(printf '%s\n' "$msgs" | grep -cE 'assertion failed|assertion could not be evaluated')
ref=$(printf '%s\n' "$msgs" | grep -cE 'assertion refused')
echo "errors $err satisfied $ok failed $bad refused $ref"
