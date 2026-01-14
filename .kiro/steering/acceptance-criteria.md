---
inclusion: always
---

# Acceptance Criteria

## Definition of Done

### Core Functionality

- [ ] Trends map loads and displays country trends with citations
- [ ] Chat can trigger agent workflows and persists conversation history
- [ ] Report Studio supports edit + version diff + approval gate
- [ ] No export without explicit analyst approval
- [ ] Every claim has a citation/reference (or is removed)
- [ ] PII policy blocks persistence/export until redacted
- [ ] OSINT discovery respects trusted-source controls
- [ ] All artifacts persisted (S3 + DB), with audit logs
- [ ] Runs on AWS London region by default
- [ ] CI/CD deploys web + services reliably

### Human-in-the-Loop

- [ ] Analyst can review all AI-generated content
- [ ] Analyst can edit any section
- [ ] Analyst can reject/regenerate sections
- [ ] Version history tracks all changes
- [ ] Diff viewer shows changes between versions
- [ ] Explicit "Approve & Export" required for final output

### Source Traceability

- [ ] Every factual claim has inline citation
- [ ] Citations link to source URL or dataset reference
- [ ] Hover/click reveals full source details
- [ ] Evidence pack downloadable per report

### PII Compliance

- [ ] PII detection runs on all content
- [ ] Flagged PII blocks save/export
- [ ] Analyst can confirm redaction or keep with justification
- [ ] All PII decisions logged for audit

### Multi-Tenant Security

- [ ] orgId enforced on all API calls
- [ ] orgId in all DB keys
- [ ] orgId prefix on all S3 paths
- [ ] Users can only see their org's data

### Report Quality

- [ ] Reports follow exact KJ structure
- [ ] Word count within 2,000-3,000 limit
- [ ] Key Judgements fit on one page
- [ ] 3 headline cards generated
- [ ] Disclaimer included
- [ ] Information Requirements section populated

### Performance

- [ ] Map loads in < 3 seconds
- [ ] Chat responses stream in real-time
- [ ] Report generation < 5 minutes
- [ ] Export generation < 30 seconds

## Hackathon Demo Checklist

1. [ ] Show Trends Map with real/sample data
2. [ ] Demonstrate Chat → Report workflow
3. [ ] Show Report Studio editing + approval
4. [ ] Export PDF with citations
5. [ ] Show PII detection blocking export
6. [ ] Demonstrate multi-tenant isolation
7. [ ] Show audit logs
