# Performance Standards

> **Goal**: Every website must achieve 90+ Lighthouse scores and load in under 3 seconds.

---

## 📊 Performance Targets

### Lighthouse Scores (Minimum)
- **Performance**: 90+
- **Accessibility**: 90+
- **Best Practices**: 90+
- **SEO**: 90+

### Core Web Vitals
- **LCP (Largest Contentful Paint)**: < 2.5s
- **FID (First Input Delay)**: < 100ms
- **CLS (Cumulative Layout Shift)**: < 0.1
- **FCP (First Contentful Paint)**: < 1.8s
- **TTFB (Time to First Byte)**: < 600ms

### Load Times
- **3G Network**: < 3s
- **4G Network**: < 2s
- **Desktop**: < 1.5s

---

## 🎯 Optimization Checklist

### Images
- [ ] **Format**: WebP format (with fallback)
- [ ] **Compression**: Optimized (TinyPNG, Squoosh)
- [ ] **Sizing**: Correct dimensions (not oversized)
- [ ] **Lazy Loading**: Lazy load below-fold images
- [ ] **Responsive**: `srcset` or `sizes` attribute
- [ ] **Dimensions**: Width/height attributes to prevent CLS

#### Image Optimization
```html
<!-- Optimized Image -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <img 
    src="image.jpg"
    alt="Descriptive alt text"
    loading="lazy"
    width="1200"
    height="630"
    decoding="async"
  />
</picture>
```

#### Image Compression Targets
- **Hero Images**: < 200KB
- **Content Images**: < 100KB
- **Thumbnails**: < 50KB
- **Icons**: < 10KB (SVG preferred)

---

### Fonts
- [ ] **Font Loading**: `font-display: swap`
- [ ] **Preload**: Preload critical fonts
- [ ] **Subset**: Use font subsets (if possible)
- [ ] **Format**: WOFF2 format (modern browsers)
- [ ] **Fallback**: System font fallback

#### Font Optimization
```css
/* Preload critical fonts */
<link rel="preload" href="/fonts/font.woff2" as="font" type="font/woff2" crossorigin>

/* Font face with display swap */
@font-face {
  font-family: 'Font Name';
  src: url('/fonts/font.woff2') format('woff2');
  font-display: swap;
  font-weight: 400;
  font-style: normal;
}
```

#### Font Loading Strategy
1. **Preload**: Critical fonts (headings)
2. **Display Swap**: Show fallback immediately
3. **Limit Fonts**: Max 2 font families
4. **Limit Weights**: Max 2-3 weights per font

---

### JavaScript
- [ ] **Code Splitting**: Automatic with Vite/React
- [ ] **Tree Shaking**: Remove unused code
- [ ] **Minification**: Minified in production
- [ ] **Bundle Size**: < 100KB gzipped (initial)
- [ ] **Lazy Loading**: Lazy load non-critical JS
- [ ] **No Blocking**: Defer non-critical scripts

#### Bundle Optimization
```typescript
// vite.config.ts
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          utils: ['./src/utils'],
        },
      },
    },
  },
});
```

---

### CSS
- [ ] **Minification**: Minified in production
- [ ] **Purge**: Remove unused CSS (Tailwind auto-purges)
- [ ] **Critical CSS**: Inline critical CSS (if needed)
- [ ] **No Render-Blocking**: Load CSS efficiently
- [ ] **Size**: < 20KB gzipped

#### CSS Optimization
- Use Tailwind CSS (auto-purges unused styles)
- Avoid large CSS frameworks
- Use CSS variables for theming
- Minimize custom CSS

---

### HTML
- [ ] **Minification**: Minified in production
- [ ] **Semantic**: Proper semantic HTML
- [ ] **Size**: < 50KB per page
- [ ] **Structure**: Clean, valid HTML

---

### Caching
- [ ] **Browser Caching**: Set cache headers
- [ ] **CDN**: Use CDN for static assets
- [ ] **Service Worker**: Consider PWA (optional)

#### Cache Headers
```
# Static assets (1 year)
Cache-Control: public, max-age=31536000, immutable

# HTML (1 hour)
Cache-Control: public, max-age=3600

# API responses (5 minutes)
Cache-Control: public, max-age=300
```

---

## 🚀 Performance Optimization Techniques

### 1. Image Optimization

#### Use WebP with Fallback
```html
<picture>
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description">
</picture>
```

#### Lazy Loading
```html
<img src="image.jpg" alt="Description" loading="lazy">
```

#### Responsive Images
```html
<img 
  srcset="
    image-400w.jpg 400w,
    image-800w.jpg 800w,
    image-1200w.jpg 1200w
  "
  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
  src="image-800w.jpg"
  alt="Description"
>
```

---

### 2. Font Optimization

#### Preload Critical Fonts
```html
<link rel="preload" href="/fonts/heading.woff2" as="font" type="font/woff2" crossorigin>
```

#### Font Display Swap
```css
@font-face {
  font-family: 'Font';
  src: url('/fonts/font.woff2') format('woff2');
  font-display: swap;
}
```

#### System Font Fallback
```css
font-family: 'Custom Font', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

---

### 3. Code Splitting

#### React Lazy Loading
```typescript
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <HeavyComponent />
    </Suspense>
  );
}
```

#### Route-Based Splitting
```typescript
// Automatic with React Router or TanStack Router
const HomePage = lazy(() => import('./pages/Home'));
const AboutPage = lazy(() => import('./pages/About'));
```

---

### 4. Resource Hints

#### Preconnect
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```

