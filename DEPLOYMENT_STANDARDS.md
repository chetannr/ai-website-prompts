# Deployment Standards

> **Goal**: Consistent, reliable deployment process for all websites.

---

## 📋 Pre-Deployment Checklist

### Content Verification
- [ ] All text content proofread and final
- [ ] All images optimized and in place
- [ ] Contact information verified (phone, email, address)
- [ ] Social media links confirmed
- [ ] Legal pages ready (Privacy Policy, Terms if needed)
- [ ] Favicon created and added
- [ ] Logo files ready (SVG preferred)

### Technical Verification
- [ ] All links work (no 404 errors)
- [ ] Forms validated and functional
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Mobile tested (320px to 1920px)
- [ ] Performance optimized (Lighthouse 90+)
- [ ] Accessibility verified (WCAG AA)
- [ ] SEO implemented (see SEO_CHECKLIST.md)
- [ ] No console errors
- [ ] Build succeeds without errors

### Configuration
- [ ] Environment variables set
- [ ] API keys configured (if needed)
- [ ] Analytics configured (if needed)
- [ ] Domain name registered
- [ ] DNS configured (if custom domain)

---

## 🚀 Deployment Methods

### Method 1: GitHub Pages (Recommended for Static Sites)

#### Setup
1. **Repository**: Create GitHub repository
2. **Build**: Run `npm run build`
3. **Deploy**: Use `gh-pages` package or GitHub Actions

#### Using gh-pages Package
```bash
# Install
npm install --save-dev gh-pages

# Add to package.json
{
  "scripts": {
    "deploy": "npm run build && gh-pages -d dist"
  }
}

# Deploy
npm run deploy
```

#### Using GitHub Actions (Recommended)
```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm install
      - run: npm run build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

#### Configuration
1. Go to repository **Settings** → **Pages**
2. Source: **GitHub Actions** (or **Deploy from branch** → `gh-pages`)
3. Site URL: `https://username.github.io/repository-name/`

#### Custom Domain
1. Add `CNAME` file to `public/` folder:
   ```
   www.example.com
   ```
2. Configure DNS:
   - Type: `CNAME`
   - Name: `www`
   - Value: `username.github.io`
3. Enable HTTPS in GitHub Pages settings

---

### Method 2: Netlify (Easiest)

#### Drag & Drop
1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag `dist/` folder
3. Site is live instantly!

