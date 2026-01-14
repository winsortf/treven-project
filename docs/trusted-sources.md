---
inclusion: always
---

# Trusted Sources

## Tier 1 — Primary Sources (Highest Trust)

### Government Reports
- US State Department Trafficking in Persons (TIP) Report
- UK Modern Slavery Annual Report
- EU Anti-Trafficking Reports
- National government trafficking statistics

### International Organizations
- UN Office on Drugs and Crime (UNODC)
- International Labour Organization (ILO)
- UNICEF
- International Organization for Migration (IOM)
- OSCE (Organization for Security and Co-operation in Europe)

### Academic/Research
- Walk Free Foundation (Global Slavery Index)
- Polaris Project
- Anti-Slavery International

## Tier 2 — Trusted Secondary Sources

### NGO Reports
- Human Rights Watch
- Amnesty International
- La Strada International
- ECPAT International
- Freedom Fund

### Industry Resources
- Business & Human Rights Resource Centre (https://www.business-humanrights.org/)
- Responsible Sourcing Network
- KnowTheChain

### Quality Journalism
- Reuters
- BBC
- The Guardian
- Associated Press
- Al Jazeera (investigative)
- Financial Times

## Tier 3 — Use with Verification

### Regional/Local NGOs
- Verify credibility before citing
- Cross-reference with Tier 1/2 sources

### News Outlets
- Local news (verify outlet reputation)
- Trade publications

## Source Evaluation Criteria

| Criterion | Weight |
|-----------|--------|
| Publisher reputation | 30% |
| Recency (prefer < 12 months) | 25% |
| Primary vs secondary data | 20% |
| Methodology transparency | 15% |
| Geographic relevance | 10% |

## Trust Score Calculation

```python
def calculate_trust_score(source):
    score = 0
    
    # Publisher tier
    if source.publisher in TIER_1:
        score += 30
    elif source.publisher in TIER_2:
        score += 20
    elif source.publisher in TIER_3:
        score += 10
    
    # Recency
    months_old = (now - source.published_date).months
    if months_old <= 6:
        score += 25
    elif months_old <= 12:
        score += 20
    elif months_old <= 24:
        score += 10
    
    # Primary data
    if source.has_primary_data:
        score += 20
    elif source.cites_primary:
        score += 10
    
    # Methodology
    if source.methodology_documented:
        score += 15
    
    # Geographic match
    if source.covers_target_region:
        score += 10
    
    return score  # Max 100
```

## Blocklist (Never Use)

- Unverified social media posts
- Anonymous blogs
- Known disinformation sources
- Sources with clear political bias on trafficking
- Paywalled content without verification

## STT Internal Data

When available, prioritize:
- ExploitX data (for sexual exploitation)
- TAH (Trafficking Analysis Hub) data
- P10 data
- Prevention campaign insights

Reference format: `[STT Internal: {dataset_name}, {date_range}]`