#### Prefetch
```html
<link rel="prefetch" href="/next-page.html">
```

#### DNS Prefetch
```html
<link rel="dns-prefetch" href="https://api.example.com">
```

---

### 5. Minimize Render-Blocking

#### Defer Non-Critical CSS
```html
<link rel="stylesheet" href="critical.css">
<link rel="preload" href="non-critical.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
```

#### Async Scripts
```html
<script src="analytics.js" async></script>
```

---

## 📊 Performance Monitoring

### Tools
- **Lighthouse**: Chrome DevTools, CI/CD
- **PageSpeed Insights**: [pagespeed.web.dev](https://pagespeed.web.dev/)
- **WebPageTest**: [webpagetest.org](https://www.webpagetest.org/)
- **Chrome DevTools**: Performance tab
- **React DevTools Profiler**: Component performance

### Metrics to Track
- Lighthouse scores (all 4 metrics)
- Core Web Vitals (LCP, FID, CLS)
- Load times (FCP, TTFB)
- Bundle sizes
- Image sizes
- Network requests

---

## ✅ Performance Checklist

### Images
- [ ] WebP format with fallback
- [ ] Optimized (< 200KB hero, < 100KB content)
- [ ] Lazy loading (below-fold)
- [ ] Responsive (`srcset`/`sizes`)
- [ ] Width/height attributes
- [ ] Proper alt text

### Fonts
- [ ] `font-display: swap`
- [ ] Preload critical fonts
- [ ] WOFF2 format
- [ ] System font fallback
- [ ] Max 2 font families
- [ ] Max 2-3 weights

### JavaScript
- [ ] Code splitting
- [ ] Tree shaking
- [ ] Minified
- [ ] Bundle < 100KB gzipped
- [ ] Lazy loading non-critical
- [ ] No blocking scripts

### CSS
- [ ] Minified
- [ ] Purged (unused removed)
- [ ] < 20KB gzipped
- [ ] No render-blocking
- [ ] Critical CSS inlined (if needed)

### HTML
- [ ] Minified
- [ ] Semantic
- [ ] < 50KB per page
- [ ] Valid HTML

### Caching
- [ ] Browser cache headers
- [ ] CDN for static assets
- [ ] Proper cache strategy

### Core Web Vitals
- [ ] LCP < 2.5s
- [ ] FID < 100ms
- [ ] CLS < 0.1
- [ ] FCP < 1.8s
- [ ] TTFB < 600ms

### Lighthouse
- [ ] Performance: 90+
- [ ] Accessibility: 90+
- [ ] Best Practices: 90+
- [ ] SEO: 90+

---

## 🚫 Performance Anti-Patterns

### Avoid
- ❌ Unoptimized images (large files)
- ❌ Too many fonts
- ❌ Render-blocking CSS/JS
- ❌ Large bundle sizes
- ❌ No lazy loading
- ❌ No code splitting
- ❌ Blocking scripts
- ❌ Unused CSS/JS
- ❌ No caching
- ❌ Poor font loading

### Prefer
- ✅ WebP images, optimized
- ✅ Max 2 fonts
- ✅ Non-blocking resources
- ✅ Small bundles
- ✅ Lazy loading
- ✅ Code splitting
- ✅ Async/defer scripts
- ✅ Purged CSS
- ✅ Proper caching
- ✅ Font display swap

---

## 🔧 Performance Optimization Tools

### Image Optimization
- [TinyPNG](https://tinypng.com/) - Compress PNG/JPG
- [Squoosh](https://squoosh.app/) - Convert to WebP
- [ImageOptim](https://imageoptim.com/) - Mac app
- [Sharp](https://sharp.pixelplumbing.com/) - Node.js library

### Font Optimization
- [Google Fonts](https://fonts.google.com/) - Use `&display=swap`
- [Font Squirrel](https://www.fontsquirrel.com/) - Web font generator
- [Font Subsetter](https://everythingfonts.com/subsetter) - Create subsets

### Build Tools
- **Vite**: Automatic code splitting, tree shaking
- **Webpack**: Manual optimization (if needed)
- **Rollup**: For libraries

### Analysis Tools
- **Lighthouse**: Chrome DevTools
- **Bundle Analyzer**: `vite-bundle-visualizer`
- **Webpack Bundle Analyzer**: For webpack projects

---

## 📈 Performance Budget

### Recommended Budgets
- **Total Page Weight**: < 1MB (uncompressed)
- **JavaScript**: < 100KB (gzipped)
- **CSS**: < 20KB (gzipped)
- **Images**: < 500KB total (optimized)
- **Fonts**: < 50KB (gzipped)
- **HTML**: < 50KB per page

### Monitoring
- Set up performance budgets in CI/CD
- Alert if budgets exceeded
- Track over time

---

## 🎯 Performance Goals

### Initial Load
- **Time to Interactive**: < 3s (3G)
- **First Contentful Paint**: < 1.8s
- **Largest Contentful Paint**: < 2.5s

### User Experience
- **Smooth Scrolling**: 60fps
- **No Layout Shift**: CLS < 0.1
- **Fast Interactions**: FID < 100ms

### SEO Impact
- **Fast Load**: Better rankings
- **Core Web Vitals**: Ranking factor
- **User Experience**: Lower bounce rate

---

**Remember**: Performance is not optional. Fast sites rank better, convert better, and provide better user experience.

---

*Last Updated: [Auto-update]*

