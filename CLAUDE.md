# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## ⛔ CRITICAL RULE: NO AI ATTRIBUTION IN COMMITS

**THIS IS MANDATORY - VIOLATION IS NOT ACCEPTABLE**

When creating git commits, Claude Code must:

1. **NEVER add `Co-Authored-By:` lines** - No AI co-author attribution of any kind
2. **NEVER mention Claude, GPT, Copilot, or any AI** in commit messages
3. **NEVER add AI credits, signatures, or references** anywhere in commits
4. **The git author is ONLY the human developer** who requested the changes

### ❌ WRONG - Never do this:
```
Feat ( API ) Add endpoint ( JO202601150200 )

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### ✅ CORRECT - Always do this:
```
Feat ( API ) Add endpoint ( JO202601150200 )
```

**Why?** The human developer owns the code and the commit history. AI assistance is a tool, not a co-author.

---

## Build and Run Commands

```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py

# Run with development dependencies
uv sync --dev

# Lint code
uv run ruff check src/

# Fix lint issues
uv run ruff check --fix src/

# Run tests
uv run pytest

# Docker build
docker build -t treven-ai .

# Docker compose
docker compose up
```

## Git Commit Standard

### Format
```
{Type} ( {Scope} ) {Short description} ( {User Story ID | Fallback ID} )
```

### Fallback ID Format
`{USER_ID}{YYYYMMDDHHMM}` - Example: `JO202601150200`

### Allowed Types
| Type | Description |
|------|-------------|
| `Build` | Build-related changes (dependencies, docker) |
| `Chore` | Maintenance not visible to end users |
| `Feat` | New feature |
| `Fix` | Bug fix |
| `Docs` | Documentation changes |
| `Refactor` | Code change that neither fixes nor adds feature |
| `Perf` | Performance improvements |
| `Style` | Styling-only changes |
| `Test` | Adding or updating tests |
| `Layout` | Adding new components or layout work |

### Examples
```
Feat ( Agents ) Add topic prioritization agent ( JO202601150130 )
Fix ( Tools ) Correct S3 upload path handling ( AMT-42 )
Chore ( Config ) Update dependencies ( JO202601150200 )
```

### ⛔ PROHIBITED - No AI Attribution (See Critical Rule Above)
- **NEVER** add `Co-Authored-By:` lines for AI assistants (Claude, GPT, Copilot, etc.)
- **NEVER** add any AI attribution, credits, or mentions in commit messages
- **NEVER** add signatures like `Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>`
- Commits must ONLY have the human developer as author
- This rule is NON-NEGOTIABLE - always check commit message before executing

## Coding Principles

### Core Principles
- **KISS** - Keep It Simple, Stupid
- **DRY** - Don't Repeat Yourself
- **YAGNI** - You Aren't Gonna Need It
- **SOLID** - Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **SOC** - Separation of Concerns

### Clean Code
- Meaningful names for variables, functions, components
- Functions should be small and do one thing
- Comments explain "why", not "what"
- Consistent formatting and style

## Version Management Rules

### MANDATORY: Always Use Latest Stable Versions

**BEFORE adding ANY dependency:**
1. **FETCH from official registry** - Do NOT rely on cached search results
2. **Verify sources:**
   - Python: `https://pypi.org/project/<package-name>/`
   - Rust: `https://crates.io/api/v1/crates/<package-name>`
   - npm: `https://www.npmjs.com/package/<package-name>`
3. **Record verification date** (YYYY-MM-DD format)
4. **NEVER downgrade** existing versions unless critical compatibility issue

### Python (treven-ai) - Verified: 2026-01-14
- **Runtime**: Python 3.12+
- **Package Manager**: uv
- **Primary Model**: Claude Sonnet 4.5 via Bedrock

| Package | Version | Purpose |
|---------|---------|---------|
| strands-agents | >=1.22.0 | Agent SDK |
| boto3 | >=1.42.27 | AWS SDK |
| httpx | >=0.28.1 | HTTP client |
| pydantic | >=2.12.5 | Validation |
| reportlab | >=4.4.1 | PDF generation |
| python-docx | >=1.1.2 | DOCX generation |
| ruff | >=0.14.11 | Linting |
| pytest | >=9.0.2 | Testing |

## Python Coding Standards

### File Structure
```
src/
├── agents/          # Agent definitions
├── tools/           # Agent tools (@tool decorated)
├── api/             # HTTP client for treven-back
├── db/              # Database models
└── config.py        # Configuration
```

### Naming Conventions
- Modules: `snake_case` (`report_generator.py`)
- Classes: `PascalCase` (`ReportGenerator`)
- Functions: `snake_case` (`generate_report`)
- Constants: `SCREAMING_SNAKE_CASE` (`MAX_TOKENS`)

### Type Hints Required
```python
from typing import Optional, List, Dict

async def generate_report(request: ReportRequest) -> Dict:
    ...
```

### Agent Pattern
```python
class SomeAgent:
    def __init__(self):
        session = boto3.Session(region_name=AWS_REGION)
        self.model = BedrockModel(
            model_id=PRIMARY_MODEL,
            boto_session=session,
        )
        self.agent = Agent(
            name="agent_name",
            model=self.model,
            system_prompt=SYSTEM_PROMPT,
            tools=[tool1, tool2],
        )
```

### Tool Pattern
```python
from strands import tool

@tool
def my_tool(param: str) -> Dict:
    """Tool description for the agent."""
    ...
```

