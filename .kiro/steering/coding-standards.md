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
├── db/              # Database operations
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
    #[error("Database error: {0}")]
    Database(#[from] sqlx::Error),
    #[error("Not found: {0}")]
    NotFound(String),
    #[error("Unauthorized")]
    Unauthorized,
}

// Use Result everywhere
pub async fn get_report(id: &str) -> Result<Report, AppError> {
    // ...
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
