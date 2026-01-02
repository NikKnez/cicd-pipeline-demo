# CI/CD Pipeline Demo

Complete CI/CD pipeline implementation using GitHub Actions. Demonstrates automated testing, building, and deployment workflows for DevOps automation.

## Overview

This repository showcases a production-grade CI/CD pipeline that:
- Runs automated tests on every commit
- Builds and pushes Docker images
- Deploys to staging on merge to develop
- Deploys to production on release tags
- Performs security scanning
- Sends notifications on success/failure

## Pipeline Stages
```
Code Push
    |
    v
Lint & Format Check
    |
    v
Unit Tests
    |
    v
Integration Tests
    |
    v
Build Docker Image
    |
    v
Security Scan
    |
    v
Push to Registry
    |
    v
Deploy to Staging (develop branch)
    |
    v
Manual Approval
    |
    v
Deploy to Production (tags only)
    |
    v
Smoke Tests
    |
    v
Notification
```

## Features

- Automated testing (unit, integration, end-to-end)
- Docker image building and caching
- Multi-environment deployments (dev, staging, prod)
- Security vulnerability scanning
- Automated rollback on failure
- Slack/email notifications
- Deployment status badges
- Branch protection enforcement

## Technology Stack

- GitHub Actions (CI/CD orchestration)
- Docker (containerization)
- Python/Flask (sample application)
- pytest (testing framework)
- Trivy (security scanning)
- AWS/DigitalOcean (deployment targets)

## Quick Start

### Prerequisites

- GitHub account with Actions enabled
- Docker Hub account (or other registry)
- Server for deployment (optional)

### Setup

1. Fork or clone this repository
2. Configure secrets in GitHub Settings > Secrets:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`
   - `DEPLOY_SSH_KEY`
   - `DEPLOY_HOST`
   - `DEPLOY_USER`
   - `SLACK_WEBHOOK` (optional)

3. Push code to trigger pipeline:
```bash
git add .
git commit -m "feat: initial commit"
git push origin main
```

4. Watch Actions tab for pipeline execution

## Repository Structure
```
.
├── .github/
│   └── workflows/
│       ├── ci.yml              # Continuous Integration
│       ├── cd-staging.yml      # Deploy to staging
│       ├── cd-production.yml   # Deploy to production
│       ├── security-scan.yml   # Security checks
│       └── cleanup.yml         # Cleanup old artifacts
├── app/
│   ├── app.py                  # Flask application
│   ├── Dockerfile
│   └── requirements.txt
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── infrastructure/
│   ├── terraform/              # Infrastructure as Code
│   └── k8s/                    # Kubernetes manifests
├── scripts/
│   ├── deploy.sh              # Deployment script
│   ├── health-check.sh        # Health verification
│   └── rollback.sh            # Rollback script
└── docs/
    ├── PIPELINE.md            # Pipeline documentation
    └── DEPLOYMENT.md          # Deployment guide
