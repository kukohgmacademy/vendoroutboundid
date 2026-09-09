import os, glob, re

files = sorted(glob.glob('**/*.html', recursive=True))
print(f"Total HTML files to process: {len(files)}")

fa_tag = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'

updated_files = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    orig = content
    
    # 1. Ensure FontAwesome is in <head>
    if 'font-awesome' not in content and 'fontawesome' not in content:
        # Insert before style.css link
        if 'assets/css/style.css' in content:
            content = re.sub(
                r'(\s*<link[^>]*rel="stylesheet"[^>]*assets/css/style\.css[^>]*>)',
                r'\n  ' + fa_tag + r'\1',
                content,
                count=1
            )
        elif '</head>' in content:
            content = content.replace('</head>', f'  {fa_tag}\n</head>')
            
    # 2. Update navbar CTA
    # Match <a class="btn-wander-cta" ...> ... </a>
    def replace_navbar_cta(match):
        full_match = match.group(0)
        # Extract href
        href_match = re.search(r'href="([^"]+)"', full_match)
        href = href_match.group(1) if href_match else 'https://wa.me/6282211221909'
        
        # Keep href intact, but change inner content to <i class="fab fa-whatsapp"></i> <span class="nav-cta-text">Hubungi Kami</span>
        return f'''<a class="btn-wander-cta"
            href="{href}"
            target="_blank" rel="noopener" aria-label="Hubungi Kami via WhatsApp">
            <i class="fab fa-whatsapp"></i>
            <span class="nav-cta-text">Hubungi Kami</span>
          </a>'''

    # Pattern for btn-wander-cta
    content = re.sub(
        r'<a[^>]*class="[^"]*btn-wander-cta[^"]*"[^>]*>.*?</a>',
        replace_navbar_cta,
        content,
        flags=re.DOTALL
    )
    
    # Also handle any remaining nav-cta-text if inside another navbar class
    content = re.sub(
        r'<span class="nav-cta-text">(?:Konsultasi Sekarang|Booking Sekarang|Konsultasikan Sekarang)</span>',
        '<span class="nav-cta-text">Hubungi Kami</span>',
        content
    )
    
    if content != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(content)
        updated_files.append(f)

print(f"Successfully updated {len(updated_files)} files.")
