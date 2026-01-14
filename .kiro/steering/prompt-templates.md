---
inclusion: manual
---

# Prompt Templates Library

## Report Generation

### Full KJ Report
```
Generate a Key Judgement report for:
- Country: {COUNTRY}
- Sector: {SECTOR}
- Time Range: {TIME_RANGE}
- Client Type: {CLIENT_TYPE}

Focus on: {EXPLOITATION_TYPE}

Use the standard KJ report structure with all required sections.
Ensure every factual claim has a citation.
Flag any areas of low confidence.
```

### Quick Report (Specific Focus)
```
Generate a focused KJ report on {SPECIFIC_TOPIC} in {COUNTRY}.
Prioritize recent sources (last 6 months).
Include red flag indicators for financial institutions.
Word limit: 2,000 words.
```

## Analysis Prompts

### Recruitment Patterns
```
Analyze recruitment patterns for {EXPLOITATION_TYPE} in {COUNTRY}.
Answer:
- Who is being recruited? (demographics, vulnerabilities)
- How are they recruited? (methods, platforms)
- Who is recruiting? (actors, networks)
- Where does recruitment happen?

Provide evidence and confidence levels for each finding.
```

### Demand Analysis
```
Analyze demand drivers for {EXPLOITATION_TYPE} in {COUNTRY/REGION}.
Consider:
- Economic factors
- Cultural factors
- Technological enablers
- Cross-border dynamics

Identify where demand is expressed (platforms, locations).
```

### Money Flow Analysis
```
Analyze financial patterns for {EXPLOITATION_TYPE} in {COUNTRY}.
Cover:
- Payment methods used
- Profit distribution
- Money movement channels
- Connections to other financial crimes

Generate FI-relevant red flag indicators.
```

## Red Flag Generation

### FI Red Flags
```
Based on the analysis of {EXPLOITATION_TYPE} in {COUNTRY}, generate 5-10 behaviour-based red flag indicators for financial institutions.

Format each as:
- Observable behaviour
- Why it may indicate exploitation
- Suggested monitoring approach

Include caveat about non-exhaustive nature.
```

## Information Gaps

### Gap Analysis
```
Review the current analysis on {TOPIC} and identify:
1. Key information gaps
2. Areas of uncertainty
3. Questions that would strengthen the assessment

Format as Information Requirements for the report.
```

## Social Media

### LinkedIn Summary
```
Create a 1-2 line LinkedIn summary for the approved KJ report on {TOPIC}.

Requirements:
- Non-sensitive (no operational details)
- High-level insight
- No PII
- Professional tone
- Include call to action for partners
```

## Evidence Collection

### Source Search
```
Find trusted sources on {TOPIC} in {COUNTRY} from the last {TIME_RANGE}.

Prioritize:
1. Government reports (TIP reports, official statistics)
2. UN/ILO publications
3. NGO reports
4. Business & Human Rights Resource Centre
5. Quality journalism

For each source, provide: title, publisher, date, URL, relevance summary.
```

## Customization Variables

| Variable | Options |
|----------|---------|
| {COUNTRY} | Any country name |
| {SECTOR} | Agriculture, Construction, Hospitality, etc. |
| {TIME_RANGE} | Last 6 months, Last 12 months, 2024-2025 |
| {CLIENT_TYPE} | FI (Financial Institution), NGO, LE (Law Enforcement) |
| {EXPLOITATION_TYPE} | Labour, Sexual, Child, Forced Marriage, etc. |
| {SPECIFIC_TOPIC} | Any specific focus area |
