#!/usr/bin/env bash
set -euo pipefail
src="ci/exp073en_home_filebacked_fullres_v0_1.sh"
tmp="${RUNNER_TEMP:-/tmp}/exp073en_home_filebacked_fullres_v0_2.generated.sh"
python3 - "$src" "$tmp" <<'PY'
from pathlib import Path
import sys
src=Path(sys.argv[1]).read_text()
start=src.index("# Live exclusivity beyond flock:")
end=src.index("# Exact 8-CPU execution contract.")
replacement="""# Live exclusivity beyond flock: infrastructure-only v0.2 retry wrapper.
bash ci/exp073en_live_exclusivity_curl_retry_v0_2.sh

"""
out=src[:start]+replacement+src[end:]
Path(sys.argv[2]).write_text(out)
PY
chmod +x "$tmp"
exec bash "$tmp"
