#!/usr/bin/env bash
set -euo pipefail

: "${RUNNER_TOKEN:?RUNNER_TOKEN must contain a fresh GitHub Actions runner registration token}"
: "${RUNNER_URL:?RUNNER_URL must be the exact repository URL}"
: "${RUNNER_NAME_INPUT:?RUNNER_NAME_INPUT must be a unique new runner name}"

REQUIRED_LABEL="dsir-32769-highmem"
ISOLATION_CONTRACT_BLOB="d9d910d89889f6d3a27461a73c3dd72c2a9d2096"
ROOT="$(pwd -P)"

test -x "$ROOT/config.sh"
test ! -e "$ROOT/.runner"
test ! -e "$ROOT/.credentials"
test ! -e "$ROOT/.credentials_rsaparams"

SELF_SHA256="$(sha256sum "$0" | awk '{print $1}')"

./config.sh \
  --url "$RUNNER_URL" \
  --token "$RUNNER_TOKEN" \
  --name "$RUNNER_NAME_INPUT" \
  --work "_work" \
  --labels "$REQUIRED_LABEL" \
  --no-default-labels \
  --unattended

unset RUNNER_TOKEN

test -f "$ROOT/.runner"

python3 - "$ROOT/.runner" "$ROOT/.dsir32769-registration-receipt.json" "$SELF_SHA256" "$REQUIRED_LABEL" "$ISOLATION_CONTRACT_BLOB" <<'PY'
import datetime
import json
import sys
from pathlib import Path

runner_settings = json.loads(Path(sys.argv[1]).read_text())
out_path = Path(sys.argv[2])
script_sha256 = sys.argv[3]
required_label = sys.argv[4]
isolation_blob = sys.argv[5]

agent_name = runner_settings.get("agentName") or runner_settings.get("AgentName")
agent_id = runner_settings.get("agentId") or runner_settings.get("AgentId")
if not isinstance(agent_name, str) or not agent_name:
    raise SystemExit("runner settings do not expose a valid agent name")
if not isinstance(agent_id, int) or agent_id <= 0:
    raise SystemExit("runner settings do not expose a valid agent id")

receipt = {
    "schema": "LAYERB_32769_HIGH_MEMORY_RUNNER_REGISTRATION_RECEIPT_V0_1",
    "classification": "LAYERB_32769_HIGH_MEMORY_RUNNER_REGISTRATION_CONFIGURED_PLUS_0_PLUS_0",
    "effect": "+0/+0",
    "configuration_method": "FROZEN_CONFIGURATOR_SCRIPT",
    "configuration_script_sha256": script_sha256,
    "runner_isolation_contract_git_blob": isolation_blob,
    "runner_name": agent_name,
    "runner_agent_id": agent_id,
    "configured_labels": [required_label],
    "required_custom_label": required_label,
    "no_default_labels": True,
    "forbidden_default_labels": ["self-hosted", "Linux", "X64"],
    "configured_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "registration_token_recorded": False,
    "credentials_recorded": False,
    "scientific_response_read": False,
    "scientific_execution_authorized": False,
    "high_memory_resource_lifecycle_preflight_pass_created": False,
    "covariance_restriction_authorized": False,
    "Wm_S3_opened": False,
}
receipt["token"] = receipt["classification"]
out_path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
print(receipt["classification"])
PY

chmod 600 "$ROOT/.dsir32769-registration-receipt.json"
echo "Runner registration receipt written to $ROOT/.dsir32769-registration-receipt.json"
