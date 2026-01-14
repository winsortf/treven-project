---
inclusion: always
---

# Local Development

## Prerequisites

- Docker & Docker Compose
- Node.js 22+
- Rust 1.85+ (for edition 2024)
- Python 3.12+
- uv (Python package manager)
- AWS CLI (for LocalStack commands)

## DynamoDB Configuration

| Setting | Value |
|---------|-------|
| **Table Name** | `lon12-table` |
| **Region** | `us-west-2` |
| **Key Schema** | PK (Partition Key), SK (Sort Key) |
| **Billing Mode** | PAY_PER_REQUEST |

**Reference:** [AWS SDK for Rust DynamoDB Guide](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_dynamodb_code_examples.html)

## Quick Start

```bash
# Clone all repos (if using submodules)
git clone --recursive <repo-url>

# Start all services
docker-compose up -d

# Or start individually:
# Frontend
cd treven-web && npm install && npm run dev

# Backend API
cd treven-back && cargo run

# Database layer
cd treven-back-db && cargo run

# AI agents
cd treven-ai && uv sync && uv run python main.py
```

## Docker Compose Services

```yaml
services:
  web:
    build: ./treven-web
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8080
      - NEXT_PUBLIC_WS_URL=ws://localhost:8081

  api:
    build: ./treven-back
    ports:
      - "8080:8080"
    environment:
      - DYNAMODB_ENDPOINT=http://localstack:4566
      - REDIS_URL=redis://redis:6379
      - AWS_REGION=us-west-2

  ws:
    build: ./treven-back
    command: ["./ws-server"]
    ports:
      - "8081:8081"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  localstack:
    image: localstack/localstack
    ports:
      - "4566:4566"
    environment:
      - SERVICES=s3,dynamodb
      - DEFAULT_REGION=us-west-2
    volumes:
      - localstack_data:/var/lib/localstack

volumes:
  localstack_data:
```

## Environment Variables

### treven-web/.env.local
```
NEXT_PUBLIC_API_URL=http://localhost:8080
NEXT_PUBLIC_WS_URL=ws://localhost:8081
NEXT_PUBLIC_COGNITO_USER_POOL_ID=local
NEXT_PUBLIC_COGNITO_CLIENT_ID=local
```

### treven-back/.env
```bash
# AWS credentials (required even for LocalStack)
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_REGION=us-west-2

# DynamoDB
DYNAMODB_TABLE=lon12-table
DYNAMODB_ENDPOINT=http://localhost:4566

# Redis
REDIS_URL=redis://localhost:6379

# S3
S3_BUCKET=treven-data-local
S3_ENDPOINT=http://localhost:4566
```

### treven-ai/.env
```bash
# AWS credentials (required even for LocalStack)
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY=test
AWS_REGION=us-west-2

# Bedrock
BEDROCK_MODEL_ID=anthropic.claude-sonnet-4-5-20250929-v1:0

# DynamoDB
DYNAMODB_TABLE=lon12-table
DYNAMODB_ENDPOINT=http://localhost:4566
```

## DynamoDB Table Setup

```bash
# Start LocalStack
docker-compose up -d localstack

# Create the DynamoDB table
docker exec treven-project-localstack-1 awslocal dynamodb create-table \
    --table-name lon12-table \
    --attribute-definitions \
        AttributeName=PK,AttributeType=S \
        AttributeName=SK,AttributeType=S \
    --key-schema \
        AttributeName=PK,KeyType=HASH \
        AttributeName=SK,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --region us-west-2

# Test DynamoDB connection from Rust
cd treven-back-db
AWS_ACCESS_KEY_ID=test AWS_SECRET_ACCESS_KEY=test \
DYNAMODB_ENDPOINT=http://localhost:4566 \
cargo run --bin treven-db-test
```

## Testing

```bash
# Frontend
cd treven-web && npm test

# Backend
cd treven-back && cargo test

# AI agents
cd treven-ai && uv run pytest
```

## LocalStack Setup

```bash
# Start LocalStack
docker-compose up -d localstack

# Create S3 bucket
docker exec treven-project-localstack-1 awslocal s3 mb s3://treven-data-local --region us-west-2

# Create DynamoDB table (single-table design)
docker exec treven-project-localstack-1 awslocal dynamodb create-table \
    --table-name lon12-table \
    --attribute-definitions \
        AttributeName=PK,AttributeType=S \
        AttributeName=SK,AttributeType=S \
    --key-schema \
        AttributeName=PK,KeyType=HASH \
        AttributeName=SK,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --region us-west-2

# Verify table created
docker exec treven-project-localstack-1 awslocal dynamodb list-tables --region us-west-2

# Scan table contents
docker exec treven-project-localstack-1 awslocal dynamodb scan \
    --table-name lon12-table \
    --region us-west-2
```

## DynamoDB Single-Table Key Patterns

| Entity | PK | SK |
|--------|----|----|
| Report | `ORG#<orgId>` | `REPORT#<reportId>` |
| Conversation | `ORG#<orgId>` | `CONVERSATION#<convId>` |
| Message | `ORG#<orgId>` | `MESSAGE#<convId>#<msgId>` |
| Trend | `TRENDS` | `TREND#<countryCode>#<trendId>` |

## Rust DynamoDB Usage

```rust
use treven_back_db::{create_client, Repository, ReportEntity};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Create client (auto-detects LocalStack via DYNAMODB_ENDPOINT)
    let client = create_client().await?;
    let repo = Repository::new(client);

    // Health check
    repo.health_check().await?;

    // Create a report
    let mut report = ReportEntity::new("org1", "report-123");
    report.title = "Labour Exploitation Report".to_string();
    repo.create_report(&report).await?;

    // Query reports
    let reports = repo.list_reports("org1").await?;

    Ok(())
}
```

**Reference:** [AWS SDK for Rust DynamoDB Examples](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_dynamodb_code_examples.html)
