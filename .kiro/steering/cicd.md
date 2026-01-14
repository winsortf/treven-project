---
inclusion: fileMatch
fileMatchPattern: "**/.github/**"
---

# CI/CD Pipeline

## GitHub Actions Workflows

### Main Pipeline (.github/workflows/main.yml)

```yaml
name: CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  AWS_REGION: eu-west-2

jobs:
  # Frontend
  web-test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: treven-web
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: treven-web/package-lock.json
      - run: npm ci
      - run: npm run lint
      - run: npm run type-check
      - run: npm test

  web-build:
    needs: web-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      - uses: aws-actions/amazon-ecr-login@v2
      - run: |
          docker build -t $ECR_REGISTRY/treven-web:${{ github.sha }} ./treven-web
          docker push $ECR_REGISTRY/treven-web:${{ github.sha }}

  # Backend API
  api-test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: treven-back
    steps:
      - uses: actions/checkout@v4
      - uses: dtolnay/rust-toolchain@stable
      - uses: Swatinem/rust-cache@v2
        with:
          workspaces: treven-back
      - run: cargo fmt --check
      - run: cargo clippy -- -D warnings
      - run: cargo test

  api-build:
    needs: api-test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      - uses: aws-actions/amazon-ecr-login@v2
      - run: |
          docker build -t $ECR_REGISTRY/treven-api:${{ github.sha }} ./treven-back
          docker push $ECR_REGISTRY/treven-api:${{ github.sha }}

  # AI Agents
  ai-test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: treven-ai
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync
      - run: uv run ruff check .
      - run: uv run mypy .
      - run: uv run pytest

  # Deploy
  deploy:
    needs: [web-build, api-build, ai-test]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ${{ env.AWS_REGION }}
      - run: |
          # Update ECS services
          aws ecs update-service --cluster treven --service web --force-new-deployment
          aws ecs update-service --cluster treven --service api --force-new-deployment
```

## Terraform Pipeline (.github/workflows/terraform.yml)

```yaml
name: Terraform

on:
  push:
    branches: [main]
    paths:
      - 'infra/**'
  pull_request:
    paths:
      - 'infra/**'

jobs:
  plan:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: infra
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-west-2
      - run: terraform init
      - run: terraform plan -out=tfplan
      - uses: actions/upload-artifact@v4
        with:
          name: tfplan
          path: infra/tfplan

  apply:
    needs: plan
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - uses: actions/download-artifact@v4
        with:
          name: tfplan
          path: infra
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: eu-west-2
      - run: terraform init
        working-directory: infra
      - run: terraform apply -auto-approve tfplan
        working-directory: infra
```

## Required Secrets

| Secret | Description |
|--------|-------------|
| AWS_ACCESS_KEY_ID | AWS IAM access key |
| AWS_SECRET_ACCESS_KEY | AWS IAM secret key |
| ECR_REGISTRY | ECR registry URL |

## Environments

- `development` - Auto-deploy from `develop` branch
- `production` - Manual approval required, deploy from `main`
