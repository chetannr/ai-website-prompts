# Lighthouse Standards: Achieving 100 in All Categories

> **Goal**: Every website must achieve **100/100** in all four Lighthouse categories: Performance, Accessibility, Best Practices, and SEO.

---

## 📊 Lighthouse Score Targets

### Minimum Requirements
- **Performance**: 100/100
- **Accessibility**: 100/100
- **Best Practices**: 100/100
- **SEO**: 100/100

### Core Web Vitals (Performance)
- **LCP (Largest Contentful Paint)**: < 2.5s (Good), < 1.8s (Excellent)
- **FID (First Input Delay)**: < 100ms (Good), < 50ms (Excellent)
- **CLS (Cumulative Layout Shift)**: < 0.1 (Good), < 0.05 (Excellent)
- **FCP (First Contentful Paint)**: < 1.8s (Good), < 1.2s (Excellent)
- **TTFB (Time to First Byte)**: < 600ms (Good), < 400ms (Excellent)

---

## 🚀 Performance (100/100)

### Critical Requirements

#### 1. Image Optimization
- ✅ **WebP Format**: All images use WebP with fallback
- ✅ **Lazy Loading**: Below-fold images use `loading="lazy"`
- ✅ **Dimensions**: Width/height attributes to prevent CLS
- ✅ **Optimization**: Images compressed (< 200KB hero, < 100KB content)
- ✅ **Responsive**: Use `srcset` or `sizes` for responsive images
- ✅ **Preload**: Critical above-fold images preloaded

```html
<!-- Optimized Image Pattern -->
<picture>
  <source srcset="image.webp" type="image/webp" />
  <img 
    src="image.jpg"
    alt="Descriptive alt text"
    loading="lazy"
    width="1200"
    height="630"
    decoding="async"
  />
</picture>

<!-- Preload Critical Hero Image -->
<link rel="preload" as="image" href="/hero.webp" type="image/webp" />
```

#### 2. Font Optimization
- ✅ **Font Display**: `font-display: swap` for all fonts
- ✅ **Preload**: Critical fonts preloaded
- ✅ **Subset**: Use font subsets when possible
- ✅ **Format**: WOFF2 format (modern browsers)
- ✅ **Limit**: Max 2 font families, max 2-3 weights
- ✅ **System Fallback**: Proper system font fallback

```html
<!-- Preload Critical Fonts -->
<link rel="preload" href="/fonts/font.woff2" as="font" type="font/woff2" crossorigin>

<!-- Font Face with Display Swap -->
@font-face {
  font-family: 'Font Name';
  src: url('/fonts/font.woff2') format('woff2');
  font-display: swap;
  font-weight: 400;
  font-style: normal;
}
```

#### 3. JavaScript Optimization
- ✅ **Code Splitting**: Automatic with Vite/React Router
- ✅ **Tree Shaking**: Remove unused code
- ✅ **Minification**: Minified in production
- ✅ **Bundle Size**: < 100KB gzipped (initial bundle)
- ✅ **Lazy Loading**: Route-based code splitting
- ✅ **No Blocking**: Defer non-critical scripts

#### 4. CSS Optimization
- ✅ **Minification**: Minified in production
- ✅ **Purge**: Remove unused CSS (Tailwind auto-purges)
- ✅ **Size**: < 20KB gzipped
- ✅ **Critical CSS**: Inline critical CSS if needed
- ✅ **No Render-Blocking**: Load CSS efficiently

#### 5. Resource Hints
- ✅ **Preconnect**: For external domains (fonts, APIs)
- ✅ **DNS Prefetch**: For third-party domains
- ✅ **Preload**: Critical resources (fonts, images)
- ✅ **Prefetch**: For likely next-page resources

```html
<!-- Resource Hints -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://api.example.com">
```

#### 6. Caching Strategy
- ✅ **Browser Caching**: Proper cache headers
- ✅ **CDN**: Use CDN for static assets
- ✅ **Service Worker**: Consider PWA (optional)

---

## ♿ Accessibility (100/100)

### Critical Requirements

