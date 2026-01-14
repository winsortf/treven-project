---
inclusion: always
---

# Tech Stack

## Frontend: treven-web/

- **Framework:** Next.js 14+ with App Router
- **Language:** TypeScript (strict mode)
- **Styling:** CSS Modules (no Tailwind)
- **Icons:** Material UI Icons (https://mui.com/material-ui/material-icons/)
- **Real-time:** WebSocket client for bidirectional communication
- **State:** React Context + hooks (keep it simple)

## Backend API: treven-back/

- **Language:** Rust
- **WebSockets:** Real-time bidirectional communication
- **Framework:** Axum or Actix-web
- **Auth:** JWT validation (Cognito tokens)
- **Responsibilities:**
  - REST API endpoints
  - WebSocket connections
  - Agent orchestration calls
  - S3 presigned URL generation

## Database Layer: treven-back-db/

- **Language:** Rust
- **Primary DB:** Amazon DynamoDB (single-table design)
- **Cache:** Redis
- **SDK:** AWS SDK for Rust (aws-sdk-dynamodb)
- **Design:** Single-table with composite keys (PK/SK pattern)

## AI Agents: treven-ai/

- **Language:** Python 3.11+
- **Framework:** Strands Agents SDK (https://strandsagents.com/latest/)
- **Models:** Amazon Bedrock API
  - Primary: Claude Opus 4.5
  - Secondary: Gemini (latest via Bedrock)
- **Deployment:** Amazon Bedrock AgentCore Runtime

## AWS Services

| Service | Purpose |
|---------|---------|
| CloudFront | CDN + single public URL |
| Cognito | Authentication (OAuth2/OIDC) |
| API Gateway | REST endpoints + Cognito authorizer |
| ECS/Fargate | Container runtime |
| ECR | Container registry |
| S3 | Files, PDFs, reports, evidence |
| DynamoDB | Primary database (all data) |
| ElastiCache Redis | Caching |
| Bedrock | LLM inference |
| Bedrock AgentCore | Agent runtime |

## Local Development

```bash
# Docker Compose runs:
- Next.js web (port 3000)
- Rust API (port 8080)
- Rust WebSocket (port 8081)
- PostgreSQL (port 5432)
- Redis (port 6379)
- LocalStack (S3 emulation)
```

## CI/CD

- **Platform:** GitHub Actions
- **IaC:** Terraform
- **Pipeline:** Build → Test → Push to ECR → Deploy ECS