```

## Workflows

### Continuous Integration (ci.yml)

Triggered on: Push to any branch, Pull Requests

Steps:
1. Checkout code
2. Set up Python environment
3. Install dependencies
4. Run linter (flake8, black)
5. Run unit tests with coverage
6. Run integration tests
7. Build Docker image
8. Run security scan (Trivy)
9. Upload test reports

### Continuous Deployment - Staging (cd-staging.yml)

Triggered on: Push to develop branch

Steps:
1. Run CI pipeline
2. Build and tag Docker image (staging)
3. Push to Docker registry
4. Deploy to staging server
5. Run smoke tests
6. Send notification

### Continuous Deployment - Production (cd-production.yml)

Triggered on: Git tags (v*.*.*)

Steps:
1. Manual approval required
2. Run full test suite
3. Build and tag Docker image (production)
4. Push to Docker registry
5. Deploy to production (blue-green)
6. Run smoke tests
7. Rollback on failure
8. Send notification

### Security Scanning (security-scan.yml)

Triggered on: Schedule (daily), Manual

Steps:
1. Scan dependencies for vulnerabilities
2. Scan Docker images
3. Check for secrets in code
4. Create security report
5. Open GitHub issue if critical vulnerabilities found

## Usage Examples

### Triggering CI Pipeline
```bash
# Any commit triggers CI
git add .
git commit -m "feat: add new feature"
git push origin feature-branch
```

### Deploying to Staging
```bash
# Merge to develop
git checkout develop
git merge feature-branch
git push origin develop
# Pipeline automatically deploys to staging
```

### Deploying to Production
```bash
# Create release tag
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
# Pipeline requires manual approval before production deploy
```

### Manual Pipeline Trigger

Go to Actions tab > Select workflow > Run workflow

## Environment Variables

### CI/CD Pipeline
```
DOCKER_USERNAME       # Docker Hub username
DOCKER_PASSWORD       # Docker Hub password/token
DEPLOY_SSH_KEY        # SSH key for deployment
DEPLOY_HOST           # Deployment server hostname
DEPLOY_USER           # SSH user for deployment
SLACK_WEBHOOK         # Slack notification webhook
```

### Application
```
FLASK_ENV             # Environment (development/production)
DATABASE_URL          # Database connection string
SECRET_KEY            # Application secret key
```

## Testing

### Run Tests Locally
```bash
# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run unit tests
pytest tests/unit/

# Run with coverage
pytest --cov=app tests/

# Run all tests
pytest tests/
```

### Test Docker Build
```bash
# Build image
docker build -t cicd-demo:test ./app

# Run container
docker run -p 5000:5000 cicd-demo:test

# Test endpoint
curl http://localhost:5000/health
```

## Deployment

### Manual Deployment
```bash
# Deploy to staging
./scripts/deploy.sh staging

# Deploy to production
./scripts/deploy.sh production
```

### Rollback
```bash
# Rollback to previous version
./scripts/rollback.sh production v1.0.0
```

## Monitoring

### Pipeline Status

Check GitHub Actions tab for:
- Build status
- Test results
- Deployment logs
- Performance metrics

### Application Health
```bash
# Check staging
curl https://staging.example.com/health

# Check production
curl https://production.example.com/health
```

## Security

- All secrets stored in GitHub Secrets (encrypted)
- SSH keys rotated regularly
- Docker images scanned for vulnerabilities
- Dependencies checked daily
- No credentials in code or logs
- Least privilege access for deployment

## Troubleshooting

### Pipeline Fails at Build Stage
```bash
# Check workflow logs in GitHub Actions
# Common issues:
# - Missing dependencies in requirements.txt
# - Docker build context issues
# - Syntax errors in Dockerfile
```

### Deployment Fails
```bash
# SSH into server and check logs
ssh user@server
docker logs app-container

# Check deployment script logs
cat /var/log/deployment.log
```

### Tests Fail
```bash
# Run tests locally to debug
pytest -v tests/

# Check specific test file
pytest -v tests/unit/test_app.py
```

## Best Practices

1. Always use feature branches
2. Require PR reviews before merging
3. Keep pipelines fast (under 10 minutes)
4. Cache dependencies when possible
5. Use matrix builds for multiple versions
6. Implement proper error handling
7. Send meaningful notifications
8. Keep deployment scripts idempotent
9. Test rollback procedures regularly
10. Document all pipeline changes

## Performance

- Average CI pipeline time: 5-7 minutes
- Docker layer caching reduces build time by 60%
- Parallel test execution saves 3-4 minutes
- Automated cleanup prevents artifact bloat

## Contributing

1. Create feature branch
2. Make changes
3. Run tests locally
4. Push and create PR
5. Pipeline runs automatically
6. Review required before merge

## License

MIT License

## Author

*Nikola Knezevic*
- AWS Certified Cloud Practitioner
- GitHub: [@NikKnez](https://github.com/NikKnez)
- LinkedIn: [Nikola Knezevic](https://linkedin.com/in/nikola-knezevic-devops)

## References

- GitHub Actions Documentation
- Docker Best Practices
- CI/CD Best Practices
- DevOps Handbook
