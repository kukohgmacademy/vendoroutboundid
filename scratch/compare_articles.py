with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('blog/peran-karakter-soft-skills-kesiapan-kerja.html', 'r', encoding='utf-8') as f:
    art1 = f.read()

import re

def analyze_structure(html, name):
    print(f"\n=================== {name} ===================")
    # Head scripts & links
    links = re.findall(r'<link[^>]+>', html)
    print("Links:")
    for l in links:
        print("  ", l)
    
    # Body scripts
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
    print(f"Scripts count: {len(scripts)}")
    for i, s in enumerate(scripts):
        src_m = re.search(r'src="([^"]+)"', html)
        if len(s.strip()) > 0 and 'application/ld+json' not in html:
            print(f"  Script {i}: {s[:100]}...")
    
    # Structural blocks
    blocks = re.findall(r'<!--\s*={3,}\s*(.*?)\s*={3,}\s*-->', html)
    print("Structural Comment Blocks:")
    for b in blocks:
        print("  ", b)

    # Check for sidebar or article layout
    if '<aside' in html:
        print("Has <aside> sidebar: True")
    else:
        print("Has <aside> sidebar: False")

    # Check for floating elements / WA float
    if 'wa-float' in html or 'floating' in html:
        print("Has floating elements: True")
    else:
        print("Has floating elements: False")

    # Check for scripts at bottom
    bottom_scripts = re.findall(r'<script[^>]*src="([^"]+)"', html)
    print("Bottom script src:", bottom_scripts)
    
    # Check for inline script
    inline_js = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
    print(f"Inline JS count: {len(inline_js)}")
    for j in inline_js:
        print("Inline JS preview:", j[:150])

analyze_structure(ref, "REFERENCE: pentingnya-manajemen-risiko-outbound-terbuka.html")
analyze_structure(art1, "ARTICLE 1: peran-karakter-soft-skills-kesiapan-kerja.html")
