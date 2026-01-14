---
inclusion: always
---

# Coding Principles and Best Practices

## Core Principles

### KISS (Keep It Simple, Stupid)

- Write simple, straightforward code
- Avoid over-engineering
- Prefer clarity over cleverness

### DRY (Don't Repeat Yourself)

- Extract reusable logic into shared functions/components
- Use design tokens instead of hardcoded values
- Create composable primitives

### YAGNI (You Aren't Gonna Need It)

- Don't add functionality until it's needed
- Build what's required, not what might be required

### SOLID Principles

- **Single Responsibility**: Each component/function has one clear purpose
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable for their base types
- **Interface Segregation**: Many specific interfaces over one general interface
- **Dependency Inversion**: Depend on abstractions, not concretions

### Separation of Concerns (SOC)

- Separate business logic from presentation
- Keep styling separate from behavior
- Isolate platform-specific code

### Modularity

- Build small, focused, reusable modules
- Each component should be independently testable
- Clear boundaries between layers (tokens → primitives → kit)

### Clean Code

- Meaningful names for variables, functions, components
- Functions should be small and do one thing
- Comments explain "why", not "what"
- Consistent formatting and style

## System Qualities

### Scalability

- Design for growth
- Use efficient data structures and algorithms
- Consider performance implications

### Maintainability

- Write code that's easy to understand and modify
- Follow consistent patterns across the codebase
- Document complex logic

### Reliability

- Handle errors gracefully
- Write comprehensive tests
- Validate inputs and outputs

### Portability

- Minimize platform-specific dependencies
- Use abstractions for platform differences
- Keep business logic platform-agnostic

### Reusability

- Build generic, configurable components
- Use composition over inheritance
- Design for multiple use cases

## UX/UI Principles

### Don't Make Me Think (DMET)

- Intuitive interfaces
- Clear visual hierarchy
- Consistent patterns and behaviors

### Single Source of Truth (SSOT)

- Design tokens are the single source for visual properties
- Centralized state management
- Avoid duplicating data

### Defensive Programming

- Validate all inputs
- Handle edge cases
- Provide meaningful error messages
- Fail gracefully

## Architecture

### Clean Architecture

- **Presentation Layer**: UI components
- **Domain Layer**: Business logic (platform-agnostic)
- **Data Layer**: Data sources and repositories

### Dependency Flow

## DynamoDB Best Practices

### Single-Table Design

- Use ONE table for all entities
- Composite keys (PK/SK) enable efficient queries
- Design access patterns FIRST, then model data
- Denormalize data to avoid joins

### Key Design Principles

- **PK (Partition Key)**: Always include `orgId` for multi-tenant isolation
- **SK (Sort Key)**: Use hierarchical prefixes (e.g., `REPORT#`, `USER#`)
- **GSIs**: Create for alternate access patterns only when needed
- **Sparse Indexes**: Only items with the GSI attribute are indexed

### Query Patterns

- Prefer `Query` over `Scan` (always)
- Use `begins_with` on SK for hierarchical queries
- Use `between` for time-range queries
- Paginate large result sets with `LastEvaluatedKey`

### Data Modeling Rules

- Store related data together (single item when possible)
- Use ISO8601 for timestamps (enables sorting)
- Include `entityType` attribute for filtering
- Version items with `version` attribute for optimistic locking

### Performance

- Keep items small (< 400KB limit)
- Use projection expressions to fetch only needed attributes
- Batch operations for bulk reads/writes (max 25 items)
- Use TTL for automatic data expiration

### Multi-Tenant Isolation

- ALWAYS prefix PK with `ORG#<orgId>`
- Validate `orgId` from JWT before every operation
- Never allow cross-org queries
- Audit all data access

## Responsive Design

### Mobile-First Approach (REQUIRED)

All CSS must be written mobile-first:
1. Base styles for mobile (no media query)
2. `@media (min-width: 768px)` for tablet
3. `@media (min-width: 1024px)` for desktop

```css
/* Mobile first example */
.component {
  padding: var(--space-2);  /* Mobile default */
}

@media (min-width: 768px) {
  .component {
    padding: var(--space-4);  /* Tablet+ */
  }
}
```

### Web (Progressive Web App)

- Mobile-first approach (REQUIRED)
- Responsive layouts using CSS Grid/Flexbox
- Touch-friendly tap targets (min 44px)
- Offline support via service worker
- App-like experience with PWA manifest
- Safe area insets for notched devices
- Bottom navigation on mobile, sidebar on desktop

### iOS

- Adaptive layouts using SwiftUI
- Support for different device sizes (iPhone, iPad)
- Dynamic Type support
- Landscape and portrait orientations

### Android

- Responsive layouts using Compose
- Support for different screen sizes and densities
- Material Design 3 guidelines
- Foldable device support

## Accessibility

### Web (WAI-ARIA Standards)

- Semantic HTML
- ARIA labels and roles
- Keyboard navigation
- Screen reader support
- Focus management
- Color contrast ratios (WCAG AA minimum)

### iOS

- VoiceOver support
- Dynamic Type
- Accessibility labels and hints
- Accessibility actions

### Android

- TalkBack support
- Content descriptions
- Accessibility actions
- Touch target sizes (minimum 48dp)

## Dark Mode

- **Default**: Dark mode is the default theme
- **Light Mode**: Available as user preference
- **System Sync**: Respect system theme preference
- **Consistent**: All components support both themes
- **Design Tokens**: Use semantic color tokens that adapt to theme