## Non-Negotiable Requirements

1. **Human-in-the-loop** - No report export without explicit analyst approval
2. **Source traceability** - Every claim must have a citation (URL or dataset reference)
3. **PII enforcement** - Detect and redact PII before storing/showing/exporting
4. **Security** - Deploy in AWS Oregon (us-west-2), encrypt at rest + in transit
5. **Multi-tenant isolation** - Enforce org isolation at API, DB, and S3 layers

## PII Policy - Hard Gate

### Must Detect and Redact
- Full names, email addresses, phone numbers
- Physical addresses, SSN/ID numbers
- Dates of birth, IP addresses
- Credit card numbers, passport/license numbers

### Rules
1. Scan ALL content before storing, exporting, or showing to users
2. Block persistence/export until PII is redacted
3. Log all PII decisions for audit

### Redaction Format
```
Names → [NAME]     Emails → [EMAIL]
Phone → [PHONE]    Address → [ADDRESS]
SSN/ID → [ID]      DOB → [DOB]
```

## Trusted Sources Hierarchy

### Tier 1 - Primary (Highest Trust)
- **Government**: US State Dept TIP, UK Modern Slavery Report, EU Anti-Trafficking
- **UN agencies**: UNODC, ILO, UNICEF, IOM, OSCE
- **Academic**: Walk Free Foundation, Polaris Project, Anti-Slavery International

### Tier 2 - Trusted Secondary
- **NGOs**: Human Rights Watch, Amnesty International, La Strada, ECPAT, Freedom Fund
- **Industry**: Business & Human Rights Resource Centre, KnowTheChain
- **Journalism**: Reuters, BBC, Guardian, AP, Al Jazeera, Financial Times

### Tier 3 - Use with Verification
- Regional NGOs (cross-reference required)
- Local news (verify outlet reputation)

### Never Use (Blocklist)
- Unverified social media posts
- Anonymous blogs
- Known disinformation sources
- Sources with clear political bias on trafficking

## Key Judgement Report Format

### Report Structure (must follow exactly)
1. **Title Block** - Country, sector, date, overview
2. **Key Judgements** - "We assess as follows:" + 5-10 lettered bullets
3. **Disclaimer** (fixed text)
4. **INTRODUCTION** - Context, scale, scope
5. **RECRUITMENT** - Who, how, where, by whom
6. **DEMAND** - Drivers, locations, cross-border aspects
7. **MONEY** - Payment forms, distribution, flows, patterns
8. **RED FLAG INDICATORS** - 5-10 behaviour-based indicators for FIs
9. **INFORMATION REQUIREMENTS** - Numbered gaps/questions

### Constraints
- **Total**: 2,000-3,000 words
- **Key Judgements**: Must fit on ONE page (max 10)
- **Citations**: Every factual claim MUST have citation [1], [2], etc.
- **PII**: NO PII in output
- **Headline Cards**: 3 required (Recruitment, Demand, Money)

### Fixed Disclaimer
> "This assessment is based on a combination of open-source research, input from subject-matter experts on the ground, accounts by those with lived experience, and data analysis."

## Architecture

### Service Communication
```
treven-ai (this) → HTTP → treven-back → DynamoDB/S3
```

- **API client**: `src/api/client.py`
- **Backend URL**: `TREVEN_API_URL` env variable
- **DynamoDB Table**: `lon12-table`
- **S3 Bucket**: `lon12-bucket`

### Agents (`src/agents/`)
| Agent | Purpose |
|-------|---------|
| ScraperAgent | OSINT collection with trusted source hierarchy |
| ReportGeneratorAgent | Key Judgement reports + PDF/DOCX export |
| TopicPrioritizationAgent | 5-question framework for topic selection |
| EducationContentAgent | School lessons, social media, infographics |
| SummariseAgent | Executive summaries |
| SocialMediaAgent | LinkedIn/Twitter content (requires approval) |
| PolicyAgent | PII detection and redaction |

### Tools (`src/tools/`)
| Tool | Purpose |
|------|---------|
| storage.py | S3 operations via treven-back API |
| document_export.py | PDF (ReportLab) / DOCX (python-docx) generation |
| pii_detector.py | PII pattern matching and redaction |
| report_generator.py | Report section generation helpers |
| osint_search.py | Source search and citation generation |

## Environment Variables

```bash
# AWS
AWS_REGION=us-west-2
AWS_ACCESS_KEY_ID=<key>
AWS_SECRET_ACCESS_KEY=<secret>

# Bedrock
BEDROCK_MODEL_ID=anthropic.claude-sonnet-4-5-20250929-v1:0

# Backend API
TREVEN_API_URL=http://lon12-backend-alb-1113535685.us-west-2.elb.amazonaws.com

# DynamoDB (local)
DYNAMODB_TABLE=lon12-table
DYNAMODB_ENDPOINT=http://localhost:4566
```

## Acceptance Criteria

### Core Requirements
- [ ] Every claim has a citation/reference (or is removed)
- [ ] PII policy blocks persistence/export until redacted
- [ ] No export without explicit analyst approval
- [ ] OSINT discovery respects trusted-source controls
- [ ] Reports follow exact KJ structure
- [ ] Word count within 2,000-3,000 limit
- [ ] 3 headline cards generated (Recruitment, Demand, Money)

### Performance
- [ ] Report generation < 5 minutes
- [ ] Export generation < 30 seconds
