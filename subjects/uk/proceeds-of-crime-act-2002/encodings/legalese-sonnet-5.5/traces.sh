#!/usr/bin/env bash
# usage: traces.sh FILE.l4 [build]  -- print the result of every #TRACE / #EVAL in FILE (not the assertions), one block each
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
B=${2:-109}
"$L4DIR/l4-main-$B" run "$HERE/$1" 2>&1 | awk '
  /^Evaluation\[/ { blk = $0 "\n"; inres = 0; next }
  /^Result:/ { inres = 1; blk = blk $0 "\n"; next }
  /^Trace:/ { if (inres && blk !~ /assertion satisfied/) printf "%s", blk; inres = 0; blk = ""; next }
  inres { blk = blk $0 "\n" }'
