# Website Creation Rulebook & Checklist

> **Mission**: Create 1000 websites in 2 years with a 2-person team (husband & wife).  
> **Goal**: Consistent, high-quality, minimal, elegant websites following design excellence principles.

---

## 📋 Quick Start Checklist

Use this checklist for every new website project:

### Phase 1: Planning & Setup (Day 1)
- [ ] **Project Brief**: Define purpose, target audience, key messages
- [ ] **Content Audit**: Gather all content (text, images, data)
- [ ] **Design Direction**: Review DESIGN_PRINCIPLES.md
- [ ] **Tech Stack**: Confirm stack from TECHNICAL_STACK.md
- [ ] **Repository Setup**: Initialize git repo with standard structure
- [ ] **Project Documentation**: Create project-specific README.md

### Phase 2: Development (Days 2-5)
- [ ] **Design System**: Set up colors, typography, spacing from DESIGN_PRINCIPLES.md
- [ ] **Component Library**: Build reusable components
- [ ] **Content Implementation**: Add all content with proper structure
- [ ] **SEO Foundation**: Implement SEO_CHECKLIST.md items
- [ ] **Accessibility**: Follow ACCESSIBILITY_STANDARDS.md
- [ ] **Performance**: Optimize per PERFORMANCE_STANDARDS.md

### Phase 3: Testing & Polish (Day 6)
- [ ] **Cross-browser Testing**: Chrome, Firefox, Safari, Edge
- [ ] **Device Testing**: Mobile (320px+), Tablet, Desktop (1920px)
- [ ] **Accessibility Audit**: WAVE, keyboard navigation, screen reader
- [ ] **Performance Audit**: Lighthouse (90+ scores)
- [ ] **SEO Validation**: Google Rich Results Test, Schema validator
- [ ] **Content Review**: Proofread, check all links

### Phase 4: Deployment (Day 7)
- [ ] **Pre-deployment**: Follow DEPLOYMENT_STANDARDS.md checklist
- [ ] **Deploy**: Use standardized deployment method
- [ ] **Post-deployment**: Verify all functionality
- [ ] **SEO Setup**: Submit sitemap, verify Search Console
- [ ] **Monitoring**: Set up analytics (if needed)

---

## 🎯 Core Principles

### 1. Design Philosophy
**Follow**: Adam Wathan, Steve Schoger, Jony Ive, Marc Newson, Elon Musk principles
- **Minimal**: Remove everything unnecessary ("The best part is no part")
- **Purposeful**: Every element serves a function
- **Elegant**: Beauty through simplicity
- **Confident**: Not needy, not desperate
- **Industrial**: Precision, clarity, restraint
- **First Principles**: Question everything, start from fundamentals

See: `DESIGN_PRINCIPLES.md` for detailed guidelines

### 2. Technical Standards
- **Framework**: React 18+ with TypeScript (or Vite for static sites)
- **Styling**: Tailwind CSS (utility-first)
- **Performance**: Lighthouse 90+ scores
- **Accessibility**: WCAG 2.1 AA minimum
- **SEO**: Complete structured data, meta tags, sitemap

See: `TECHNICAL_STACK.md` for full stack details

### 3. Code Quality
- **TypeScript**: Strict mode, no `any` types
- **Functional**: Prefer functions over classes
- **Modular**: Reusable components, DRY principle
- **Semantic HTML**: Proper element usage
- **Clean Code**: Readable, maintainable, documented

### 4. Content Strategy
- **Clear Purpose**: Single purpose per page
- **Information Scent**: Title → Hero → Content flow
- **Human-First**: Written for humans, keywords blend naturally
- **Trust Signals**: Real testimonials, authentic imagery
- **Action-Oriented**: Clear CTAs throughout

---

## 📐 Project Structure Template

Every project should follow this structure:

```
project-name/
├── README.md                 # Project-specific documentation
├── DESIGN_PLAN.md            # Design decisions and rationale
├── DEPLOYMENT.md             # Deployment instructions
├── package.json              # Dependencies
├── tsconfig.json             # TypeScript config
├── tailwind.config.js        # Tailwind config
├── vite.config.ts            # Vite config (if using)
├── public/                   # Static assets
│   ├── favicon.ico
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── manifest.json
│   └── images/               # Optimized images
├── src/
│   ├── components/           # React components
│   │   ├── layout/          # Header, Footer, Navigation
│   │   ├── sections/        # Page sections
│   │   ├── ui/              # Reusable UI components
│   │   └── shared/          # Shared utilities
│   ├── data/                # Static data, JSON
│   ├── types/               # TypeScript types
│   ├── utils/               # Helper functions
│   ├── App.tsx              # Main app component
│   └── main.tsx             # Entry point
└── dist/                     # Build output (gitignored)
```

---

## ✅ Pre-Development Checklist

Before writing any code:

### Content
- [ ] All text content written and proofread
- [ ] All images collected and optimized (WebP format preferred)
- [ ] Logo files ready (SVG preferred, PNG fallback)
- [ ] Contact information verified
- [ ] Social media links confirmed
- [ ] Legal pages ready (Privacy, Terms if needed)

