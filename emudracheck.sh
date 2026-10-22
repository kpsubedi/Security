#!/usr/bin/env bash

# eMudhra October 2026 TLS trust assessment
# Usage: bash check-emudhra.sh

set -u

HOSTS=(
  "dv-g3b-emudhra.we-have-a-problem.com"
  "dv-g3b-aaa-emudhra.we-have-a-problem.com"
  "dv-g3b-noct-emudhra.we-have-a-problem.com"
  "dv-g3b-aaa-noct-emudhra.we-have-a-problem.com"
)

echo "=== eMudhra TLS Security Assessment ==="
date -u
echo

echo "[1] Operating System"
if [[ -f /etc/os-release ]]; then
  grep -E '^(NAME|VERSION)=' /etc/os-release
fi

echo
echo "[2] TLS Library"
curl --version | head -n 2
openssl version

echo
echo "[3] CA Certificate Package"
if command -v rpm >/dev/null; then
  rpm -q ca-certificates
elif command -v dpkg-query >/dev/null; then
  dpkg-query -W ca-certificates
elif command -v apk >/dev/null; then
  apk info -v ca-certificates
fi

echo
echo "[4] Compromised CA Trust Tests"

vulnerable=0
blocked=0
unknown=0

for host in "${HOSTS[@]}"; do
  echo
  echo "Testing: $host"

  result=$(curl \
    --silent --show-error \
    --noproxy '*' \
    --connect-timeout 5 \
    --max-time 12 \
    --output /dev/null \
    --write-out '%{http_code}' \
    "https://$host/" 2>&1)

  status=$?

  if [[ $status -eq 0 ]]; then
    echo "[VULNERABLE] TLS certificate accepted"
    ((vulnerable+=1))
  elif [[ $status -eq 60 ]]; then
    echo "[PROTECTED] Certificate rejected"
    ((blocked+=1))
  else
    echo "[INCONCLUSIVE] curl exit code: $status"
    echo "$result"
    ((unknown+=1))
  fi
done

echo
echo "=== SUMMARY ==="
echo "Accepted:     $vulnerable"
echo "Rejected:     $blocked"
echo "Inconclusive: $unknown"

if (( vulnerable > 0 )); then
  echo "RESULT: POTENTIALLY VULNERABLE"
  exit 2
elif (( unknown > 0 )); then
  echo "RESULT: INCOMPLETE TEST"
  exit 3
else
  echo "RESULT: TESTED CHAINS BLOCKED"
  exit 0
fi

Displaying demo.sh.
