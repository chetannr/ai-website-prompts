# Testing and Deployment Workflow

> **Purpose**: Standardized workflow for AI assistants to test and deploy code changes after user approval.

---

## 🔄 Workflow Pattern

When a user requests changes and approves them, follow this standardized testing and deployment process:

### Step 1: Fix Linting Errors
```bash
# Run linter to check for errors
npm run lint

# Fix any linting errors before proceeding
# Common issues:
# - Unused variables (remove or prefix with _)
# - Self-assignments (remove redundant code)
# - TypeScript errors (fix type issues)
# - Missing dependencies
```

**Action**: Fix all linting errors before proceeding to build.

---

### Step 2: Build and Test
```bash
# Run the build command
npm run build

# Verify build succeeds without errors
# Check for:
# - TypeScript compilation errors
# - Missing dependencies
# - Build configuration issues
# - Asset optimization issues
```

**Action**: Ensure build completes successfully. If build fails, fix errors and rebuild.

---

### Step 3: Deploy to GitHub Pages
```bash
# Deploy using the deploy script (typically runs build + gh-pages)
npm run deploy

# Or manually:
npm run build && gh-pages -d dist
```

**Expected Output**: 
- Build completes successfully
- Files are pushed to `gh-pages` branch
- Output shows "Published" confirmation

---

## 📋 Standard Package.json Scripts

Ensure these scripts are available in `package.json`:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview",
    "deploy": "npm run build && gh-pages -d dist"
  },
  "devDependencies": {
    "gh-pages": "^6.3.0"
  }
}
```

---

## ✅ Pre-Deployment Checklist

Before running deployment, verify:

- [ ] **Linting**: `npm run lint` passes with no errors
- [ ] **Build**: `npm run build` completes successfully
- [ ] **No Console Errors**: Check for runtime errors
- [ ] **TypeScript**: No type errors
- [ ] **Dependencies**: All required packages installed

---

## 🚀 Deployment Commands by Framework

### Vite + React (Most Common)
```bash
npm run lint          # Check for errors
npm run build         # Build the project
npm run deploy        # Deploy to gh-pages
```

### Next.js
```bash
npm run lint          # Check for errors
npm run build         # Build the project
npm run export        # Export static site (if static export)
# Then deploy using gh-pages or other method
```

### Vanilla HTML/CSS/JS
```bash
# Usually no build step needed
# Just deploy the dist/ or public/ folder
gh-pages -d dist
```

---

## 🔧 Common Issues and Solutions

### Issue: Linting Errors
**Solution**: 
- Fix unused variables
- Remove self-assignments
- Fix TypeScript errors
- Add missing type definitions

### Issue: Build Fails
**Solution**:
- Check TypeScript errors
- Verify all imports are correct
- Check for missing dependencies
- Verify build configuration

### Issue: Deployment Fails
**Solution**:
- Ensure `gh-pages` package is installed
- Check GitHub authentication
- Verify repository has gh-pages branch enabled
- Check base path in build config matches GitHub Pages path

---

## 📝 Workflow Summary

**When user approves changes:**

1. ✅ **Lint**: Run `npm run lint` and fix all errors
2. ✅ **Build**: Run `npm run build` and verify success
3. ✅ **Deploy**: Run `npm run deploy` to push to gh-pages
4. ✅ **Confirm**: Verify deployment succeeded (look for "Published" message)

**Always follow this order. Never skip linting or building before deployment.**

---

## 🎯 Best Practices

### For AI Assistants
- **Always lint first**: Catch errors before building
- **Always build before deploy**: Ensure code compiles
- **Verify success**: Check command output for errors
- **Report status**: Inform user of deployment status

### For Projects
- **Automated scripts**: Use npm scripts for consistency
- **Pre-deploy hooks**: Use `prebuild` or `predeploy` for optimization
- **Error handling**: Scripts should fail fast on errors
- **Documentation**: Keep deployment instructions in README

---

## 🔗 Related Documentation

- **[DEPLOYMENT_STANDARDS.md](./DEPLOYMENT_STANDARDS.md)** - Full deployment guide
- **[WEBSITE_CREATION_RULEBOOK.md](./WEBSITE_CREATION_RULEBOOK.md)** - Overall project workflow
- **[TECHNICAL_STACK.md](./TECHNICAL_STACK.md)** - Technology configurations

---

## 💡 Example Workflow

```bash
# User: "test and push the code to gh-pages"

# Step 1: Lint
npm run lint
# Output: ✓ No linting errors

# Step 2: Build
npm run build
# Output: ✓ Build successful

# Step 3: Deploy
npm run deploy
# Output: ✓ Published to gh-pages branch

# Report to user:
# "✅ All tests passed. Code has been built and deployed to GitHub Pages."
```

---

**Remember**: Testing and deployment should be automatic after user approval. Always verify each step succeeds before proceeding to the next.

---

*Last Updated: [Auto-update]*

