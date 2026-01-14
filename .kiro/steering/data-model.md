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

## DynamoDB Tables (Document + Audit)

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

## RDS PostgreSQL Tables (Relational)

### users
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  org_id UUID NOT NULL REFERENCES organizations(id),
  cognito_sub VARCHAR(255) UNIQUE NOT NULL,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  role VARCHAR(50) NOT NULL, -- admin, analyst, viewer
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);
```

### organizations
```sql
CREATE TABLE organizations (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(50), -- fi, ngo, le
  settings JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### partners
```sql
CREATE TABLE partners (
  id UUID PRIMARY KEY,
  org_id UUID NOT NULL REFERENCES organizations(id),
  name VARCHAR(255) NOT NULL,
  type VARCHAR(50), -- fi, ngo, le
  contact_email VARCHAR(255),
  settings JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### report_access
```sql
CREATE TABLE report_access (
  id UUID PRIMARY KEY,
  report_id VARCHAR(255) NOT NULL,
  partner_id UUID REFERENCES partners(id),
  access_level VARCHAR(50), -- view, download
  granted_by UUID REFERENCES users(id),
  granted_at TIMESTAMPTZ DEFAULT NOW()
);
```

### report_versions
```sql
CREATE TABLE report_versions (
  id UUID PRIMARY KEY,
  report_id VARCHAR(255) NOT NULL,
  version INTEGER NOT NULL,
  content_hash VARCHAR(64),
  changes_summary TEXT,
  created_by UUID REFERENCES users(id),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(report_id, version)
);
```

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