#### 1. Semantic HTML
- ✅ **Proper Elements**: Use semantic HTML (`<header>`, `<nav>`, `<main>`, `<footer>`, `<article>`, `<section>`)
- ✅ **Heading Hierarchy**: Single `<h1>`, proper H2 → H3 order (no skipping)
- ✅ **Landmarks**: Proper ARIA landmarks or semantic elements
- ✅ **Lists**: Use `<ul>`, `<ol>`, `<dl>` for lists

#### 2. Keyboard Navigation
- ✅ **Tab Order**: Logical tab order through all interactive elements
- ✅ **Focus Indicators**: Visible focus styles (2px+ outline) on all interactive elements
- ✅ **Skip Links**: "Skip to main content" link at top
- ✅ **Keyboard Traps**: No keyboard traps (can tab out of modals/menus)
- ✅ **Keyboard Shortcuts**: Document any keyboard shortcuts

```css
/* Focus Styles */
*:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
  border-radius: 2px;
}

/* Skip Link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

#### 3. ARIA & Screen Readers
- ✅ **ARIA Labels**: Descriptive labels for icons, buttons without text
- ✅ **ARIA Roles**: Proper roles for custom components
- ✅ **ARIA States**: `aria-expanded`, `aria-selected`, `aria-hidden` where needed
- ✅ **Live Regions**: `aria-live` for dynamic content updates
- ✅ **Descriptions**: `aria-describedby` for form errors, help text

```html
<!-- Icon Button -->
<button aria-label="Close menu">
  <svg aria-hidden="true">
    <path d="..."/>
  </svg>
</button>

