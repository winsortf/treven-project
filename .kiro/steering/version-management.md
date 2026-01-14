---
inclusion: always
---

# Version Management

## Semantic Versioning (SemVer)

All projects follow [Semantic Versioning 2.0.0](https://semver.org/):

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: Breaking changes (incompatible API changes)
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes (backwards compatible)

## Current Versions

| Project | Version | Runtime |
|---------|---------|---------|
| treven-web | 0.1.0 | Node.js 22.x, Next.js 16.x |
| treven-back | 0.1.0 | Rust 1.75+ |
| treven-back-db | 0.1.0 | Rust 1.75+ |
| treven-ai | 0.1.0 | Python 3.11+ |

## Dependency Update Policy

### Critical Updates (Immediate)
- Security vulnerabilities (CVE)
- Breaking changes in AWS services
- Runtime deprecations

### Regular Updates (Weekly Review)
- Minor version bumps
- Patch releases
- Dev dependency updates

### Major Updates (Planned)
- Major version bumps require testing
- Breaking changes need migration plan
- Document in CHANGELOG

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
- Use exact versions for AWS SDK dependencies

### Python (treven-ai)
- **uv.lock**: MUST be committed (using uv package manager)
- Use `uv sync` to install dependencies
- Pin all production dependencies
- Use `uv pip compile` for reproducible builds

## Version Pinning Rules

### Production Dependencies
```toml
# Rust - Use major version with caret
aws-sdk-dynamodb = "1"
serde = { version = "1", features = ["derive"] }

# Or exact version for critical deps
tokio = "=1.35.0"
```

```json
// JavaScript - Use exact versions
"next": "16.1.1",
"react": "19.2.3"
```

```toml
# Python - Use compatible release
dependencies = [
    "strands-agents>=0.1.0,<1.0.0",
    "boto3>=1.35.0,<2.0.0"
]
```

### Dev Dependencies
- Can use ranges (^, ~, >=)
- Update frequently
- Less strict pinning allowed

## AWS SDK Versioning

All AWS SDK dependencies should use the same major version:

```toml
# Rust - All AWS SDK v1
aws-config = "1"
aws-sdk-dynamodb = "1"
aws-sdk-s3 = "1"
aws-sdk-bedrockruntime = "1"
```

```python
# Python - All boto3 1.x
boto3 = "^1.35"
```

## Pre-release Versions

- Use `-alpha`, `-beta`, `-rc` suffixes
- Never deploy pre-release to production
- Document known issues

```
0.2.0-alpha.1
0.2.0-beta.1
0.2.0-rc.1
0.2.0
```

## Version Bump Process

1. Update version in package file (package.json, Cargo.toml, pyproject.toml)
2. Update CHANGELOG.md
3. Commit with message: `Release ( {Project} ) v{VERSION} ( {ID} )`
4. Tag the release: `git tag v{VERSION}`
5. Push with tags: `git push --tags`

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
| treven-back | - | 1.75+ | - | 1.x |
| treven-back-db | - | 1.75+ | - | 1.x |
| treven-ai | - | - | 3.11+ | boto3 1.x |

## Breaking Change Policy

When introducing breaking changes:

1. Increment MAJOR version
2. Document migration steps
3. Deprecate old APIs first (when possible)
4. Provide migration tools/scripts
5. Update all consuming projects
