#!/bin/bash
# Health check script

set -euo pipefail

ENVIRONMENT=${1:-staging}
MAX_RETRIES=5
RETRY_DELAY=5

case $ENVIRONMENT in
  staging)
    URL="https://staging.example.com/health"
    ;;
  production)
    URL="https://production.example.com/health"
    ;;
  local)
    URL="http://localhost:5000/health"
    ;;
  *)
    echo "Unknown environment: $ENVIRONMENT"
    exit 1
    ;;
esac

echo "Checking health of $ENVIRONMENT environment..."
echo "URL: $URL"

for i in $(seq 1 $MAX_RETRIES); do
    echo "Attempt $i of $MAX_RETRIES..."
    
    if curl -sf "$URL" > /dev/null; then
        echo "Health check PASSED"
        exit 0
    fi
    
    if [ $i -lt $MAX_RETRIES ]; then
        echo "Health check failed, retrying in $RETRY_DELAY seconds..."
        sleep $RETRY_DELAY
    fi
done

echo "Health check FAILED after $MAX_RETRIES attempts"
exit 1
