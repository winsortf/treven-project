---
inclusion: fileMatch
fileMatchPattern: "**/api/**"
---

# API Contracts

## REST Endpoints

### Authentication
All endpoints require `Authorization: Bearer <jwt>` header.
JWT contains `orgId` claim for multi-tenant isolation.

### Reports

#### List Reports
```
GET /api/reports
Query: ?status=draft|in_review|approved&country=UK&limit=20&cursor=xxx

Response 200:
{
  "reports": [
    {
      "id": "rpt_xxx",
      "title": "LABOUR EXPLOITATION IN UK AGRICULTURE",
      "country": "UK",
      "sector": "Agriculture",
      "status": "draft",
      "version": 1,
      "wordCount": 2450,
      "createdAt": "2026-01-14T10:00:00Z",
      "updatedAt": "2026-01-14T12:00:00Z"
    }
  ],
  "nextCursor": "xxx"
}
```

#### Get Report
```
GET /api/reports/:id

Response 200:
{
  "id": "rpt_xxx",
  "title": "...",
  "status": "draft",
  "version": 1,
  "content": {
    "titleBlock": {...},
    "keyJudgements": [...],
    "introduction": [...],
    "recruitment": [...],
    "demand": [...],
    "money": [...],
    "redFlags": [...],
    "informationRequirements": [...]
  },
  "citations": [...],
  "headlineCards": [...],
  "metadata": {...}
}
```

#### Create Report
```
POST /api/reports
Body:
{
  "country": "UK",
  "sector": "Agriculture",
  "exploitationType": "labour",
  "timeRange": "12m",
  "clientType": "fi"
}

Response 201:
{
  "id": "rpt_xxx",
  "status": "generating"
}
```

#### Update Report Section
```
PATCH /api/reports/:id/sections/:section
Body:
{
  "content": [...],
  "reason": "Analyst edit"
}

Response 200:
{
  "version": 2,
  "updatedAt": "..."
}
```

#### Approve Report
```
POST /api/reports/:id/approve
Body:
{
  "notes": "Reviewed and approved"
}

Response 200:
{
  "status": "approved",
  "approvedBy": "user_xxx",
  "approvedAt": "..."
}
```

#### Export Report
```
POST /api/reports/:id/export
Body:
{
  "format": "pdf|docx|md"
}

Response 200:
{
  "downloadUrl": "https://...",
  "expiresAt": "..."
}
```

### Conversations

#### Create Conversation
```
POST /api/conversations
Body:
{
  "context": {
    "country": "UK",
    "sector": "Agriculture"
  }
}

Response 201:
{
  "id": "conv_xxx"
}
```

#### Send Message
```
POST /api/conversations/:id/messages
Body:
{
  "content": "Generate a report on UK agriculture"
}

Response 200:
{
  "messageId": "msg_xxx",
  "status": "processing"
}
```

### Trends

#### Get Trends
```
GET /api/trends
Query: ?country=UK&exploitationType=labour

Response 200:
{
  "trends": [
    {
      "id": "trend_xxx",
      "title": "Rising labour exploitation in UK farms",
      "country": "UK",
      "confidence": "high",
      "sources": [...],
      "tags": ["recruitment", "agriculture"],
      "updatedAt": "..."
    }
  ]
}
```

### Sources

#### Search Sources
```
POST /api/sources/search
Body:
{
  "query": "UK agriculture labour exploitation",
  "country": "UK",
  "timeRange": "12m",
  "limit": 20
}

Response 200:
{
  "sources": [
    {
      "id": "src_xxx",
      "title": "...",
      "publisher": "ILO",
      "url": "https://...",
      "publishedDate": "...",
      "trustScore": 85,
      "summary": "..."
    }
  ]
}
```

## WebSocket Protocol

### Connection
```
ws://api.treven.io/ws?token=<jwt>
```

### Message Types

#### Client → Server
```json
{"type": "subscribe", "channel": "report:rpt_xxx"}
{"type": "unsubscribe", "channel": "report:rpt_xxx"}
{"type": "chat", "conversationId": "conv_xxx", "content": "..."}
```

#### Server → Client
```json
{"type": "report:update", "reportId": "rpt_xxx", "section": "recruitment", "content": [...]}
{"type": "chat:response", "conversationId": "conv_xxx", "content": "...", "done": false}
{"type": "chat:tool", "conversationId": "conv_xxx", "tool": "search_sources", "status": "running"}
{"type": "agent:status", "runId": "run_xxx", "status": "completed"}
```

## Error Responses

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Report not found",
    "details": {}
  }
}
```

| Code | HTTP Status |
|------|-------------|
| UNAUTHORIZED | 401 |
| FORBIDDEN | 403 |
| NOT_FOUND | 404 |
| VALIDATION_ERROR | 400 |
| PII_DETECTED | 422 |
| INTERNAL_ERROR | 500 |
