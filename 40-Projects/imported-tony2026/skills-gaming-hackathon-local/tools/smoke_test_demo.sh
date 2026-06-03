#!/usr/bin/env bash
set -euo pipefail
BASE_URL="${1:-http://127.0.0.1:8000}"

echo '[1] health'
curl -fsS "$BASE_URL/health"
echo

echo '[2] tournament'
curl -fsS "$BASE_URL/tournament/current"
echo

echo '[3] ingest event'
MATCH_ID="match-smoke-$(date +%s)"
curl -fsS -X POST "$BASE_URL/events" \
  -H 'Content-Type: application/json' \
  -d "{\"events\":[{\"event_name\":\"smoke_test\",\"player_id\":\"smoke\",\"match_id\":\"$MATCH_ID\",\"emitted_at\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\",\"payload\":{\"source\":\"smoke_script\"}}]}"
echo

echo '[4] submit score'
curl -fsS -X POST "$BASE_URL/match/submit-score" \
  -H 'Content-Type: application/json' \
  -d "{\"match_id\":\"$MATCH_ID\",\"player_id\":\"smoke\",\"correct_count\":7,\"error_count\":2,\"streak_bonus\":4,\"error_penalty\":2,\"duration_ms\":31000,\"client_version\":\"smoke-0.1\"}"
echo

echo '[5] result'
curl -fsS "$BASE_URL/result/$MATCH_ID"
echo
