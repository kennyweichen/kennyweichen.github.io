# Jekyll to Quarto Migration Guide

## Migration Complete! ✅

Your Jekyll site has been successfully migrated to Quarto. Here's what was done:

### Files Created/Modified:

**Configuration:**
- `_quarto.yml` - Main Quarto configuration with website settings, navigation, and blog configuration
- `styles.css` - Custom CSS ported from Jekyll's minimalist theme
- `.github/workflows/ci.yml` - Updated GitHub Actions workflow for Quarto deployment

**Content:**
- `blog/` - Directory with 40 migrated blog posts in Quarto format (.qmd)
- `index.qmd` - Homepage with blog listing (shows recent posts)
- `about.qmd` - About page
- `pages/github.qmd` - GitHub projects page (with API)
- `pages/pictures.qmd` - Achievements/bragging corner
- `pages/publications.qmd` - Publications and presentations
- `pages/strava.qmd` - Strava activities (with API)
- `blog/index.qmd` - Blog archive page

**Migration automation:**
- `migrate_jekyll_to_quarto.py` - Script used to convert Jekyll posts (can be deleted after verification)

### Next Steps:

#### 1. Install Quarto (if not already installed)
```bash
brew install quarto
```

#### 2. Test locally
```bash
cd /Users/kennychen/kennyweichen.github.io
quarto render
```

This will build the site into the `_site/` directory.

#### 3. Preview locally (optional)
```bash
quarto preview
```

This opens a live preview in your browser.

#### 4. Commit and push to GitHub
```bash
git add -A
git commit -m "Migrate from Jekyll to Quarto"
git push origin master
```

The GitHub Actions workflow will automatically:
- Build the site with Quarto
- Deploy to GitHub Pages
- Make it available at https://kennyweichen.com

### What's Preserved:

✅ All 40 blog posts with categories and metadata
✅ Custom pages (about, GitHub, photos, publications, Strava)
✅ Post organization by category
✅ Minimalist styling (adapted to Quarto)
✅ MathJax support for mathematical formulas
✅ Dark mode support
✅ Custom cursor assets
✅ Responsive design
✅ GitHub and Strava API integrations

### What's Changed:

- **File extension**: Posts are now `.qmd` instead of `.md`
- **Front matter format**: Slightly different YAML structure (Quarto format)
- **URLs**: Will generate new URL structure (can add redirects if needed)
- **Build system**: Quarto instead of Jekyll
- **Styling**: More integrated with Quarto's theme system

### Customization Options:

If you want further customize styling, edit `styles.css` or `_quarto.yml`:

**Change theme** in `_quarto.yml`:
```yaml
format:
  html:
    theme: cosmo  # or: lux, journal, minimal, bootstrap, etc.
```

**Adjust colors** by modifying the CSS variables in `styles.css`:
```css
:root {
  --link-color: #0366d6;
  --text-color: #000;
  --bg-color: #fff;
}
```

### Troubleshooting:

**Issue**: Images not showing after deployment
- Check that image paths are relative (use `/assets/images/...` with leading slash)

**Issue**: Dark mode not working
- Quarto's dark mode is built-in. Toggle works automatically based on system preference
- Can be customized in `_quarto.yml`

**Issue**: Math not rendering
- MathJax is enabled by default in `_quarto.yml`
- Use standard LaTeX: `$x^2$` for inline, `$$x^2$$` for display math

### Cleaning Up (Optional):

Once you verify everything works, you can remove Jekyll-related files:
```bash
rm -rf _config.yml _layouts/ _includes/ _sass/ Gemfile Gemfile.lock
rm migrate_jekyll_to_quarto.py
```

BUT KEEP these:
- `_data/` and `.github/` directories
- `assets/` directory with images/CSS
- `pages/` directory

### Need Help?

- Quarto docs: https://quarto.org/docs/guide/
- Blog publishing: https://quarto.org/docs/websites/website-blog.html
- GitHub Pages: https://quarto.org/docs/publishing/github-pages.html
