---
inclusion: always
---

# AWS Architecture

## Region Requirement

**Primary:** eu-west-2 (London)

All services must be deployed in London region for data residency.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         CloudFront                               │
│                    (Single Public URL)                           │
└─────────────────────┬───────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
   ┌─────────┐  ┌──────────┐  ┌─────────┐
   │ Next.js │  │   API    │  │   WS    │
   │ (S3/    │  │ Gateway  │  │  (ALB)  │
   │ Origin) │  │          │  │         │
   └─────────┘  └────┬─────┘  └────┬────┘
                     │             │
                     │   ┌─────────┘
                     │   │
                     ▼   ▼
              ┌──────────────────┐
              │   ECS/Fargate    │
              │  ┌────────────┐  │
              │  │ Rust API   │  │
              │  │ Rust WS    │  │
              │  └────────────┘  │
              └────────┬─────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
    ┌─────────┐  ┌──────────┐  ┌─────────┐
    │   S3   │  │ DynamoDB │  │   RDS   │
    │        │  │          │  │ Postgres│
    └─────────┘  └──────────┘  └────┬────┘
                                    │
                              ┌─────┴─────┐
                              │   Redis   │
                              │(ElastiCache)│
                              └───────────┘

              ┌──────────────────┐
              │  Amazon Bedrock  │
              │  ┌────────────┐  │
              │  │ AgentCore  │  │
              │  │  Runtime   │  │
              │  └────────────┘  │
              └──────────────────┘

              ┌──────────────────┐
              │     Cognito      │
              │   User Pools     │
              └──────────────────┘
```

## Service Configuration

### CloudFront
- Custom domain with HTTPS
- Origins: S3 (static), ALB (API/WS)
- WebSocket support enabled

### Cognito
- User Pools for authentication
- OAuth2/OIDC flow
- Custom claims for orgId (multi-tenant)

### API Gateway
- REST/HTTP endpoints
- Cognito authorizer
- Rate limiting

### ECS/Fargate
- Rust API service (port 8080)
- Rust WebSocket service (port 8081)
- Auto-scaling based on CPU/memory

### ECR
- Container images for services
- Lifecycle policies for cleanup

### S3
- `treven-data-{env}` bucket
- Presigned URLs for upload/download
- Encryption at rest (SSE-S3)
- Versioning enabled

### DynamoDB
- On-demand capacity
- Point-in-time recovery
- Encryption at rest

### RDS PostgreSQL
- db.t3.medium (start)
- Multi-AZ for production
- Automated backups
- Encryption at rest

### ElastiCache Redis
- cache.t3.micro (start)
- Cluster mode disabled
- Encryption in transit

### Bedrock
- Claude Opus 4.5 (primary)
- Gemini latest (secondary)
- AgentCore for agent runtime

## Security

- All data encrypted at rest
- TLS 1.2+ in transit
- VPC with private subnets for compute/data
- Security groups: least privilege
- IAM roles: least privilege
- Secrets in AWS Secrets Manager

## Cost Estimation

| Service | Estimated Monthly |
|---------|-------------------|
| CloudFront | $10-50 |
| Cognito | $5-20 |
| API Gateway | $10-30 |
| ECS/Fargate | $50-150 |
| S3 | $5-20 |
| DynamoDB | $10-50 |
| RDS | $50-100 |
| ElastiCache | $15-30 |
| Bedrock | $100-500 (usage) |
| **Total** | **$255-950/month** |

*Varies significantly based on usage and report generation volume*
