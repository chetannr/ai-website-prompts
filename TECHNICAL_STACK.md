# Technical Stack Standards

> **Goal**: Consistent, modern, performant technology choices for all websites.

---

## 🎯 Core Stack (Standard)

### Frontend Framework
**React 18+ with TypeScript**
- **Why**: Industry standard, excellent ecosystem, type safety
- **Version**: React 18.2+ (latest stable)
- **TypeScript**: Strict mode enabled
- **Alternatives**: 
  - Vite + React (for static sites)
  - Next.js (for SSR/SSG if needed)

### Build Tool
**Vite 5+**
- **Why**: Fast, modern, excellent DX
- **Features**: HMR, fast builds, optimized output
- **Config**: Standard Vite config with React plugin

### Styling
**Tailwind CSS 3+**
- **Why**: Utility-first, consistent, fast development
- **Config**: Custom design tokens (colors, spacing, typography)
- **Plugins**: 
  - `@tailwindcss/forms` (form styling)
  - `@tailwindcss/typography` (if needed for content)

### Language
**TypeScript 5+**
- **Why**: Type safety, better DX, fewer bugs
- **Config**: Strict mode, no `any` types
- **Target**: ES2020+ (modern browsers)

---

## 📦 Standard Dependencies

### Core
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.2.0",
    "typescript": "^5.3.0",
    "vite": "^5.0.0",
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.0",
    "autoprefixer": "^10.4.0"
  }
}
```

### Optional (Add as needed)
- **Routing**: TanStack Router (if multi-page SPA)
- **State Management**: React hooks (useState, useEffect) - avoid Redux unless complex
- **Forms**: React Hook Form (if complex forms)
- **Animations**: Framer Motion (if needed, but prefer CSS)
- **Icons**: Lucide React or Heroicons

---

## 🏗️ Project Structure

### Standard Structure
```
project/
├── public/              # Static assets
│   ├── favicon.ico
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── manifest.json
│   └── images/
├── src/
│   ├── components/
│   │   ├── layout/
│   │   ├── sections/
│   │   ├── ui/
│   │   └── shared/
│   ├── data/           # JSON, static data
│   ├── types/          # TypeScript types
│   ├── utils/          # Helper functions
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css       # Tailwind imports
├── index.html
├── package.json
├── tsconfig.json
├── tsconfig.app.json
├── tsconfig.node.json
├── tailwind.config.js
├── postcss.config.js
├── vite.config.ts
└── README.md
```

---

## ⚙️ Configuration Files

### `vite.config.ts`
```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    sourcemap: false, // Disable in production
    minify: 'esbuild',
  },
  server: {
    port: 5173,
    open: true,
  },
});
```

### `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

### `tailwind.config.js`
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0fdf4',
          500: '#16a34a',
          600: '#15803d',
          900: '#14532d',
        },
        accent: {
          500: '#ca8a04',
          600: '#a16207',
        },
      },
      fontFamily: {
        heading: ['Playfair Display', 'serif'],
        body: ['Quicksand', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
    },
  },
  plugins: [],
}
```

### `postcss.config.js`
```javascript
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
```

---

## 🎨 Styling Approach

### Tailwind CSS
- **Utility-first**: Use Tailwind classes directly
- **Custom tokens**: Define in `tailwind.config.js`
- **Components**: Extract repeated patterns to components
- **Responsive**: Mobile-first breakpoints

### Custom CSS
- **Global styles**: `index.css` for base styles
- **Animations**: CSS keyframes for animations
- **Utilities**: Custom utility classes if needed

### CSS Organization
```css
/* index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  /* Base styles, resets */
}

@layer components {
  /* Component styles */
}

