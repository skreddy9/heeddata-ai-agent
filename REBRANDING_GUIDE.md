# Rebranding Guide: From Kortix Suna to Your Company

This guide will help you rebrand the AI agent from "Kortix Suna" to your company's branding.

## Quick Start

Replace the following placeholders throughout the codebase:
- `Kortix` → `[YOUR_COMPANY_NAME]`
- `Suna` → `[YOUR_PRODUCT_NAME]` (optional)
- `kortix.ai` → `[YOUR_DOMAIN]`
- `suna.so` → `[YOUR_APP_DOMAIN]`
- `support@kortix.ai` → `[YOUR_SUPPORT_EMAIL]`
- `@kortixai` → `[YOUR_SOCIAL_HANDLE]`
- `kortix-ai` → `[YOUR_GITHUB_ORG]`

## Files to Update

### 1. Frontend Configuration Files

#### `frontend/src/lib/site.ts`
```typescript
export const siteConfig = {
  name: '[YOUR_COMPANY_NAME] [YOUR_PRODUCT_NAME]',
  url: '[YOUR_APP_URL]',
  description: '[YOUR_COMPANY_NAME] AI',
  links: {
    twitter: '[YOUR_TWITTER_URL]',
    github: '[YOUR_GITHUB_URL]',
    linkedin: '[YOUR_LINKEDIN_URL]',
  },
};
```

#### `frontend/src/lib/home.tsx`
- Update site configuration object
- Update all branding references in content
- Update company showcase logos
- Update footer links

#### `frontend/package.json`
```json
{
  "name": "[YOUR_PRODUCT_NAME_LOWERCASE]",
  // ... rest of the file
}
```

### 2. Backend Configuration Files

#### `backend/utils/config.py`
```python
OR_SITE_URL: Optional[str] = "[YOUR_DOMAIN]"
OR_APP_NAME: Optional[str] = "[YOUR_COMPANY_NAME] AI"
SANDBOX_IMAGE_NAME = "[YOUR_DOCKER_ORG]/[YOUR_PRODUCT_NAME_LOWERCASE]:0.1.3"
```

#### `backend/pyproject.toml`
```toml
name = "[YOUR_PRODUCT_NAME_LOWERCASE]"
homepage = "[YOUR_APP_URL]"
repository = "[YOUR_GITHUB_URL]"
```

#### `backend/services/email.py`
- Update sender email and name
- Update email templates
- Update welcome messages

#### `backend/supabase/email-template.html`
- Update email template branding
- Update footer links

### 3. Logo and Branding Assets

Replace these files in `frontend/public/`:
- `kortix-logo.svg` → `[YOUR_COMPANY]-logo.svg`
- `kortix-logo-white.svg` → `[YOUR_COMPANY]-logo-white.svg`
- `kortix-symbol.svg` → `[YOUR_COMPANY]-symbol.svg`
- `banner.png` → Update with your branding
- `favicon.png` → Update with your logo

### 4. Component Files

#### `frontend/src/components/home/sections/navbar.tsx`
- Update logo references
- Update alt text

#### `frontend/src/components/sidebar/kortix-logo.tsx`
- Rename file to `[YOUR_COMPANY]-logo.tsx`
- Update component name and references

#### `frontend/src/components/sidebar/kortix-enterprise-modal.tsx`
- Rename file to `[YOUR_COMPANY]-enterprise-modal.tsx`
- Update component name and references

### 5. Documentation Files

#### `README.md`
- Update title and description
- Update all branding references
- Update GitHub links
- Update social media links

#### `setup.py`
- Update all branding references
- Update Docker image names

### 6. Docker Configuration

#### `backend/docker-compose.yml`
- Update image references

#### `backend/sandbox/docker/docker-compose.yml`
- Update image references

### 7. Database and API Configuration

#### `backend/api.py`
- Update allowed origins
- Update CORS settings

#### `backend/supabase/migrations/`
- Update any hardcoded email domains

### 8. Agent Prompts

#### `backend/agent/prompt.py`
```python
You are [YOUR_PRODUCT_NAME].so, an autonomous AI Agent created by the [YOUR_COMPANY_NAME] team.
```

#### `backend/agent/gemini_prompt.py`
- Update system prompt

#### `backend/agent/agent_builder_prompt.py`
- Update team references

## Step-by-Step Rebranding Process

### Step 1: Prepare Your Assets
1. Create your company logo in SVG format (regular and white versions)
2. Create a symbol/icon version of your logo
3. Update the banner image with your branding
4. Create a favicon

### Step 2: Update Configuration Files
1. Start with `frontend/src/lib/site.ts` and `frontend/src/lib/home.tsx`
2. Update `backend/utils/config.py`
3. Update `backend/pyproject.toml`

### Step 3: Replace Logo Files
1. Replace all logo files in `frontend/public/`
2. Update component references

### Step 4: Update Content
1. Update all text content in the frontend
2. Update email templates
3. Update documentation

### Step 5: Update URLs and Domains
1. Update all hardcoded URLs
2. Update CORS settings
3. Update allowed origins

### Step 6: Test Your Changes
1. Build and test the frontend
2. Test the backend API
3. Test email functionality
4. Test all integrations

## Important Notes

1. **Docker Images**: If you're using Docker, you'll need to build and push your own images
2. **Environment Variables**: Update any environment variables that reference the old branding
3. **Database**: If you have existing data, you may need to migrate it
4. **External Services**: Update any external service configurations (Supabase, etc.)
5. **Legal**: Update legal pages and terms of service

## Verification Checklist

- [ ] All company names updated
- [ ] All product names updated
- [ ] All URLs updated
- [ ] All email addresses updated
- [ ] All social media links updated
- [ ] All logo files replaced
- [ ] All component references updated
- [ ] All documentation updated
- [ ] All configuration files updated
- [ ] All Docker images updated
- [ ] All environment variables updated
- [ ] All legal pages updated
- [ ] All email templates updated
- [ ] All API endpoints tested
- [ ] All integrations tested

## Need Help?

If you need assistance with the rebranding process, you can:
1. Use search and replace tools to find all instances
2. Use the grep command: `grep -r "Kortix\|Suna" .`
3. Test each change incrementally
4. Keep backups of original files

Remember to update your deployment configurations and any CI/CD pipelines that reference the old branding. 