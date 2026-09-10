import re

files = [
    'blog/peran-karakter-soft-skills-kesiapan-kerja.html',
    'blog/manfaat-outbound-vs-seminar-motivasi-siswa.html',
    'blog/jasa-fasilitator-outbound-edukasi-sekolah-kampus.html'
]

with open('blog/pentingnya-manajemen-risiko-outbound-terbuka.html', 'r', encoding='utf-8') as f:
    ref = f.read()

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    print(f"==============================\nFILE: {fpath}")
    
    # 1. Check tag balances
    tags_to_check = ['div', 'section', 'article', 'main', 'header', 'footer', 'aside', 'script', 'style']
    for tag in tags_to_check:
        opens = len(re.findall(rf'<{tag}\b', c, re.IGNORECASE))
        closes = len(re.findall(rf'</{tag}>', c, re.IGNORECASE))
        if opens != closes:
            print(f"  [MISMATCH] <{tag}>: {opens} opens, {closes} closes (diff: {opens-closes})")
        else:
            print(f"  [OK] <{tag}>: {opens}")
            
    # 2. Check Baca Juga
    baca = re.findall(r'<div class="baca-juga-box">.*?</div>\s*</div>', c, re.DOTALL)
    print(f"  Baca Juga count: {len(baca)}")
    for i, b in enumerate(baca):
        print(f"    Baca {i+1}: {b.strip().replace(chr(10), ' ')}")

    # 3. Check FAQ
    faq = re.search(r'<div class="faq-section"[^>]*>.*?</div>\s*</div>\s*</div>', c, re.DOTALL)
    print(f"  FAQ Section found: {bool(faq)}")
    faq_items = re.findall(r'<div class="faq-item">', c)
    print(f"  FAQ Items count: {len(faq_items)}")
    
    # 4. Check CTA band
    cta = re.search(r'<div class="cta-band">.*?</div>', c, re.DOTALL)
    print(f"  CTA band found: {bool(cta)}")
    
    # 5. Check Author Box
    author = re.search(r'<div class="author-bio-card">|<div class="author-box">', c)
    print(f"  Author box match: {author.group(0) if author else 'NONE'}")
    
    # 6. Check Rekomendasi / Related articles
    rek = re.search(r'<section class="related-articles-section">|<section class="rekomendasi-section">', c)
    print(f"  Related section match: {rek.group(0) if rek else 'NONE'}")