@layer utilities {
  /* Custom utilities */
}
```

---

## 🔧 Development Tools

### Required
- **Node.js**: 18+ LTS
- **npm**: 9+ (or pnpm/yarn)
- **Git**: Version control
- **VS Code/Cursor**: IDE

### Recommended Extensions
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- TypeScript and JavaScript Language Features
- Error Lens

### Linting & Formatting
```json
// .eslintrc.json (if using ESLint)
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react-hooks/recommended"
  ],
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "error"
  }
}
```

---

## 📱 Browser Support

### Target Browsers
- **Chrome**: Last 2 versions
- **Firefox**: Last 2 versions
- **Safari**: Last 2 versions
- **Edge**: Last 2 versions
- **Mobile**: iOS Safari 14+, Chrome Android

### Polyfills
- **Modern browsers**: No polyfills needed (ES2020+)
- **Legacy**: Use `@vitejs/plugin-legacy` if needed (rare)

---

## 🚀 Build & Deployment

### Build Commands
```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0"
  }
}
```

### Build Output
- **Directory**: `dist/`
- **Format**: ES modules
- **Minification**: Enabled (esbuild)
- **Source maps**: Disabled in production

### Deployment Targets
- **Static hosting**: GitHub Pages, Netlify, Vercel
- **CDN**: Cloudflare Pages
- **Traditional**: Any web server (upload `dist/` folder)

---

## 🔐 Environment Variables

### Standard Variables
```bash
# .env.local
VITE_SITE_URL=https://example.com
VITE_API_URL=https://api.example.com  # If needed
VITE_ANALYTICS_ID=GA_MEASUREMENT_ID    # If using analytics
```

### Usage
```typescript
// Access via import.meta.env
const siteUrl = import.meta.env.VITE_SITE_URL;
```

---

## 📊 Performance Standards

### Bundle Size Targets
- **Initial JS**: < 100KB (gzipped)
- **CSS**: < 20KB (gzipped)
- **Total**: < 200KB (gzipped) for initial load

### Optimization
- **Code splitting**: Automatic with Vite
- **Tree shaking**: Automatic
- **Image optimization**: Use WebP, lazy loading
- **Font loading**: `font-display: swap`

---

## 🧪 Testing (Optional but Recommended)

### Unit Testing
- **Framework**: Vitest (Vite-native)
- **Library**: React Testing Library

### E2E Testing
- **Framework**: Playwright or Cypress (if needed)

### Manual Testing
- Cross-browser testing
- Device testing
- Accessibility testing

---

## 🔄 Alternative Stacks

### For Static Sites (No React)
- **Vite** + **Vanilla JS/TypeScript**
- **Tailwind CSS** (same)
- Simpler, faster builds

### For SSR/SSG
- **Next.js 14+** (App Router)
- **React** + **TypeScript**
- **Tailwind CSS** (same)
- Use when: SEO critical, dynamic content

### For Simple Sites
- **HTML** + **Tailwind CSS** (CDN or build)
- **Vanilla JS**
- Fastest development, simplest deployment

---

## ✅ Stack Checklist

Before starting development:

- [ ] Node.js 18+ installed
- [ ] Project initialized with Vite + React + TypeScript
- [ ] Tailwind CSS configured
- [ ] TypeScript strict mode enabled
- [ ] Project structure created
- [ ] Git repository initialized
- [ ] Dependencies installed
- [ ] Development server runs (`npm run dev`)
- [ ] Build works (`npm run build`)

---

## 🚫 Anti-Patterns

### Avoid
- ❌ Mixing CSS frameworks (only Tailwind)
- ❌ Using `any` types in TypeScript
- ❌ Inline styles (use Tailwind)
- ❌ Unused dependencies
- ❌ Large bundle sizes
- ❌ Blocking scripts
- ❌ Render-blocking CSS

### Prefer
- ✅ TypeScript strict mode
- ✅ Tailwind utility classes
- ✅ Functional components
- ✅ Small, focused components
- ✅ Code splitting
- ✅ Lazy loading

---

## 📚 Resources

### Documentation
- [React Docs](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Vite Guide](https://vitejs.dev/guide/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)

### Learning
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- [Tailwind UI](https://tailwindui.com/) (reference)
- [Vite Best Practices](https://vitejs.dev/guide/performance.html)

---

**Remember**: Keep it simple. The standard stack works for 95% of projects. Only add complexity when necessary.

---

*Last Updated: [Auto-update]*