### Design
- [ ] Color palette defined (max 3-4 colors)
- [ ] Typography chosen (2 fonts max: heading + body)
- [ ] Spacing system defined (4px or 8px base)
- [ ] Component designs sketched/mocked
- [ ] Responsive breakpoints planned

### Technical
- [ ] Domain name registered
- [ ] Hosting platform chosen
- [ ] Repository created
- [ ] Environment variables identified
- [ ] Third-party services configured (analytics, forms, etc.)

---

## 🚀 Development Workflow

### Day 1: Foundation
1. Initialize project (Vite + React + TypeScript + Tailwind)
2. Set up Tailwind config with design tokens
3. Create layout components (Header, Footer)
4. Set up routing (if multi-page)
5. Configure build tools

### Day 2-3: Core Sections
1. Hero section
2. Main content sections
3. CTA sections
4. Contact/forms
5. Footer

### Day 4: Enhancements
1. Add animations/transitions
2. Implement image optimization
3. Add structured data (Schema.org)
4. Implement SEO meta tags
5. Add accessibility features

### Day 5: Content & Polish
1. Add all content
2. Optimize images
3. Fine-tune spacing/typography
4. Test responsive design
5. Fix any bugs

### Day 6: Testing
1. Cross-browser testing
2. Device testing
3. Accessibility audit
4. Performance audit
5. SEO validation

### Day 7: Deployment
1. Final build
2. Deploy to hosting
3. Verify functionality
4. Submit to search engines
5. Document deployment

---

## 📊 Quality Gates

A website is **NOT ready** until ALL of these pass:

### Performance
- [ ] Lighthouse Performance: **90+**
- [ ] Lighthouse Accessibility: **90+**
- [ ] Lighthouse Best Practices: **90+**
- [ ] Lighthouse SEO: **90+**
- [ ] First Contentful Paint: **< 1.8s**
- [ ] Largest Contentful Paint: **< 2.5s**
- [ ] Cumulative Layout Shift: **< 0.1**

### Accessibility
- [ ] WCAG 2.1 AA compliance
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Color contrast ratios pass
- [ ] Focus indicators visible
- [ ] Skip links present
- [ ] ARIA labels where needed

### SEO
- [ ] Unique title tags (50-60 chars)
- [ ] Meta descriptions (150-160 chars)
- [ ] Open Graph tags complete
- [ ] Twitter card tags complete
- [ ] Structured data validated
- [ ] Sitemap.xml present
- [ ] Robots.txt configured
- [ ] Canonical tags set

### Code Quality
- [ ] TypeScript strict mode, no errors
- [ ] No console errors/warnings
- [ ] ESLint passes
- [ ] All images have alt text
- [ ] Semantic HTML throughout
- [ ] No unused code/dependencies

### Content
- [ ] All text proofread
- [ ] All links work (no 404s)
- [ ] Contact information correct
- [ ] Images optimized and loaded
- [ ] Forms validated and functional

---

## 🎨 Design System Template

### Colors (Max 3-4)
```typescript
const colors = {
  primary: '#16a34a',      // Main brand color
  accent: '#ca8a04',       // CTA, highlights
  secondary: '#7c3aed',    // Optional accent
  neutral: {
    50: '#fafaf9',         // Backgrounds
    100: '#f5f5f4',
    500: '#78716c',        // Body text
    900: '#1c1917',        // Headings
  }
}
```

### Typography (Max 2 Fonts)
```typescript
const typography = {
  heading: 'Playfair Display',  // Or: Inter, Poppins, etc.
  body: 'Quicksand',            // Or: Inter, System UI, etc.
  sizes: {
    xs: '0.75rem',    // 12px
    sm: '0.875rem',   // 14px
    base: '1rem',     // 16px
    lg: '1.125rem',   // 18px
    xl: '1.25rem',    // 20px
    '2xl': '1.5rem',  // 24px
    '3xl': '1.875rem', // 30px
    '4xl': '2.25rem',  // 36px
  }
}
```

### Spacing (4px or 8px base)
```typescript
const spacing = {
  xs: '0.5rem',   // 8px
  sm: '1rem',     // 16px
  md: '1.5rem',   // 24px
  lg: '2rem',     // 32px
  xl: '3rem',     // 48px
  '2xl': '4rem',  // 64px
  '3xl': '6rem',  // 96px
}
```

### Breakpoints
```typescript
const breakpoints = {
  sm: '640px',   // Mobile landscape
  md: '768px',   // Tablet
  lg: '1024px',  // Desktop
  xl: '1280px',  // Large desktop
  '2xl': '1536px' // Extra large
}
```

---

## 🔄 Reusable Components Library

Build these once, reuse everywhere:

### Layout Components
- `Header.tsx` - Navigation, logo, mobile menu
- `Footer.tsx` - Links, copyright, social
- `Navigation.tsx` - Menu items, active states
- `Container.tsx` - Max-width wrapper

### UI Components
- `Button.tsx` - Primary, secondary, outline variants
- `Card.tsx` - Content cards with hover states
- `Section.tsx` - Page sections with consistent padding
- `Heading.tsx` - Typography component
- `Image.tsx` - Optimized image with lazy loading

