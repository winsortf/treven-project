---
inclusion: always
---

# Version Management Rules

## MANDATORY: Always Use Latest Stable/LTS Versions

**This rule applies to ALL dependency management across the entire project.**

### CRITICAL: Version Verification Process

**BEFORE adding ANY dependency, you MUST:**

1. **FETCH the official source DIRECTLY** - Do NOT rely on web search results which may be cached/outdated
2. **Use WebFetch tool** to check the OFFICIAL package registry:
   - **Rust crates**: `https://crates.io/api/v1/crates/<package-name>`
   - **Python**: `https://pypi.org/project/<package-name>/`
   - **npm**: `https://www.npmjs.com/package/<package-name>`
3. **Extract the EXACT current version** from the official page
4. **Record the verification date** (YYYY-MM-DD format)
5. **NEVER trust cached search results** - always verify directly

### Before Adding Any Dependency

1. **ALWAYS fetch from official registry** at the EXACT time of the request
2. **NEVER use outdated versions** - verify against official source
3. **NEVER downgrade** existing dependency versions unless critical compatibility issue
4. **Document the version** with the EXACT date it was verified

---

## Treven Project Versions (Verified: 2026-01-14)

### Rust (treven-back, treven-back-db)

**Rust Edition**: 2024 (requires Rust 1.85+)

| Crate | Version | Purpose |
|-------|---------|---------|
| tokio | 1.49.0 | Async runtime |
| axum | 0.8.8 | Web framework |
| tower | 0.5.3 | Service abstractions |
| tower-http | 0.6.8 | HTTP middleware |
| serde | 1.0.228 | Serialization |
| serde_json | 1.0.149 | JSON |
| aws-config | 1.8.12 | AWS configuration |
| aws-sdk-dynamodb | 1.101.0 | DynamoDB client |
| aws-sdk-s3 | 1.119.0 | S3 client |
| aws-sdk-bedrockruntime | 1.120.0 | Bedrock client |
| serde_dynamo | 4.3.0 | DynamoDB serialization |
| redis | 1.0.2 | Redis client |
| jsonwebtoken | 10.2.0 | JWT handling |
| uuid | 1.19.0 | UUIDs |
| chrono | 0.4.42 | Date/time |
| thiserror | 2.0.17 | Error handling |
| anyhow | 1.0.100 | Error handling |
| tracing | 0.1.44 | Logging |
| tracing-subscriber | 0.3.22 | Log subscriber |
| dotenvy | 0.15.7 | Environment |
| futures | 0.3.31 | Futures utilities |
| tokio-tungstenite | 0.28.0 | WebSocket |

### Frontend (treven-web)

| Package | Version | Purpose |
|---------|---------|---------|
| next | 16.1.1 | React framework |
| react | 19.2.3 | UI library |
| react-dom | 19.2.3 | React DOM |
| typescript | 5.9.3 | Type safety |
| @emotion/react | 11.14.0 | CSS-in-JS |
| @emotion/styled | 11.14.1 | Styled components |
| @mui/material | 7.3.7 | Material UI |
| @mui/icons-material | 7.3.7 | Material Icons |
| @types/node | 25.0.8 | Node types |
| @types/react | 19.2.8 | React types |
| @types/react-dom | 19.2.3 | ReactDOM types |
| eslint | 9.39.2 | Linting |
| eslint-config-next | 16.1.1 | Next.js ESLint |

### Python (treven-ai)

**Runtime**: Python 3.12+
**Package Manager**: uv
**Primary AI Framework**: Strands Agents (AWS Bedrock)

| Package | Version | Purpose |
|---------|---------|---------|
| strands-agents | 1.22.0 | Agent Development Kit |
| boto3 | 1.42.27 | AWS SDK |
| httpx | 0.28.1 | Async HTTP client |
| beautifulsoup4 | 4.14.3 | HTML parsing |
| lxml | 6.0.2 | XML/HTML processing |
| pydantic | 2.12.5 | Data validation |
| PyPDF2 | 3.0.1 | PDF processing |
| pytest | 9.0.2 | Testing |
| ruff | 0.14.11 | Linting |
| pytest-asyncio | 1.3.0 | Async testing |

### Docker Images

| Image | Tag | Purpose |
|-------|-----|---------|
| rust | 1-slim-bookworm | Rust build |
| debian | bookworm-slim | Runtime |
| python | 3.12-slim-bookworm | Python runtime |
| node | 22-alpine | Node.js build |

---

## UV Commands Reference (treven-ai)

```bash
uv sync              # Install dependencies from lockfile
uv add <pkg>         # Add dependency
uv add --dev <pkg>   # Add dev dependency
uv run <cmd>         # Run command in venv
uv lock --upgrade    # Update all dependencies
```

## Version Documentation Format

When adding dependencies, document:

```
# Added: <package-name> v<version>
# Verified: <YYYY-MM-DD>
# Source: <crates.io/pypi/npm>
```

## Lock File Management

### JavaScript (treven-web)
- **package-lock.json**: MUST be committed
- Use `npm ci` in CI/CD (not `npm install`)
- Run `npm outdated` weekly to check for updates
- Run `npm audit` to check for vulnerabilities

### Rust (treven-back, treven-back-db)
- **Cargo.lock**: MUST be committed
- Use `cargo update` to update dependencies
- Run `cargo audit` for security vulnerabilities

### Python (treven-ai)
- **uv.lock**: MUST be committed (using uv package manager)
- Use `uv sync` to install dependencies
- Pin all production dependencies

## Dependency Audit Commands

```bash
# JavaScript
npm outdated
npm audit

# Rust
cargo outdated  # requires cargo-outdated
cargo audit     # requires cargo-audit

# Python
uv pip list --outdated
pip-audit       # requires pip-audit
```

## Compatibility Matrix

| Component | Node.js | Rust | Python | AWS SDK |
|-----------|---------|------|--------|---------|
| treven-web | 22.x | - | - | - |
| treven-back | - | 1.85+ | - | 1.x |
| treven-back-db | - | 1.85+ | - | 1.x |
| treven-ai | - | - | 3.12+ | boto3 1.x |
