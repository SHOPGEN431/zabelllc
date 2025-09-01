from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

# Load CSV data
def load_csv_data():
    try:
        # Try multiple possible CSV paths for different environments
        possible_paths = [
            "LLC Data.csv",  # Current directory (Vercel)
            "C:\\zabel\\LLC Data.csv",  # Local development
            "./LLC Data.csv",  # Relative path
            os.path.join(os.path.dirname(__file__), "LLC Data.csv")  # Script directory
        ]
        
        for csv_path in possible_paths:
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                return df
        
        # If no CSV file found, create sample data
        sample_data = {
            'name': ['Sample Business 1', 'Sample Business 2', 'Sample Business 3', 'Sample Business 4', 'Sample Business 5', 'Sample Business 6'],
            'city': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia'],
            'us_state': ['New York', 'California', 'Illinois', 'Texas', 'Arizona', 'Pennsylvania'],
            'phone': ['(555) 123-4567', '(555) 234-5678', '(555) 345-6789', '(555) 456-7890', '(555) 567-8901', '(555) 678-9012'],
            'rating': [4.5, 4.2, 4.8, 4.1, 4.6, 4.3],
            'reviews': [150, 89, 234, 67, 189, 123],
            'site': ['https://example1.com', 'https://example2.com', 'https://example3.com', 'https://example4.com', 'https://example5.com', 'https://example6.com'],
            'us_address': ['123 Main St', '456 Oak Ave', '789 Pine Rd', '321 Elm St', '654 Maple Dr', '987 Cedar Ln'],
            'subtypes': ['doctors', 'real-estate', 'ecommerce', 'plumbers', 'restaurants', 'consultants']
        }
        return pd.DataFrame(sample_data)
    except Exception as e:
        print(f"Error loading CSV: {e}")
        # Return empty DataFrame with correct columns
        return pd.DataFrame(columns=['name', 'city', 'us_state', 'phone', 'rating', 'reviews', 'site', 'us_address', 'subtypes'])

# Business types configuration
business_types = {
    'healthcare': {
        'name': 'Healthcare',
        'services': ['doctors', 'dentists', 'nurses', 'pharmacists', 'therapists', 'chiropractors']
    },
    'construction': {
        'name': 'Construction & Trades',
        'services': ['plumbers', 'electricians', 'contractors', 'landscapers', 'roofers', 'carpenters']
    },
    'real-estate': {
        'name': 'Real Estate',
        'services': ['real-estate', 'property-management', 'real-estate-agents', 'investors', 'developers']
    },
    'ecommerce': {
        'name': 'E-commerce & Online',
        'services': ['ecommerce', 'online-retail', 'dropshipping', 'digital-products', 'affiliate-marketing']
    },
    'transportation': {
        'name': 'Transportation',
        'services': ['trucking', 'delivery', 'transportation', 'logistics', 'limo', 'taxi']
    },
    'food-hospitality': {
        'name': 'Food & Hospitality',
        'services': ['restaurants', 'catering', 'food-trucks', 'hotels', 'bars', 'cafes']
    },
    'beauty': {
        'name': 'Beauty & Personal Care',
        'services': ['salons', 'barbers', 'spas', 'cosmetologists', 'nail-technicians', 'estheticians']
    },
    'professional-services': {
        'name': 'Professional Services',
        'services': ['consultants', 'accountants', 'lawyers', 'architects', 'engineers', 'designers']
    },
    'digital-creative': {
        'name': 'Digital & Creative',
        'services': ['social-media-influencers', 'online-coaches', 'content-creators', 'videographers', 'podcasters']
    },
    'finance': {
        'name': 'Finance & Investment',
        'services': ['stock-trading', 'day-trading', 'crypto-trading', 'financial-advisors', 'insurance-agents']
    },
    'specialized': {
        'name': 'Specialized',
        'services': ['vending-machines', 'cannabis', 'woodworking', 'jewelry-makers', 'farmers']
    }
}