<!-- Modal -->
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">Modal Title</h2>
</div>
```

#### 4. Color Contrast
- ✅ **Normal Text**: 4.5:1 contrast ratio (WCAG AA)
- ✅ **Large Text** (18px+ or 14px+ bold): 3:1 contrast ratio
- ✅ **UI Components**: 3:1 contrast ratio
- ✅ **Graphics**: 3:1 contrast ratio (if informative)
- ✅ **Color Independence**: Don't rely on color alone

```css
/* Good Contrast Examples */
.text-primary { color: #1c1917; } /* 16.5:1 on white */
.text-secondary { color: #78716c; } /* 4.6:1 on white */

/* Bad - Avoid */
.text-light { color: #d4d4d4; } /* 1.4:1 on white - FAILS */
```

#### 5. Forms
- ✅ **Labels**: All inputs have associated `<label>`
- ✅ **Error Messages**: Clear, descriptive error messages
- ✅ **Validation**: Real-time validation with `aria-invalid`, `aria-describedby`
- ✅ **Required Fields**: Indicated with `aria-required` or visual indicator

#### 6. Images
- ✅ **Alt Text**: Descriptive alt text on all images
- ✅ **Decorative Images**: Empty alt `alt=""` for decorative images
- ✅ **Complex Images**: Use `<figcaption>` for detailed descriptions

---

## ✅ Best Practices (100/100)

### Critical Requirements

#### 1. HTTPS
- ✅ **HTTPS Only**: Site served over HTTPS
- ✅ **No Mixed Content**: No HTTP resources on HTTPS pages
- ✅ **HSTS**: HTTP Strict Transport Security header (optional but recommended)

#### 2. Security Headers
- ✅ **Content Security Policy**: CSP header configured
- ✅ **X-Frame-Options**: Prevent clickjacking
- ✅ **X-Content-Type-Options**: Prevent MIME sniffing
- ✅ **Referrer Policy**: Appropriate referrer policy

```html
<!-- Security Headers (via server or meta tags) -->
<meta http-equiv="Content-Security-Policy" content="default-src 'self'">
<meta http-equiv="X-Frame-Options" content="DENY">
<meta http-equiv="X-Content-Type-Options" content="nosniff">
<meta name="referrer" content="strict-origin-when-cross-origin">
```

#### 3. Console Errors
- ✅ **No Console Errors**: Fix all JavaScript console errors
- ✅ **No Console Warnings**: Fix all console warnings
- ✅ **No Deprecated APIs**: Avoid deprecated browser APIs

#### 4. Image Aspect Ratio
- ✅ **Width/Height**: All images have width and height attributes
- ✅ **Aspect Ratio**: Use CSS aspect-ratio or explicit dimensions
- ✅ **No Layout Shift**: Images don't cause CLS

#### 5. Modern JavaScript
- ✅ **ES6+**: Use modern JavaScript features
- ✅ **No Polyfills**: Avoid unnecessary polyfills
- ✅ **Browser Support**: Support modern browsers (last 2 versions)

#### 6. Third-Party Scripts
- ✅ **Minimize**: Limit third-party scripts
- ✅ **Async/Defer**: Load third-party scripts asynchronously
- ✅ **No Blocking**: Don't block page rendering

#### 7. User Agent String
- ✅ **Valid**: Valid user agent string
- ✅ **No Manipulation**: Don't manipulate user agent

---

## 🔍 SEO (100/100)

### Critical Requirements

#### 1. Meta Tags
- ✅ **Title Tags**: Unique, 50-60 characters, keyword-rich
- ✅ **Meta Descriptions**: 150-160 characters, compelling
- ✅ **Open Graph Tags**: Complete OG tags for social sharing
- ✅ **Twitter Cards**: Summary or large image cards
- ✅ **Canonical Tags**: Self-referential canonical URLs
- ✅ **Language Tag**: `<html lang="en">` (or appropriate language)

```html
<!-- Complete Meta Tags -->
<title>Page Title - Site Name | Value Proposition</title>
<meta name="description" content="Compelling one-sentence description that includes value proposition and key benefit.">

<!-- Open Graph -->
<meta property="og:title" content="Page Title">
<meta property="og:description" content="Description">
<meta property="og:type" content="website">
<meta property="og:url" content="https://example.com/page">
<meta property="og:image" content="https://example.com/og-image.jpg">
<meta property="og:site_name" content="Site Name">
<meta property="og:locale" content="en_US">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Description">
<meta name="twitter:image" content="https://example.com/og-image.jpg">

<!-- Canonical -->
<link rel="canonical" href="https://example.com/page">
```

#### 2. Structured Data (Schema.org)
- ✅ **Organization Schema**: Company/brand information
- ✅ **WebSite Schema**: Site name, URL, search action
- ✅ **WebPage Schema**: Page-specific information
- ✅ **BreadcrumbList Schema**: Navigation breadcrumbs (if multi-page)
- ✅ **Article Schema**: If blog/content pages
- ✅ **LocalBusiness Schema**: If local business

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Company Name",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "Company description",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+1-123-456-7890",
    "contactType": "customer service",
    "email": "contact@example.com"
  },
  "sameAs": [
    "https://facebook.com/company",
    "https://twitter.com/company"
  ]
}
```

#### 3. Technical SEO
- ✅ **Sitemap.xml**: Generated and accessible at `/sitemap.xml`
- ✅ **Robots.txt**: Configured and accessible at `/robots.txt`
- ✅ **Mobile-Friendly**: Responsive design, mobile-first
- ✅ **Page Speed**: Fast loading (90+ Performance score)

```txt
# robots.txt
User-agent: *
Allow: /

Sitemap: https://example.com/sitemap.xml
```

#### 4. Content SEO
- ✅ **Single H1**: One `<h1>` per page
- ✅ **Heading Hierarchy**: Proper H1 → H2 → H3 order
- ✅ **Alt Text**: Descriptive alt text on all images
- ✅ **Internal Linking**: Links to relevant internal pages
- ✅ **Content Quality**: Unique, valuable content (300+ words minimum)

#### 5. Social Sharing
- ✅ **OG Images**: 1200×630px for all pages
- ✅ **Twitter Cards**: Properly configured
- ✅ **Social Links**: Social media links in footer (if applicable)

---

## 📋 Complete Checklist for 100/100

### Performance Checklist
- [ ] All images use WebP with fallback
- [ ] Images lazy-loaded (below-fold)
- [ ] Images have width/height attributes
- [ ] Critical images preloaded
- [ ] Fonts use `font-display: swap`
- [ ] Critical fonts preloaded
- [ ] Max 2 font families, max 2-3 weights
- [ ] JavaScript code-split and minified
- [ ] Bundle size < 100KB gzipped
- [ ] CSS minified and purged
- [ ] CSS size < 20KB gzipped
- [ ] Resource hints (preconnect, dns-prefetch)
- [ ] Proper cache headers
- [ ] LCP < 2.5s
- [ ] FID < 100ms
- [ ] CLS < 0.1
- [ ] FCP < 1.8s
- [ ] TTFB < 600ms

### Accessibility Checklist
- [ ] Semantic HTML elements
- [ ] Single `<h1>` per page
- [ ] Proper heading hierarchy
- [ ] Skip link present
- [ ] Visible focus indicators (2px+)
- [ ] All interactive elements keyboard accessible
- [ ] ARIA labels for icons/buttons
- [ ] ARIA roles for custom components
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Don't rely on color alone
- [ ] All images have alt text
- [ ] Forms have labels
- [ ] Error messages accessible
- [ ] No keyboard traps

### Best Practices Checklist
- [ ] Site served over HTTPS
- [ ] No mixed content
- [ ] Security headers configured
- [ ] No console errors
- [ ] No console warnings
- [ ] Images have aspect ratio
- [ ] Modern JavaScript (ES6+)
- [ ] Minimal third-party scripts
- [ ] Valid HTML
- [ ] Valid CSS

### SEO Checklist
- [ ] Unique title tags (50-60 chars)
- [ ] Meta descriptions (150-160 chars)
- [ ] Complete Open Graph tags
- [ ] Twitter card tags
- [ ] Canonical tags on all pages
- [ ] Organization schema
- [ ] WebSite schema
- [ ] BreadcrumbList schema (if multi-page)
- [ ] Sitemap.xml present
- [ ] Robots.txt configured
- [ ] Single H1 per page
- [ ] Proper heading hierarchy
- [ ] Alt text on all images
- [ ] Mobile-friendly
- [ ] Fast page speed (90+)

---

## 🧪 Testing & Validation

### Lighthouse Testing
1. **Chrome DevTools**: Run Lighthouse audit
2. **PageSpeed Insights**: [pagespeed.web.dev](https://pagespeed.web.dev/)
3. **CI/CD Integration**: Automate Lighthouse in CI/CD pipeline

### Accessibility Testing
1. **WAVE**: [wave.webaim.org](https://wave.webaim.org/)
2. **axe DevTools**: Browser extension
3. **Lighthouse**: Accessibility audit
4. **Keyboard Navigation**: Manual testing
5. **Screen Reader**: NVDA, JAWS, VoiceOver

### SEO Testing
1. **Google Rich Results Test**: [search.google.com/test/rich-results](https://search.google.com/test/rich-results)
2. **Schema.org Validator**: [validator.schema.org](https://validator.schema.org/)
3. **Facebook Debugger**: [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug/)
4. **Twitter Card Validator**: [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator)

---

## 🚫 Common Issues & Solutions

### Performance Issues
- **Large Images**: Compress and use WebP
- **Render-Blocking CSS**: Inline critical CSS or use `preload`
- **Large JavaScript Bundles**: Code split and lazy load
- **No Image Dimensions**: Add width/height attributes
- **Font Loading**: Use `font-display: swap` and preload

### Accessibility Issues
- **Low Contrast**: Use darker text colors (gray-900 instead of gray-700)
- **Missing Alt Text**: Add descriptive alt text to all images
- **No Focus Indicators**: Add visible focus styles
- **Keyboard Traps**: Ensure all modals/menus are keyboard accessible
- **Missing ARIA Labels**: Add labels to icon buttons

### Best Practices Issues
- **Console Errors**: Fix all JavaScript errors
- **Mixed Content**: Ensure all resources use HTTPS
- **Missing Security Headers**: Configure security headers
- **Deprecated APIs**: Update to modern APIs

### SEO Issues
- **Missing Meta Tags**: Add title, description, OG tags
- **No Structured Data**: Add Schema.org markup
- **Missing Sitemap**: Generate and submit sitemap
- **No Robots.txt**: Create robots.txt file
- **Duplicate Content**: Use canonical tags

---

## 📚 Resources

### Tools
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [WAVE](https://wave.webaim.org/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)

### Documentation
- [Web.dev Performance](https://web.dev/performance/)
- [Web.dev Accessibility](https://web.dev/accessible/)
- [Web.dev SEO](https://web.dev/learn/seo/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Remember**: Achieving 100/100 in all categories requires attention to detail, proper optimization, and thorough testing. Use this guide as a checklist and validate with Lighthouse after each change.

---

*Last Updated: [Auto-update]*

