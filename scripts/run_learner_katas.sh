#!/usr/bin/env bash
# Run kata tests against the student's stubs (no solutions copy).
# Always exits 0 after printing a per-module status table so unfinished
# modules do not turn course CI / deploy red. Tooling crashes still surface
# in the log; solutions-* jobs are the gate that proves tests are valid.
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

declare -a ROWS=()
PASS=0
FAIL=0
SKIP=0

run_py() {
  local dir="$1"
  (
    cd "$dir" || exit 2
    if [ -f requirements.txt ]; then
      pip install -q -r requirements.txt
    else
      pip install -q pytest
    fi
    python3 -m pytest -q
  )
}

run_go_mod() {
  local dir="$1"
  (
    cd "$dir" || exit 2
    go test ./...
  )
}

run_go_totp() {
  (
    cd 01-challenge-gym/go-totp || exit 2
    go test ./...
  )
}

run_node_phish() {
  (
    cd 17-phish-lite || exit 2
    npm test
  )
}

run_node_admin() {
  (
    cd 08-mailguard-admin || exit 2
    npm test
  )
}

record() {
  local name="$1" code="$2"
  if [ "$code" -eq 0 ]; then
    ROWS+=("| $name | pass |")
    PASS=$((PASS + 1))
  else
    ROWS+=("| $name | fail (stubs unfinished or regressions) |")
    FAIL=$((FAIL + 1))
  fi
}

echo "## Learner kata status (stubs as committed)"
echo

PY_DIRS=(
  01-challenge-gym
  02-mailguard-mfa
  03-oidc-access
  04-ztna-lite
  05-email-auth
  07-mailguard-api
  10-secure-drop
  11-security-notes
  12-ci-aws
  13-infra
  14-k8s-local
  15-observability
  16-gitops-policy
  19-capstone
  20-scim-provisioning
  21-global-privacy-collab
  22-collab-review
)

for d in "${PY_DIRS[@]}"; do
  echo "=== learner python: $d ==="
  if run_py "$d"; then
    record "$d (python)" 0
  else
    record "$d (python)" 1
  fi
done

echo "=== learner go: 09-mailguard-worker ==="
if run_go_mod 09-mailguard-worker; then
  record "09-mailguard-worker (go)" 0
else
  record "09-mailguard-worker (go)" 1
fi

echo "=== learner go: 01-challenge-gym/go-totp ==="
if run_go_totp; then
  record "01-challenge-gym/go-totp" 0
else
  record "01-challenge-gym/go-totp" 1
fi

echo "=== learner node: 17-phish-lite ==="
if run_node_phish; then
  record "17-phish-lite (node)" 0
else
  record "17-phish-lite (node)" 1
fi

echo "=== learner node: 08-mailguard-admin ==="
if run_node_admin; then
  record "08-mailguard-admin (node)" 0
else
  record "08-mailguard-admin (node)" 1
fi

echo
echo "| Module | Status |"
echo "|--------|--------|"
for row in "${ROWS[@]}"; do
  echo "$row"
done
echo
echo "Summary: pass=$PASS fail=$FAIL (learner job always green; see solutions-* for test validity)"
exit 0
