---
inclusion: always
---

# AI Agents Specification

## Required Agents

### A) Scraper / OSINT Collector Agent

**Purpose:** Pull latest trusted sources for selected scenario

**Inputs:**
- Country/region
- Sector/theme
- Time range (default: last 6–12 months)
- Exploitation type

**Outputs:**
- Ranked source list with:
  - Title, publisher, date, URL
  - Short summary
  - Trust score
  - Citation reference

**Trusted Sources:**
- Government reports (State Dept TIP reports)
- UN/ILO publications
- NGO reports
- Business & Human Rights Resource Centre
- Quality journalism (verified outlets)

### B) Report Generator Agent

**Purpose:** Produce full KJ report draft + headline cards

**Inputs:**
- Collected sources from OSINT agent
- STT dataset references
- Country/sector/time parameters
- Client type (FI, NGO, LE)

**Outputs:**
- Full KJ report following exact structure
- 3 headline cards (Recruitment/Demand/Money)
- "Why we think this" reasoning for each judgement
- Citation links for every factual claim
- Uncertainty flags where confidence is low

**Constraints:**
- 2,000–3,000 words total
- Key Judgements fit on one page
- No PII in output

### C) Summarise Agent

**Purpose:** Create summaries and change tracking

**Outputs:**
- Executive summary
- Section summaries
- Change summaries between versions
- Diff highlights

### D) Social Media Agent

**Purpose:** Generate safe social copy

**Inputs:**
- Approved report content only

**Outputs:**
- 1–2 line LinkedIn-ready summary
- Must be: non-sensitive, high-level, no PII, no operationally risky detail

**Constraints:**
- Only runs on analyst-approved content
- PII check before output

### E) Policy Agent (PII)

**Purpose:** Detect and redact PII

**Detects:**
- Full names
- Email addresses
- Phone numbers
- Physical addresses
- SSN/ID numbers
- Dates of birth
- IP addresses
- Credit card numbers
- Passport/license numbers
- Biometric data references

**Actions:**
- Flag detected PII
- Block persistence/export until clean
- Require analyst confirmation to keep/redact
- Log all PII decisions for audit

## Agent Configuration

```python
# Model preferences
PRIMARY_MODEL = "anthropic.claude-opus-4-5"
SECONDARY_MODEL = "google.gemini-latest"

# Bedrock region
AWS_REGION = "us-west-2"  # London

# Agent runtime
RUNTIME = "bedrock-agentcore"
```

## Tool Calling

Agents can call:
- `search_osint` - Web search for trusted sources
- `query_stt_dataset` - Query STT internal data
- `detect_pii` - Run PII detection
- `generate_citation` - Create citation reference
- `calculate_confidence` - Assess claim confidence
- `store_evidence` - Save to evidence pack
