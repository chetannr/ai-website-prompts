# Accessibility Standards

> **Goal**: WCAG 2.1 AA compliance - websites usable by everyone.

---

## 📋 Accessibility Checklist

### Phase 1: Semantic HTML
- [ ] **Proper Elements**: Use semantic HTML (`<header>`, `<nav>`, `<main>`, `<footer>`, `<article>`, `<section>`)
- [ ] **Heading Hierarchy**: Single `<h1>`, proper H2 → H3 order (no skipping)
- [ ] **Landmarks**: Proper ARIA landmarks or semantic elements
- [ ] **Lists**: Use `<ul>`, `<ol>`, `<dl>` for lists
- [ ] **Forms**: Proper form structure with `<label>`, `<fieldset>`, `<legend>`

### Phase 2: Keyboard Navigation
- [ ] **Tab Order**: Logical tab order through all interactive elements
- [ ] **Focus Indicators**: Visible focus styles on all interactive elements
- [ ] **Skip Links**: "Skip to main content" link at top
- [ ] **Keyboard Traps**: No keyboard traps (can tab out of modals/menus)
- [ ] **Keyboard Shortcuts**: Document any keyboard shortcuts

### Phase 3: ARIA & Screen Readers
- [ ] **ARIA Labels**: Descriptive labels for icons, buttons without text
- [ ] **ARIA Roles**: Proper roles for custom components
- [ ] **ARIA States**: `aria-expanded`, `aria-selected`, `aria-hidden` where needed
- [ ] **Live Regions**: `aria-live` for dynamic content updates
- [ ] **Descriptions**: `aria-describedby` for form errors, help text

### Phase 4: Visual Accessibility
- [ ] **Color Contrast**: WCAG AA contrast ratios (4.5:1 text, 3:1 large text)
- [ ] **Color Independence**: Don't rely on color alone to convey information
- [ ] **Text Size**: Minimum 16px body text, scalable to 200%
- [ ] **Focus Styles**: Clear, visible focus indicators (2px+ outline)
- [ ] **Text Alternatives**: Alt text for all images

### Phase 5: Forms & Interactions
- [ ] **Labels**: All inputs have associated `<label>`
- [ ] **Error Messages**: Clear, descriptive error messages
- [ ] **Validation**: Real-time validation with `aria-invalid`, `aria-describedby`
- [ ] **Required Fields**: Indicated with `aria-required` or visual indicator
- [ ] **Help Text**: Accessible help text for complex inputs

---

## 🎯 WCAG 2.1 AA Requirements

### Perceivable
- ✅ **Text Alternatives**: Alt text for images
- ✅ **Time-based Media**: Captions for videos (if applicable)
- ✅ **Adaptable**: Content structure, not presentation-dependent
- ✅ **Distinguishable**: Color contrast, text size, audio control

### Operable
- ✅ **Keyboard Accessible**: All functionality via keyboard
- ✅ **Enough Time**: No time limits (or adjustable)
- ✅ **Seizures**: No flashing content
- ✅ **Navigable**: Skip links, headings, focus order

### Understandable
- ✅ **Readable**: Language declared, readable text
- ✅ **Predictable**: Consistent navigation, no unexpected changes
- ✅ **Input Assistance**: Error identification, labels, suggestions

### Robust
- ✅ **Compatible**: Valid HTML, proper ARIA, screen reader compatible

---

## 🔧 Implementation Guide

### 1. Semantic HTML

#### Proper Structure
```html
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
</header>

<main id="main-content">
  <article>
    <h1>Page Title</h1>
    <section>
      <h2>Section Title</h2>
      <p>Content...</p>
    </section>
  </article>
</main>

<footer>
  <p>&copy; 2024 Company Name</p>
</footer>
```

#### Heading Hierarchy
```html
<h1>Main Page Title</h1>
  <h2>Section Title</h2>
    <h3>Subsection Title</h3>
  <h2>Another Section</h2>
    <h3>Subsection</h3>
```

---

### 2. Skip Link

#### Implementation
```html
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
</style>
```

---

### 3. Focus Styles

#### Global Focus Styles
```css
/* Visible focus indicators */
*:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
  border-radius: 2px;
}

/* Remove default outline for mouse users */
*:focus:not(:focus-visible) {
  outline: none;
}

/* Button focus */
button:focus-visible,
a:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 4px;
}
```