# States configuration
states = {
    'alabama': {'name': 'Alabama', 'abbr': 'AL', 'cost': '200'},
    'alaska': {'name': 'Alaska', 'abbr': 'AK', 'cost': '250'},
    'arizona': {'name': 'Arizona', 'abbr': 'AZ', 'cost': '50'},
    'arkansas': {'name': 'Arkansas', 'abbr': 'AR', 'cost': '45'},
    'california': {'name': 'California', 'abbr': 'CA', 'cost': '70'},
    'colorado': {'name': 'Colorado', 'abbr': 'CO', 'cost': '50'},
    'connecticut': {'name': 'Connecticut', 'abbr': 'CT', 'cost': '120'},
    'delaware': {'name': 'Delaware', 'abbr': 'DE', 'cost': '90'},
    'district-of-columbia': {'name': 'District of Columbia', 'abbr': 'DC', 'cost': '99'},
    'florida': {'name': 'Florida', 'abbr': 'FL', 'cost': '125'},
    'georgia': {'name': 'Georgia', 'abbr': 'GA', 'cost': '100'},
    'hawaii': {'name': 'Hawaii', 'abbr': 'HI', 'cost': '50'},
    'idaho': {'name': 'Idaho', 'abbr': 'ID', 'cost': '100'},
    'illinois': {'name': 'Illinois', 'abbr': 'IL', 'cost': '150'},
    'indiana': {'name': 'Indiana', 'abbr': 'IN', 'cost': '90'},
    'iowa': {'name': 'Iowa', 'abbr': 'IA', 'cost': '50'},
    'kansas': {'name': 'Kansas', 'abbr': 'KS', 'cost': '160'},
    'kentucky': {'name': 'Kentucky', 'abbr': 'KY', 'cost': '40'},
    'louisiana': {'name': 'Louisiana', 'abbr': 'LA', 'cost': '100'},
    'maine': {'name': 'Maine', 'abbr': 'ME', 'cost': '175'},
    'maryland': {'name': 'Maryland', 'abbr': 'MD', 'cost': '100'},
    'massachusetts': {'name': 'Massachusetts', 'abbr': 'MA', 'cost': '500'},
    'michigan': {'name': 'Michigan', 'abbr': 'MI', 'cost': '50'},
    'minnesota': {'name': 'Minnesota', 'abbr': 'MN', 'cost': '155'},
    'mississippi': {'name': 'Mississippi', 'abbr': 'MS', 'cost': '50'},
    'missouri': {'name': 'Missouri', 'abbr': 'MO', 'cost': '50'},
    'montana': {'name': 'Montana', 'abbr': 'MT', 'cost': '70'},
    'nebraska': {'name': 'Nebraska', 'abbr': 'NE', 'cost': '100'},
    'nevada': {'name': 'Nevada', 'abbr': 'NV', 'cost': '75'},
    'new-hampshire': {'name': 'New Hampshire', 'abbr': 'NH', 'cost': '100'},
    'new-jersey': {'name': 'New Jersey', 'abbr': 'NJ', 'cost': '125'},
    'new-mexico': {'name': 'New Mexico', 'abbr': 'NM', 'cost': '50'},
    'new-york': {'name': 'New York', 'abbr': 'NY', 'cost': '200'},
    'north-carolina': {'name': 'North Carolina', 'abbr': 'NC', 'cost': '125'},
    'north-dakota': {'name': 'North Dakota', 'abbr': 'ND', 'cost': '135'},
    'ohio': {'name': 'Ohio', 'abbr': 'OH', 'cost': '99'},
    'oklahoma': {'name': 'Oklahoma', 'abbr': 'OK', 'cost': '100'},
    'oregon': {'name': 'Oregon', 'abbr': 'OR', 'cost': '100'},
    'pennsylvania': {'name': 'Pennsylvania', 'abbr': 'PA', 'cost': '125'},
    'rhode-island': {'name': 'Rhode Island', 'abbr': 'RI', 'cost': '150'},
    'south-carolina': {'name': 'South Carolina', 'abbr': 'SC', 'cost': '110'},
    'south-dakota': {'name': 'South Dakota', 'abbr': 'SD', 'cost': '150'},
    'tennessee': {'name': 'Tennessee', 'abbr': 'TN', 'cost': '300'},
    'texas': {'name': 'Texas', 'abbr': 'TX', 'cost': '300'},
    'utah': {'name': 'Utah', 'abbr': 'UT', 'cost': '70'},
    'vermont': {'name': 'Vermont', 'abbr': 'VT', 'cost': '125'},
    'virginia': {'name': 'Virginia', 'abbr': 'VA', 'cost': '100'},
    'washington': {'name': 'Washington', 'abbr': 'WA', 'cost': '200'},
    'west-virginia': {'name': 'West Virginia', 'abbr': 'WV', 'cost': '100'},
    'wisconsin': {'name': 'Wisconsin', 'abbr': 'WI', 'cost': '130'},
    'wyoming': {'name': 'Wyoming', 'abbr': 'WY', 'cost': '100'}
}