### Form Components
- `Input.tsx` - Text inputs with labels
- `Textarea.tsx` - Textarea with validation
- `Select.tsx` - Dropdown selects
- `Form.tsx` - Form wrapper with validation

### Utility Components
- `SkipLink.tsx` - Accessibility skip link
- `Loading.tsx` - Loading states
- `ErrorBoundary.tsx` - Error handling

---

## 📝 Documentation Requirements

Every project must include:

1. **README.md** - Project overview, setup, deployment
2. **DESIGN_PLAN.md** - Design decisions, color/typography choices
3. **DEPLOYMENT.md** - Step-by-step deployment instructions
4. **CHANGELOG.md** - Version history (optional but recommended)

---

## 🚫 Anti-Patterns (What NOT to Do)

### Design
- ❌ Too many colors (stick to 3-4 max)
- ❌ Too many fonts (2 max: heading + body)
- ❌ Inconsistent spacing
- ❌ Cluttered layouts
- ❌ Weak visual hierarchy
- ❌ Poor contrast ratios

### Code
- ❌ `any` types in TypeScript
- ❌ Inline styles (use Tailwind)
- ❌ Unused imports/dependencies
- ❌ Console.logs in production
- ❌ Hardcoded values (use constants)
- ❌ Duplicate code (DRY principle)

### Performance
- ❌ Unoptimized images
- ❌ Blocking scripts
- ❌ Large bundle sizes
- ❌ No lazy loading
- ❌ Render-blocking CSS

### SEO
- ❌ Missing meta tags
- ❌ No structured data
- ❌ Poor heading hierarchy
- ❌ Missing alt text
- ❌ No sitemap

---

## 📚 Reference Documents

- `DESIGN_PRINCIPLES.md` - Detailed design guidelines
- `TECHNICAL_STACK.md` - Technology choices and setup
- `SEO_CHECKLIST.md` - Complete SEO implementation
- `ACCESSIBILITY_STANDARDS.md` - WCAG compliance guide
- `PERFORMANCE_STANDARDS.md` - Performance optimization
- `DEPLOYMENT_STANDARDS.md` - Deployment procedures

---

## 🎯 Success Metrics

Track these for each website:

### Technical
- Lighthouse scores (all 90+)
- Page load time (< 3s on 3G)
- Accessibility score (WCAG AA)
- SEO score (all green)

### Business
- Time to deploy (< 7 days)
- Code reusability (components library)
- Maintenance ease (documentation quality)
- Client satisfaction

---

## 🚀 Rapid Iteration Philosophy

**Elon's Principle**: "Move fast. Iterate quickly. Ship often."

**For 1000 Websites**: This aligns with your goal, but balance with quality.

### The Approach

**Ship Fast**:
- Complete 7-day workflow
- Don't overthink initial version
- Ship within quality gates
- Iterate based on real usage

**Maintain Quality**:
- Quality gates are non-negotiable (Lighthouse 90+)
- Don't ship broken
- Don't skip accessibility
- Don't skip SEO

**Iterate Based on Data**:
- Monitor performance
- Gather user feedback
- Improve based on real usage
- Perfect through iteration, not before shipping

### Balance

✅ Ship fast (7-day workflow)  
✅ Maintain quality gates (minimum standards)  
✅ Iterate based on data  
❌ Don't ship broken  
❌ Don't skip quality gates  
❌ Don't wait for perfection

**The Philosophy**: Ship version 1.0 fast (within quality gates), iterate based on real usage data. Quality gates are minimums, not maximums. Perfect through iteration.

---

## 🔄 Continuous Improvement

After each website:
1. **Retrospective**: What went well? What to improve?
2. **Component Library**: Add reusable components
3. **Documentation**: Update rulebook with learnings
4. **Templates**: Create starter templates
5. **Automation**: Automate repetitive tasks

---

## 📞 Quick Reference

### Common Commands
```bash
# Setup
npm create vite@latest . -- --template react-ts
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Development
npm run dev

# Build
npm run build

# Deploy
npm run deploy  # (if configured)
```

### Essential Tools
- **Design**: Figma, Tailwind UI (reference)
- **Development**: VS Code, Cursor
- **Testing**: Lighthouse, WAVE, BrowserStack
- **Deployment**: GitHub Pages, Netlify, Vercel
- **SEO**: Google Search Console, Rich Results Test

---

## ✅ Final Checklist Before Launch

- [ ] All quality gates passed
- [ ] Cross-browser tested
- [ ] Mobile tested
- [ ] Accessibility verified
- [ ] Performance optimized
- [ ] SEO implemented
- [ ] Content proofread
- [ ] Links verified
- [ ] Forms tested
- [ ] Analytics configured (if needed)
- [ ] Sitemap submitted
- [ ] Documentation complete
- [ ] Deployment successful
- [ ] Post-deployment verification

---

**Remember**: Quality over quantity. Each website should be a masterpiece of minimal elegance.

**Goal**: Build fast, but never compromise on design excellence or code quality.

---

*Last Updated: [Auto-update with each project]*

