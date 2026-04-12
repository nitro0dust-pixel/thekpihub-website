#!/usr/bin/env python3
"""
Add Google Analytics 4 tracking code to all HTML files
GA4 Measurement ID: G-DZPCCPEP1J
"""

import os
import glob
from pathlib import Path

GA4_CODE = """
    <!-- Google Analytics 4 -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-DZPCCPEP1J"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-DZPCCPEP1J');
    </script>
"""

def add_ga4_to_html(filepath):
    """Add GA4 tracking code to HTML file if not already present"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if GA4 is already present
    if 'G-DZPCCPEP1J' in content or 'gtag' in content:
        print(f"✓ {filepath} - GA4 already present, skipping")
        return False
    
    # Find </head> tag and insert GA4 code before it
    if '</head>' not in content:
        print(f"✗ {filepath} - No </head> tag found, skipping")
        return False
    
    # Insert GA4 code before </head>
    updated_content = content.replace('</head>', f'{GA4_CODE}\n</head>')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✓ {filepath} - GA4 tracking added")
    return True

def main():
    # Get all HTML files in current directory
    html_files = glob.glob('*.html')
    
    if not html_files:
        print("No HTML files found in current directory")
        return
    
    print(f"\n🎯 Adding GA4 tracking (G-DZPCCPEP1J) to {len(html_files)} HTML files...\n")
    
    updated_count = 0
    for html_file in sorted(html_files):
        if add_ga4_to_html(html_file):
            updated_count += 1
    
    print(f"\n✅ Done! Updated {updated_count}/{len(html_files)} files")
    print(f"📊 GA4 Measurement ID: G-DZPCCPEP1J")
    print(f"🔗 View analytics at: https://analytics.google.com/")

if __name__ == '__main__':
    main()
