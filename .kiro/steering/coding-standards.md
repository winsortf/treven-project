---
inclusion: always
---

# Coding Standards

## General Principles

- KISS: Keep It Simple, Stupid
- DRY: Don't Repeat Yourself
- YAGNI: You Aren't Gonna Need It
- SOLID principles
- Clean Code practices

## TypeScript (treven-web)

### File Structure
```
src/
├── app/              # Next.js App Router pages
├── components/       # React components
│   ├── ui/          # Primitive UI components
│   └── features/    # Feature-specific components
├── hooks/           # Custom React hooks
├── lib/             # Utilities and helpers
├── services/        # API and WebSocket services
├── types/           # TypeScript type definitions
└── styles/          # Global styles and CSS modules
```

### Naming Conventions
- Components: PascalCase (`TrendsMap.tsx`)
- Hooks: camelCase with `use` prefix (`useWebSocket.ts`)
- Utils: camelCase (`formatDate.ts`)
- Types: PascalCase (`Report.ts`)
- CSS Modules: camelCase (`trendsMap.module.css`)

### Component Pattern
```tsx
// components/features/TrendsMap/TrendsMap.tsx
import styles from './TrendsMap.module.css';
import { TrendsMapProps } from './types';

export function TrendsMap({ countries, onSelect }: TrendsMapProps) {
  // hooks first
  // derived state
  // handlers
  // render
}
```

### TypeScript Rules
- Strict mode enabled
- No `any` types (use `unknown` if needed)
- Explicit return types on functions
- Interface over type for objects

## Rust (treven-back, treven-back-db)

### File Structure
```
src/
├── main.rs          # Entry point
├── lib.rs           # Library root
├── api/             # HTTP handlers
├── ws/              # WebSocket handlers
├── dynamodb/        # DynamoDB operations
│   ├── client.rs    # DynamoDB client setup
│   ├── queries.rs   # Query helpers
│   └── models.rs    # Item serialization
├── models/          # Data structures
├── services/        # Business logic
└── utils/           # Helpers
```

### Naming Conventions
- Modules: snake_case (`trends_map.rs`)
- Structs: PascalCase (`TrendsMap`)
- Functions: snake_case (`get_trends`)
- Constants: SCREAMING_SNAKE_CASE (`MAX_RETRIES`)

### Error Handling
```rust
// Use thiserror for custom errors
#[derive(Debug, thiserror::Error)]
pub enum AppError {
    #[error("DynamoDB error: {0}")]
    DynamoDB(String),
    #[error("Not found: {0}")]
    NotFound(String),
    #[error("Unauthorized")]
    Unauthorized,
    #[error("Serialization error: {0}")]
    Serde(#[from] serde_json::Error),
}

// Use Result everywhere
pub async fn get_report(org_id: &str, report_id: &str) -> Result<Report, AppError> {
    // ...
}
```

### DynamoDB Patterns

**Table:** `lon12-table`
**Region:** `us-west-2`
**Docs:** https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_dynamodb_code_examples.html

```rust
use aws_sdk_dynamodb::{Client, Config};
use aws_sdk_dynamodb::types::AttributeValue;
use serde::{Deserialize, Serialize};
use serde_dynamo::{from_items, to_item};

const TABLE_NAME: &str = "lon12-table";

// Client setup
pub async fn create_client() -> Client {
    let config = aws_config::defaults(aws_config::BehaviorVersion::latest())
        .region("us-west-2")
        .load()
        .await;
    Client::new(&config)
}

// Item serialization with serde_dynamo
#[derive(Serialize, Deserialize)]
pub struct ReportItem {
    #[serde(rename = "PK")]
    pub pk: String,
    #[serde(rename = "SK")]
    pub sk: String,
    pub report_id: String,
    pub title: String,
    pub status: String,
}

// Put item
pub async fn put_report(client: &Client, item: &ReportItem) -> Result<(), AppError> {
    let item = to_item(item)?;
    client
        .put_item()
        .table_name(TABLE_NAME)
        .set_item(Some(item))
        .send()
        .await
        .map_err(|e| AppError::DynamoDB(e.to_string()))?;
    Ok(())
}

// Get item
pub async fn get_report(client: &Client, org_id: &str, report_id: &str) -> Result<ReportItem, AppError> {
    let pk = format!("ORG#{}", org_id);
    let sk = format!("REPORT#{}", report_id);

    let result = client
        .get_item()
        .table_name(TABLE_NAME)
        .key("PK", AttributeValue::S(pk))
        .key("SK", AttributeValue::S(sk))
        .send()
        .await
        .map_err(|e| AppError::DynamoDB(e.to_string()))?;

    match result.item {
        Some(item) => serde_dynamo::from_item(item).map_err(|e| AppError::Serde(e.into())),
        None => Err(AppError::NotFound(report_id.to_string())),
    }
}

// Query items
pub async fn get_reports_by_org(client: &Client, org_id: &str) -> Result<Vec<ReportItem>, AppError> {
    let pk = format!("ORG#{}", org_id);

    let result = client
        .query()
        .table_name(TABLE_NAME)
        .key_condition_expression("PK = :pk AND begins_with(SK, :prefix)")
        .expression_attribute_values(":pk", AttributeValue::S(pk))
        .expression_attribute_values(":prefix", AttributeValue::S("REPORT#".to_string()))
        .send()
        .await
        .map_err(|e| AppError::DynamoDB(e.to_string()))?;

    from_items(result.items.unwrap_or_default())
        .map_err(|e| AppError::Serde(e.into()))
}
```

### Async Rules
- Use `tokio` runtime
- Prefer `async fn` over manual futures
- Use `?` for error propagation

## Python (treven-ai)

### File Structure
```
src/
├── agents/          # Agent definitions
│   ├── scraper.py
│   ├── generator.py
│   ├── summarise.py
│   ├── social.py
│   └── pii.py
├── tools/           # Agent tools
├── models/          # Data models
├── services/        # External services
└── utils/           # Helpers
```

### Naming Conventions
- Modules: snake_case (`report_generator.py`)
- Classes: PascalCase (`ReportGenerator`)
- Functions: snake_case (`generate_report`)
- Constants: SCREAMING_SNAKE_CASE (`MAX_TOKENS`)

### Type Hints
```python
from typing import Optional, List
from pydantic import BaseModel

class ReportRequest(BaseModel):
    country: str
    sector: str
    time_range: Optional[str] = "12m"

async def generate_report(request: ReportRequest) -> Report:
    ...
```

### Agent Pattern
```python
from strands import Agent, tool

class ReportGeneratorAgent(Agent):
    model = "anthropic.claude-opus-4-5"
    
    @tool
    async def search_sources(self, query: str) -> List[Source]:
        ...
```

## CSS Modules

### Naming
- Use camelCase for class names
- Descriptive names (`containerMain`, not `cm`)

### Structure
```css
/* Component.module.css */
.container {
  /* layout */
}

.header {
  /* component parts */
}

.isActive {
  /* state modifiers */
}
```

### Use Design Tokens
```css
.button {
  background: var(--color-primary);
  padding: var(--space-4);
  border-radius: var(--radius-md);
}
```

## Git Conventions

### Branch Names
- `feature/trends-map`
- `fix/pii-detection`
- `chore/update-deps`

### Commit Messages
```
type(scope): description

feat(web): add trends map component
fix(api): handle missing org_id
docs(readme): update setup instructions
```

### PR Requirements
- Descriptive title
- Link to issue/task
- Screenshots for UI changes
- Tests for new functionality
