# Zabel LLC Directory

A comprehensive directory website for LLC formation services, organized by business type and state.

## Features

- **Business Type Pages**: Dedicated pages for different business types (doctors, plumbers, real estate, etc.)
- **State-Specific Pages**: Location-based LLC formation services for all 50 states
- **Top Online Services**: Comparison of the best LLC formation services with pros/cons
- **Local Business Directory**: Local service providers from CSV data
- **Responsive Design**: Mobile-friendly interface
- **SEO Optimized**: Dynamic sitemap and meta tags
- **Sticky CTA**: Northwest Registered Agent affiliate integration

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Templates**: Jinja2
- **Data**: Pandas for CSV processing
- **Hosting**: Vercel

## File Structure

```
zabel/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel configuration
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── business_type.html
│   ├── business_type_state.html
│   ├── about.html
│   ├── contact.html
│   ├── privacy.html
│   └── sitemap.xml
├── static/               # Static assets
│   ├── styles.css
│   └── script.js
└── LLC Data.csv          # Business data (not included in repo)
```

## Deployment to Vercel

### Prerequisites

1. Install [Vercel CLI](https://vercel.com/docs/cli)
2. Have a Vercel account

### Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Deploy to Vercel**
   ```bash
   vercel
   ```

3. **Follow the prompts:**
   - Link to existing project or create new
   - Set project name
   - Confirm deployment settings

4. **Environment Variables** (if needed):
   - Add any environment variables in Vercel dashboard
   - Update `vercel.json` if needed

### Configuration Files

- **vercel.json**: Routes all requests to `app.py`
- **requirements.txt**: Lists all Python dependencies
- **app.py**: Main Flask application with all routes

## Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd zabel
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   python app.py
   ```

4. **Access the site**
   - Open http://localhost:5000

## Data Management

The application uses a CSV file (`LLC Data.csv`) for business data. The file should contain:

- `name`: Business name
- `city`: City location
- `us_state`: Full state name
- `phone`: Phone number
- `rating`: Rating (optional)
- `reviews`: Number of reviews (optional)
- `site`: Website URL (optional)
- `us_address`: Full address (optional)
- `subtypes`: Business type categories (optional)

## Customization

### Adding New Business Types

1. Update `business_types` dictionary in `app.py`
2. Add new service slugs to the appropriate category

### Adding New States

1. Update `states` dictionary in `app.py`
2. Include name, abbreviation, and filing cost

### Styling

- Main styles: `static/styles.css`
- Responsive design included
- Custom CSS variables for easy theming

## SEO Features

- Dynamic sitemap generation
- Meta tags for all pages
- Structured data ready
- Breadcrumb navigation
- Clean URLs

## Affiliate Integration

- Northwest Registered Agent as top recommendation
- Sticky CTA button
- Affiliate disclosure on all service pages
- External link tracking

## Support

For questions or issues:
1. Check the Vercel deployment logs
2. Verify all dependencies are installed
3. Ensure CSV file is properly formatted
4. Check Flask debug output for errors

## License

This project is for internal use only.
