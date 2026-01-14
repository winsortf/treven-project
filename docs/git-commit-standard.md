```markdown
# Commit message convention

Keep commit messages consistent so they’re easy to scan, search, and reference in tickets.

---

## Commit composition

### Pattern

`{Type} ( {Scope} ) {Short description} ( {User Story ID | Fallback ID} )`

### Example

`Build ( Shapes ) Create card styles ( AMT-2 )`

---

## Field rules

### 1) Type
- **Required**
- Use **one of the allowed types** listed below.
- **Capitalize** the first letter in the commit message (e.g., `Build`, `Fix`, `Feat`).

### 2) Scope
- **Required**
- The module/area you worked on (e.g., `Shapes`, `Auth`, `Payments`).

### 3) Short description
- **Required**
- A brief, clear summary of what changed.
- Use sentence case (e.g., `Create card styles`, `Fix hover state`).

### 4) ID (User Story ID or fallback)
- **Required**
- If you have a **User Story ID**, use it (example: `AMT-2`).
- If you **don’t** have a User Story ID, use a fallback ID:

#### Fallback ID format
`{USER_ID}{YYYYMMDDHHMM}`

For you:
- `USER_ID` = `JO`
- Example timestamp: `JO202601071403`

> Note: `YYYYMMDDHHMM` is 24-hour time and should be based on the moment you commit.

---

## Git command examples

### With **User Story ID**

```bash
git commit -m 'Build ( Shapes ) Create card styles ( AMT-2 )'

```

### Without **User Story ID**

Given:

- `JO` = your user ID
- date = `20260107`
- time = `1403`

```bash
git commit -m 'Build ( Shapes ) Create card styles ( JO202601071403 )'
```

---

## Commit examples (by type)

```
Build ( Shapes ) Create card styles ( AMT-2 )
Chore ( Shapes ) Create card styles ( AMT-2 )
Feat ( Shapes ) Create card styles ( AMT-2 )
Fix ( Shapes ) Create card styles ( AMT-2 )
Docs ( Shapes ) Create card styles ( AMT-2 )
Refactor ( Shapes ) Create card styles ( AMT-2 )
Perf ( Shapes ) Create card styles ( AMT-2 )
Style ( Shapes ) Create card styles ( AMT-2 )
Layout ( Shapes ) Create card styles ( AMT-2 )
Test ( Shapes ) Create card styles ( AMT-2 )
```

---

## Allowed types (must match exactly)

- `build`: Build-related changes (e.g., npm changes, adding external dependencies)
- `chore`: Maintenance changes not visible to end users (e.g., `.gitignore`, `.prettierrc`)
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code change that neither fixes a bug nor adds a feature (e.g., renaming variables/functions)
- `perf`: Performance improvements
- `style`: Styling-only changes (formatting/UI styling)
- `test`: Adding or updating tests
- `layout`: Adding new components or layout/styling work

---

## Prohibited in commits

### No AI Co-Author Attribution
- **NEVER** add `Co-Authored-By` lines for AI assistants (Claude, GPT, Copilot, etc.)
- **NEVER** add any AI attribution, credits, or mentions in commit messages
- Commits must only have the human developer as the author
- The git author should be the person who requested/approved the changes

#### Bad (DO NOT DO THIS)
```
Feat ( API ) Add new endpoint ( JO202601142030 )

Co-Authored-By: Claude <noreply@anthropic.com>
```

#### Good
```
Feat ( API ) Add new endpoint ( JO202601142030 )
```