#### Git Integration (Recommended)
1. Sign up at [Netlify](https://netlify.com)
2. **New site from Git**
3. Connect GitHub repository
4. Build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
5. Deploy!

#### Custom Domain
1. Go to **Site settings** → **Domain management**
2. Add custom domain
3. Follow DNS instructions
4. SSL automatically provisioned

---

### Method 3: Vercel (Best for React/Next.js)

#### Setup
1. Sign up at [Vercel](https://vercel.com)
2. **Import Project** from GitHub
3. Framework: **Vite** (or auto-detected)
4. Build settings:
   - Build command: `npm run build`
   - Output directory: `dist`
5. Deploy!

#### Custom Domain
1. Go to **Project Settings** → **Domains**
2. Add domain
3. Configure DNS as instructed
4. SSL automatically provisioned

---

### Method 4: Cloudflare Pages (Fast & Free)

#### Setup
1. Sign up at [Cloudflare Pages](https://pages.cloudflare.com)
2. Connect GitHub repository
3. Build settings:
   - Build command: `npm run build`
   - Build output directory: `dist`
4. Deploy!

#### Custom Domain
1. Go to **Custom domains**
2. Add domain
3. Configure DNS in Cloudflare
4. SSL automatically provisioned

---

### Method 5: Traditional Web Hosting (FTP/SFTP)

#### Setup
1. Get FTP credentials from hosting provider
2. Use FTP client (FileZilla, Cyberduck, etc.)
3. Upload `dist/` folder contents to `public_html/` or `www/`
4. Set permissions:
   - Folders: `755`
   - Files: `644`

#### File Structure
```
public_html/
├── index.html
├── assets/
│   ├── index-xxx.js
│   └── index-xxx.css
├── images/
└── favicon.ico
```

---

## 🔧 Build Configuration

### Vite Build Config
```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: 'esbuild',
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },
  base: '/', // Change to '/repository-name/' for GitHub Pages
});
```

### Environment Variables
```bash
# .env.production
VITE_SITE_URL=https://example.com
VITE_API_URL=https://api.example.com
```

---

## 🌐 DNS Configuration

### For Custom Domain

#### A Record (Root Domain)
```
Type: A
Name: @
Value: [Hosting Provider IP]
TTL: 3600
```

#### CNAME Record (www)
```
Type: CNAME
Name: www
Value: [Hosting Provider Domain]
TTL: 3600
```

### Hosting Provider IPs
- **Netlify**: `75.2.60.5`
- **Vercel**: Use their DNS (not A record)
- **Cloudflare Pages**: Use Cloudflare DNS
- **GitHub Pages**: `185.199.108.153` (and others)

---

## 🔒 SSL/HTTPS

### Automatic SSL
- **Netlify**: Automatic (Let's Encrypt)
- **Vercel**: Automatic
- **Cloudflare Pages**: Automatic
- **GitHub Pages**: Automatic (when custom domain added)

### Manual SSL
- **Traditional Hosting**: Install Let's Encrypt certificate
- **Cloudflare**: Enable SSL/TLS (Full or Full Strict)

---

## 📧 Email Configuration (Optional)

### Zoho Mail Setup
1. Sign up at [Zoho Mail](https://www.zoho.com/mail/)
2. Add domain
3. Configure DNS records:

#### MX Records
```
Type: MX
Name: @
Priority: 10
Value: mx.zoho.in

Type: MX
Name: @
Priority: 20
Value: mx2.zoho.in
```

#### SPF Record
```
Type: TXT
Name: @
Value: v=spf1 include:zoho.in ~all
```

#### DKIM Record
```
Type: TXT
Name: zoho._domainkey
Value: [Provided by Zoho]
```

---

## 🧪 Post-Deployment Testing

### Functionality Tests
- [ ] All pages load correctly
- [ ] All links work (no 404s)
- [ ] Images load correctly
- [ ] Forms submit successfully
- [ ] Navigation works
- [ ] Mobile menu works
- [ ] Search works (if applicable)

### Performance Tests
- [ ] Lighthouse Performance: 90+
- [ ] Page load time: < 3s
- [ ] Images optimized
- [ ] No console errors

### SEO Tests
- [ ] Sitemap accessible: `https://example.com/sitemap.xml`
- [ ] Robots.txt accessible: `https://example.com/robots.txt`
- [ ] Meta tags present (view source)
- [ ] Structured data validated
- [ ] Google Search Console: No errors

### Accessibility Tests
- [ ] WAVE: No critical errors
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Color contrast passes

### Cross-Browser Tests
- [ ] Chrome (desktop & mobile)
- [ ] Firefox
- [ ] Safari (desktop & iOS)
- [ ] Edge

---

## 🔄 Update Process

### For Git-Based Deployments
```bash
# Make changes
git add .
git commit -m "Update: description"
git push origin main

# Auto-deploys (if using GitHub Actions, Netlify, Vercel)
```

### For FTP Deployments
1. Make changes locally
2. Build: `npm run build`
3. Upload changed files via FTP
4. Clear CDN cache (if applicable)

---

## 🆘 Troubleshooting

### Site Not Loading
1. **Check DNS**: Use [DNS Checker](https://dnschecker.org)
2. **Clear Cache**: Hard refresh (Ctrl+Shift+R / Cmd+Shift+R)
3. **Check SSL**: Ensure HTTPS is enabled
4. **Wait**: DNS can take 24-48 hours to propagate

### 404 Errors
1. **Check Base Path**: Verify `vite.config.ts` base path
2. **Check File Paths**: Ensure all paths are correct
3. **Check Server Config**: Some servers need `.htaccess` for SPA routing

### Images Not Loading
1. **Check Paths**: Verify image paths are correct
2. **Check Permissions**: Ensure files have correct permissions
3. **Check Format**: Verify image formats are supported

### Build Errors
1. **Check Dependencies**: Run `npm install`
2. **Check TypeScript**: Run `npm run build` locally first
3. **Check Environment Variables**: Ensure all vars are set

---

## 📊 Deployment Checklist

### Before Deployment
- [ ] All content final
- [ ] All images optimized
- [ ] All links verified
- [ ] Forms tested
- [ ] Cross-browser tested
- [ ] Performance optimized
- [ ] SEO implemented
- [ ] Accessibility verified

### Deployment
- [ ] Build succeeds
- [ ] Files uploaded/deployed
- [ ] DNS configured (if custom domain)
- [ ] SSL enabled
- [ ] Site accessible

### After Deployment
- [ ] All pages load
- [ ] All links work
- [ ] Forms functional
- [ ] Performance verified
- [ ] SEO verified
- [ ] Analytics configured (if needed)
- [ ] Sitemap submitted
- [ ] Search Console verified

---

## 🎯 Deployment Best Practices

### Version Control
- ✅ Use Git for all projects
- ✅ Commit frequently with clear messages
- ✅ Use branches for features
- ✅ Tag releases

### Build Process
- ✅ Build locally before deploying
- ✅ Test build output locally
- ✅ Verify no errors in build
- ✅ Check bundle sizes

### Deployment
- ✅ Use automated deployments (CI/CD)
- ✅ Test on staging first (if possible)
- ✅ Deploy during low-traffic hours
- ✅ Monitor after deployment

### Post-Deployment
- ✅ Verify site is live
- ✅ Test critical paths
- ✅ Monitor error logs
- ✅ Check analytics

---

## 📚 Deployment Resources

### Documentation
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Netlify Docs](https://docs.netlify.com/)
- [Vercel Docs](https://vercel.com/docs)
- [Cloudflare Pages Docs](https://developers.cloudflare.com/pages/)

### Tools
- [DNS Checker](https://dnschecker.org)
- [SSL Labs](https://www.ssllabs.com/ssltest/)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)

---

**Remember**: Always test locally before deploying. A broken deployment is worse than no deployment.

---

*Last Updated: [Auto-update]*

