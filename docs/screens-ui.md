---
inclusion: always
---

# UI Screens Specification

## Screen Overview

1. **Trends Map** (Home) - Global/country trend discovery
2. **Intel Chat** - Conversational control plane
3. **Report Studio** - Analyst workspace for review/edit/approve
4. **Partners** - Manage orgs/clients and report access
5. **To-Do / Insights** - Recommended next reports
6. **Admin** - Users, roles, settings

## 1. Trends Map (Home)

**Purpose:** Global/country trend discovery + launch workflows

**Components:**
- Interactive world map (clickable countries)
- Country list sidebar (searchable)
- Trend cards per country showing:
  - Short title
  - Confidence indicator (high/medium/low)
  - Top 3–5 trusted source links
  - Exploitation type tags
- Popup on trend click:
  - Full trend details
  - Source citations
  - Last updated timestamp

**Actions:**
- "Generate KJ Report" button → opens Report Studio
- "Open Chat" button → opens Intel Chat with context

**Data:**
- Aggregated from OSINT agent runs
- Refreshed periodically or on-demand

## 2. Intel Chat

**Purpose:** Conversational control plane for agents

**Components:**
- Chat message list (user + assistant)
- Context bar showing: country/sector/time range/client type
- Prompt templates library (saved prompts)
- Tool call transparency panel:
  - Which agent ran
  - Citations used
  - Uncertainty indicators
- Input area with suggestions

**Actions from chat:**
- "Start new report"
- "Add sources"
- "Request evidence pack"
- "Generate social summary"
- "Find trends in {country}"

**Prompt Templates (seed):**
- "Generate KJ report for {COUNTRY} / {SECTOR} / {TIME_RANGE} for {CLIENT_TYPE}"
- "List top recruitment patterns + evidence + confidence"
- "Draft FI red flags for this typology"
- "Identify information gaps and turn them into Information Requirements"

## 3. Report Studio

**Purpose:** Analyst workspace to review/edit/approve

**Layout:**
- Left nav: Report sections (clickable)
- Main area: Section content with inline editing
- Right panel: Citations + reasoning

**Features:**
- Inline citations per sentence/claim (hover to see source)
- Toggle: "Show reasoning" (why AI thinks this)
- Uncertainty highlighting (yellow/orange/red)
- Version history + diff viewer
- Word count indicator

**Approval Workflow:**
```
Draft → In Review → Approved → Exported
```

**Export Options:**
- PDF
- DOCX
- Markdown

**Critical:** No export without explicit "Approve & Export" click

## 4. Partners

**Purpose:** Manage orgs/clients and access to reports

**Components:**
- Partners list (FIs, NGOs, Law Enforcement)
- Partner detail view:
  - Name, type, contact
  - Reports shared with them
  - Access permissions
- Delivery settings:
  - Export bundle locations
  - Webhook notifications (optional)

**Permissions:**
- View only
- Download
- None

## 5. To-Do / Insights

**Purpose:** Recommended next reports based on trend changes

**Components:**
- "Suggested topics" queue
- "New/Spiking trends" alerts
- Insight cards with:
  - Topic summary
  - Why it's suggested
  - Confidence score
  - One-click: "Start report from suggestion"

**Data sources:**
- Trend analysis from OSINT agent
- Gap analysis from existing reports
- Client interest signals

## 6. Admin

**Purpose:** System configuration

**Sections:**
- Users & Roles (admin, analyst, viewer)
- Organizations management
- PII policy settings
- Trusted sources allowlist/blocklist
- Model routing settings (Bedrock preferences)
- Data retention + export controls
- Audit logs viewer

## Navigation

```
┌─────────────────────────────────────────┐
│  [Logo]  Trends  Chat  Reports  Partners  To-Do  [User] │
└─────────────────────────────────────────┘
```

## Responsive Behavior

- Desktop-first design
- Tablet: Collapsible sidebars
- Mobile: Bottom nav, stacked layouts
