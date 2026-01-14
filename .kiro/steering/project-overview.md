---
inclusion: always
---

# Treven — Project Overview

## What is Treven?

Treven is an AWS-native, analyst-in-the-loop platform that helps **STOP THE TRAFFIK (STT)** transform large volumes of trafficking/exploitation data + trusted OSINT into **fast, evidence-backed Key Judgement (KJ) reports** without losing analytical quality or trust.

## Value Proposition

**Treven turns trafficking data + trusted OSINT into analyst-approved, evidence-linked Key Judgement reports in hours—not weeks—so partners can spot and disrupt exploitation earlier.**

## Maslow Mapping

- **Painkiller (primary):** Removes urgent operational pain for STT analysts (manual research + drafting is slow → limited output)
- **Vitamin (secondary):** Improves consistency, auditability, and partner usability
- **Safety needs:** Reduces real-world harm by accelerating credible intel to institutions that can disrupt exploitation
- **Esteem:** Analysts keep control (review/approve), improving trust and confidence
- **Self-actualization:** Enables STT to scale impact (more routes/sectors/countries covered per month)

## Main User Conflict

Analysts need **speed at scale** *without* sacrificing **accuracy, transparency, source traceability, and PII safety**.

## Repository Structure

```
treven-project/
├── treven-web/      # NextJS (TypeScript, CSS Modules)
├── treven-back/     # Rust (WebSockets + realtime + REST)
├── treven-back-db/  # Rust (PostgreSQL, RDS AWS, Redis)
├── treven-ai/       # Python (Strands Agents SDK + Bedrock)
└── docs/            # Documentation
```

## Non-Negotiable Requirements

1. **Human-in-the-loop:** No report export without explicit analyst approval
2. **Source traceability:** Every claim must have a citation (URL or dataset reference)
3. **PII enforcement:** Detect and redact PII before storing/showing/exporting
4. **Security:** Deploy in AWS Oregon (us-west-2), encrypt at rest + in transit
5. **Multi-tenant isolation:** Enforce org isolation at API, DB, and S3 layers
