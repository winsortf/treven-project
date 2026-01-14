---
inclusion: always
---

# Local Development

## Prerequisites

- Docker & Docker Compose
- Node.js 20+
- Rust 1.75+
- Python 3.11+
- uv (Python package manager)
- AWS CLI (for LocalStack commands)

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
      - AWS_REGION=eu-west-2

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
      - DEFAULT_REGION=eu-west-2
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
```
DYNAMODB_ENDPOINT=http://localhost:4566
DYNAMODB_TABLE=treven-main
REDIS_URL=redis://localhost:6379
AWS_REGION=eu-west-2
S3_BUCKET=treven-data-local
S3_ENDPOINT=http://localhost:4566
```

### treven-ai/.env
```
AWS_REGION=eu-west-2
BEDROCK_MODEL_ID=anthropic.claude-opus-4-5
```

## DynamoDB Table Setup

```bash
cd treven-back-db

# Create tables (runs against LocalStack)
cargo run -- setup-tables

# Seed sample data (optional)
cargo run -- seed
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
# Create S3 bucket
aws --endpoint-url=http://localhost:4566 s3 mb s3://treven-data-local

# Create main DynamoDB table
aws --endpoint-url=http://localhost:4566 dynamodb create-table \
  --table-name treven-main \
  --attribute-definitions \
    AttributeName=PK,AttributeType=S \
    AttributeName=SK,AttributeType=S \
    AttributeName=cognitoSub,AttributeType=S \
    AttributeName=GSI2SK,AttributeType=S \
  --key-schema \
    AttributeName=PK,KeyType=HASH \
    AttributeName=SK,KeyType=RANGE \
  --global-secondary-indexes \
    '[
      {
        "IndexName": "GSI1-CognitoSub",
        "KeySchema": [{"AttributeName": "cognitoSub", "KeyType": "HASH"}, {"AttributeName": "PK", "KeyType": "RANGE"}],
        "Projection": {"ProjectionType": "ALL"}
      },
      {
        "IndexName": "GSI2-Status",
        "KeySchema": [{"AttributeName": "PK", "KeyType": "HASH"}, {"AttributeName": "GSI2SK", "KeyType": "RANGE"}],
        "Projection": {"ProjectionType": "ALL"}
      }
    ]' \
  --billing-mode PAY_PER_REQUEST

# Verify table created
aws --endpoint-url=http://localhost:4566 dynamodb describe-table --table-name treven-main
```
