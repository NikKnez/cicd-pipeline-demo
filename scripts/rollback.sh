#!/bin/bash
# Rollback to previous version

set -euo pipefail

ENVIRONMENT=${1:-staging}
VERSION=${2:-}

if [ -z "$VERSION" ]; then
    echo "Usage: $0 <environment> <version>"
    echo "Example: $0 production 1.0.0"
    exit 1
fi

echo "=========================================="
echo "Rolling back $ENVIRONMENT to version $VERSION"
echo "=========================================="

case $ENVIRONMENT in
  staging)
    HOST="staging.example.com"
    ;;
  production)
    HOST="production.example.com"
    ;;
  *)
    echo "Unknown environment: $ENVIRONMENT"
    exit 1
    ;;
esac

IMAGE="your-dockerhub/cicd-demo:$VERSION"

echo "Pulling version $VERSION..."
# ssh user@$HOST "docker pull $IMAGE"

echo "Stopping current container..."
# ssh user@$HOST "docker stop cicd-demo"
# ssh user@$HOST "docker rm cicd-demo"

echo "Starting previous version..."
# ssh user@$HOST "docker run -d --name cicd-demo -p 5000:5000 $IMAGE"

echo "Running health check..."
sleep 5
# curl -f http://$HOST/health

echo "=========================================="
echo "Rollback completed successfully"
echo "=========================================="