---

### 4. ARIA Labels

#### Icons & Buttons
```html
<!-- Icon button -->
<button aria-label="Close menu">
  <svg aria-hidden="true">
    <path d="..."/>
  </svg>
</button>

<!-- Decorative icon -->
<img src="icon.svg" alt="" aria-hidden="true">

<!-- Informative icon -->
<img src="warning.svg" alt="Warning: This action cannot be undone">
```

#### Form Labels
```html
<label for="email">Email Address</label>
<input 
  type="email" 
  id="email" 
  name="email"
  aria-required="true"
  aria-describedby="email-error"
>
<span id="email-error" class="error" role="alert">
  Please enter a valid email address
</span>
```

---

### 5. Color Contrast

#### Contrast Ratios
- **Normal Text**: 4.5:1 contrast ratio (WCAG AA)
- **Large Text** (18px+ or 14px+ bold): 3:1 contrast ratio
- **UI Components**: 3:1 contrast ratio
- **Graphics**: 3:1 contrast ratio (if informative)

#### Tools
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/)
- Chrome DevTools: Accessibility panel

#### Example
```css
/* Good contrast */
.text-primary {
  color: #1c1917; /* Dark gray on white = 16.5:1 */
}

.text-secondary {
  color: #78716c; /* Medium gray on white = 4.6:1 */
}

/* Bad contrast - avoid */
.text-light {
  color: #d4d4d4; /* Light gray on white = 1.4:1 - FAILS */
}
```

---

### 6. Forms

#### Accessible Form
```html
<form>
  <fieldset>
    <legend>Contact Information</legend>
    
    <div>
      <label for="name">Full Name *</label>
      <input 
        type="text" 
        id="name" 
        name="name"
        required
        aria-required="true"
        aria-describedby="name-help"
      >
      <span id="name-help" class="help-text">
        Enter your first and last name
      </span>
    </div>
    
    <div>
      <label for="email">Email Address *</label>
      <input 
        type="email" 
        id="email" 
        name="email"
        required
        aria-required="true"
        aria-invalid="false"
        aria-describedby="email-error"
      >
      <span id="email-error" class="error" role="alert" aria-live="polite">
        <!-- Error message appears here -->
      </span>
    </div>
    
    <button type="submit">Submit</button>
  </fieldset>
</form>
```

#### Form Validation
```typescript
function validateEmail(email: string): boolean {
  const isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  const input = document.getElementById('email') as HTMLInputElement;
  const error = document.getElementById('email-error');
  
  if (!isValid) {
    input.setAttribute('aria-invalid', 'true');
    if (error) {
      error.textContent = 'Please enter a valid email address';
      error.setAttribute('role', 'alert');
    }
    return false;
  }
  
  input.setAttribute('aria-invalid', 'false');
  if (error) {
    error.textContent = '';
  }
  return true;
}
```

---

### 7. Images

#### Alt Text Guidelines
```html
<!-- Informative image -->
<img src="chart.jpg" alt="Sales increased 25% from Q1 to Q2 2024">

<!-- Decorative image -->
<img src="decoration.jpg" alt="" aria-hidden="true">

<!-- Complex image (chart, diagram) -->
<img src="chart.jpg" alt="Sales chart showing 25% increase">
<figcaption>
  Detailed description of chart data and trends
</figcaption>

<!-- Image with text -->
<img src="logo.jpg" alt="Company Name Logo">
```

#### Alt Text Rules
- **Be specific**: Describe what's in the image
- **Be concise**: Keep under 125 characters
- **Don't say "image of"**: Screen readers already announce it
- **Include context**: Why is this image here?
- **Decorative images**: Use empty alt `alt=""`

---

### 8. Keyboard Navigation

#### Tab Order
- Logical order (left to right, top to bottom)
- Skip links at top
- Focusable elements: links, buttons, inputs, selects, textareas
- Non-focusable: Use `tabindex="-1"` for programmatic focus only
- Custom components: Make keyboard accessible

#### Keyboard Shortcuts
```typescript
// Escape to close modal
useEffect(() => {
  function handleEscape(e: KeyboardEvent) {
    if (e.key === 'Escape' && isOpen) {
      closeModal();
    }
  }
  document.addEventListener('keydown', handleEscape);
  return () => document.removeEventListener('keydown', handleEscape);
}, [isOpen]);
```

---

