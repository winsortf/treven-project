---
inclusion: always
---

# PII Policy — Hard Gate

## What is PII?

Personally Identifiable Information (PII) is any data that can identify, locate, or contact a specific individual.

## Direct Identifiers (MUST REDACT)

- Full Name
- Social Security Number (SSN)
- Driver's License Number
- Passport Number
- Email Address
- Phone Number
- Biometric Data (fingerprints, facial recognition)

## Indirect Identifiers (MUST REDACT when combined)

- Date of Birth
- Home Address / Mailing Address
- IP Address
- Credit Card Numbers
- Vehicle Identification Number (VIN)
- Bank Account Numbers
- Medical Record Numbers

## PII Detection Rules

The Policy Agent MUST:

1. **Scan all content** before:
   - Storing to database
   - Showing to other users
   - Exporting (PDF/DOCX)
   - Generating social posts

2. **Flag detected PII** with:
   - Type of PII
   - Location in content
   - Suggested redaction

3. **Block persistence/export** until:
   - All PII is redacted, OR
   - Analyst explicitly confirms to keep (with justification)

4. **Log all decisions** for audit:
   - What was detected
   - Action taken (redacted/kept)
   - Who approved (if kept)
   - Timestamp

## Redaction Format

Replace PII with generic placeholders:
- Names → `[NAME]`
- Emails → `[EMAIL]`
- Phone → `[PHONE]`
- Address → `[ADDRESS]`
- SSN/ID → `[ID]`
- DOB → `[DOB]`

## Implementation

```python
# PII patterns (regex examples)
PII_PATTERNS = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone": r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "ssn": r"\d{3}-\d{2}-\d{4}",
    "credit_card": r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}",
    "ip_address": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
}
```

## Why This Matters

- **Security:** PII is valuable for identity theft
- **Compliance:** GDPR, UK DPA, and other regulations
- **Trust:** Partners expect data protection
- **Ethics:** Protecting vulnerable individuals