@app.route('/')
def index():
    df = load_csv_data()
    businesses = []
    if not df.empty:
        businesses = df.head(6).to_dict('records')
    
    return render_template('index.html', 
                         business_types=business_types, 
                         states=states, 
                         businesses=businesses)

@app.route('/llc-for-<business_type>')
def business_type_page(business_type):
    # Find the category for this business type
    category_data = None
    for category, data in business_types.items():
        if business_type in data['services']:
            category_data = data
            break
    
    if not category_data:
        return "Business type not found", 404
    
    df = load_csv_data()
    businesses = []
    if not df.empty:
        # Filter businesses by business type if possible
        try:
            filtered_df = df[df['subtypes'].str.contains(business_type, case=False, na=False)]
            businesses = filtered_df.head(6).to_dict('records')
        except:
            businesses = df.head(6).to_dict('records')
    
    return render_template('business_type.html',
                         business_type=business_type,
                         category_data=category_data,
                         states=states,
                         businesses=businesses)

@app.route('/llc-for-<business_type>/<state>')
def business_type_state_page(business_type, state):
    if state not in states:
        return "State not found", 404
    
    # Find the category for this business type
    category_data = None
    for category, data in business_types.items():
        if business_type in data['services']:
            category_data = data
            break
    
    if not category_data:
        return "Business type not found", 404
    
    df = load_csv_data()
    businesses = []
    if not df.empty:
        # Filter businesses by state
        try:
            state_filter = df['us_state'].str.lower() == states[state]['name'].lower()
            filtered_df = df[state_filter]
            businesses = filtered_df.head(20).to_dict('records')
        except:
            businesses = df.head(20).to_dict('records')
    
    return render_template('business_type_state.html',
                         business_type=business_type,
                         state=state,
                         state_data=states[state],
                         category_data=category_data,
                         states=states,
                         businesses=businesses)

@app.route('/about')
def about():
    return render_template('about.html', business_types=business_types)

@app.route('/contact')
def contact():
    return render_template('contact.html', business_types=business_types)

@app.route('/privacy')
def privacy():
    return render_template('privacy.html', business_types=business_types)

@app.route('/sitemap.xml')
def sitemap():
    # Generate sitemap dynamically
    urls = []
    
    # Add static pages
    static_pages = ['', '/about', '/contact', '/privacy']
    for page in static_pages:
        urls.append({
            'loc': f'https://www.zabelllc.org{page}',
            'changefreq': 'monthly',
            'priority': '0.6'
        })
    
    # Add business type pages
    for category, data in business_types.items():
        for service in data['services']:
            urls.append({
                'loc': f'https://www.zabelllc.org/llc-for-{service}',
                'changefreq': 'weekly',
                'priority': '0.8'
            })
    
    # Add state-specific pages
    for category, data in business_types.items():
        for service in data['services']:
            for state_key in states.keys():
                urls.append({
                    'loc': f'https://www.zabelllc.org/llc-for-{service}/{state_key}',
                    'changefreq': 'weekly',
                    'priority': '0.9'
                })
    
    return render_template('sitemap.xml', urls=urls, business_types=business_types)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