### 9. ARIA Patterns

#### Modal/Dialog
```html
<div 
  role="dialog" 
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <h2 id="modal-title">Modal Title</h2>
  <p id="modal-description">Modal description</p>
  <button aria-label="Close modal">×</button>
</div>
```

#### Menu
```html
<button 
  aria-expanded="false"
  aria-controls="menu"
  aria-haspopup="true"
>
  Menu
</button>
<ul id="menu" role="menu" hidden>
  <li role="menuitem"><a href="/">Home</a></li>
  <li role="menuitem"><a href="/about">About</a></li>
</ul>
```

#### Tabs
```html
<div role="tablist" aria-label="Product tabs">
  <button 
    role="tab"
    aria-selected="true"
    aria-controls="panel-1"
    id="tab-1"
  >
    Description
  </button>
  <div 
    role="tabpanel"
    id="panel-1"
    aria-labelledby="tab-1"
  >
    Content...
  </div>
</div>
```

---

## 🧪 Testing

### Automated Testing
- **WAVE**: [wave.webaim.org](https://wave.webaim.org/)
- **axe DevTools**: Browser extension
- **Lighthouse**: Accessibility audit
- **Pa11y**: CLI tool

### Manual Testing
- **Keyboard Navigation**: Tab through entire site
- **Screen Reader**: NVDA (Windows), JAWS, VoiceOver (Mac/iOS)
- **Color Contrast**: Check with tools
- **Zoom**: Test at 200% zoom
- **Focus Indicators**: Verify all interactive elements have focus styles

### Screen Reader Testing
```bash
# Test with NVDA (Windows)
# Test with VoiceOver (Mac: Cmd+F5)
# Test with JAWS (Windows)
```

---

## ✅ Accessibility Checklist

### HTML Structure
- [ ] Semantic HTML elements
- [ ] Single `<h1>` per page
- [ ] Proper heading hierarchy
- [ ] Landmarks (header, nav, main, footer)
- [ ] Lists use `<ul>`, `<ol>`, `<dl>`

### Keyboard Navigation
- [ ] All interactive elements keyboard accessible
- [ ] Logical tab order
- [ ] Visible focus indicators
- [ ] Skip link present
- [ ] No keyboard traps

### ARIA
- [ ] ARIA labels for icons/buttons
- [ ] ARIA roles for custom components
- [ ] ARIA states (expanded, selected, etc.)
- [ ] ARIA descriptions for complex content
- [ ] Live regions for dynamic updates

### Visual
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Don't rely on color alone
- [ ] Text scalable to 200%
- [ ] Focus indicators visible (2px+)
- [ ] Alt text on all images

### Forms
- [ ] All inputs have labels
- [ ] Error messages clear and accessible
- [ ] Validation with `aria-invalid`
- [ ] Required fields indicated
- [ ] Help text accessible

### Testing
- [ ] WAVE: No critical errors
- [ ] Keyboard navigation tested
- [ ] Screen reader tested
- [ ] Color contrast verified
- [ ] Zoom tested (200%)

---

## 🚫 Accessibility Anti-Patterns

### Avoid
- ❌ `<div>` for buttons (use `<button>`)
- ❌ `<div>` for links (use `<a>`)
- ❌ Missing alt text
- ❌ Poor color contrast
- ❌ No focus indicators
- ❌ Keyboard traps
- ❌ Missing labels
- ❌ Decorative images with alt text
- ❌ Skipping heading levels
- ❌ Relying on color alone

### Prefer
- ✅ Semantic HTML
- ✅ Proper form labels
- ✅ Descriptive alt text
- ✅ WCAG AA contrast
- ✅ Clear focus indicators
- ✅ Keyboard accessible
- ✅ ARIA where needed
- ✅ Empty alt for decorative images
- ✅ Proper heading hierarchy
- ✅ Multiple indicators (color + text)

---

## 📚 Resources

### Documentation
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)

### Tools
- [WAVE](https://wave.webaim.org/)
- [axe DevTools](https://www.deque.com/axe/devtools/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/)

### Screen Readers
- **NVDA**: Free, Windows
- **JAWS**: Paid, Windows
- **VoiceOver**: Built-in, Mac/iOS
- **TalkBack**: Built-in, Android

---

**Remember**: Accessibility is not optional. Every user deserves equal access to your website.

---

*Last Updated: [Auto-update]*

