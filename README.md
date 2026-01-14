# Treven - Intelligence Platform

AI-powered trafficking intelligence platform by STOP THE TRAFFIK. Transforms large volumes of trafficking data + trusted OSINT into analyst-approved, evidence-linked Key Judgement reports.

## Quick Start

### Prerequisites
- Node.js 20+
- Rust 1.75+
- Python 3.11+
- Docker & Docker Compose

### Local Development

```bash
# Start all services with Docker
docker-compose up -d

# Or run individually:

# Frontend (port 3000)
cd treven-web && npm install && npm run dev

# Backend API (port 8080)
cd treven-back && cargo run

# AI Agents
cd treven-ai && uv sync && uv run python main.py
```

### Environment Setup

Copy example env files:
```bash
cp treven-web/.env.local.example treven-web/.env.local
cp treven-back/.env.example treven-back/.env
cp treven-ai/.env.example treven-ai/.env
```

## Project Structure

```
treven-project/
├── treven-web/        # Next.js frontend (TypeScript, CSS Modules)
├── treven-back/       # Rust backend (Axum, WebSockets)
├── treven-back-db/    # Database migrations (PostgreSQL)
├── treven-ai/         # AI agents (Python, Strands SDK, Bedrock)
└── docs/              # Documentation
```

## Core Features

### Screens
- **Trends Map** - Global/country trend discovery with trusted sources
- **Intel Chat** - Conversational agent interface for report generation
- **Report Studio** - Analyst workspace for review/edit/approve
- **Partners** - Manage organizations and report access
- **To-Do** - Recommended reports based on trend changes

### AI Agents
- **Scraper Agent** - OSINT collection from trusted sources
- **Report Generator** - Key Judgement report drafting
- **Summarise Agent** - Executive summaries and change tracking
- **Social Media Agent** - Safe social copy generation
- **Policy Agent** - PII detection and enforcement

### Key Requirements
- Human-in-the-loop: No export without analyst approval
- Source traceability: Every claim has a citation
- PII compliance: Detection and redaction before persistence
- Multi-tenant: Organization isolation at all layers

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 14+, TypeScript, CSS Modules |
| Backend | Rust, Axum, WebSockets |
| Database | PostgreSQL (RDS), DynamoDB, Redis |
| AI | Strands Agents SDK, Amazon Bedrock |
| Cloud | AWS (eu-west-2 London) |

## AWS Architecture

- CloudFront (CDN + single URL)
- Cognito (Authentication)
- API Gateway + ECS/Fargate
- S3 (Files, reports, evidence)
- DynamoDB (Documents, audit)
- RDS PostgreSQL (Relational data)
- Amazon Bedrock (LLM inference)

## License

Proprietary - STOP THE TRAFFIK
