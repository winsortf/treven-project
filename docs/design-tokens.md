---
inclusion: always
---

# Design Tokens — STOP THE TRAFFIK Brand

## Color Palette

Match the STOP THE TRAFFIK website (https://stopthetraffik.org/)

```css
:root {
  /* Primary Colors */
  --color-primary: #FCCA01;        /* Yellow - main brand */
  --color-secondary: #2E657C;      /* Teal - secondary */
  
  /* Neutrals */
  --color-ink: #262524;            /* Near-black - text */
  --color-muted: #ADB3B6;          /* Gray - secondary text */
  --color-background: #F7F7F7;     /* Light gray - backgrounds */
  --color-white: #FFFFFF;
  
  /* Semantic Colors */
  --color-success: #2E7D32;
  --color-warning: #ED6C02;
  --color-error: #D32F2F;
  --color-info: #0288D1;
  
  /* Confidence Indicators */
  --color-high-confidence: #2E7D32;
  --color-medium-confidence: #ED6C02;
  --color-low-confidence: #D32F2F;
}
```

## Typography

```css
:root {
  --font-primary: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
  
  /* Scale */
  --text-xs: 0.75rem;    /* 12px */
  --text-sm: 0.875rem;   /* 14px */
  --text-base: 1rem;     /* 16px */
  --text-lg: 1.125rem;   /* 18px */
  --text-xl: 1.25rem;    /* 20px */
  --text-2xl: 1.5rem;    /* 24px */
  --text-3xl: 1.875rem;  /* 30px */
  
  /* Weights */
  --font-normal: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
}
```

## Spacing

```css
:root {
  --space-1: 0.25rem;   /* 4px */
  --space-2: 0.5rem;    /* 8px */
  --space-3: 0.75rem;   /* 12px */
  --space-4: 1rem;      /* 16px */
  --space-5: 1.25rem;   /* 20px */
  --space-6: 1.5rem;    /* 24px */
  --space-8: 2rem;      /* 32px */
  --space-10: 2.5rem;   /* 40px */
  --space-12: 3rem;     /* 48px */
}
```

## Shadows

```css
:root {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
}
```

## Border Radius

```css
:root {
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
}
```

## UI Style Guidelines

- Clean, editorial, "intel product" feel
- Strong hierarchy, high readability
- Icons consistent across nav + cards
- Emphasize uncertainty and citations visually
- Use yellow (#FCCA01) sparingly for CTAs and highlights
- Teal (#2E657C) for secondary actions and links
