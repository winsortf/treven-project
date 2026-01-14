---
inclusion: always
---

# Data Model

## Multi-Tenant Rules

- Every record MUST include `orgId`
- Enforce org isolation at:
  - API layer (JWT claim check)
  - DB partitioning (orgId keys)
  - S3 path prefix (`orgId/...`)

## DynamoDB Single-Table Design

All data is stored in a single DynamoDB table using composite primary keys (PK/SK pattern) for efficient querying and multi-tenant isolation.

### Table: lon12-table

**Region:** us-west-2

### Organizations
```json
{
  "PK": "ORG#<orgId>",
  "SK": "METADATA",
  "orgId": "string",
  "name": "string",
  "policy": "object",
  "createdAt": "ISO8601",
  "updatedAt": "ISO8601"
}
```

### Conversations
```json
{
  "PK": "ORG#<orgId>",
  "SK": "CONV#<conversationId>",
  "conversationId": "string",
  "userId": "string",
  "status": "active|archived",
  "context": {
    "country": "string",
    "sector": "string",
    "timeRange": "string"
  },
  "createdAt": "ISO8601",
  "updatedAt": "ISO8601"
}
```

### Messages
```json
{
  "PK": "ORG#<orgId>#CONV#<conversationId>",
  "SK": "MSG#<timestamp>",
  "messageId": "string",
  "role": "user|assistant|system",
  "content": "string",
  "contentRef": "s3://...",
  "toolCalls": ["array"],
  "citations": ["array"],
  "createdAt": "ISO8601"
}
```

### AgentRuns
```json
{
  "PK": "ORG#<orgId>",
  "SK": "RUN#<runId>",
  "runId": "string",
  "conversationId": "string",
  "agentType": "scraper|generator|summarise|social|pii",
  "model": "string",
  "toolsUsed": ["array"],
  "inputTokens": "number",
  "outputTokens": "number",
  "durationMs": "number",
  "status": "running|completed|failed",
  "createdAt": "ISO8601"
}
```

### ReportsIndex
```json
{
  "PK": "ORG#<orgId>",
  "SK": "REPORT#<reportId>",
  "reportId": "string",
  "title": "string",
  "country": "string",
  "sector": "string",
  "exploitationType": "string",
  "status": "draft|in_review|approved|exported",
  "version": "number",
  "wordCount": "number",
  "s3Keys": {
    "markdown": "string",
    "pdf": "string",
    "docx": "string"
  },
  "approvedBy": "string",
  "approvedAt": "ISO8601",
  "createdAt": "ISO8601",
  "updatedAt": "ISO8601"
}
```

### Sources
```json
{
  "PK": "ORG#<orgId>",
  "SK": "SOURCE#<sourceId>",
  "sourceId": "string",
  "url": "string",
  "title": "string",
  "publisher": "string",
  "publishedDate": "ISO8601",
  "trustScore": "number",
  "summary": "string",
  "tags": ["array"],
  "createdAt": "ISO8601"
}
```

### Users
```json
{
  "PK": "ORG#<orgId>",
  "SK": "USER#<userId>",
  "userId": "string",
  "cognitoSub": "string",
  "email": "string",
  "name": "string",
  "role": "admin|analyst|viewer",
  "createdAt": "ISO8601",
  "updatedAt": "ISO8601"
}
```

### Partners
```json
{
  "PK": "ORG#<orgId>",
  "SK": "PARTNER#<partnerId>",
  "partnerId": "string",
  "name": "string",
  "type": "fi|ngo|le",
  "contactEmail": "string",
  "settings": "object",
  "createdAt": "ISO8601"
}
```

### ReportAccess
```json
{
  "PK": "ORG#<orgId>#REPORT#<reportId>",
  "SK": "ACCESS#<partnerId>",
  "accessLevel": "view|download",
  "grantedBy": "string",
  "grantedAt": "ISO8601"
}
```

### ReportVersions
```json
{
  "PK": "ORG#<orgId>#REPORT#<reportId>",
  "SK": "VERSION#<version>",
  "version": "number",
  "contentHash": "string",
  "changesSummary": "string",
  "createdBy": "string",
  "createdAt": "ISO8601"
}
```

### AuditLogs
```json
{
  "PK": "ORG#<orgId>",
  "SK": "AUDIT#<timestamp>#<eventId>",
  "eventId": "string",
  "eventType": "string",
  "userId": "string",
  "resourceType": "string",
  "resourceId": "string",
  "action": "string",
  "details": "object",
  "createdAt": "ISO8601"
}
```

## Global Secondary Indexes (GSIs)

### GSI1: User Lookup by Cognito Sub
- **PK:** `cognitoSub`
- **SK:** `orgId`
- **Use:** Find user by Cognito identity

### GSI2: Reports by Status
- **PK:** `ORG#<orgId>`
- **SK:** `status#<updatedAt>`
- **Use:** List reports filtered by status

## S3 Structure

```
s3://treven-data-{env}/
├── {orgId}/
│   ├── reports/
│   │   └── {reportId}/
│   │       ├── v{version}/
│   │       │   ├── report.md
│   │       │   ├── report.pdf
│   │       │   └── report.docx
│   │       └── evidence/
│   │           └── {sourceId}.json
│   ├── uploads/
│   │   └── {uploadId}/
│   │       └── {filename}
│   └── exports/
│       └── {exportId}/
│           └── bundle.zip
```
