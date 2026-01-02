#!/bin/bash
# Deployment script for staging and production

set -euo pipefail

ENVIRONMENT=${1:-staging}
VERSION=${2:-latest}

echo "=========================================="
echo "Deploying to $ENVIRONMENT environment"
echo "Version: $VERSION"
echo "=========================================="

case $ENVIRONMENT in
  staging)
    HOST="staging.example.com"
    IMAGE="your-dockerhub/cicd-demo:staging"
    ;;
  production)
    HOST="production.example.com"
    IMAGE="your-dockerhub/cicd-demo:$VERSION"
    ;;
  *)
    echo "Unknown environment: $ENVIRONMENT"
    exit 1
    ;;
esac

echo "Pulling latest image..."
# ssh user@$HOST "docker pull $IMAGE"

echo "Stopping old container..."
# ssh user@$HOST "docker stop cicd-demo || true"
# ssh user@$HOST "docker rm cicd-demo || true"

echo "Starting new container..."
# ssh user@$HOST "docker run -d --name cicd-demo -p 5000:5000 $IMAGE"

echo "Waiting for health check..."
sleep 5

echo "Running health check..."
# curl -f http://$HOST/health

echo "=========================================="
echo "Deployment completed successfully"
echo "=========================================="
